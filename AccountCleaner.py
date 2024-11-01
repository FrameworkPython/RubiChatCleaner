from pyrubi import Client
from concurrent.futures import ThreadPoolExecutor
import logging

class Cleaner:
    def __init__(self, session, safe_guids):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.client = Client(session=session)
        self.safe_guids = safe_guids
        self.own_guid = self.client.get_me()['user']['user_guid'] 
        self.chats = self.client.get_chats()['chats']
        self.chat_counts = self.count_chats()
        self.clean_account()

    def count_chats(self):
        pv_count = sum(1 for chat in self.chats if chat['object_guid'].startswith('u') and chat['object_guid'] not in self.safe_guids)
        group_count = sum(1 for chat in self.chats if chat['object_guid'].startswith('g') and chat['object_guid'] not in self.safe_guids)
        channel_count = sum(1 for chat in self.chats if chat['object_guid'].startswith('c') and chat['object_guid'] not in self.safe_guids)
        return {"pv": pv_count, "group": group_count, "channel": channel_count}

    def leave_chat(self, object_guid):
        try:
            if object_guid != self.own_guid:
                self.client.leave_chat(object_guid)
                self.logger.info(f"Left group or channel with GUID: {object_guid}")
        except Exception as e:
            self.logger.error(f"Error leaving group or channel with GUID {object_guid}: {str(e)}")

    def delete_user_chat(self, object_guid, last_deleted_message_id):
        try:
            if object_guid != self.own_guid:  
                self.client.delete_user_chat(object_guid, last_deleted_message_id)
                self.logger.info(f"Private chat with GUID {object_guid} deleted")
        except Exception as e:
            self.logger.error(f"Error deleting private chat with GUID {object_guid}: {str(e)}")

    def handle_chat(self, chat, option):
        object_guid = chat['object_guid']
        if object_guid not in self.safe_guids and object_guid != self.own_guid:  # بررسی گویید خود اکانت
            if option == '1' and object_guid.startswith('u'):
                last_deleted_message_id = chat['last_message']['message_id']
                self.delete_user_chat(object_guid, last_deleted_message_id)
            elif option == '2' and object_guid.startswith('g'):
                self.leave_chat(object_guid)
            elif option == '3' and object_guid.startswith('c'):
                self.leave_chat(object_guid)
            elif option == '4':
                if object_guid.startswith('u'):
                    last_deleted_message_id = chat['last_message']['message_id']
                    self.delete_user_chat(object_guid, last_deleted_message_id)
                elif object_guid.startswith('g') or object_guid.startswith('c'):
                    self.leave_chat(object_guid)

    def clean_account(self):
        print(f"Private chats: {self.chat_counts['pv']}, Groups: {self.chat_counts['group']}, Channels: {self.chat_counts['channel']}")
        print("1. Clean private chats\n2. Clean groups\n3. Clean channels\n4. Clean all")
        option = input("Choose an option to clean (1/2/3/4): ").strip()
        if option in ["1", "2", "3", "4"]:
            with ThreadPoolExecutor() as executor:
                executor.map(lambda chat: self.handle_chat(chat, option), self.chats)
        else:
            print("Invalid option selected.")
#لیست گویید هایی که نمیخواید پاک شه رو در قسمت safe_guids بزارید
my_cleaner = Cleaner(session="AccCleaner", safe_guids=["guid1", "guid2"])

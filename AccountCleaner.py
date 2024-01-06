from pyrubi import Client
from concurrent.futures import ThreadPoolExecutor
import logging

class Cleaner:
    def __init__(self, session, safe_guids):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.client = Client(session=session)
        self.safe_guids = safe_guids
        self.clean_account()

    def leave_chat(self, object_guid):
        try:
            self.client.leave_chat(object_guid)
            self.logger.info(f"لفت داده شد از گروه یا کانال با شناسه: {object_guid}")
        except Exception as e:
            self.logger.error(f"خطا در لفت دادن از گروه یا کانال با شناسه {object_guid}: {str(e)}")

    def delete_user_chat(self, object_guid, last_deleted_message_id):
        try:
            self.client.delete_user_chat(object_guid, last_deleted_message_id)
            self.logger.info(f"چت خصوصی با شناسه {object_guid} پاک شد")
        except Exception as e:
            self.logger.error(f"خطا در حذف چت خصوصی با شناسه {object_guid}: {str(e)}")

    def handle_chat(self, chat):
        object_guid = chat['object_guid']
        if object_guid not in self.safe_guids:
            if object_guid.startswith('c') or object_guid.startswith('g'):
                self.leave_chat(object_guid)
            elif object_guid.startswith('u'):
                last_deleted_message_id = chat['last_message']['message_id']
                self.delete_user_chat(object_guid, last_deleted_message_id)

    def clean_account(self):
        chats = self.client.get_chats()
        with ThreadPoolExecutor() as executor:
            executor.map(self.handle_chat, chats['chats'])
#توی قسمت safe_guid گویید هایی که میخواید پاک نشن رو بزنید
my_cleaner = Cleaner(session="AccCleaner", safe_guids=["guid1", "guid2"])

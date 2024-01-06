# پاکسازی کننده اکانت 
این یه اسکریپت پایتونی هست که با کتابخونه [pyrubi](https://github.com/AliGanji1/pyrubi) نوشته شده است

## **قابلیت ها**
این اسکریپت کاملا بهینه و ساده نوشته شده تا کاربر خیلی راحت استفاده کنه

- **قابلیت حذف نکردن گویید های مشخص شده**
- این قابلیت به شما اجازه میده تا شناسه چت هایی که میخواید پاک نشه رو در قسمت safe_guid وارد کنید 

## **نیازمندی ها**
- برای اجرای این اسکریپت بدون مشکل شما نیازمند کتابخانه های زیر هستید:
```
  pyrubi(v3.3.1)
  logging
  concurrent.futures
  ```
## **آموزش اجرا کردن در Termux**
برای اجرای این اسکریپت در ترموکس اول پکیج هارو اپدیت کنید
```bash
apt update -y && apt upgrade -y
```
سپس git و python رو نصب کنید 
```bash
pkg install git -y && pkg install python -y
```
سپس اسکریپت رو دانلود کنید 
```bash
git clone https://github.com/FrameworkPython/RubiChatCleaner
```
سپس وارد پوشه اسکریپت بشید 
```bash
cd RubiChatCleaner
```
و در آخر میتونید سورس رو با دستور زیر اجرا کنید
```bash
python AccountCleaner.py
```
- توجه ⚠️:

# پاکسازی کننده اکانت 
این یه اسکریپت پایتونی هست که با کتابخونه [pyrubi](https://github.com/AliGanji1/pyrubi) نوشته شده است

## **قابلیت ها**
این اسکریپت کاملا بهینه و ساده نوشته شده تا کاربر خیلی راحت استفاده کنه

- **قابلیت حذف نکردن گویید های مشخص شده**
- این قابلیت به شما اجازه میده تا چت هایی که مشخص میکنید رو پاک نکنه، فقط باید گویید چت های مورد نظرتون اعم از پیوی یا گپ یا کانال رو توی بخش safe_guids وارد کنید 

## **نیازمندی ها**
- برای اجرای این اسکریپت بدون مشکل شما نیازمند کتابخانه های زیر هستید:
```
  pyrubi(v3.3.1)
  logging
  concurrent.futures
  ```
## **آموزش اجرا کردن در [Termux](https://f-droid.org/repo/com.termux_118.apk)**
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
- توجه ⚠️: اگه میخواید بعضی چت ها حذف نشن، باید guid اون چت هارو به دست بیارید و در لاین 65 و در قسمت safe_guids وارد کنید

## **ویدیو آموزشی**
برای دیدن ویدیوی آموزشی نحوه اجرا و استفاده از اسکریپت به این  [لینک](https://uupload.ir/view/cleaner_lex3.mp4/) مراجعه کنید.

## توسعه 
شما میتوانید این اسکریپت رو توسعه بدید در صورتی که حتما نام سازنده رو در اسکریپت ذکر کنید،در‌غیر اینصورت اجازه توسعه و یا ادیت این اسکریپت رو ندارید و هرگونه ادیت و یا توسعه بدون ذکر نام سازنده ، حرام بوده و مورد پیگرد خواهد بود ،🚷

## مجوز ⚠️

این پروژه تحت مجوز MIT منتشر شده است. برای اطلاعات بیشتر، لطفا فایل LICENSE را مطالعه کنید.

## سازنده
جهت ارائه پیشنهادات و یا مشکلات و تماس با سازنده این اسکریپت ، از [روبیکا](https://rubika.ir/framework_pythonm) یا [تلگرام](https://t.me/Framework_Python) با من در ارتباط باشید.


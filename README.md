# Messenger Group Chat Member Message Sender Script
This is a python script that can be executed in a local machine. The aim of this script is to collect all the members/users inside a messenger group chat and message them directly, one by one. The message can be `text`,`links` or `images`. You can also send multiple messages.

This script uses Google Chrome Web Driver and Python 3.9.0

### Python Libraries/Packages Dependancies
- Iterable
- Selenium
- time

Make sure you have these Libraries installed on your machine.
You can install these globally or locally using `pip install`

### Content Files
- main.py
Main script

### Important Notes:
- Look for the appropriate web driver base on your browser and its version. Here I used `Google Chrome Webdriver`
- Make sure that your `webdriver` is located somewhere in your computer that is easy to found. The suggested location is in `C:\Program Files (x86)`
- Python 3.9.0 must be installed and the said libraries
- This scripts require your Facebook Credentials such as your `username` and `password`. Be careful on this part. If you want more secure login, use `getpass` function from `getpass` library.

### Target Group Conversation
Target Group Conversation is the `url` or `id` of the group chat conversation. It is where the script will look for the members. Example: `https://www.messenger.com/t/33000932210120365`. You can find this by opening the target group chat in your browser.

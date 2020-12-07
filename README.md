# Messenger Group Chat Member Message Sender Script
This is a python script that can be executed in a local machine. The aim of this script is to collect all the members/users inside a messenger group chat and message them directly, one by one. The message can be a `text`,`link` or `image`. You can also send multiple messages at one execution.
This script uses `webdriver`.

## Why I create this script?
There are a lot of times when messages in Group Chats are ignored bacause there's a lot of stuff going on. Another reason is... group chat messages can be covered by newer messages and as the new messages come up, it takes time to scroll up and down and look back certain messages. It can deccrease the dissemination of the information or announcement or an event as other users get tired of looking and reading back in the conversation. 

One solution is to message each member directly, one by one. But that is very impractical specially if we have a big number of members in the group. So, why not automate these things out?

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
- Make sure that your `webdriver` is located somewhere in your computer that is easy to find. Suggested location is inside `C:\Program Files(x86)\`
- Python 3.9.0 must be installed and the said libraries
- This script requires your Facebook Credentials such as your `username` and `password`. Be careful on this part. If you want more secure login, use `getpass` function from `getpass` library.

### Target Group Conversation
Target Group Conversation is the `url` or `id` of the group chat conversation. It is where the script will look for the members. Example: `https://www.messenger.com/t/33000932210120365`. You can find this by opening the target group chat in your browser.

#### If you have questions or suggestions, you can contact me here:
- (+63) 939 422 8185
- eechemane29@gmail.com
- https://facebook.com/e.echemane

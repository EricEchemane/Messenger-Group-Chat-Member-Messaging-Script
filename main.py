from logging import warn
from typing import Iterable
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from colorama import Fore

# ======================= color indication
WARNING = Fore.RED
SUCCESS = Fore.GREEN
RESET = Fore.RESET
# ======================= color indication

# webdriver path
PATH = 'C:\Program Files (x86)\chromedriver.exe'
# instance of the Chrome driver 
driver = webdriver.Chrome(PATH)

# TARGET Group Conversation Link
# cbi_convo = 'https://www.messenger.com/t/3251448648318216'
# driver.get(cbi_convo)
TARGET_CONVO = "https://www.messenger.com/t/2611033062293200"
driver.get(TARGET_CONVO)

# ======================================== LOGIN form 
try:
    # find email input
    email = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.ID,"email"))
    )
    print(SUCCESS+"Email input found..."+RESET)
except:
    driver.quit()
    print(WARNING+"Email input cannot found."+RESET)
    exit()
try:
    # find password input
    password = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.ID,"pass"))
    )
    print(SUCCESS+"Password input found..."+RESET)
except: 
    driver.quit()
    print(WARNING+"Password input cannot found."+RESET)
    exit()
# ======================================== LOGIN form 


#===================== Actual Login =========================
try:
    email.send_keys("e.echemane")
    password.send_keys("E03292000E")
    password.send_keys(Keys.RETURN)
    print(SUCCESS+"Login successful..."+RESET)
except:
    driver.quit()
    print(WARNING+"Login Failed."+RESET)
    exit()
#===================== Actual Login =========================

# path for the HTML UL LIST
ul_path = "/html/body/div[1]/div/div/div/div[2]/span/div[2]/div[1]/div/div/div[1]/div/div/div/div[3]/div[2]/span/div/div/ul"

# find the element 
try:
    ul = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,ul_path))
    )
    print(SUCCESS+"Members UL Container found..."+RESET)
except:
    driver.quit()
    print(WARNING+"MEMBERS UL Container cannot found."+RESET)
    exit()

# return the lists or members
try:

    lists = ul.find_elements(By.XPATH,"./li")
    print(SUCCESS+"Members' list found..."+RESET)
except:
    driver.quit()
    print(WARNING+"Members' list cannot found."+RESET)
    exit()

# count of group members
number_of_members = len(lists)
# Message to be sent
message = "[ SB19: Test-3 lang po ulit-PASENSYA NA :) ]"

# In case you want to send an image
image_path = 'C:/Users/eeche/Pictures/Wallpapers/apple.jpg'

# ========================= EXECUTION ===============================
for x in range(0, number_of_members):    

    time.sleep(1)

    print(Fore.BLUE + "\nIteration No." + str(x) + RESET)
    # ========= FIND THE MEMBER LIST
    try:
        ul = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,ul_path))
        )
        print("Members UL Container found...")
    except:
        driver.quit()
        print(WARNING+"MEMBERS UL Container cannot found."+RESET)
        exit()
    
    try:
        lists = ul.find_elements(By.XPATH,"./li")
        print("Members' list found...")
    except:
        driver.quit()
        print(WARNING+"Member lists cannot found."+RESET)
        exit()


    lists[x].click() # Click through each list to open conversation


    # find the message input
    try:
        msg_box = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.CLASS_NAME,"notranslate"))
        )
        print("Message Box found...")
    except:
        driver.quit()
        print(WARNING+"Message input cannot found."+RESET)
        exit()


    msg_box.send_keys(message) # write the message
    msg_box.send_keys(Keys.RETURN) # send the message
    time.sleep(1)
    print(SUCCESS+"Message Sent..."+RESET)

    # # get photo input
    # photo_input = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/form/div/span/input")
    # # get photo
    # photo_input.send_keys(image_path)
    
    # time.sleep(wait_time)

    # # execute: click send
    # driver.execute_script('document.getElementsByClassName("_30yy _38lh _7kpi")[0].click()')


    # go back to the Group Conversation page
    # driver.get('https://www.messenger.com/t/3251448648318216')
    driver.back()

print(SUCCESS+"\n\nCOMPLETED"+RESET)
from typing import Iterable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# webdriver path
PATH = 'C:\Program Files (x86)\chromedriver.exe'
# instance of the Chrome driver 
driver = webdriver.Chrome(PATH)

# TARGET Group Conversation Link
driver.get('https://www.messenger.com/t/3251448648318216')

# ================== LOGIN form ======================
# find email input
email = driver.find_element_by_id("email")
# find password input
password = driver.find_element_by_id("pass")
# ================== LOGIN form ======================

# wait until it finds the element
time.sleep(1)

#===================== Actual Login =========================
email.send_keys("e.echemane")
password.send_keys("E03292000E")
password.send_keys(Keys.RETURN)
#===================== Actual Login =========================

# path for the HTML UL LIST
ul_path = "/html/body/div[1]/div/div/div/div[2]/span/div[2]/div[1]/div/div/div[1]/div/div/div/div[3]/div[2]/span/div/div/ul"

# find the element 
ul = driver.find_element_by_xpath(ul_path)

# return the lists or members
lists = ul.find_elements_by_xpath("./li")

# count of group members
number_of_members = len(lists)
# Message to be sent
message = "Test-drive"

# In case you want to send an image
image_path = 'C:/Users/eeche/Pictures/Wallpapers/apple.jpg'

# seconds to wait before executing a command
wait_time = 2

# ========================= EXECUTION ===============================
for x in range(0, number_of_members):    
    
    # ========= FIND THE MEMBER LIST
    ul = driver.find_element_by_xpath(ul_path)
    lists = ul.find_elements_by_xpath("./li")

    time.sleep(wait_time) # wait until page loads

    lists[x].click() # Click through each list to open conversation

    time.sleep(wait_time) # wait until page loads

    # find the message input
    msg_box = driver.find_element_by_class_name("notranslate")

    time.sleep(wait_time) # wait until page loads

    msg_box.send_keys(message) # write the message
    msg_box.send_keys(Keys.RETURN) # send the message

    # get photo input
    photo_input = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/form/div/span/input")
    # get photo
    photo_input.send_keys(image_path)
    
    time.sleep(wait_time)

    # execute: click send
    driver.execute_script('document.getElementsByClassName("_30yy _38lh _7kpi")[0].click()')

    time.sleep(wait_time) # wait until page loads

    # go back to the Group Conversation page
    driver.get('https://www.messenger.com/t/3251448648318216')
    
    time.sleep(wait_time) # wait until page loads
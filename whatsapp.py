from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome() 

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"Group or person name"'

# Replace the below string with your own message
string = "Hello world """

#string=input("Enter message which you want to send: ")

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located(( 
	By.XPATH, x_arg))) 
group_title.click() 
inp_xpath = '//div[@class="_3u328 copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located(( 
	By.XPATH, inp_xpath)))



#This loop will send the message number of times indicated in the range function. 

for i in range(1): 
	input_box.send_keys(string + Keys.ENTER) 
	time.sleep(1) 
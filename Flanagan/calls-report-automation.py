from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox('C:/Program Files/geckodriver/')
#driver.get("https://horizon.akixi.com/CCS/App/Horizon;jsessionid=6A10518822CA89B93FAD58FE3F4CD6C6?ServletCmd=CMD_AUTHENTICATE&tbReversionServletCmd=CMD_AUTHENTICATE")
driver.get("https://horizon.akixi.com/CCS/App/Horizon;jsessionid=0C96A4A1D82D38CF6A8B148627E90284?ServletCmd=CMD_AUTHENTICATE&amp;tbReversionServletCmd=CMD_MAIN")

print(driver.title)

u_name = "paul.braniff@flanagan-flooring.com"
psswd = input("Please enter password:")

user_entry = driver.find_element_by_id("idUserNameEnter")
psswd_entry = driver.find_element_by_id("idPasswordEnter")
user_entry.send_keys(u_name)
psswd_entry.send_keys(psswd)
psswd_entry.send_keys(Keys.RETURN)

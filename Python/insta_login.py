from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://instagram.com')

user_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
user_box.send_keys('enter username here')

pass_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pass_box.send_keys('enter password here')

log_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
log_button.click()

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://instagram.com')

user_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
user_box.send_keys('srinand._')

pass_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pass_box.send_keys('N@ndlp23')

log_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
log_button.click()
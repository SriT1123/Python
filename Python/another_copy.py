from selenium import webdriver

driver = webdriver.Firefox(executable_path = "C:\\Users\\srina\\Desktop\\geckodriver.exe")
#minimizes the window
driver.minimize_window()

#Function definition for later on
def removing_lone_list(hehehe):
    x = hehehe[0]
    return x


#opening genesis
driver.get('https://parents.robbinsville.k12.nj.us/genesis/parents?tab1=studentdata&tab2=gradebook&tab3=weeklysummary&studentid=230658&action=form')
#entering username
user_box = driver.find_element_by_xpath('//*[@id="j_username"]')
user_box.send_keys("23tanakalas@rvilleschools.org")
#entering password
pass_box = driver.find_element_by_xpath('//*[@id="j_password"]')
pass_box.send_keys("23Heenan")

button = driver.find_element_by_xpath('/html/body/form/div/div[2]/input[1]')
button.click()

#opening classes
class_name = input("What class do you want for your grade? ")
if "draw" in class_name.lower() :
    class_button = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/span')
    class_button.click()
elif "paint" in class_name.lower():
    class_button = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/span')
    class_button.click()
elif "bus" in class_name.lower():
    class_button = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[4]/td[1]/span')
    class_button.click()
elif "eng" in class_name.lower():
    class_button = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[5]/td[1]/span')
    class_button.click()
elif "history" in class_name.lower():
    class_button = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[6]/td[1]/span')
    class_button.click()
elif "pre" in class_name.lower():
    class_button = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[7]/td[1]/span')
    class_button.click()
elif "pe" in class_name.lower():
    class_button = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[8]/td[1]/span')
    class_button.click()
elif "health" in class_name.lower():
    class_button = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[9]/td[1]/span')
    class_button.click()
elif "chem" in class_name.lower():
    class_button = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[10]/td[1]/span')
    class_button.click()
elif "comp" in class_name.lower():
    class_button = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[11]/td[1]/span')
    class_button.click()
else:
    class_button = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[12]/td[1]/span')
    class_button.click()

#finding whether I want grades for marking periods or full year
time_period = input("Do you want MP 1, 2, 3, 4 or full year? ")

if "1" in time_period:
    button3 = driver.find_element_by_xpath('//*[@id="fldDateRange"]')
    button3.click()
    option = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/form/table/tbody/tr[2]/td[4]/select/option[5]')
    option.click()
elif "2" in time_period:
    button3 = driver.find_element_by_xpath('//*[@id="fldDateRange"]')
    button3.click()
    option = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/form/table/tbody/tr[2]/td[4]/select/option[6]')
    option.click()
elif "3" in time_period:
    button3 = driver.find_element_by_xpath('//*[@id="fldDateRange"]')
    button3.click()
    option = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/form/table/tbody/tr[2]/td[4]/select/option[7]')
    option.click()
elif "4" in time_period:
    button3 = driver.find_element_by_xpath('//*[@id="fldDateRange"]')
    button3.click()
    option = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/form/table/tbody/tr[2]/td[4]/select/option[8]')
    option.click()
else:
    button3 = driver.find_element_by_xpath('//*[@id="fldDateRange"]')
    button3.click()
    option = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/form/table/tbody/tr[2]/td[4]/select/option[9]')
    option.click()
search = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/form/table/tbody/tr[3]/td/input')
search.click()

#setting the grades table as a variable
table_id = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/table')
#finding all rows in the table above and setting that equal to variable rows
rows = table_id.find_elements_by_tag_name("tr") 

print("Amount of rows: " + str(len(rows)))
my_list = []
#my_list.append([])
numerator = 0
denominator = 0
for row in rows:
    #setting cols equal to the columns in row i
    i = 0
    cols = row.find_elements_by_tag_name("td")
    if len(cols) == 17:
        grade = cols[12].text
        grade = grade.split('/')
        grade[1] = grade[1].split('\n')
        grade[1].pop(1)

        y = removing_lone_list(grade[1])
        grade.pop(1)
        grade.append(y)
        
        grade[0] = float(grade[0])
        grade[1] = float(grade[1])

        numerator += grade[0]
        denominator += grade[1]
        
print("Final Grade: " + str(round(((numerator/denominator) * 100), 2)) + "%")

driver.close()
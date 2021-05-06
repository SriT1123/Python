from selenium import webdriver

driver = webdriver.Firefox(executable_path = "C:\\Users\\srina\\Desktop\\geckodriver.exe")
#minimizes the window
driver.minimize_window()

#opening genesis
driver.get('https://parents.robbinsville.k12.nj.us/genesis/parents?tab1=studentdata&tab2=gradebook&tab3=weeklysummary&studentid=230658&action=form')
#entering username
user_box = driver.find_element_by_xpath('//*[@id="j_username"]')
user_box.send_keys("Enter your Email here")
#entering password
pass_box = driver.find_element_by_xpath('//*[@id="j_password"]')
pass_box.send_keys("Enter Your Password here")

button = driver.find_element_by_xpath('/html/body/form/div/div[2]/input[1]')
button.click()

#opening drawing
button2 = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/span')
button2.click()

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
my_list = [[]]
#my_list.append([])

for row in rows:
    #setting cols equal to the columns in row i
    i = 0
    cols = row.find_elements_by_tag_name("td")
    if len(cols) == 17:
        grade = cols[12].text
        grade = grade.split('/')
        print(grade)
        try:
            my_list[i].append(int(grade[0]))
            my_list[i].append(int(grade[1].split('\n')[0]))
            i+=1
            print(my_list)
        except Exception as err:
            print(err)
            continue
    """
    if len(cols)==17:
         results = [x.strip() for x in cols[12].text.split('/')]
         if(len(results)>1):
            my_list[i][0].append(results[0] )
            total=(results[1].split('\n')[0])
    """
print(my_list)
driver.close()

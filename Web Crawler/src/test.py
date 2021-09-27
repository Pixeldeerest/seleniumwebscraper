from selenium import webdriver
import re
import csv
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import string


DRIVER_PATH = "C:/Users/Student/workspace/Test/webdrivers/chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.montmere.com/test.php')


wait = WebDriverWait(driver, 10)

#Create a loop variable to keep track of the success of the code block
#Essentially, the loop will continue to try/refresh the web page until it is able to find the CSS selectors that the code is looking for
i = 0
while i == 0:
    #Try the below block of code
    try:
        #find the HTML element with ID of username
        username = driver.find_element_by_css_selector('#username')
        #input the text 'test' into the username field
        username.send_keys('test')
        
        #find the HTML element with ID of password
        password = driver.find_element_by_css_selector('#password')
        #input the text 'test' into the password field
        password.send_keys('test')
        
        #find the HTML element that submit the form
        submit = driver.find_element_by_css_selector('#login > input[type=submit]:nth-child(6)')
        #click the submit
        submit.click()
        
        #increment the variable in order to denote that the actions within the try block succeeded
        #exit the while loop as a result
        i+= 1
    
    #If the NoSuchElementException is encountered, refresh the page
    except NoSuchElementException:
        driver.refresh()


#Create a loop variable to keep track of the success of the code block
#Essentially, the loop will continue to try/refresh the web page until it is able to find the CSS selectors that the code is looking for
e = 0
while e == 0:
    try: 
        #the browser will wait to see if it can find the particular table row/table head element it is looking for
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/table[1]/tr[1]/th[1]")))       
        #increment the loop variable to let our code know to break the loop
        e += 1
        
    #if the specified element is not found, refresh the web page
    except:
        driver.refresh()

#find the table element and save it to a variable
table = driver.find_element_by_xpath("/html/body/div/div[2]/div/table[1]")
#find all of the row elements and save them 
rows = table.find_elements_by_css_selector("tr")


#initialize an empty list variable to hold the list of rows
table_list = []

#iterate over each row in the rows from above
for row in rows:
    #initialize an empty list variable to hold the table heads and table data
    row_list = []
    #add the th and td data into the row_list
    for data in row.find_elements_by_xpath("./th|./td"):
        row_list.append(data.text)
    #add the list of row data to the table list
    table_list.append(row_list)
        

#for each piece of data in the table list, as it exists within a row, add it to the CSV file, and make each row a new line     
with open('tpa_stream.csv', 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerows(table_list)
    
driver.close()

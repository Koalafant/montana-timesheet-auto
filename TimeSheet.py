import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

import getpass

def main():
    #input credentials
    username = input("NetID: ")
    password = getpass.getpass("Password: ")
    testHours = 1

    #open Edge (to be implemented: chrome and firefox functionality
    driver = webdriver.Edge()
    driver.maximize_window()
    #navigate through MyInfo
    driver.get("https://montana.edu/students")
    driver.find_element(By.LINK_TEXT, 'MyInfo').click()

    driver.find_element(By.LINK_TEXT, 'Log in to MyInfo (NetID)').click()

    #identify user and password fields
    userBox = driver.find_element(By.ID, 'username')
    passBox = driver.find_element(By.ID, 'password')

    #input username and password
    userBox.send_keys(username)
    passBox.send_keys(password)

    #navigate to TimeSheet
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    #wait for page to load -- issues
    time.sleep(1)
    driver.find_elements(By.LINK_TEXT, 'Employee Services')[0].click()
    driver.find_element(By.LINK_TEXT, 'Time Sheet').click()

    #configure day/time
    driver.find_element(By.XPATH, '//input[@type="submit" and @value="Time Sheet"]').click()

    monthDay = driver.find_elements(By.CLASS_NAME, 'dddefault')[2].text.split(",")
    #month holds current month. Day holds day start of week (str)
    month = monthDay[0]
    day = monthDay[1]
    if(month == "Jan" or month == "Mar" or month == "May" or month == "July" or month == "Sep" or month == "Nov"):
        monthEnd = 31
    elif(month == "Feb"):
            monthEnd = 28
    else:
        monthEnd = 30

    try:
        dayEntries = (driver.find_elements(By.LINK_TEXT, 'Enter Hours'))
    except Exception:
        dayEntries = (driver.find_elements(By.LINK_TEXT, '0'))

    #fill out not overtime entries
    for x in dayEntries:
        if x == 0 or x == 1:
            pass
        else:
            dayEntries[x].click()
            driver.find_element(By.ID, 'hours_id').send_keys(Keys.BACKSPACE)
            driver.find_element(By.ID, 'hours_id').send_keys(Keys.BACKSPACE)
            driver.find_element(By.ID, 'hours_id').send_keys(testHours)
            driver.find_element(By.XPATH, '//input[@value="Save"]').click()
            try:
                dayEntries = (driver.find_elements(By.LINK_TEXT, 'Enter Hours'))
            except Exception:
                dayEntries = (driver.find_elements(By.LINK_TEXT, '0'))


    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    main()

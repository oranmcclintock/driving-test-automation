import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#User details
booking_reference = 'xxxxxxxxxx'
driver_no = 'xxxxxxxx'
date_of_birth = 'xxxxxxxx'

driver = webdriver.Chrome()
driver.get('https://dva-bookings.nidirect.gov.uk/MyBookings/FindDriver')

#Log in using Selenium
def login():
    try:

        #Access website
        driver = webdriver.Chrome()
        driver.get('https://dva-bookings.nidirect.gov.uk/MyBookings/FindDriver')

        #Enter details
        driver.find_element(By.NAME, 'BookingReference').send_keys(booking_reference)
        driver.find_element(By.NAME, 'DriverNo').send_keys(driver_no)
        driver.find_element(By.NAME, 'DateOfBirth').send_keys(date_of_birth)
        driver.find_element(By.ID, 'btnFind').click()

        #Allow time for page to change
        time.sleep(1)
        driver.find_element(By.ID, 'btnChange').click()

        #Keep the program open
        time.sleep(360)

        #Close browser
        driver.quit()

    #Print error
    except Exception as e:
        print('Exception occurred:', e)
        print('In the queue. Retrying...\n')
        time.sleep(5)

login()

# Bot to automatically create email accounts at gazeta.pl
#
# It uses:
# * selenium chromedriver to locate and fill form inputs
# * pyautogui to deal with capchta
#
# Works just fine, but can't defeat capchta yet...

from selenium import webdriver
import pyautogui
import time


class User:

    def __init__(self, login, password, current_email, gender, birth_date):
        self.login = login
        self.password = password
        self.email = login + '@gazeta.pl'
        self.current_email = current_email
        self.gender = gender
        self.birth_date = birth_date

    def __str__(self):
        return self.login


for i in range(5):

    user1 = User('test_monkey' + str(29), '********', 'psor2.0@gmail.com', 'male', '2000-12-21')

    file = open('email_db.txt', 'a')
    file.write(str(user1.email) + '\n')

    url = 'https://konto.gazeta.pl/konto/rejestracja.do'
    driver_path = '/home/hp/Pobrane/chromedriver'

    driver = webdriver.Chrome(driver_path)
    driver.get(url)

    # click anywhere to tell the gui we're in a browser window
    # and to hide a rodo pop-up
    pyautogui.click(200, 200)

    driver.find_element_by_id('login').send_keys(user1.login)
    driver.find_element_by_id('pass').send_keys(user1.password)
    driver.find_element_by_id('emailPassRecovery').send_keys(user1.current_email)

    if user1.gender == 'female':
        driver.find_element_by_id('sex1').click()
    else:
        driver.find_element_by_id('sex2').click()

    driver.find_element_by_id('birthDate').send_keys(user1.birth_date)

    pyautogui.scroll(-10)  # scroll down to see a capchta

    # fill a capchta
    # I've used pyautogui, because selenium couldn't locate a capchta by class name
    # I don't know why single click doesn't work...
    pyautogui.doubleClick(455, 475, interval=0.1)

    driver.find_element_by_id('acceptEmailAccountTerms').click()
    driver.find_element_by_id('acceptAll').click()

    driver.find_element_by_class_name('btn').click()

    time.sleep(5)
    
    driver.close()


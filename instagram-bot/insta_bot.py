# Bot to automatically create Instagram accounts
# Works fine as expected, we'll see what will occur during tests...

from selenium import webdriver
import pyautogui
from time import sleep

from instagram_bot.user import User


# it's basically a wrapper for e.g.
# driver.find_element_by_name('emailOrPhone').send_keys(user.email)
# sleep(1)
def type_slowly(driv, field_name, send_keys_arg):

    for char in range(len(send_keys_arg)):
        driv.find_element_by_name(field_name).send_keys(send_keys_arg[char])
        sleep(0.2)


# user_list = []

for i in range(100):

    email = 'test_monkey' + str(10 + i) + '@gazeta.pl'
    password = '********'

    user = User(i, email, password)
    user.save_to_file()

    # user_list.append(user)

    url = 'https://www.instagram.com/accounts/emailsignup/'
    driver_path = '/home/hp/Pobrane/chromedriver'

    driver = webdriver.Chrome(driver_path)
    driver.get(url)

    pyautogui.click(950, 200)  # hide the cookies
    sleep(1)

    driver.find_element_by_name('emailOrPhone').click()
    sleep(1)

    type_slowly(driver, 'emailOrPhone', user.email)
    type_slowly(driver, 'fullName', user.name)
    type_slowly(driver, 'username', user.login)
    type_slowly(driver, 'password', user.password)

    # driver.find_element_by_xpath('button[@type="submit"]').click()
    # driver.find_element_by_class_name('_0mzm- sqdOP  L3NKy       ').click()
    pyautogui.click(525, 625)  # submit
    sleep(1)
    pyautogui.click(355, 655)  # confirm you're 18+
    sleep(1)
    pyautogui.click(525, 740)  # submit again

    sleep(5)

    driver.close()

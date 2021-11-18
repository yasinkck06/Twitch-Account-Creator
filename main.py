from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random,string
import os
print("Yasin + Oberonskiiv2 Twitch Account Creator V2")
print("For help DM: Yasin#0009 or Oberonskiiv2#4620 on Discord")
createdaccounts = 0
howmany = int(input("How many accounts you want to generate: "))
howcooldown = int(input("How many seconds the cooldown of creating Accounts should be: "))

if howcooldown < 1:
    print('You cannot wait ' + str(howcooldown) + ' seconds')
    time.sleep(3)
    quit()

while createdaccounts < howmany:
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    dictionary = open("Data/userdictionary.txt")
    lines = dictionary.readlines()
    createdaccounts = createdaccounts + 1

    username = random.choice(lines)
    password = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
    email = username + '@gmail.com'
    tokenlist = open("tokens.txt", "a")
    accountlist = open("accounts.txt", "a")
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://twitch.com")
    
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button/div/div').click()
    time.sleep(2)
    print("Entering Account-Information")
    driver.find_element_by_xpath('//*[@id="signup-username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password-input"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="password-input-confirmation"]').send_keys(password)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[1]/div/input').send_keys(
        "27")
    Select(driver.find_element_by_xpath(
        '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[2]/select')).select_by_value(
        "8")
    driver.find_element_by_xpath(
        '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[3]/div/input').send_keys(
        "1998")
    driver.find_element_by_xpath('//*[@id="email-input"]').send_keys(email)

    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[5]/button/div/div').click()
    os.system('cls')
    input("Hit enter when your done solving the captcha.")

    driver.refresh()
    time.sleep(1)
    print("Writing Token into tokens.txt")
    tokenvalue = driver.get_cookie('auth-token')
    tokenlist.write("\n")
    tokenlist.write(tokenvalue["value"])
    driver.close()

    print("Writing Account-Information into accounts.txt")
    accountvalue = username + ":" + password
    accountlist.write("\n")
    accountlist.write(accountvalue)

    print("Account succesfully created")
    print('Waiting ' + str(howcooldown) + 'seconds')
    time.sleep(howcooldown)

else:
    print('Succesfully created ' + str(howmany) + ' account/s')
    quti = input("Hit Enter to quit")
    quit()

    

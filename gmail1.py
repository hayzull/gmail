from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://gmail.com')

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('dannabob5@gmail.com')

loginElem = browser.find_element_by_id('next')
loginElem.click()

print('Input your password')
userPassword = input()

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys(userPassword)

passwordElem.submit()

composeElem = browser.find_element_by_id('z0')
composeElem.click()
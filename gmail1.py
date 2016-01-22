from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://yahoo.com')

loginElem = browser.find_element_by_link_text('Mail')
loginElem.click()

emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('dannabob5@yahoo.com')

passElem = browser.find_element_by_id('login-passwd')
passElem.send_keys('hellogoodbye')

signElem = browser.find_element_by_id('login-signin')
signElem.click()

composeElem = browser.find_element_by_id('Compose')
composeElem.click()

print('Who are you sending this email to?')
sendTo = input()

sendtoElem = browser.find_element_by_id('to-field')
sendtoElem.send_keys(sendTo)

print('What is the subject?')
subjectLine = input()

subjectElem = browser.find_element_by_id('subject-field')
subjectElem.send_keys(subjectLine)

print('What is going to be written in the body?')
bodyLine = input()

bodyElem = browser.find_element_by_id('rtetext')
bodyElem.send_keys (bodyLine)

time.sleep(3)

sendElem = browser.find_element_by_link_text('Send')
sendElem.click()
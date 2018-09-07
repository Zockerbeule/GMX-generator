from selenium import webdriver
import time

url = 'https://registrierung.gmx.net/#.pc_page.mail.index.hero_1.registrierung'

driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
driver.get(url)

driver.find_element_by_class_name('pos-form-element').send_keys('EmailPrefix')

driver.find_element_by_name('salutation').click()

driver.find_element_by_xpath('//*[@data-test="first-name-input"]').send_keys('FirstName')
driver.find_element_by_xpath('//*[@data-test="last-name-input"]').send_keys('LastName')
driver.find_element_by_xpath('//*[@data-test="postal-code-input"]').send_keys('ZIP-Code')
driver.find_element_by_xpath('//*[@data-test="town-input"]').send_keys('City')
driver.find_element_by_xpath('//*[@data-test="street-and-number-input"]').send_keys('Street')
driver.find_element_by_xpath('//*[@data-test="day"]').send_keys('BithdayDay')
driver.find_element_by_xpath('//*[@data-test="month"]').send_keys('BirthdayMonth')
driver.find_element_by_xpath('//*[@data-test="year"]').send_keys('BithdayYear')
driver.find_element_by_id('password').send_keys('Password')
driver.find_element_by_id('confirm-password').send_keys('Password')
driver.find_element_by_class_name('pos-input-checkbox__checker').click()
time.sleep(3)
driver.find_element_by_id('contactEmail').send_keys('ConfirmationMail')

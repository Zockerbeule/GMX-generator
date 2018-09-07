from selenium import webdriver
import time

url = 'https://registrierung.gmx.net/#.pc_page.mail.index.hero_1.registrierung'

driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
driver.get(url)

driver.find_element_by_class_name('pos-form-element').send_keys('marlonbuga19')

driver.find_element_by_name('salutation').click()

driver.find_element_by_xpath('//*[@data-test="first-name-input"]').send_keys('Marlon')
driver.find_element_by_xpath('//*[@data-test="last-name-input"]').send_keys('Buga')
driver.find_element_by_xpath('//*[@data-test="postal-code-input"]').send_keys('97318')
driver.find_element_by_xpath('//*[@data-test="town-input"]').send_keys('Kitzingen')
driver.find_element_by_xpath('//*[@data-test="street-and-number-input"]').send_keys('Friedrich Ebert Strasse 13')
driver.find_element_by_xpath('//*[@data-test="day"]').send_keys('20')
driver.find_element_by_xpath('//*[@data-test="month"]').send_keys('04')
driver.find_element_by_xpath('//*[@data-test="year"]').send_keys('1995')
driver.find_element_by_id('password').send_keys('Ma2004Do')
driver.find_element_by_id('confirm-password').send_keys('Ma2004Do')
driver.find_element_by_class_name('pos-input-checkbox__checker').click()
time.sleep(3)
driver.find_element_by_id('contactEmail').send_keys('zockerbeule@gmx.de')

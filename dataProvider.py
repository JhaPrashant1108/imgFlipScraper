from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')

url = "https://imgflip.com/memegenerator/Running-Away-Balloon"

driver.get(url)
time.sleep(5)
print(len(driver.find_elements_by_class_name('drag-box')))
print(driver.find_elements_by_class_name('drag-box')[0].get_attribute('style'))
print(driver.find_elements_by_class_name('drag-box')[1].get_attribute('style'))
print(driver.find_elements_by_class_name('drag-box')[2].get_attribute('style'))
print(driver.find_elements_by_class_name('drag-box')[3].get_attribute('style'))
print(driver.find_elements_by_class_name('drag-box')[4].get_attribute('style'))


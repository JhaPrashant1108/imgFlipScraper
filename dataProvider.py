from selenium import webdriver
import json
import time

driver = webdriver.Chrome('chromedriver.exe')

# url = "https://imgflip.com/memegenerator/Running-Away-Balloon"

# driver.get(url)
# time.sleep(5)
# print(len())
# print()
# print(driver.find_elements_by_class_name('drag-box')[1].get_attribute('style'))
# print(driver.find_elements_by_class_name('drag-box')[2].get_attribute('style'))
# print(driver.find_elements_by_class_name('drag-box')[3].get_attribute('style'))
# print(driver.find_elements_by_class_name('drag-box')[4].get_attribute('style'))
imgLinkDict = {}
outFile = open("imgLinks.json", ) 
data = json.load(outFile)

for i in range(816):
    driver.get(data['Image'+str(i+1)]['Template Link'])
    print("scraping Image"+str(i+1))
    time.sleep(2)
    textField = driver.find_elements_by_class_name('drag-box')
    textFieldNumber = len(textField)
    styles = []
    for k in range(len(driver.find_elements_by_class_name('drag-box'))):
        styles.append(driver.find_elements_by_class_name('drag-box')[k].get_attribute('style'))
    imgLinkDict['Image'+str(i+1)]={'Title':data['Image'+str(i+1)]['Title'],
                                'Image Link':data['Image'+str(i+1)]['Image Link'],
                                'Template Link':data['Image'+str(i+1)]['Template Link'],
                                'Preview Image Link':data['Image'+str(i+1)]['Preview Image Link'],
                                'Text Fields':textFieldNumber,
                                'Styles':styles}
    print(imgLinkDict['Image'+str(i+1)])

outFileFinal = open("imgLinksFinal.json", "w") 
	
json.dump(imgLinkDict, outFileFinal, indent = 4) 
	
outFile.close() 
driver.close()
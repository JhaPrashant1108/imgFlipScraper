import requests
from bs4 import BeautifulSoup
import json 

imgLinkDict = {}

basicUrl = "https://imgflip.com"
url = "https://imgflip.com/memetemplates?page="
imageUrl = "https://imgflip.com/s/meme/"
memeGenerator = "https://imgflip.com/memegenerator"


for i in range(21):
    getUrl = url+str(i+1)
    htmlContent = requests.get(getUrl).content
    soup = BeautifulSoup(htmlContent,'html.parser')
    for divs in soup.findAll("div",{"class":"mt-box"}):
        previewImage = 'https:'+divs.find("img",{"class":"shadow"})['src']
        imgLinks = divs.find("a",{"class":"mt-caption l but"})
        name = imgLinks['title'].replace(" Meme Generator","")
        link = imageUrl+imgLinks['href'].split("/")[2]+".jpg"
        generator = memeGenerator+"/"+imgLinks['href'].split("/")[2]
        imgLinkDict[str(name)]={'Title':name,'Image Link':link,'Template Link':generator,'Preview Image Link':previewImage}
        
	


	
outFile = open("imgLinks.json", "w") 
	
json.dump(imgLinkDict, outFile, indent = 4) 
	
outFile.close() 

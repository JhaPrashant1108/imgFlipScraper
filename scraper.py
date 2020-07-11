import requests
from bs4 import BeautifulSoup
import json 

imgLinkDict = {}

basicUrl = "https://imgflip.com"
url = "https://imgflip.com/memetemplates?page="
imageUrl = "https://imgflip.com/s/meme/"



for i in range(21):
    getUrl = url+str(i+1)
    print(getUrl)
    htmlContent = requests.get(getUrl).content
    soup = BeautifulSoup(htmlContent,'html.parser')
    for imgLinks in soup.findAll("a",{"class":"mt-caption l but"}):
        name = imgLinks['title'].replace(" Meme Generator","")
        link = imageUrl+imgLinks['href'].split("/")[2]+".jpg"
        print(name+":-"+link)
        imgLinkDict.update({name:link})

	


	

out_file = open("imgLinks.json", "w") 
	
json.dump(imgLinkDict, out_file, indent = 4) 
	
out_file.close() 

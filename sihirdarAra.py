from bs4 import BeautifulSoup
import requests




isim = input("Sihirdar adını gir --> ")
url ="https://tr.op.gg/summoner/userName="
isim_parca =isim.split()
if len(isim_parca)==1:
    url=url+isim
else :
    url =url+isim_parca[0]
    for i in range(0,len(isim_parca)):
        url=url+"+"+isim_parca[i]
    




    
haders_parameters={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
glassdor=requests.get(url,haders_parameters)
jobs=glassdor.content
soup = BeautifulSoup(jobs,"html.parser")
elo = soup.find("div",{"class":"TierRank"}).text
oran=soup.find("span",{"class":"winratio"}).text
en_cok_oynanan_champ =soup.find("div",{"class":"ChampionName"}).text
sampiyon=en_cok_oynanan_champ.split()
print(f"{isim} adlı sihirdarın ; \n\n Elosu :{elo}\n {oran}\n En cok oynadığı sampiyon : {sampiyon[0]}")

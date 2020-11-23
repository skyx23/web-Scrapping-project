import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/asus-rog-strix-g15-core-i7-10th-gen-16-gb-1-tb-ssd-windows-10-home-4-gb-graphics-nvidia-geforce-gtx-1650-ti-144-hz-g512li-hn085t-gaming-laptop/p/itma045e09e44af6?pid=COMFT8GXH89GATFZ&lid=LSTCOMFT8GXH89GATFZTV0PA5&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_823f80ef-056c-4508-9447-012285ab8e32_4_F4P7IUP122_MC.COMFT8GXH89GATFZ&ppt=clp&ppn=gaming-laptops-store&ssid=mcytoci7ps0000001606114193490&otracker=clp_pmu_v2_Asus%2BGaming%2BLaptops_2_4.productCard.PMU_V2_Asus%2BROG%2BStrix%2BG15%2BCore%2Bi7%2B10th%2BGen%2B-%2B%252816%2BGB%252F1%2BTB%2BSSD%252FWindows%2B10%2BHome%252F4%2BGB%2BGraphics%252FNVIDIA%2BGeforce%2BGTX%2B1650%2BTi%252F144%2BHz%2529%2BG512LI-HN085T%2BGaming%2BLaptop_gaming-laptops-store_COMFT8GXH89GATFZ_neo%2Fmerchandising_1&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Asus%2BGaming%2BLaptops_LIST_productCard_cc_2_NA_view-all&cid=COMFT8GXH89GATFZ"

r = requests.get(url)

soup = BeautifulSoup(r.content,"html5lib")

def title():
    title = soup.find(class_='B_NuCI').get_text()
    print(title)

def price():  
    price = soup.find(class_="_30jeq3 _16Jk6d").get_text()
    print(price)

def offers() :
    offers = soup.find_all('li',class_='_16eBzU')
    for x in range(len(offers)) :
        offer = offers[x].get_text()
        print(offer)

def highlights():
     highlights = soup.find_all("li",class_="_21Ahn-") 
     for x in range(len(highlights)):
         highlight = highlights[x].get_text()
         print(highlight)

def description():
    description = soup.find("div",class_="_1mXcCf").get_text()
    print(description)

print("What would you like to know about the product we are monitoring ?")
print("1. Name/Title of the product")
print("2. Price of the product")
print('3. Offers on the product.')
print('4. highlights of the product.')
print("5. Description on the product.")

x = input("Please Enter Your Choice : ")

if x =="1" :
    title()
elif x == "2" :
    price()
elif x == "3" :
    offers()
elif x == "4" :
    highlights()
elif x == "5" :
    description()
else :
    print("INVAlID OPTION")



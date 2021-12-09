from bs4 import BeautifulSoup  #pip install bs4
import requests #pip install requests
import pandas as pd #pip install pandas


page_num = input("Enter the number of pages you want to Scrap: ") # One page has 24 devices (Enter more than 2 for 40+ entries)(Total pages = 4)
phone_name = []
phone_price = []
phone_rating = []
for i in range(1,int(page_num)+1):
    url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DPOCO&otracker=clp_metro_expandable_2_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_O1WYX08RHODP_wp3&fm=neo%2Fmerchandising&iid=M_5fd73371-d652-4a6d-bcb8-e33b703e5957_3.O1WYX08RHODP&ppt=hp&ppn=homepage&ssid=aiolyys8n40000001639052068148&page=" + str(i)
    req = requests.get(url)
    content = BeautifulSoup(req.content,'html.parser')
    name = content.find_all('div', {"class":"_4rR01T"})
    price = content.find_all('div', {"class":"_30jeq3 _1_WHN1"})
    rating = content.find_all('div', {"class":"_3LWZlK"})
    
    for i in name:
        phone_name.append(i.text)
    for i in price:
        phone_price.append(i.text[1:]) #Sliced the string to avoid the Rupees symbol
    for i in rating:
        phone_rating.append(i.text)

data = {"Name": phone_name, "Price (in Rs)": phone_price, "Rating":phone_rating}
df = pd.DataFrame(data)
print(df)
df.to_csv('test.csv')

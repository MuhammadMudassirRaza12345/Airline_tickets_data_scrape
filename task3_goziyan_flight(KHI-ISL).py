# ----Run1--
import requests
import json
import pandas as pd 

url = "https://production.gozayaan.com/api/flight/search/"

# I Create Dictionary in Which i passed date , current location and destination and put into payload so it
# is automatically takes as input for search

# ----Run2--
data={
  "adult": 1,
  "child": 0,
  "child_age": [],
  "infant": 0,
  "cabin_class": "Economy",
  "trips": [
    {
      "origin": "KHI",
      "destination":"ISB" ,
      "preferred_time": "2023-02-24"
    }
  ],
  "currency": "PKR",
  "region": "PK",
  "segment_id": "779d3eb1-e97b-4c94-ba2d-7f68c49238ff",
  "platform_type": "GZ_WEB"
} 
# ----Run3-- 
#  This take input from user date for flight , current place and destination 

for i in range(0,1):
    journey_date=input('Enter the date for which you want to check the ticket e.g:(2023-02-24)(year-Month-Day):')
    data["trips"][0]["preferred_time"]=journey_date
    starting_point=input('Enter the place from where you want to fly e.g(KHI,ISB,LHE):')
    data["trips"][0]["origin"]=starting_point
    ending_point=input('Enter the place destination e.g(KHI,ISB,LHE):')
    data["trips"][0]["destination"]=str(ending_point)
    print(data)
# ----Run4--   
payload = json.dumps(data)
print(payload)    

# ----Run5--
headers = {
  'authority': 'production.gozayaan.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ru;q=0.7',
  'content-type': 'application/json',
  'origin': 'https://www.gozayaan.com',
  'referer': 'https://www.gozayaan.com/',
  'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# ----Run6--
response = requests.request("POST", url, headers=headers, data=payload)
# print(response.text)

# Then i convert data from str to dictionary for view
# ----Run7--
son=response.json()

# Then Check Keys
son.keys()

# O:dict_keys(['error', 'result', 'status'])
son['status']

# print(son['result']['results'][0]['flights'][0]['origin'])
# print( son['result']['results'][0]['flights'][0]['destination'])
# print(son['result']['results'][0]['flights'][0]["options"][0]["departure_time"]) 
# print(son['result']['results'][0]['flights'][0]["options"][0]["arrival_time"])  
# print(son['result']['results'][0]["total_price"])  
# print(son['result']['results'][0]['flights'][0]['preferred_time'] )  
# print(son['result']['results'][0]['flights'][0])
# print(son['result']['results'][0])  
 
#  origin=son['result']['results'][i]['flights'][0]['origin']
#   print(origin)
#   destination=son['result']['results'][i]['flights'][0]['destination']
#   departure_time=son['result']['results'][i]['flights'][0]["options"][0]["departure_time"]
#   arrival_time=son['result']['results'][i]['flights'][0]["options"][0]["arrival_time"]
#   fare=son['result']['results'][i]["total_base_price"]
#   preferred_date=son['result']['results'][i]['flights'][0]['preferred_time']

# ----Run8-- 
df6=pd.DataFrame()

# ----Run 8b-- 
for i in range(len(son['result']['results'])):
  flight_names=son['result']['results'][i]['flights'][0]['plating_carrier']['name']
  origin=son['result']['results'][i]['flights'][0]['origin']
  destination=son['result']['results'][i]['flights'][0]['destination']
  departure_time=son['result']['results'][i]['flights'][0]["options"][0]["departure_time"]
  arrival_time=son['result']['results'][i]['flights'][0]["options"][0]["arrival_time"]
  actual_price=son['result']['results'][0]["total_price"]
  print(actual_price)
#   here in guziyan no keys present in which discount price present so i will try manually not sucess
#   try :
#     discount=son['result']['results'][0]['discount']['discount_name']
#     discount_price=son['result']['results'][0]['discount']['discount_markup']['markup_amount'] 
#     Final_Discount_price=int(float(discount_price))  * actual_price /100
#     print(Final_Discount_price)
#   except :
#     pass
  flight_dict={
    "flightname":flight_names,
    "departure_time":departure_time,
    "arrival_time":arrival_time, 
    "origin":origin,
    "destination":destination,
    "fare": actual_price
  }
  df6=df6.append(flight_dict,ignore_index=True)

# ----Run9--    
print(df6)  

# ***********KHI TO ISL******************

# OUTPUT:=========>24-FEB-2023<========= 

# #                         flightname       departure_time         arrival_time origin destination     fare
# # 0                         AIR SIAL  2023-02-24 19:00:00  2023-02-24 21:00:00    KHI         ISB  15850.0
# # 1                         AIR SIAL  2023-02-24 07:00:00  2023-02-24 09:00:00    KHI         ISB  15850.0
# # 2                         Air Blue  2023-02-24 21:00:00  2023-02-24 23:00:00    KHI         ISB  15850.0
# # 3                         AIR SIAL  2023-02-24 19:00:00  2023-02-24 21:00:00    KHI         ISB  15850.0
# # 4                         AIR SIAL  2023-02-24 07:00:00  2023-02-24 09:00:00    KHI         ISB  15850.0
# # 5                         AIR SIAL  2023-02-24 13:00:00  2023-02-24 15:00:00    KHI         ISB  15850.0
# # 6  Pakistan International Airlines  2023-02-24 07:00:00  2023-02-24 08:55:00    KHI         ISB  15850.0
# # 7  Pakistan International Airlines  2023-02-24 13:00:00  2023-02-24 14:55:00    KHI         ISB  15850.0
# # 8  Pakistan International Airlines  2023-02-24 16:00:00  2023-02-24 17:55:00    KHI         ISB  15850.0
# # 9                         AIR SIAL  2023-02-24 13:00:00  2023-02-24 15:00:00    KHI         ISB  15850.0

# # OUTPUT: =========>25-FEB-2023<========= 
# flightname       departure_time         arrival_time origin destination     fare
# 0                         AIR SIAL  2023-02-25 19:00:00  2023-02-25 21:00:00    KHI         ISB  15850.0
# 1                         AIR SIAL  2023-02-25 07:00:00  2023-02-25 09:00:00    KHI         ISB  15850.0
# 2                         Air Blue  2023-02-25 21:00:00  2023-02-25 23:00:00    KHI         ISB  15850.0
# 3                         AIR SIAL  2023-02-25 19:00:00  2023-02-25 21:00:00    KHI         ISB  15850.0
# 4                         AIR SIAL  2023-02-25 07:00:00  2023-02-25 09:00:00    KHI         ISB  15850.0
# 5                         AIR SIAL  2023-02-25 13:00:00  2023-02-25 15:00:00    KHI         ISB  15850.0
# 6  Pakistan International Airlines  2023-02-25 07:00:00  2023-02-25 08:55:00    KHI         ISB  15850.0
# 7  Pakistan International Airlines  2023-02-25 13:00:00  2023-02-25 14:55:00    KHI         ISB  15850.0
# 8  Pakistan International Airlines  2023-02-25 16:00:00  2023-02-25 17:55:00    KHI         ISB  15850.0
# 9  Pakistan International Airlines  2023-02-25 20:00:00  2023-02-25 21:55:00    KHI         ISB  15850.0
# OUTPUT: =========>26-FEB-2023<========= 
#                         flightname       departure_time         arrival_time origin destination     fare
# 0                         Air Blue  2023-02-26 21:00:00  2023-02-26 23:00:00    KHI         ISB  14000.0
# 1                         AIR SIAL  2023-02-26 19:00:00  2023-02-26 21:00:00    KHI         ISB  14000.0
# 2                         AIR SIAL  2023-02-26 07:00:00  2023-02-26 09:00:00    KHI         ISB  14000.0
# 3                         AIR SIAL  2023-02-26 19:00:00  2023-02-26 21:00:00    KHI         ISB  14000.0
# 4                         AIR SIAL  2023-02-26 07:00:00  2023-02-26 09:00:00    KHI         ISB  14000.0
# 5                         AIR SIAL  2023-02-26 13:00:00  2023-02-26 15:00:00    KHI         ISB  14000.0
# 6  Pakistan International Airlines  2023-02-26 07:00:00  2023-02-26 08:55:00    KHI         ISB  14000.0
# 7  Pakistan International Airlines  2023-02-26 13:00:00  2023-02-26 14:55:00    KHI         ISB  14000.0
# 8  Pakistan International Airlines  2023-02-26 16:00:00  2023-02-26 17:55:00    KHI         ISB  14000.0
# 9                         AIR SIAL  2023-02-26 13:00:00  2023-02-26 15:00:00    KHI         ISB  14000.0

# ***********ISL TO KHI ******************

# OUTPUT:=========>24-FEB-2023<========= 

#                         flightname       departure_time         arrival_time origin destination     fare
# 0                         AIR SIAL  2023-02-24 10:00:00  2023-02-24 11:59:00    ISB         KHI  15850.0
# 1                         AIR SIAL  2023-02-24 22:00:00  2023-02-24 23:59:00    ISB         KHI  15850.0
# 2                         Air Blue  2023-02-24 18:00:00  2023-02-24 20:00:00    ISB         KHI  15850.0
# 3                         AIR SIAL  2023-02-24 16:00:00  2023-02-24 18:00:00    ISB         KHI  15850.0
# 4                         AIR SIAL  2023-02-24 10:00:00  2023-02-24 11:59:00    ISB         KHI  15850.0
# 5                         AIR SIAL  2023-02-24 22:00:00  2023-02-24 23:59:00    ISB         KHI  15850.0
# 6                         AIR SIAL  2023-02-24 16:00:00  2023-02-24 18:00:00    ISB         KHI  15850.0
# 7  Pakistan International Airlines  2023-02-24 10:00:00  2023-02-24 11:55:00    ISB         KHI  15850.0
# 8  Pakistan International Airlines  2023-02-24 19:00:00  2023-02-24 20:55:00    ISB         KHI  15850.0
# 9  Pakistan International Airlines  2023-02-24 21:00:00  2023-02-24 22:55:00    ISB         KHI  15850.0

# OUTPUT: =========>25-FEB-2023<========= 
#                         flightname       departure_time         arrival_time origin destination     fare
# 0                         AIR SIAL  2023-02-25 10:00:00  2023-02-25 11:59:00    ISB         KHI  15850.0
# 1                         AIR SIAL  2023-02-25 22:00:00  2023-02-25 23:59:00    ISB         KHI  15850.0
# 2                         Air Blue  2023-02-25 18:00:00  2023-02-25 20:00:00    ISB         KHI  15850.0
# 3                         AIR SIAL  2023-02-25 10:00:00  2023-02-25 11:59:00    ISB         KHI  15850.0
# 4                         AIR SIAL  2023-02-25 22:00:00  2023-02-25 23:59:00    ISB         KHI  15850.0
# 5                         AIR SIAL  2023-02-25 16:00:00  2023-02-25 18:00:00    ISB         KHI  15850.0
# 6  Pakistan International Airlines  2023-02-25 10:00:00  2023-02-25 11:55:00    ISB         KHI  15850.0
# 7  Pakistan International Airlines  2023-02-25 16:00:00  2023-02-25 17:55:00    ISB         KHI  15850.0
# 8  Pakistan International Airlines  2023-02-25 19:00:00  2023-02-25 20:55:00    ISB         KHI  15850.0
# 9                         AIR SIAL  2023-02-25 16:00:00  2023-02-25 18:00:00    ISB         KHI  15850.0

# OUTPUT: =========>26-FEB-2023<========= 
#  flightname       departure_time         arrival_time origin destination     fare
# 0                         Air Blue  2023-02-26 18:00:00  2023-02-26 20:00:00    ISB         KHI  15490.0
# 1                         AIR SIAL  2023-02-26 10:00:00  2023-02-26 11:59:00    ISB         KHI  15490.0
# 2                         AIR SIAL  2023-02-26 22:00:00  2023-02-26 23:59:00    ISB         KHI  15490.0
# 3                         AIR SIAL  2023-02-26 10:00:00  2023-02-26 11:59:00    ISB         KHI  15490.0
# 4                         AIR SIAL  2023-02-26 16:00:00  2023-02-26 18:00:00    ISB         KHI  15490.0
# 5                         AIR SIAL  2023-02-26 22:00:00  2023-02-26 23:59:00    ISB         KHI  15490.0
# 6  Pakistan International Airlines  2023-02-26 10:00:00  2023-02-26 11:55:00    ISB         KHI  15490.0
# 7  Pakistan International Airlines  2023-02-26 11:00:00  2023-02-26 14:40:00    ISB         KHI  15490.0
# 8  Pakistan International Airlines  2023-02-26 19:00:00  2023-02-26 20:55:00    ISB         KHI  15490.0
# 9  Pakistan International Airlines  2023-02-26 21:00:00  2023-02-26 22:55:00    ISB         KHI  15490.0

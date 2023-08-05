# ----Run1--
import requests
import json
import pandas as pd
url = "https://www.sastaticket.pk/api/v4/flights/" 

# I Create Dictionary in Which i passed date , current location and destination and put into payload so it
# is automatically takes as input for search

# ----Run2--
data={
    "route_type": "ONEWAY",
  "cabin_class": {
    "code": "Y",
    "label": "Economy"
  },
  "traveler_count": {
    "num_adult": 1,
    "num_child": 0,
    "num_infant": 0
  },
  "legs": [
    {
      "departure_date": "2023-02-24",
      "origin": "KHI",
      "destination": "ISB"
    }
  ]
}
 

for i in range(0,1):
    journey_date=input('Enter the date for which you want to check the ticket e.g:(2023-02-24)(year-Month-Day):')
    data["legs"][0]["departure_date"]=journey_date
    starting_point=input('Enter the place from where you want to fly e.g(KHI,ISB,LHE):')
    data["legs"][0]["origin"]=starting_point
    ending_point=input('Enter the place destination e.g(KHI,ISB,LHE):')
    data["legs"][0]["destination"]=str(ending_point)
    print(data)
    
 # ----Run4--   
payload = json.dumps(data)
print(payload)

# ----Run5--   
headers = {
  'authority': 'www.sastaticket.pk',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ru;q=0.7',
  'content-type': 'application/json',
  'origin': 'https://flights.sastaticket.pk',
  'referer': 'https://flights.sastaticket.pk/',
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
# son.keys()
# son['data'].keys() 
# son['data']['flights']
# departure_datetime=son['data']['flights'][0][0]['legs'][0]['segments'][0]['departure_datetime'] 
# filght_name=son['data']['flights'][0][3]['legs'][0]['segments'][0]['operating_airline']['name'] 
# filght_name
# # len(son['data']['flights'][0])
# arrival_datetime=son['data']['flights'][0][3]['legs'][0]['segments'][0]['arrival_datetime']
# Actual_fare=son['data']['flights'][0][0]['fare_options'][0]['price']['gross_fare']
# Actual_fare
# discount_fare=son['data']['flights'][0][0]['fare_options'][0]['price']['selling_fare']
# discount_fare

# ----Run8-- 
df6=pd.DataFrame()

# ----Run 8b-- 
for i in range(len(son['data']['flights'][0])):
    filght_name=son['data']['flights'][0][i]['legs'][0]['segments'][0]['operating_airline']['name'] 
    print(filght_name)
    current_location=son['data']['flights'][0][i]['legs'][0]['segments'][0]['origin']['iata_code']
    destionation=son['data']['flights'][0][i]['legs'][0]['segments'][0]['destination']['iata_code']
    Actual_fare=son['data']['flights'][0][i]['fare_options'][0]['price']['gross_fare']
    print(Actual_fare)
    discount_fare=son['data']['flights'][0][i]['fare_options'][0]['price']['selling_fare']
    print(discount_fare) 
    arrival_datetime=son['data']['flights'][0][i]['legs'][0]['segments'][0]['arrival_datetime']
    print(arrival_datetime)
    departure_datetime=son['data']['flights'][0][i]['legs'][0]['segments'][0]['departure_datetime'] 
    # departure_datetime
    flight_dict={
        'filght_name':filght_name,
        'Actual_fare':Actual_fare,
        'discount_fare':discount_fare,
        'current_location':current_location,
        'destionation':destionation,
        'arrival_datetime':arrival_datetime,
        'departure_datetime':departure_datetime,
       }
    df6=df6.append(flight_dict,ignore_index=True)

# ----Run9--    
print(df6) 
    
# ***********KHI TO ISL******************

# OUTPUT:=========>24-FEB-2023<========= 
#    filght_name  Actual_fare  discount_fare     arrival_datetime   departure_datetime
# 0          PIA      16700.0          16684  2023-02-24T17:55:00  2023-02-24T16:00:00
# 1      Airsial      15850.0          14753  2023-02-24T21:00:00  2023-02-24T19:00:00
# 2      Airsial      16100.0          14983  2023-02-24T09:00:00  2023-02-24T07:00:00
# 3      Airsial      17450.0          16225  2023-02-24T15:00:00  2023-02-24T13:00:00
# 4   Serene Air      13457.0          13230  2023-02-24T16:45:00  2023-02-24T14:45:00
# 5      Airblue      16300.0          16724  2023-02-24T23:00:00  2023-02-24T21:00:00
# 6   Fly Jinnah      15000.0          15976  2023-02-24T09:05:00  2023-02-24T07:05:00
# 7   Fly Jinnah      15000.0          15976  2023-02-24T20:50:00  2023-02-24T18:50:00
# 8          PIA      16700.0          16684  2023-02-24T08:55:00  2023-02-24T07:00:00
# 9          PIA      16700.0          16684  2023-02-24T14:55:00  2023-02-24T13:00:00
# 10         PIA      16700.0          16684  2023-02-24T17:55:00  2023-02-24T16:00:00
# OUTPUT: =========>25-FEB-2023<========= 
# O:  filght_name  Actual_fare  discount_fare     arrival_datetime   departure_datetime
# 0     Airsial      15850.0          14698  2023-02-25T21:00:00  2023-02-25T19:00:00
# 1     Airsial      16100.0          14927  2023-02-25T09:00:00  2023-02-25T07:00:00
# 2     Airsial      17450.0          16164  2023-02-25T15:00:00  2023-02-25T13:00:00
# 3     Airblue      16300.0          16724  2023-02-25T23:00:00  2023-02-25T21:00:00
# 4  Fly Jinnah      15000.0          15976  2023-02-25T09:05:00  2023-02-25T07:05:00
# 5  Fly Jinnah      15000.0          15976  2023-02-25T20:50:00  2023-02-25T18:50:00
# 6         PIA      16700.0          16684  2023-02-25T08:55:00  2023-02-25T07:00:00
# 7         PIA      16700.0          16684  2023-02-25T14:55:00  2023-02-25T13:00:00
# 8         PIA      16700.0          16684  2023-02-25T17:55:00  2023-02-25T16:00:00
# 9         PIA      16700.0          16684  2023-02-25T21:55:00  2023-02-25T20:00:00


# OUTPUT:=========>26-FEB-2023<========= 
#  filght_name  Actual_fare  discount_fare     arrival_datetime   departure_datetime
# 0     Airsial      15850.0          14753  2023-02-26T21:00:00  2023-02-26T19:00:00
# 1     Airsial      16100.0          14983  2023-02-26T09:00:00  2023-02-26T07:00:00
# 2     Airsial      17450.0          16225  2023-02-26T15:00:00  2023-02-26T13:00:00
# 3  Serene Air      14337.0          14093  2023-02-26T21:20:00  2023-02-26T19:20:00
# 4     Airblue      14000.0          14350  2023-02-26T23:00:00  2023-02-26T21:00:00
# 5  Fly Jinnah      15000.0          15976  2023-02-26T09:05:00  2023-02-26T07:05:00
# 6  Fly Jinnah      15000.0          15976  2023-02-26T20:50:00  2023-02-26T18:50:00
# 7         PIA      16700.0          16684  2023-02-26T08:55:00  2023-02-26T07:00:00
# 8         PIA      16700.0          16684  2023-02-26T14:55:00  2023-02-26T13:00:00
# 9         PIA      16700.0          16684  2023-02-26T17:55:00  2023-02-26T16:00:00

# ***********ISL TO KHI******************

# OUTPUT:=========>24-FEB-2023<========= 
# 1      Airsial      15850.0          14753              ISB          KHI  2023-02-24T23:59:00  2023-02-24T22:00:00
# 2      Airsial      16700.0          15535              ISB          KHI  2023-02-24T18:00:00  2023-02-24T16:00:00
# 3   Serene Air      13457.0          13230              ISB          KHI  2023-02-24T19:45:00  2023-02-24T17:45:00
# 4      Airblue      16300.0          16724              ISB          KHI  2023-02-24T20:00:00  2023-02-24T18:00:00
# 5   Fly Jinnah      15000.0          15976              ISB          KHI  2023-02-24T23:35:00  2023-02-24T21:30:00
# 6   Fly Jinnah      16500.0          17590              ISB          KHI  2023-02-24T11:50:00  2023-02-24T09:45:00
# 7          PIA      16700.0          16684              ISB          KHI  2023-02-24T11:55:00  2023-02-24T10:00:00
# 8          PIA      16700.0          16684              ISB          KHI  2023-02-24T14:55:00  2023-02-24T13:00:00
# 9          PIA      16700.0          16684              ISB          KHI  2023-02-24T17:55:00  2023-02-24T16:00:00
# 10         PIA      16700.0          16684              ISB          KHI  2023-02-24T20:55:00  2023-02-24T19:00:00
# 11         PIA      16700.0          16684              ISB          KHI  2023-02-24T22:55:00  2023-02-24T21:00:00

# OUTPUT:=========>25-FEB-2023<=========
# filght_name  Actual_fare  discount_fare current_location destionation     arrival_datetime   departure_datetime
# 0     Airsial      15850.0          14698              ISB          KHI  2023-02-25T11:59:00  2023-02-25T10:00:00
# 1     Airsial      15850.0          14698              ISB          KHI  2023-02-25T23:59:00  2023-02-25T22:00:00
# 2     Airsial      17450.0          16164              ISB          KHI  2023-02-25T18:00:00  2023-02-25T16:00:00
# 3     Airblue      16300.0          16724              ISB          KHI  2023-02-25T20:00:00  2023-02-25T18:00:00
# 4  Fly Jinnah      15000.0          15976              ISB          KHI  2023-02-25T11:50:00  2023-02-25T09:45:00
# 5  Fly Jinnah      15000.0          15976              ISB          KHI  2023-02-25T23:35:00  2023-02-25T21:30:00
# 6         PIA      16700.0          16684              ISB          KHI  2023-02-25T11:55:00  2023-02-25T10:00:00
# 7         PIA      16700.0          16684              ISB          KHI  2023-02-25T17:55:00  2023-02-25T16:00:00
# 8         PIA      16700.0          16684              ISB          KHI  2023-02-25T20:55:00  2023-02-25T19:00:00
#  
# OUTPUT:=========>26-FEB-2023<========= 
# 0     Airsial      15850.0          14753              ISB          KHI  2023-02-26T11:59:00  2023-02-26T10:00:00
# 1     Airsial      16700.0          15535              ISB          KHI  2023-02-26T23:59:00  2023-02-26T22:00:00
# 2     Airsial      17450.0          16225              ISB          KHI  2023-02-26T18:00:00  2023-02-26T16:00:00
# 3     Airblue      15490.0          15888              ISB          KHI  2023-02-26T20:00:00  2023-02-26T18:00:00
# 4         PIA      16700.0          16684              ISB          KHI  2023-02-26T11:55:00  2023-02-26T10:00:00
# 5         PIA      16700.0          16684              ISB          KHI  2023-02-26T17:55:00  2023-02-26T16:00:00
# 6         PIA      16700.0          16684              ISB          KHI  2023-02-26T20:55:00  2023-02-26T19:00:00
# 7         PIA      16700.0          16684              ISB          KHI  2023-02-26T22:55:00  2023-02-26T21:00:00

import requests

#try:
    #response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?units=imperial&lat=42.3601&lon=71.0589&appid=b203ee60cff20ac3ead35d0c4eb23f6a")
    ##print(response.json())
#except:
    #print("No Internet access.")

#response_json = response.json()

#temp=response_json["main"]["temp"]
#temp_min=response_json["main"]["temp_min"]
#temp_max=response_json["main"]["temp_max"]

#print(f"In Hong Kong, it is currently {temp} F degrees.")
#print(f"Today's high will be {temp_max} F degrees.")
#print(f"Today's low will be {temp_min} F degrees.")

class City:
    def __init__(self, name, lat, lon, units="imperial"):
        self.name= name
        self.lat=lat
        self.lon=lon
        self.units=units
        self.get_data()
    
    def get_data(self):
        try:
            response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=b203ee60cff20ac3ead35d0c4eb23f6a")
        except:
            print("No Internet access.")
        
        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min=self.response_json["main"]["temp_min"]
        self.temp_max=self.response_json["main"]["temp_max"]
    
    def temp_print(self):
        if self.units=="imperial":
            print(f"In {self.name}, it is currently {self.temp} F degrees.")
            print(f"Today's high will be {self.temp_max} F degrees.")
            print(f"Today's low will be {self.temp_min} F degrees.")
        if self.units=="metric":
            print(f"In {self.name}, it is currently {self.temp} C degrees.")
            print(f"Today's high will be {self.temp_max} C degrees.")
            print(f"Today's low will be {self.temp_min} C degrees.")
        else:
            print("please try again with impreial or metric units specified.")

my_city = City("Hong Kong",22.302711,114.177216)
my_city.temp_print()

vacation_city = City("Providence, RI",41.825226,-71.418884)
vacation_city.temp_print()
#print(my_city.response_json)

eu_city = City("London, UK",51.509865,-0.118092,"metric")
eu_city.temp_print()
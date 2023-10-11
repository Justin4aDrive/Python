import requests

try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=35.6762&lon=139.6503&appid=79007029562c2ab46617d801d8018750")

    print(response.json())
except:
    print("No internet access :(")

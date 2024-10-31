import requests
from twilio.rest import Client
import os

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
OWM_API_KEY = os.environ.get('OWM_API_KEY')
account_sid = 'AC827a388f5dd24fb733e25407904b0790'
auth_token = os.environ.get('auth_token')

print(OWM_API_KEY)
print(auth_token)

weather_params = {
    "lat": 37.386051,
    "lon": -122.083855,
    "appid": OWM_API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='18333629439',
    body='Its going to rain',
    to='14155833084'
)
print(message.sid)
print(message.status)
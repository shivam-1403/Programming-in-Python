import requests
from twilio.rest import Client

api_key = "Your Api Key"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
acc_sid = "Your Account SID"
auth_token = "Your Auth Token"

weather_params = {
    "lat": 30.185400,
    "lon": 74.496300,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
weather_id = data["weather"][0]["id"]

if weather_id < 700:
    client = Client(acc_sid, auth_token)
    message = client.messages.create(
    body="There will be Rain today. Don't forget to bring an ☂️",
    from_="Your Number Generated from Twilio",
    to="Your Target Number",
    )
    print(message.status)
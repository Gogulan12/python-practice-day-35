import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""
account_sid = ""
auth_token = ""


weather_params = {
    "lat":43.653225,
    "lon": -79.383186,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

repsonse = requests.get(OWM_Endpoint, params=weather_params)
# print(repsonse.status_code)
weather_data = repsonse.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False


for hour_data in weather_slice:
    # print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("Bring an umbrella.")

if will_rain:
    # print("Bring and umbrella")
    #only get called once instead of hourly
    client = Client(account_sid,auth_token)
    message = client.messages\
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from ="+12057362627",
        to= "Your verified number",
    )


import requests

# 1. Create a dictionary with the query parameters
owm_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "8c18caf9adc77518ebc82cf3e161260d"

weather_params = {
    "lat":"51.507351",
    "lon":"-0.127758",
    "appid":api_key,
    "exclude":"current,minutely,daily",
    "units":"metric"
}

data = requests.get(url=owm_endpoint, params=weather_params)
data.raise_for_status()
weather_data = data.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        print("Bring an umbrella.")
        break
    


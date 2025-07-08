import requests

def fetch_weather_forecast():
    url = "https://api.meteo.lt/v1/places/vilnius/forecasts/long-term"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for HTTP errors
        data = response.json()

         # Let's print a simple summary: timestamp and air temperature for each forecasted time
        print(f"Weather forecast for {data['place']['name']}:\n")
        for forecast in data['forecastTimestamps']:
            timestamp = forecast['forecastTimeUtc']
            temperature = forecast['airTemperature']
            condition = forecast.get('conditionCode', 'unknown')
            print(f"{timestamp}: {temperature}°C, condition: {condition}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage:
fetch_weather_forecast()
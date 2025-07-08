import requests
import numpy as np

def fetch_forecast_temperatures():
    url = "https://api.meteo.lt/v1/places/vilnius/forecasts/long-term"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    temps = [item["airTemperature"] for item in data["forecastTimestamps"]]
    return np.array(temps)

def analyze_temperatures(temps):
    mean = np.mean(temps)
    median = np.median(temps)
    min_temp = np.min(temps)
    max_temp = np.max(temps)
    return {
        "mean": mean,
        "median": median,
        "min": min_temp,
        "max": max_temp
    }

if __name__ == "__main__":
    temps = fetch_forecast_temperatures()
    analysis = analyze_temperatures(temps)
    print("Temperature analysis for Vilnius:")
    print(f"Mean: {analysis['mean']:.2f} °C")
    print(f"Median: {analysis['median']:.2f} °C")
    print(f"Min: {analysis['min']:.2f} °C")
    print(f"Max: {analysis['max']:.2f} °C")

# This script fetches the long-term weather forecast for Vilnius, Lithuania,
# analyzes the air temperatures, and prints the mean, median, minimum, and maximum temperatures.
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd

# Using API key and fetching data
API_KEY = "15904308ddc645c3da09a0a59e84e422"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def fetch_weather_data(city, api_key):
    query_parameters = {
        "q": city,           # City name
        "appid": api_key,    # API key
        "units": "metric",   # Temperatures in Celsius
    }

    try:
        response = requests.get(BASE_URL, params=query_parameters)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return None

#Data processing and visualization
def process_weather_data(data):
    weather_list = data.get("list", [])
    if not weather_list:
        print("No weather data available.")
        return pd.DataFrame()

    weather_df = pd.DataFrame({
        "DateTime": [entry["dt_txt"] for entry in weather_list],
        "Temperature (°C)": [entry["main"]["temp"] for entry in weather_list],
        "Humidity (%)": [entry["main"]["humidity"] for entry in weather_list],
        "Wind Speed (m/s)": [entry["wind"]["speed"] for entry in weather_list],
    })

    # Convert 'DateTime' column to datetime for better plotting
    weather_df["DateTime"] = pd.to_datetime(weather_df["DateTime"])
    return weather_df

def create_visualizations(weather_df):
    if weather_df.empty:
        print("No data available for visualization.")
        return

    sns.set(style="whitegrid")

    # Temperature trends
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="DateTime", y="Temperature (°C)", data=weather_df, marker="o", color="#50C878", linewidth=2)  # Emerald green
    plt.title("Temperature Trends", fontsize=16)
    plt.xlabel("Date & Time", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d\n%H:%M'))
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.grid(visible=True, linestyle="--", linewidth=0.5)
    plt.show()

     # Humidity levels as line plot for better trend visualization
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="DateTime", y="Humidity (%)", data=weather_df, marker="o", color="#1f77b4", linewidth=2)  # Blue color for clarity
    plt.title("Humidity Levels", fontsize=16)
    plt.xlabel("Date & Time", fontsize=12)
    plt.ylabel("Humidity (%)", fontsize=12)

    # Limit the number of x-axis labels to avoid overlap
    plt.xticks(rotation=45, fontsize=10)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d\n%H:%M'))
    plt.tight_layout()
    plt.grid(visible=True, linestyle="--", linewidth=0.5)
    plt.show()

    # Wind speed trends with adjusted x-axis labels and markers
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="DateTime", y="Wind Speed (m/s)", data=weather_df, marker="o", color="#800080", linewidth=2)  # Purple for wind speed
    plt.title("Wind Speed Trends", fontsize=16)
    plt.xlabel("Date & Time", fontsize=12)
    plt.ylabel("Wind Speed (m/s)", fontsize=12)

    # Reduce x-axis labels to avoid overlap
    plt.xticks(weather_df["DateTime"][::3], rotation=45, fontsize=10)  # Show every 3rd label for clarity
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d\n%H:%M'))
    plt.tight_layout()
    plt.grid(visible=True, linestyle="--", linewidth=0.5)
    plt.show()


def main():
    city = input("Enter the city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        return

    data = fetch_weather_data(city, API_KEY)
    if data:
        weather_df = process_weather_data(data)
        if not weather_df.empty:
            create_visualizations(weather_df)

if __name__ == "__main__":
    main()

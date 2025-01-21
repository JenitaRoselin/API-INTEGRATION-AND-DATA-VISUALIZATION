# API-INTEGRATION-AND-DATA-VISUALIZATION

*Company* - CodTech IT Solutions

*Name* - A Jenita Roselin

*Intern ID* - CT08FYS

*Domain* - Python Programming

*Duration* - 4 weeks

*Mentor* - Neela Santhosh Kumar

# Task Description
The objective of this task was to develop a Python program that fetches weather forecast data from a public API (OpenWeatherMap) and visualizes it using Matplotlib and Seaborn. The goal was to retrieve weather data for a specified city and then present it in the form of graphs that show trends in temperature, humidity, and wind speed. This program can be used for weather monitoring, trend analysis, or as part of a larger data-driven weather application.

# *Tools Used*
Google Colab: The code was written and executed in Google Colab, providing an interactive and cloud-based environment for running Python code.
OpenWeatherMap API: A widely used public API that provides real-time and forecast weather data. It is useful in applications that require weather information, such as weather apps, IoT systems, and environmental monitoring tools.

# *Python Libraries Used*
requests: Used to make HTTP requests to the OpenWeatherMap API and fetch data in JSON format.
pandas: Used to process the fetched weather data into a structured DataFrame, making it easier to handle and analyze.
matplotlib: A library for creating static, interactive, and animated visualizations. It was used to generate the plots for visualizing weather trends.
seaborn: A data visualization library based on Matplotlib, which was used to enhance the style and readability of the plots.

# *1. API Integration (Fetching Weather Data)*
The core task of API integration involves the fetch_weather_data function. This function interacts with the OpenWeatherMap API by:

Constructing a URL with query parameters like the city name, API key, and unit of measurement (Celsius).
Sending a GET request to the API using the requests.get() method.
Handling any errors gracefully in case of invalid inputs or network issues.
Using response.json() to convert the returned JSON data into a Python dictionary.
This process enables the program to retrieve real-time weather forecast data, which is essential for applications requiring up-to-date weather information.

# *2. Data Processing and Structuring*
The raw weather data returned from the API is then processed by the process_weather_data function. This step involves:

Extracting relevant weather information, such as:
Date and Time: Converted to datetime objects to make it easier to plot on the x-axis of graphs.
Temperature (°C): The forecasted temperature for each time point.
Humidity (%): The percentage of humidity at each time point.
Wind Speed (m/s): The wind speed in meters per second.
Organizing the extracted data into a structured pandas DataFrame, which makes it easier to manipulate and visualize.
This step is vital for cleaning and organizing the data so that it can be easily plotted in the next step.

# *3. Data Visualization*
The create_visualizations function is responsible for generating the visual representation of the data. It includes three main plots:

Temperature Trends: A line plot showing how temperature changes over time. This helps users understand daily temperature fluctuations and long-term trends.
Humidity Levels: A line plot visualizing how humidity levels vary. Humidity is a key factor in weather-related decision-making, and this visualization helps track it over time.
Wind Speed Trends: A plot that shows the variations in wind speed over the forecast period. Wind speed is another important factor in weather forecasting and is used in areas like outdoor event planning, construction, and aviation.
Each plot is formatted with:

Custom Date-Time Labels: To clearly show when each data point was recorded.
Rotated X-Axis Labels: To avoid label overlap and ensure readability.
Gridlines, Titles, and Axis Labels: For improved clarity and presentation.

# *4. User Interaction*
The program prompts the user to input a city name, which is then passed to the API request function. The user is also alerted if the input is invalid or if the API request fails, ensuring that the program handles errors gracefully and provides meaningful feedback to the user.

# *Outcome*
This Python program demonstrates how to:

Integrate with an External API: The program effectively fetches weather data from OpenWeatherMap, processes it, and uses it in real-time applications.
Process and Analyze Data: It extracts and organizes raw data into a structured format suitable for visualization.
Create Informative Visualizations: The visualizations produced help users analyze and understand weather trends, which can be used for weather forecasting, environmental monitoring, and more.

# *Where It Can Be Used*
This type of program can be used in various applications:
  Weather Monitoring Apps: To provide users with up-to-date weather forecasts and trends.
  Environmental Studies: For analyzing long-term weather patterns and their effects on the environment.
  Event Planning: Helps determine the weather conditions for outdoor events by predicting temperature, wind, and humidity trends.
  Research in Meteorology: Assists in visualizing weather data to identify patterns and anomalies.
By fetching data from a reliable API and visualizing it, the program supports decision-making in industries and fields where weather data is crucial.

# *Pictures of the Program Output*
![Image](https://github.com/user-attachments/assets/f57b72e8-3db1-4073-b9fe-01dddfa4e9db)

![Image](https://github.com/user-attachments/assets/74a57b1c-39d0-461a-8412-047994e0f05e)

![Image](https://github.com/user-attachments/assets/9d09e4bb-1b6e-4599-8c20-edc8c2d537f4)

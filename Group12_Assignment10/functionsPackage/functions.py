# Name: Johnny Liu, Jack Smith
# Email: liu4j4@mail.uc.edu, smit4jk@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: Nov 9, 2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: execute an API call using a URL and receive results
# Citations: https://open-meteo.com/
# Anything else that's relevant: NA

# functions.py

import requests

# This function requests and receives the data from the API server 
def get_weather():
    # requests the data from URL
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=39.1271&longitude=-84.5144&current=temperature_2m,precipitation,windspeed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum,precipitation_hours&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York")
    # parses the results received into a dictionary
    data = response.json()
    # returns data
    return data

# This function extracts the data needed and prints the results
def print_weather():
    # invoke the function and get the results 
    weather_data = get_weather()
    # extracts the necessary data and put them into different variables for easier assembly later
    max_temp = weather_data["daily"]["temperature_2m_max"][0]                   # extracts the maximum temperature for today
    min_temp = weather_data["daily"]["temperature_2m_min"][0]                   # extracts the minimum temperature for today
    current_temp = weather_data["current"]["temperature_2m"]                    # extracts the current temperature
    current_windspeed = weather_data["current"]["windspeed_10m"]                # extracts the current wind speed
    current_precipitation = weather_data["current"]["precipitation"]            # extracts the current precipitation
    total_precipitation = weather_data["daily"]["precipitation_sum"][0]         # extracts the total precipitation for today
    precipitation_hour = weather_data["daily"]["precipitation_hours"][0]        # extracts the total precipitation hours for today
    
    # assembles and formats all the data extracted into a readable and informative format
    today_weather = (f"Today's Weather Info:\n"
                     f"Maximum Temperature: {max_temp}°F\n"
                     f"Minimum Temperature: {min_temp}°F\n"
                     f"Current Temperature: {current_temp}°F\n"
                     f"Current Wind Speed: {current_windspeed} mph \n"
                     f"Current Precipitation: {current_precipitation} in.\n"
                     f"Total Precipitation: {total_precipitation} in.\n"
                     f"Total Precipitation Hours: {precipitation_hour} hours")
    
    # print the info 
    print(today_weather)
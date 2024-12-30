import requests
import json
import math
import pyttsx3
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather and speak the result
def get_weather():
    city = city_name_entry.get()
    if not city: 
        messagebox.showerror("Input Error", "Please enter a city name.")
        return
    
    # OpenWeatherMap API URL (replace with your own API key)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9f8bc2575714d61ef6f5fb41e9ae6c09"

    try:
        r = requests.get(url)
        weather_dict = json.loads(r.text)

        if weather_dict["cod"] != 200:  # Check if the city is valid
            messagebox.showerror("City Not Found", "The city was not found. Please try again.")
            return

        # Extract temperature in Kelvin and convert it to Celsius
        temp = weather_dict['main']['feels_like']
        temp_in_C = math.floor(temp - 273.15)

        # Display the result in the label
        result_label.config(text=f"Temperature: {temp_in_C}°C")

        # Use pyttsx3 to speak the weather
        engine = pyttsx3.init()
        engine.say(f"The current weather in {city} is {temp_in_C} degrees Celsius.")
        engine.runAndWait()

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data: {str(e)}")


# Set up the main Tkinter window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# Create and place the widgets
city_label = tk.Label(root, text="Enter City Name:", font=("Arial", 12))
city_label.pack(pady=10)

city_name_entry = tk.Entry(root, font=("Arial", 12))
city_name_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()

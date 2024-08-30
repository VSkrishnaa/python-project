from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image

# Initialize the Tkinter root window
root = Tk()
root.title("Weather App")
root.geometry("400x650")
root.configure(bg="#D3D3D3")  

# Load weather icons
weather_icons = {
    "Clear": "sun.png",
    "Clouds": "cloud.png",
    "Rain": "rain.png",
    "Snow": "snow.png",
    "Thunderstorm": "storm.png",
    "default": "default.png"
}

# Function to update the background based on weather condition
def update_background(weather_main):
    bg_color = {
        "Clear": "#87CEEB",
        "Clouds": "#B0C4DE",
        "Rain": "#778899",
        "Snow": "#ADD8E6",
        "Thunderstorm": "#4682B4"
    }
    root['background'] = bg_color.get(weather_main, "#D3D3D3")  # Default to a slightly darker gray background

# Frame for city and search
city_frame = Frame(root, bg='#D3D3D3')
city_frame.pack(pady=10)

city_name_var = StringVar()
city_entry = Entry(city_frame, textvariable=city_name_var, width=30, font=("Helvetica", 14))
city_entry.pack(side=LEFT, padx=10)

city_nameButton = Button(city_frame, text="Search", command=lambda: fetch_weather_data(city_name_var.get()), font=("Helvetica", 12))
city_nameButton.pack(side=LEFT, padx=10)

# Frame for the main weather information
weather_frame = Frame(root, bg='#D3D3D3')
weather_frame.pack(pady=20)

city_country_label = Label(weather_frame, text="City, Country", bg='#D3D3D3', fg="#000000", font=("Helvetica", 20))
city_country_label.grid(row=0, column=0, sticky="w", padx=20)

coord_label = Label(weather_frame, text="00.00   00.00", bg='#D3D3D3', fg="#000000", font=("Helvetica", 12))
coord_label.grid(row=0, column=1, sticky="e", padx=20)

datetime_label = Label(weather_frame, text="Day, Month Date", bg='#D3D3D3', fg="#000000", font=("Helvetica", 12))
datetime_label.grid(row=1, column=0, columnspan=2, pady=5)

time_label = Label(weather_frame, text="00:00 AM/PM", bg='#D3D3D3', fg="#000000", font=("Helvetica", 12))
time_label.grid(row=2, column=0, columnspan=2, pady=5)

temp_frame = Frame(root, bg='#D3D3D3')
temp_frame.pack(pady=5)

temp_label = Label(temp_frame, text="0", bg='#D3D3D3', fg="#000000", font=("Helvetica", 70, 'bold'))
temp_label.pack(side=LEFT, padx=10)

weather_icon_label = Label(temp_frame, bg='#D3D3D3')
weather_icon_label.pack(side=RIGHT, padx=10)

details_frame = Frame(root, bg='#D3D3D3')
details_frame.pack(pady=5)

humidity_label = Label(details_frame, text="Humidity: --", bg='#D3D3D3', fg="#000000", font=("Helvetica", 12))
humidity_label.grid(row=0, column=0, padx=10, pady=5)

max_temp_label = Label(details_frame, text="Max Temp.: --", bg='#D3D3D3', fg="#000000", font=("Helvetica", 12))
max_temp_label.grid(row=1, column=0, padx=10, pady=5)

min_temp_label = Label(details_frame, text="Min Temp.: --", bg='#D3D3D3', fg="#000000", font=("Helvetica", 12))
min_temp_label.grid(row=2, column=0, padx=10, pady=5)

temp_unit_label = Label(root, text="All temperatures in degree Celsius", bg='#D3D3D3', fg="#000000", font=("Helvetica", 10, "italic"))
temp_unit_label.pack(pady=5)

# Frame for the signature at the bottom
signature_frame = Frame(root, bg='#D3D3D3')
signature_frame.pack(side=BOTTOM, pady=10)

signature_label = Label(signature_frame, text="myWeather", bg='#D3D3D3', fg="#000000", font=("Helvetica", 20, "bold italic"))
signature_label.pack()

developer_label = Label(signature_frame, text="Rahul Krishna V S", bg='#D3D3D3', fg="#000000", font=("Helvetica", 10, "italic"))
developer_label.pack()

def fetch_weather_data(city):
    try:
        api_key = 'fad5927473caec47a8bbb594cdde46a9'
        api_request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")
        api = api_request.json()

        if api['cod'] == 200:
            # Update city, country, and coordinates
            city_country_label.config(text=f"{api['name']}, {api['sys']['country']}")
            coord_label.config(text=f"{api['coord']['lat']}   {api['coord']['lon']}")

            # Update temperature
            temp_label.config(text=f"{int(api['main']['temp'])}")

            # Update weather description and icon
            weather_main = api['weather'][0]['main']
            update_background(weather_main)
            
            try:
                weather_icon = weather_icons.get(weather_main, weather_icons['default'])
                weather_icon_img = ImageTk.PhotoImage(Image.open(f'icons/{weather_icon}'))
                weather_icon_label.config(image=weather_icon_img)
                weather_icon_label.image = weather_icon_img  # Keep a reference to avoid garbage collection
            except Exception as img_err:
                print("Error loading image:", img_err)
                weather_icon_label.config(image='')  # Remove the icon if loading fails

            # Update date and time
            dt = datetime.datetime.now()
            datetime_label.config(text=dt.strftime('%A, %B %d'))
            time_label.config(text=dt.strftime('%I:%M %p'))

            # Update additional details
            humidity_label.config(text=f"Humidity: {api['main']['humidity']}%")
            max_temp_label.config(text=f"Max Temp.: {api['main']['temp_max']}°C")
            min_temp_label.config(text=f"Min Temp.: {api['main']['temp_min']}°C")
        else:
            city_country_label.config(text="City not found!")
            temp_label.config(text="--")
            weather_icon_label.config(image='')
            root['background'] = "#D3D3D3"

    except Exception as e:
        print("Error fetching data:", e)


root.mainloop()

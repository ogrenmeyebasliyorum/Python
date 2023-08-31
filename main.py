from tkinter import *
from PIL import ImageTk, Image
import requests

# API Configuration
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
api_key = "577ad84bcc03282615193123e684a687"
iconUrl = "https://openweathermap.org/img/wn/{}@2x.png"


# Functions
def getWeather(city):
    response = requests.get(url.format(city, api_key)).json()
    if response.get("weather"):
        weather = response["weather"][0]
        city_name = response["name"]
        country = response["sys"]["country"]
        temp_kelvin = response["main"]["temp"]
        icon_code = weather["icon"]
        condition = weather["description"]
        return city_name, country, temp_kelvin, icon_code, condition
    else:
        return None


def update_weather():
    city = cityEntry.get()
    weather_data = getWeather(city)
    if weather_data:
        locationLabel["text"] = f"{weather_data[0]}, {weather_data[1]}"
        temp_celsius = int(weather_data[2] - 273.15)
        tempLabel["text"] = f"Temperature: {temp_celsius}°C"
        icon_url = iconUrl.format(weather_data[3])
        icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url, stream=True).raw))
        iconLabel.config(image=icon)
        iconLabel.image = icon


# GUI Setup
app = Tk()
app.geometry("300x450")
app.title("Apocan Hava Durumu")

cityEntry = Entry(app, justify="center")
cityEntry.pack(fill=BOTH, ipady=10, padx=18, pady=5)
cityEntry.focus()

searchButton = Button(
    app,
    text="Arama",
    font=("Arial", 15),
    command=update_weather,
)
searchButton.pack(fill=BOTH, ipady=10, padx=20)

iconLabel = Label(app)
iconLabel.pack()

locationLabel = Label(app, font=("Arial", 14))
locationLabel.pack()

tempLabel = Label(app, font=("Arial", 14))
tempLabel.pack()

app.mainloop()

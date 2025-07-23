# Libraries and Modules
import tkinter as tk # For UI
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
import requests # For Weather API's
country = ''

# Base API Urls
weather_url = "https://api.open-meteo.com/v1/forecast"
geo_url = "https://geocoding-api.open-meteo.com/v1/search"

# Reset Text After Error
def reset_text():
    text.config(text="Enter Country/City Name")
    text.place(x=70, y=2.5)

def on_button_click():
    btn_done.config(state=tk.DISABLED)
    #Get country from text inputted
    country = str(input_widget.get(1.0, tk.END).strip())
    input_widget.delete(1.0, tk.END)
    print(country)
    # Geocoding API Parameters
    geo_params = {
        "name" : country # REQUIRED
    }
    # Geocoding API Response
    geo_response = requests.get(geo_url, params=geo_params)
    if geo_response.status_code == 200:
        # Storing Geo Data in Json Form
        geo_data = geo_response.json()

        if geo_data.get("results"):
            # Storing the Longitude and Latitude
            lat = geo_data["results"][0]["latitude"]
            lon = geo_data["results"][0]["longitude"]
            # Weather API Parameters
            weather_params = {
                "latitude" : lat, # REQUIRED
                "longitude" : lon, # REQUIRED
                "current_weather" : True,
                "timezone" : "auto"
            }
            # Weather API Response
            weather_response = requests.get(weather_url,params=weather_params)
            # Storing Weather Data in Json Form
            weather_data = weather_response.json()
            # Draw New Weather
            temp_label = tk.Label(main, text=f"{weather_data['current_weather']['temperature']} °C", font=("Arial", 30))
            temp_label.place(relx=0.5, rely=0.5, anchor="center")
            btn_done.config(state=tk.NORMAL)
        else:
            text.config(text="Area Not Found")
            text.place(x=115, y=10)
            text.after(3000, reset_text)
            btn_done.config(state=tk.NORMAL)
    else:
        print("Failed to Retrieve Geocoding Data")
        btn_done.config(state=tk.NORMAL)



# Main Window Properties
main = tk.Tk()
main.title("Weather")
main.resizable(False, False)
# Screen Variables for Window Centring
scr_wid, scr_hei, win_wid, win_hei = main.winfo_screenwidth(), main.winfo_screenheight(), 400, 500
# Centring the Window
win_x = (scr_wid-win_wid) // 2
win_y = (scr_hei-win_hei) //2
# Setting Window Dimensions
main.geometry(f"{win_wid}x{win_hei}+{win_x}+{win_y}")
# Text Label
text = tk.Label(main, text="Enter Country/City Name", font=("Helvetica", 12, 'bold'))
text.place(x=70, y=2.5)
# User Input Text
input_widget = tk.Text(main, width=12, height=1, font=("Helvetica", 12))
input_widget.place(x=win_x/6, y=40)
# Done Button
btn_done = tk.Button(main, text="Done", command=on_button_click)
btn_done.place(x=win_x/4.3, y=80)
# Main Loop
main.mainloop()
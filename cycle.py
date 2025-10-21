from main import tts, get_time, get_weather
from enum import Enum
import time
from gpiozero import Button
from signal import pause

button_cycle = Button(17)
button_main = Button(27)

cycle_dict = {
    0: 'Time',
    1: 'Temperature',
    2: 'Compass'
}
current_cycle = 0

def on_button_cycle_pressed():
    """ 
    Cycle through modes: Time, Temperature, Compass 
    """
    current_cycle = current_cycle + 1

    if current_cycle > 2:
        current_cycle = 0
    # Wrap around to first cycle

    tts(cycle_dict[current_cycle])

def on_button_main_pressed():
    """ 
    Execute action based on current cycle
    """
    if cycle_dict[current_cycle] == 'Time':
        timezone_name = 'America/Phoenix' 
        # Using Phoenix timezone for prototyping

        current_time = get_time(timezone_name)
        tts(f"The current time is {current_time}")

    elif cycle_dict[current_cycle] == 'Temperature':
        lat = 33.4484
        lon = -112.0740  
        # Phoenix, AZ coordinates (for prototyping)

        temperature = get_weather(lat, lon)
        tts(f"The current temperature is {temperature} degrees Fahrenheit")

    elif cycle_dict[current_cycle] == 'Compass':
        pass

pause()

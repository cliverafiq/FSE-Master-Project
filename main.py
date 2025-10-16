from datetime import datetime
from zoneinfo import ZoneInfo
import pyttsx3
from pymeteosource.api import Meteosource  
from pymeteosource import types

weather_api = "wxlztgj4vd4go6k5o5qasp6mzthosos146sv4ab0"
weather_tier = 'FREE'

def tts(out):
    """
    Method for Text to Speach
    """
    engine = pyttsx3.init()
    engine.say(out)
    engine.runAndWait()

def get_time(timezone_name):
    """
    Method to get time
    """
    tz_info = ZoneInfo(timezone_name)
    current_time = datetime.now(tz_info)
    time = current_time.strftime("%H:%M")
    return time

def get_weather(lat, lon):
    """
    Method to get weather
    """
    meteosource = Meteosource(weather_api, weather_tier)
    forecast = meteosource.get_point_forecast(
        sections=[types.sections.CURRENT],
        units=types.units.US
    )
    current_weather = forecast.current

    if current_weather:
        temperature = current_weather.temperature
        return(f"Current temperature: {temperature}°F")

def main():
    time = get_time("America/Phoenix")
    print("The current time is:", time)
    #tts("The current time is:", time)

    PHOENIX_LATITUDE = 33.4484
    PHOENIX_LONGITUDE = -112.0740
    #weather = get_weather(PHOENIX_LATITUDE, PHOENIX_LONGITUDE)
    #print("The current weather is: ", weather)
    #tts("The current weather is: ", weather)

if __name__ == "__main__":
    main()

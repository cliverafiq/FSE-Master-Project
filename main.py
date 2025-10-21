from datetime import datetime
from zoneinfo import ZoneInfo
import pyttsx3
from pymeteosource.api import Meteosource  
from pymeteosource import types
from enum import Enum


weather_api = "wxlztgj4vd4go6k5o5qasp6mzthosos146sv4ab0"
weather_tier = 'free'

def tts(out: str):
    """
    Method for Text to Speach
    """
    engine = pyttsx3.init()
    engine.say(out)
    engine.runAndWait()

def get_time(timezone_name: str) -> str:
    """
    Method to get time
    """
    tz_info = ZoneInfo(timezone_name)
    current_time = datetime.now(tz_info)
    # Gets current time

    time = current_time.strftime("%H:%M")
    # Formats current time to Hours:Minutes

    return time

def get_weather(lat: float, lon: float) -> str:
    """
    Method to get weather
    """
    ms = Meteosource(weather_api, weather_tier)
    # initate the Meteosource API
    try:
        forecast = ms.get_point_forecast(
            lat=lat,
            lon=lon,
            sections=["current"],      
            units="us"                 
        )
        # HTTP Request to the Point endpoint (refer to documentation)

        cw = getattr(forecast, "current", None)
        # Ensures the interpreter access the current attribute safely

        if cw is None and isinstance(forecast, dict):
            cw = forecast.get("current")
            # If version is old

        if cw is None:
            return "Current weather not available."
            # Gaurd if nothing is found

        if hasattr(cw, "temperature"):
            return cw.temperature
            # If Object: reads cw.temperature

        if isinstance(cw, dict) and "temperature" in cw:
            return cw.temperature
            # If Dict reads cw['temperature']

        return "Current weather not available."

    except Exception as e:
        return f"Weather error: {e}"
    
def main():
    time = get_time("America/Phoenix")
    print("The current time is:", time)
    #tts("The current time is:", time)

    PHOENIX_LATITUDE = 33.4484
    PHOENIX_LONGITUDE = -112.0740
    weather = get_weather(PHOENIX_LATITUDE, PHOENIX_LONGITUDE)
    print("The current weather is:", weather, "°F")
    #tts("The current weather is:", weather ,"°F")

if __name__ == "__main__":
    main()

from datetime import datetime
from zoneinfo import ZoneInfo

def get_time():
    """
    Method to get time in Phoneix
    """
    
    timezone_name = "America/Phoenix"
    tz_info = ZoneInfo(timezone_name)
    current_time = datetime.now(tz_info)
    time = current_time.strftime("%H:%M")
    return time

def main():
    time = get_time()
    print("The current time is:", time)

if __name__ == "__main__":
    main()

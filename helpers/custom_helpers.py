from datetime import datetime

def utc_time_calculator():
    current_time = datetime.now()

    formatted_time = current_time.strftime("%Y-%m-%dT%H:%M:%S")
    return formatted_time
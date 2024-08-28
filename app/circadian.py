from datetime import time, datetime, timedelta

def get_circadian_lighting():
    current_time = datetime.now().time()
    
    # Define light settings for different times of the day
    if current_time < time(6, 0):
        return {"brightness": 50, "color": "warm_white"}  # Early morning
    elif current_time < time(12, 0):
        return {"brightness": 100, "color": "cool_white"}  # Morning
    elif current_time < time(18, 0):
        return {"brightness": 100, "color": "natural_white"}  # Afternoon
    else:
        return {"brightness": 70, "color": "warm_white"}  # Evening

from datetime import datetime, time, timedelta


def get_circadian_lighting():
    current_time = datetime.now().time()

    if time(9, 0) <= current_time < time(17, 0):
        return "work_from_home_scene"
    return "wind_down_scene"

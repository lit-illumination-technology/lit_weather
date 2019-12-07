from . import _weather_api
import logging

RAIN_COLOR = (0, 5, 15)
TODAY_COLOR = (0, 20, 0)
YESTERDAY_COLOR = (20, 0, 0)
CURRENT_COLOR = (15, 15, 15)
PADDING = 0.05
logger = logging.getLogger(__name__)
name = "Weather"

start_string = name + " started!"

description = "Current, high, and low temperatures"

schema = {}
schema.update(_weather_api.weather_api_schema)


def update(lights, step, state):
    api = state[_weather_api.WEATHER_API_FIELD]
    yesterday_details = api.get_previous_day()
    today_details = api.get_next_day()
    current_temp = yesterday_details[0]["Temperature"]["Imperial"]["Value"]
    yesterday_temps = yesterday_details[0]["TemperatureSummary"]["Past24HourRange"]
    yesterday_low = yesterday_temps["Minimum"]["Imperial"]["Value"]
    yesterday_high = yesterday_temps["Maximum"]["Imperial"]["Value"]
    today_temps = today_details["DailyForecasts"][0]["Temperature"]
    today_low = today_temps["Minimum"]["Value"]
    today_high = today_temps["Maximum"]["Value"]
    today_precip = today_details["DailyForecasts"][0]["Day"]["HasPrecipitation"]
    if today_precip:
        lights.set_all_pixels(*RAIN_COLOR)
    total_min = min(today_low, yesterday_low, current_temp)
    total_max = max(today_high, yesterday_high, current_temp)

    PADDING_PIXELS = PADDING * lights.num_leds
    scale = (lights.num_leds - PADDING_PIXELS * 2) / (total_max - total_min)

    def temp_to_pixel(temp):
        return int((temp - total_min) * scale + PADDING_PIXELS)

    lights.set_pixel(temp_to_pixel(today_low), *TODAY_COLOR)
    lights.set_pixel(temp_to_pixel(today_high), *TODAY_COLOR)
    lights.set_pixel(temp_to_pixel(yesterday_low), *YESTERDAY_COLOR)
    lights.set_pixel(temp_to_pixel(yesterday_high), *YESTERDAY_COLOR)
    lights.set_pixel(temp_to_pixel(current_temp), *CURRENT_COLOR)

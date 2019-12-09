import logging
import json
import os
import requests

from cachetools.func import ttl_cache

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
WEATHER_API_FIELD = "weather_api"

logger = logging.getLogger(__name__)


def create_weather_api(controller, args):
    class api:
        def __init__(self):
            config = json.loads(open(CONFIG_PATH, "r").read())
            self.api_key = config["accuweather_api_key"]
            self.zipcode = config["zipcode"]
            loc_key_url = "http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey={0}&q={1}".format(
                self.api_key, self.zipcode
            )
            location = requests.get(loc_key_url).json()
            self.location_key = location[0]["Key"]

        @ttl_cache(maxsize=1, ttl=60 * 60)
        def get_current(self):
            data = requests.get(
                "http://dataservice.accuweather.com/currentconditions/v1/{0}?apikey={1}".format(
                    self.location_key, self.api_key
                )
            ).json()
            return data

        @ttl_cache(maxsize=1, ttl=60 * 60)
        def get_next_day(self):
            data = requests.get(
                "http://dataservice.accuweather.com/forecasts/v1/daily/1day/{0}?apikey={1}".format(
                    self.location_key, self.api_key
                )
            ).json()
            return data

        @ttl_cache(maxsize=1, ttl=60 * 60)
        def get_previous_day(self):
            data = requests.get(
                "http://dataservice.accuweather.com/currentconditions/v1/{0}/historical/24?details=true&apikey={1}".format(
                    self.location_key, self.api_key
                )
            ).json()
            return data

    return api()


weather_api_schema = {
    WEATHER_API_FIELD: {
        "value": {"type": "weather_api", "default_gen": create_weather_api},
        "user_input": False,
    },
}

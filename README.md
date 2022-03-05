# lit weather
LIT effects for weather displays

## Reading 1 dimentional weather forcasts
The `weather` effect will display weather data using 4 visual indicators
- Red pixels: 2 red pixels will display yesterday's low (leftmost) and high (right) temperatures. This is used as an anchor and only works if you went outside yestersday.
- Green pixels: 2 green pixels display the high and low for today. Since no numerical temperatures are displayed, they only have meaning when compared to the red pixels.
- White blinking pixel: This is the current temperature.
- Background color: If there is percipitation in the day's forcast, then the background color of the entire strip will be blue

Overlaps:
- If a green and red pixel would fall on the same location, that pixels will appear yellow.
- If the current temperature falls on a high or low, that pixel will blink.

## Setup
### Requirements
- [litd](https://github.com/lit-illumination-technology/lit_core)
- accuweather api key
- python3 cachetools (`sudo pip3 install cachetools`)
- go outside at least for a little bit everyday

### Installation
1. `mkdir ~/.lit/litd/effects`
2. `touch ~/.lit/litd/effects/__init__.py`
3. `git clone https://github.com/lit-illumination-technology/lit_weather.git ~/.lit/litd/effects/lit_weather`
4. Create and open `~/.lit/litd/effects/lit_weather/config.json` in your preferred editor and enter:
```
{
    "accuweather_api_key": YOUR_API_KEY,
    "zipcode": YOUR_POSTALCODE
}
```

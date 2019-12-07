# lit weather
LIT effects for weather displays

## Setup
### Prerequisites
- litd
- accuweather api key
- python3 cachetools (`sudo pip3 install cachetools`)

### Installation
1. `mkdir ~/.lit/litd/effects`
2. `touch ~/.lit/litd/effects/__init__.py`
3. `git clone https://github.com/nickpesce/lit_weather.git ~/.lit/litd/effects/lit_weather`
4. Create and open `~/.lit/litd/effects/lit_weather/config.json` in your preferred editor and enter:
```
{
    "accuweather_api_key": YOUR_API_KEY,
    "zipcode": YOUR_POSTALCODE
}
```

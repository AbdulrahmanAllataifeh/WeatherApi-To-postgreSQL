from request import Request
from auth import api_key
from datetime import datetime, timedelta

yesterday_date = datetime.now().date() - timedelta(days=1)
formatted_yesterday_date = yesterday_date.strftime("%Y-%m-%d")

class WeatherSearch:
    def __init__(self,date=formatted_yesterday_date,city='dubai'):
        self._param = {'key': api_key, 'q': city, 'dt': date}
        self._base_url = 'https://api.weatherapi.com/v1/history.json'
        self._day_weather_list = self._get_todays_weather()

    def _get_todays_weather(self):
            weather_search_request = Request.get_content(url=self._base_url, param=self._param)
            self._longitute = weather_search_request['location']['lon']
            self._latitude = weather_search_request['location']['lat']
            return (weather_search_request['forecast']['forecastday'][0]['hour']) if weather_search_request is not None else []

    def _parse_results(self,data):
        timestamp = datetime.strptime(data['time'], "%Y-%m-%d %H:%M")
        isDay = False if data["is_day"] == 0 else True,

        return {"time": timestamp, "temp_c": data['temp_c'],"is_day": isDay,"wind_kph": data['wind_kph'],"wind_degree": data['wind_degree'],
                "wind_dir": data['wind_dir'],"pressure_mb": data['pressure_mb'],"precip_mm": data['precip_mm'],"humidity": data['humidity'],
                "feelslike_c": data['feelslike_c'],"windchill_c": data['windchill_c'],"heatindex_c": data['heatindex_c'],
                "chance_of_rain": data['chance_of_rain'],"vis_km": data['vis_km'],"gust_kph": data['gust_kph'],
                "uv": data['uv'],"longitute": self._longitute,"latitude": self._latitude}

    def get_results(self):
        return [self._parse_results(hour) for hour in self._day_weather_list]
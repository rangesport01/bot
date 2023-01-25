
from config import open_weather_token
from pprint import pprint
import requests

#requests.packages.urllib3.disable_warnings()

#verify=False


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json
        pprint(data)
    except Exception as ex:
        print(ex)
        print("Проверьте название города!")



def main():
    city = input("Введите название города:")
    get_weather(city, open_weather_token)



if __name__ == '__main__':
    main()

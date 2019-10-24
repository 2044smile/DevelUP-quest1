from pyowm import OWM
import secret
# https://junolefou.tistory.com/1
# https://openweathermap.org/
# https://pyowm.readthedocs.io/en/latest/

API_key = secret.API_key # API Key는 secret 으로 관리
owm = OWM(API_key)


def weather():
    obs = owm.weather_at_place('Yangju')
    w = obs.get_weather()
    return w
# print('Yangju : ', w.get_status(), w.get_temperature(unit='celsius')['temp'], '˚C')
# weather()
from django.shortcuts import render
import weather
import time


def index(request):
    w = weather.weather()
    status = w.get_status() # 구름 상태를 가져온다. ex) Clear
    temp = round(w.get_temperature(unit='celsius')['temp'], 1) # 온도를 가져온다. round로 소수점 1자리 까지만

    now = time.localtime()
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    # 현재 시각을 s 에 저장 ex) 2019-10-24 14:03:59
    return render(request, 'index.html', {
        'status' : status,
        'temp' : temp,
        'time' : s,
    })

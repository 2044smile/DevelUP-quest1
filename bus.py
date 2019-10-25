# import secret, requests
# from bs4 import BeautifulSoup
#
# URL = 'http://openapi.gbis.go.kr/ws/rest/busrouteservice/area?serviceKey='
# SERVICE_KEY = secret.SERVICE_KEY
# AREAID = '18'
# KEYWORD = '11'
#
# parms = URL + SERVICE_KEY + '&areaId=' + AREAID +  '&keyword=' + KEYWORD
#
# req = requests.get(parms)
# html = req.text
#
# soup = BeautifulSoup(html, 'html.parser')
# for bus in soup.findAll('routeTypeCd'):
#     print(bus.text)

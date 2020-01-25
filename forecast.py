#import libraries
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = 'https://g1.globo.com/previsao-do-tempo/sp/sao-paulo.ghtml'
PAGE = urlopen(URL)
PARSE = BeautifulSoup(PAGE,'html.parser')

date_box = PARSE.find('p', attrs = {'class' : 'forecast-header__date'})
place_box = PARSE.find('p', attrs = {'class' : 'forecast-header__place'})
max_box = PARSE.find('div', attrs = {'class' : 'forecast-today__temperature forecast-today__temperature--max'})
min_box = PARSE.find('div', attrs = {'class' : 'forecast-today__temperature forecast-today__temperature--min'})
rain_box = PARSE.find('span', attrs = {'class' : 'forecast-today-detail__item-value'})


date = date_box.text.strip()
place = place_box.text.strip()
Min = min_box.text.strip()
Max = max_box.text.strip()
rain = rain_box.text.strip()

print (date)
print (place)
print(Max)
print(Min)
print ("Chuva: " + rain)

with open("forecast.txt", "a") as f:
    Time = str(datetime.today())
    f.write(Time + " ==> ")
    f.write(date + " ")
    f.write(place + " ")
    f.write(Max + " ")
    f.write(Min + " ")
    f.write("Chuva: " + rain + "\n")
    print("Informações escritas no arquivo forecast.txt")

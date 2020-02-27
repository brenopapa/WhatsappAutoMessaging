from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from selenium import webdriver    
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def get_forecast_info():
    URL = 'https://g1.globo.com/previsao-do-tempo/sp/sao-paulo.ghtml'
    PAGE = urlopen(URL)
    PARSE = bs(PAGE, 'html.parser')
    
    tag_date = PARSE.find('p', attrs = {'class' : 'forecast-header__date'})
    tag_place = PARSE.find('p', attrs = {'class' : 'forecast-header__place'})
    tag_max = PARSE.find('div', attrs = {'class' : 'forecast-today__temperature forecast-today__temperature--max'})
    tag_min = PARSE.find('div', attrs = {'class' : 'forecast-today__temperature forecast-today__temperature--min'})
    tag_rain = PARSE.find('span', attrs = {'class' : 'forecast-today-detail__item-value'})
    
    date = tag_date.text.strip()
    place = tag_place.text.strip()
    Max = tag_max.text.strip()
    Min = tag_min.text.strip()
    rain = tag_rain.text.strip()
    
    message = ' {} \n {} \n Max: {} \n Min: {} \n Chuva: {} \n'.format(date, place, Max, Min, rain)
    
    return(message)

def get_todays_emmissary():
    URL = 'https://pt.wowhead.com/world-quests/bfa/na'
    PAGE = urlopen(URL)
    PARSE = bs(PAGE,'html.parser')
    
    wqheader = PARSE.find_all('a')
    wqtimers = PARSE.find_all('dd')
    message = ''
    message += '{} => {} \n'.format(wqheader[6].text, wqtimers[0].text.strip())
    message += '{} => {} \n'.format(wqheader[7].text, wqtimers[1].text.strip())
    message += '{} => {} \n'.format(wqheader[8].text, wqtimers[2].text.strip())
    message += '{} => {} \n'.format(wqheader[9].text, wqtimers[3].text.strip())

    return(message)

def send_message(message_target, message):
    options = webdriver.ChromeOptions();
    options.add_argument('--user-data-dir=C:/Users/breno.zipoli/Desktop/Python/WhatsappAutoMessaging/data/User_Data')
    driver = webdriver.Chrome(executable_path="C:/Users/breno.zipoli/Desktop/Python/WhatsappAutoMessaging/data/chromedriver.exe", options=options)
    driver.get('https://web.whatsapp.com/')   
    chat_title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@title='" + message_target + "']")))
    chat_title.click()
    input_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-tab='1'][@dir='ltr']")))
    input_box.click()
    input_box.send_keys(message + Keys.ENTER)
    
    driver.WebDriverWait(driver, 5)
    driver.quit()
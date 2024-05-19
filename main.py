"""
Структура пакета
driver - содержит драйвера Chrome и FireFox
"""

from selenium.webdriver.common.by import By

import moduls.webdriver as driver
import moduls.sysos as System

import requests

'''1 Приложение должно произвести первичную авторизацию и отобразить окно ввода учётных данных от ЛК МТТ Бизнес. Если
все данные введены верно, решение выдаст приложению два токена: токен доступа (access_token) и токен обновления (refresh_token);

2 Срок годности токена доступа (access_token) – 2 часа, токена обновления (refresh_token) - 3 календарных дня. При истечении срока годности токена
доступа (access_token) он должен быть обновлен с использованием токена обновления (refresh_token) и уникального идентификатора интеграции (Id
клиента). В случае истечения срока действия токена доступа (access_token) решение будет отвечать кодом ответа HTTP 401 (Unauthorized) 

'''
settings = System.settings()
parser = driver.Parser('firefox')

class mtt_conector:
    
    def __init__(self): 
        mtt = settings.getsitings("setings.yaml")['mtt']['authorize']        
        self.mtt = settings.getsitings("setings.yaml")['mtt']['authorize']
        self.client_id = mtt['client_id']
        self.redict_url = mtt['redirect_uri']
        self.email = mtt['email']
        self.passwd = mtt['passwd']
        self.client_secret = mtt['client_secret']

    def authorize(self):
    
        #Собираем url
        url = ''
        list = ['https://oauth.mtt.ru/oauth/authorize?response_type=code&client_id=',self.client_id,'&redirect_uri=', self.redict_url,'&scope=https://mtt.ru/auth.tokens.readwrite']  
        url = url.join(list)
        
        #Получаем страницу  
        parser.walker.get(url)
        
        #Заносим поле ввода
        form_email = parser.find(By.NAME,"login", parser.walker)
        form_email.send_keys(self.email)
        
        form_passwd = parser.find(By.NAME,"password", parser.walker)
        form_passwd.send_keys(self.passwd)
        
        #Кликаем по кнопке войти
        login = parser.find(By.CSS_SELECTOR,".button", parser.walker)
        login.click()  

        return parser.walker.current_url.split('?code=')[1]
            
    def get_token(self):
    
        code = self.authorize() 
        
        njson = {'client_id':str(self.client_id), 
                'client_secret':str(self.client_secret), 
                'code': code,
                'redirect_uri':str(self.redict_url),
                'scope': 'https://mtt.ru/auth.tokens.readwrite',
                'grant_type': 'authorization_code'
                }
        
        html = requests.post("https://oauth.mtt.ru/oauth/token",headers={"Content-Type":"application/x-www-form-urlencoded"}, params = njson)
        return html.json()

def get_sitings(siting):
    """Получает объект настроки биржжи"""
    return settings.getsitings("setings.yaml")[siting]    

m = mtt_conector()
b = m.get_token()
get_token()

#authorize('client_id','redict_url','email','passwd') 


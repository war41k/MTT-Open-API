"""
Структура пакета
driver - содержит драйвера Chrome и FireFox
"""

import moduls.webdriver as driver

'''1 Приложение должно произвести первичную авторизацию и отобразить окно ввода учётных данных от ЛК МТТ Бизнес. Если
все данные введены верно, решение выдаст приложению два токена: токен доступа (access_token) и токен обновления (refresh_token);

2 Срок годности токена доступа (access_token) – 2 часа, токена обновления (refresh_token) - 3 календарных дня. При истечении срока годности токена
доступа (access_token) он должен быть обновлен с использованием токена обновления (refresh_token) и уникального идентификатора интеграции (Id
клиента). В случае истечения срока действия токена доступа (access_token) решение будет отвечать кодом ответа HTTP 401 (Unauthorized) 

'''


parser = driver.Parser('firefox')

def authorize(parser,client_id, redict_url):
   
    url = ''  
    list = ['https://oauth.mtt.ru/oauth/authorize?response_type=code&client_id=',client_id,'&redirect_uri=', redict_url,'&scope=https://mtt.ru/auth.tokens.readwrite']  
    url = url.join(list)
      
    url = parser.walker.get(url)
    
    

authorize(parser) 
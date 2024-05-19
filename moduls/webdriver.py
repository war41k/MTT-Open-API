
import os
import time
import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as FireFox_Options


import moduls.sysos as sysos



system = sysos.System()

class brauser:

    def __init__(self,name):
        
        self.name = name 
        self.platform = system.getplatform()
        self.profile = ""
        self.name_proc = ""
        self.path_driver = ""
        self.user_dir = os.path.expanduser("~")
        self.root_dir = os.getcwd()
        self.x = system.x[0]
        
        
        self.binary_location = self.root_dir+"\\driver\\"
          
                            
        if self.name == 'firefox':
            
            #options
            self.options = FireFox_Options()   
            self.options.add_argument("--window-size=1920,1080")
            self.options.add_argument("--start-maximized")
            self.options.add_argument("--disable-popup-blocking")
            self.options.add_argument("--no-sandbox")
            self.options.add_argument("--incognito")
            self.options.add_argument("--disable-extensions")            
                         
                  
            if self.platform =='Windows':
                                
                self.options.binary_location = self.root_dir +'\\driver\\Firefox\\firefox.exe'    
                #path`s                
                
                self.name_proc = 'firefox.exe'
                self.path_driver = self.root_dir +'\\driver\\geckodriver.exe'
                self.path_defolt_profile = self.user_dir+'\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles'
                
                self.profile = self.get_profile_default()
                
                system.close_process(self.name_proc)
                
                self.path_driver = system.copydriver_inpath(system.get_path() , self.path_driver)        
                self.service = Service(executable_path=self.path_driver)            
                        
                self.options.profile = FirefoxProfile(self.profile)
               
            else:
                self.options.binary_location = "/usr/bin/firefox/"    
                self.path_defolt_profile = "~/.mozilla/firefox"     
                       
            self.walker = Firefox(service=self.service, options = self.options)     
            
 
    def get_profile_default(self):
         
        file_path = '' 
                     
        for filename in os.listdir(self.path_defolt_profile):
            file_path = os.path.join(self.path_defolt_profile, filename)
            if file_path.find('default-release') >0:
                break
                
        return file_path      
    
    
class cookies:
    
    def __init__(self, old_cookies, new_cookies):   
        self.new_cookies = '' 
        pass
   
    def copy(self, src):

        if system.isdir(self.new_cookies):
            system.delete_dir(self.new_cookies)    
        
        if system.isdir(src) :
                system.copy_dir(src,self.profile_path)
                                            
class Parser:
    
    def __init__(self, brauser_name):
               
        self.connected = False
        self.platform = system.getplatform()
            
        self.list_user_agents = self.get_list_user_agents()
        brouser = brauser(brauser_name)        

        self.walker = brouser.walker
     
    def get_list_user_agents(self):
        
        list =[]
        for i in [{"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.3", "pct": 36.86}, {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.", "pct": 31.2}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.", "pct": 11.3}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.", "pct": 3.93}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3", "pct": 2.46}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.", "pct": 2.46}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.", "pct": 1.97}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3", "pct": 1.97}, {"ua": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.", "pct": 1.47}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.4", "pct": 0.98}, {"ua": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.", "pct": 0.49}, {"ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/25.0 Chrome/121.0.0.0 Safari/537.3", "pct": 0.49}, {"ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.", "pct": 0.49}, {"ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.3", "pct": 0.49}, {"ua": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.10", "pct": 0.49}, {"ua": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Geck", "pct": 0.49}, {"ua": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.3", "pct": 0.49}, {"ua": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.", "pct": 0.49}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.", "pct": 0.49}, {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.3", "pct": 0.49}, {"ua": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.3", "pct": 0.49}]:
            list.append(i['ua'])       
        
        return list 
                     
    def drivername(self, brauser_name):
        
        if brauser_name == 'firefox':
            if system.platform == "Windows":
                return 'geckodriver.exe'
            else:
                return 'geckodriver'        
       

    def find(self, by, value_search,  driver, timewait=10, format="element_to_be_clickable"):
        """Ищет элемент по условию задержки
        :by: selenium.webdriver.common.by
        :value_search: Значение для поска
        :timewait: Задержка в секундах
        """

        if format == "element_to_be_clickable":
            element = WebDriverWait(driver=driver, timeout=timewait).until(
                ec.element_to_be_clickable((by, value_search))
            )

        elif format == "visibility_of_element_located":
            element = WebDriverWait(driver=driver, timeout=timewait).until(
                ec.visibility_of_element_located((by, value_search))
            )

        elif format == "invisibility_of_element_located":
            element = WebDriverWait(driver=driver, timeout=timewait).until(
                ec.invisibility_of_element_located((by, value_search))
            )

        elif format == "element_located_to_be_selected":
            element = WebDriverWait(driver=driver, timeout=timewait).until(
                ec.element_located_to_be_selected((by, value_search))
            )

        elif format == "presence_of_element_located":
            element = WebDriverWait(driver=driver, timeout=timewait).until(
                ec.presence_of_element_located((by, value_search))
            )

        return element


    def get_pagesource(self):
        """Получает исходный код страницы"""

        page_source = self.walker.execute_script("return document.body.innerHTML;")

        return page_source

    def get_text(self):
        return self.walker.text

    def get_url(self, url):
        """get запрос с задержкой"""
        self.walker.get(url)
        time.sleep(1)

    def get_all_requests(self):
        """Список перехваченных запросов в хронологическом порядке."""
        return self.walker.requests

    def ajax_request_wait(self, request):
        """Wait for the request/response to complete"""
        return self.walker.wait_for_request(request)

    def iter_requests(self):
        """Возвращает итератор для перехваченных запросов. Полезно при работе с большим количеством запросов."""
        return self.walker.iter_requests()

    def get_last_header(self):
        last_request = self.walker.requests[-1]
        # Print the headers of the last request
        return last_request.headers

        
    def get_headers_webdriver(self, driver):
        
        script = """
        var xhr = new XMLHttpRequest();
        xhr.open('GET', window.location.href, false);
        xhr.send(null);
        return xhr.getAllResponseHeaders();
        """
        headers = driver.execute_script(script)
                
        
        # Преобразование строки заголовков в словарь
        headers = headers.splitlines()
        headers = dict([header.split(": ", 1) for header in headers])

        return headers    

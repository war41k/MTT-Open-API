import sys
import platform  # определяем виндовс линукс
import argparse

from moduls import yaml
import os
import shutil
import psutil
import platform

###########################ВРЕМЯ
from datetime import datetime

#Класс для работы с файлами и командной строкой
class System():
 
    def __init__(self) -> dict:
        self.platform = self.getplatform()
        self.x = self.get_x()
        
    #Парсинг командной сторки Виндовс                              
    def get_args(self):
        parser = argparse.ArgumentParser()
        # parser.add_argument ('-u', '--url',help = 'запрос в гугл',type=str)  #Запрос в гугл
        return parser

    #Получить разряд x32 или X64
    def get_x(self):
        return platform.architecture()

    def getplatform(self):
        if platform.system() == "Windows":
            return "Windows"
        else:
            return "Linux"

    def block_dir(self, dir,block_list):

        for filename in os.listdir(dir):
            
            try:
                file = open(dir+'\\'+filename, 'rb')
                block_list.append(file)                      
            except:
                pass    

    def unblock_dir(self, block_list):
        
        for i in block_list:
            i.close()
                 
    def chmod_dir(self, dir, chmod):
        os.chmod(dir, chmod)

        for filename in os.listdir(dir):
            os.chmod(dir+'\\'+filename, chmod)           
                
    def delete_dir(self,dir):
        shutil.rmtree(dir)            
    
    def copy_dir(self,src,dst):
        shutil.copytree(src,dst)

    def isdir(self,path):
        return os.path.isdir(path)
    
    def get_filename(source):
        list = source.split('\\')
        return list[len(list)-1]
    
    def copy_file(self, source, destination):
    
        try:   
            shutil.copyfile(source, destination)        
        except:
            pass
                
    def get_next_filename(self, file_nane, extension):
        global counter
        counter += 1
        return f"{file_nane}{counter}.{extension}"

    def isfile(self, path):        
        return os.path.isfile(path) 
    
    def create_file(self, path):
        return file(path)
        
    def remove_file(self,path):
        os.remove(path)
    
    def close_process(self,process):
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            if proc.info['name'] == process:
               proc.kill()
     
    def get_path(self):
        
        if self.platform == "Windows":
            return os.getenv('PATH')
        else:
            return os.environ("PATH")
    
    def copydriver_inpath(self, path, bin):

        pathlist = path.split(';')
        
        list = bin.split('\\')
        name_file = list[len(list)-1]       
        
        for i in pathlist:     
            if i =='':
                continue
            
            if self.isdir(i) ==False:
                continue 
                       
            try:                   
                file = os.path.join(i,name_file)                        
                if self.isfile(file):
                    self.remove_file()       
                   
                self.copy_file(bin, file)
                
                if self.isfile(file):
                    break
            except:
                pass
        
        return file
    
class file():
    
    def __init__(self, path):
        self._file =  open(path, 'w')     
         
    def save(self):        
        self._file.close()       
               
class settings():
    
    def getnamespace(self):
        parser = self.get_args()
        parser.parse_args(sys.argv[1:])

    def getsitings(self, setings):
        with open(setings, "r") as file:
            self = yaml.safe_load(file)
            file.close()

        return self
#Класс для работы со строками создан для обрамления запроса sqllite3     
class formater():        

    def __init__(self):
        pass
    
    @staticmethod
    def toto_string(sting):
        return  "'"+sting+"'"   

#Класс для работы со временем создан для обрамления запроса sqllite3   
#Выводит текущие время в формате час и полный формат
class clock():
    
    def whats_time_now(self):
        return datetime.now()
    
    def get_minute(self):
        return self.whats_time_now().strftime("%Y-%m-%d %H:%M") 
    
    def what_minuts_now(self):
        return self.get_minute()[-2:]
          
    def get_hours(self):
        return self.whats_time_now().strftime("%Y-%m-%d %H")       
    
    def what_hour_now(self):
        return self.get_hours()[-2:]
    
    def get_days(self):
        return self.whats_time_now().strftime("%Y-%m-%d")       

    def what_days_now(self):
        return self.get_days()[-2:]
    
    def get_month(self):
        return self.whats_time_now().strftime("%Y-%m")       

    def what_month_now(self):
        return self.get_month()[-2:]

    def get_year(self):
        return self.whats_time_now().strftime("%Y")       

    def what_year_now(self):
        return self.get_year()    
  
    
    # def get_timestamp(self, date, time='minute'):
        
    #     """
    #     Возвращает время в зависимости от параметра time
    #     :time:
    #     minute - минута
    #     hour - час
    #     day - день
    #     month - месяц
    #     year - годав
    #     """   
    #     time_foramat = ""
    #     now = date
        
    #     if time == 'minute':
    #         time_foramat = "%Y-%m-%d %H:%M"
    #     elif time == 'hour':
    #         time_foramat = "%Y-%m-%d %H"
    #     elif time == 'day':
    #         time_foramat = "%Y-%m-%d"
    #     elif time == 'month':
    #         time_foramat = "%Y-%m"            
    #     elif time == 'year':
    #         time_foramat = "%Y"
        
    #     format_time = now.strftime(time_foramat)           
    #     format_time = "'"+format_time+"'"
        
    #     return format_time.replace(":", "':'")               


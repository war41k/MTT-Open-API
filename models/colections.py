

class value_table():
    #Таблица значений
    def __init__(self):
        
        self.colums = colums() # массив dict {name: Имя колонки, type: тип колонки}
        self.rows = rows() # строки таблицы значений
        self.Indexes = []
          
    def get_row(self):
        
        nr = row()
        for i in self.colums._col:     
            setattr(nr, i.name, None)

        setattr(nr,'index',len(self.rows._col))
    
        self.rows._col.append(nr)   
        
        return nr
                
class colums(value_table):

    # Колонки
    def __init__(self):
        self._col = []
    
    def add_to_collections(self, name, types):
            
        self._col.append(
            colum(
                name=name,
                types=self.get_types_sqllite(types),
                index=len(self._col)
            )
        )      
              
    def add_colums(self, name, types):
        self.add_to_collections(name, types)  
           
    def add_keys(self, name, types):
        self.add_to_collections(name, types)               
                 
    def get_types_sqllite(self, types, notnull=False):
        
        type_sql = ''        
        if types == key:
            type_sql = 'PRIMARY KEY'
        elif types == str:
            type_sql = 'TEXT'
        elif types == int:
            type_sql = "INTEGER" 
        elif types == float:
            type_sql = "REAL" 
        elif types == bool:
            type_sql = 'TEXT'       
        elif types == bytes:
            type_sql = "BLOB" 
            
        else:
            type_sql = "NULL"
        
        if notnull and type_sql != 'NULL':
            type_sql  = type_sql + " NOT NULL" # запрет пустых значений
                     
        return type_sql          
               
class colum(colums):
    #Колонка 
    def __init__(self, name, types, index):
        self.name = name
        self.type = types
        self.index = index
 
    def get_index(self):
        return self.index
    

class rows(value_table):
    #Строки
    def __init__(self):
        self._col = []
    
    def add(self,row):
        
      self._col.append(row)  
        
class row(value_table):
    #Строка 
    def __init__(self):    
        self.get_new_row()              
                                     
    def get_new_row(self):
        return self          
    
class key():
    def __init__(self,types):
        self.type_sql = ''        

        if types == str:
            self.type_sql = 'TEXT'
        elif types == int:
            self.type_sql = "INTEGER" 
        elif types == float:
            self.type_sql = "REAL"       

    
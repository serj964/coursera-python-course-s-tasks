#погружение в python
#неделя 4 задание 1
#файл с магическими методами

import os.path
import tempfile
import random

class File:
    def __init__(self, file_path):
        if os.path.exists(file_path):
            self.file_path = file_path
        else:
            with open(file_path, 'x') as f:
                self.file_path = file_path
        
    def read(self):
        with open(self.file_path, 'r') as f:
            return f.read()
        
    def write(self, string):
        with open(self.file_path, 'w') as f:
            return f.write(string)
            
    def __str__(self):
        return os.path.abspath(self.file_path)
    
    def __iter__(self):
        string_list = []
        with open(self.file_path, 'r') as f:
            for line in f:
                string_list.append(line)
        return iter(string_list)
    
    def __add__(self, obj):
        a = random.randint(1, 100)
        with open(self.file_path, 'r') as f1:
            self.value1 = f1.read()
        with open(obj.file_path, 'r') as f2:
            self.value2 = f2.read()
        with open(tempfile.gettempdir() + '/temp{}.txt'.format(a), 'w') as f:
            f.write(self.value1 + self.value2)
        return File(f.name)

from difflib import Differ 
  
with open('provamain.py') as file_1, open('provagay.py') as file_2: 
    differ = Differ() 
  
    for line in differ.compare(file_1.readlines(), file_2.readlines()): 
        print(line) 

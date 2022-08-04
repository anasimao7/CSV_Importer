# import OS
from os import listdir
 
input_folder = 'D:\\Teste_4\\Original\\'
for file_name in listdir(input_folder):
 if file_name.endswith('.csv'):
       text = open(input_folder + file_name, "r", encoding="utf8")
       text = ''.join([i for i in text]) \
       .replace('","', '+') \
       .replace('"','') \
       .replace('+','-') \
       .replace(',', '|') \
       .replace('.', ',') \
       .replace('-', '') \
       .replace('\r', '|')
       #.strip('\r') 
       x = open(input_folder + file_name,"w", encoding="utf8")
       x.writelines(text)
       x.close()
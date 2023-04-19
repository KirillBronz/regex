from pprint import pprint
import csv
import re

with open ('phonebook_raw.csv', encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=',')
    contact_list = list(rows)
    pprint(contact_list)

def normalise (rows):
    result = [''.join(worker[0:3]).split('')[0:3] + worker[3:7] for worker in rows]
        
    return result

def rm_duplicates (correct_name_list):
    no_duplicates = []
    for compared in correct_name_list:
      for worker in correct_name_list:
          if compared [0:2] == worker [0:2]:
             worker_list = compared
             compared = worker_list[0:2]
             for i in range (2,7): 
                 if worker_list[i] == '':
                     compared.append(worker[i])
                 else : 
                    compared.append(worker_list[i])
    if compared not in no_duplicates:
        no_duplicates.append(compared)

    return no_duplicates
        
def num_upd(rows , regular , new): 
    phonebook = []
    ptrn = re.compile(regular)
    phonebook = [[ptrn.sub(new,string) for string in strings] for strings in rows] 

    return phonebook

correct_name_list = normalise(contact_list)
no_duplicates_list = rm_duplicates(correct_name_list)
reg_1 = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})'
corrected_list = num_upd(no_duplicates_list , reg_1, r'+7(\2)\3-\4-\5')
reg_2 = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s]*[(доб.\s]*(\d+)[)]*'
corrected_phone_book = num_upd(corrected_list, reg_2, r'+7(\2)\3-\4-\5 доб.\6')

with open ('phonebook.csv', 'w', encoding='utf-8') as f:
  writer = csv.writer(f ,delimiter=",")
  writer.writerow(corrected_phone_book)







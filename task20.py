
import re 
def isCyrillic(text): 	
    return bool(re.search('[а-я А-Я]', text)) 
list_en = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JZ', 10:'QZ'} 
list_ru = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'} 
text = input('Введите слово: ').upper() 
if isCyrillic(text): 	
    print('Стоимость слова: ')
    print(sum([a for b in text for a, v in list_ru.items() if b in v])) 
else: 	
    print('Стоимость слова: ')
    print(sum([a for b in text for a, v in list_en.items() if b in v])) 

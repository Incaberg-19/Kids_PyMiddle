# Словари (dict). Структура данных каждый элемент которой
# имеет шаблон ключ : значение

my_dict = {1: "значение", 'hello': 123}

#Чтобы получить значение по ключу:
print(my_dict['hello'])

my_dict = dict(ключ="значение", ключ2=123)
print(my_dict)

my_dict["новый_ключ"] = 'hello no'
print(my_dict)

my_dict['ключ'] = "new" # изменение значения по ключу
print(my_dict)

del my_dict["ключ"] # удаление по ключу
print(my_dict)

my_dict['ключ'] = "Я здесь!!"
print(my_dict)
removed_value = my_dict.pop("ключ") # снова удаление, но теперь
# значение удалённого ключа мы сохраняем в removed_value
print(my_dict,removed_value)

myDict={1:'am i',2:'not u',3:'hell to u'}
for key in myDict:
    print(key)

for value in myDict.values():
    print(value)

my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
#value = my_dict.pop('aple') # выдаст ошибку ведь такого элемента нету
value = my_dict.pop('aple', None) # не выдаст ошибку
print(my_dict,value)


days_of_week = {
    1:"понедельник",
    2:"вторник",
    3:"среда",
    4:"четверг",
    5:"пятница",
    6:"суббота",
    7:"воскресенье",
}

number=int(input("День недели? - "))
print(days_of_week[number])
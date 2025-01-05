# Анонимные функции - функции без имени, которые применяет обычно там,
# где они используются. В отличии от расположения обычных функций - сверху.

# Шаблон:
# lambda аргументы: выражение

amount = lambda x,y: x+y 
square = lambda x: x * x

print(amount(10,5)) # 15
print(square(5)) # 25

# Функция map(). Шаблон:
# map(function, iterable) # iterable - итерируемый объект
# Итерабельным объектом считается любой Python объект, 
# который может возвращать свои элементы по одному, 
# разрешая их перебрать в цикле for.

numbers=['1','2','3','4','5']
# Превратить все элементы списка в числа. Здесь есть несколько способов:

numbers2=[int(num) for num in numbers] # списковые включения
numbers3=list(map(int,numbers)) # применение int к каждому элементу списка numbers

print(numbers2,'num2')
print(numbers3,'num3')

numbers=['123','12','12345','','0001']

lenList=list(map(len,numbers)) # формирование списка длин элементов numbers
print(lenList)

# использование анонимных функций вместе с map

numbers=[1,2,3,4,5,6,7,8,9,10]
newNumbers=list(map(lambda x:str(x+10),numbers))
print(newNumbers)
# Создание списков.

# Создать список заполненный от 1 до 10.
numbers1=[]
for i in range(1,10+1):
    numbers1.append(i)
print(numbers1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# краткая запись
numbers2=[i for i in range(1,10+1)] 
print(numbers2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# такая запись называется списковым включением (list comprehension).

# Шаблон:
# new_list = [выражение for элемент in последовательность if условие].
# Часть с условием if указывается опционально.

numbers3=[i for i in range(1,22) if i%3==0]
# создали список с числами которые кратны 3
print(numbers3)

# Помимо списковых включений можно использовать
# range(началоДиапозона,конецДиапозона,шаг)
numbers4=list(range(1,10+1)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers4)

numbers5=list(range(10,-1,-1))
print(numbers5) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
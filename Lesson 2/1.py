# Showing why we need functions

# Задача - суммировать все цифры в строке.
string1 = '12345'
summa=0
for symvol in string1:
    summa=summa+int(symvol)
print(summa)
# А что если у нас несколько строк?
string2 = '4546'
summa=0
for symvol in string2:
    summa=summa+int(symvol)
print(summa)

string3 = '1234999'
summa=0
for symvol in string3:
    summa=summa+int(symvol)
print(summa)

# Получается большой код, не правда ли? А делаем то мы одно и то же.
# Amount - сумма.

# Функция - блок кода выполняющий определённую задачу.
def amountInString(string):
    amount=0
    for symvol in string:
        amount+=int(symvol)
    return amount
print(f'Сумма цифр в первой строке: {amountInString(string1)}')
print(f'Сумма цифр во второй строке: {amountInString(string2)}')
print(f'Сумма цифр в третьей строке: {amountInString(string3)}')

# Код уменьшился в несколько раз.

# Для чего нужны функции?
# 1. Сокращение кода. С их использованием дублировать код не требуется.

import time
start_time = time.time()
for i in range(10**9):
    pass # Пропустить - ничего не делать
end_time = time.time() 
execution_time = end_time - start_time  # Вычисление времени выполнения
print(f"Время выполнения программы без функции: {execution_time:.2f} секунд")
# Получается около 32 секунд

start_time = time.time()
def example():
    for i in range(10**9):
        pass
example()
end_time = time.time() 
execution_time = end_time - start_time
print(f"Время выполнения программы с функцией: {execution_time:.2f} секунд")
# Получается около 15 секунд

# Почему так? Код внутри функции кэшируется автоматически, а обычный код нет.

# Для чего нужны функции?
# 1. Сокращение кода. С их использованием дублировать код не требуется.
# 2. Ускорение выполняемого кода. 

# нотация - принятая норма в какой либо области которой все придерживаются
# в данном случае нотация писания имён функций - example_case, exampleCase
# case - дело, случай, обстоятельство.
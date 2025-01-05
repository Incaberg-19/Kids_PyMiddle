# w — запись или создание файла
# r — чтение файла
# Для работы c файлами в Python требуется открыть отдельный поток работы с файлом
# делается это при помощи функции open. ДВА ПОТОКА С ОДНИМ ФАЙЛОМ РАБОТАТЬ НЕ МОГУТ!
fileWrite = open("test_file.txt","w") # создаёт/пересоздаёт файл
fileWrite.write("hello") # запись в файл сообщения
fileWrite.write("everyone") # записывается не на новой строчке!
fileWrite.write("\nevery") # \n - символ перехода на новую строку

fileRead = open("twist.txt","r") # можем открыть другой поток для работы с другим файлом
print(fileRead)
#<_io.TextIOWrapper name='twist.txt' mode='r' encoding='cp1252'>
print(fileWrite)
#<_io.TextIOWrapper name='test_file.txt' mode='w' encoding='cp1252'>
#<_io.TextIOWrapper> - это объект, возвращаемый функцией open()
# при открытии файла для чтения/записи текста.
# Атрибуты объекта <_io.TextIOWrapper>:
# name - имя файла
# mode - режим открытия ('r' для чтения, 'w' для записи)
# encoding - кодировка файлов (например, 'cp1252')
# Кодировка - это способ представления символов и информации в компьютерной системе. 


text = fileRead.read()
print(f'Текст из {fileRead.name}\n{text}')
fileRead.close()
# а чтобы прочитать первый (test_file.txt) нужно закрыть поток записи в файл
# и открыть новый поток - чтения
fileWrite.close() # закрыли
fileRead = open("test_file.txt","r") # открыли
text = fileRead.read()
print(f'Текст из {fileRead.name}\n{text}')
fileWrite.close() # не забываем закрывать после работы!

# Попробуем поработать с русскими символами
ruFile = open ('russian.txt','r')
text = ruFile.read()
print(f'Текст из {ruFile.name}\n{text}')
ruFile.close()
# Получим это:
# ÐŸÑ€Ð¸Ð²ÐµÑ‚! ÐšÐ°Ðº Ñ‚Ð²Ð¾Ð¸ Ð´ÐµÐ»Ð°,
# Ð”Ñ€ÑƒÐ¶Ð¸Ñ‰Ðµ?

# А что будет если самому записать русские символы в файл?

# ruFile = open ('newRussian.txt','w')
# ruFile.write('Привет! Как твои дела?\nВсё отлично!')
# ruFile.close()
# ruFile = open ('newRussian.txt','r')
# text = ruFile.read()
# print(f'Текст из {ruFile.name}\n{text}')
# ruFile.close()

# Получим ошибку
# Traceback (most recent call last):
#   File "pyMiddle\Lesson 6\1.py", line 47, in <module>
#     ruFile.write('Привет! Как твои дела?\nВсё отлично!')
#     ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "AppData\Local\Programs\Python\Python313\Lib\encodings\cp1252.py", line 19, in encode
#     return codecs.charmap_encode(input,self.errors,encoding_table)[0]
#            ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-5: character maps to <undefined>

# Что из этого следует? Предположительно, кодировка 'cp1252', которая используется
# по умолчанию, не может обработать русские символы. Давайте попробуем её сменить.

ruFile = open ('russian.txt','r',encoding='utf-8')
text = ruFile.read()
print(f'Текст из {ruFile.name}\n{text}')
ruFile.close()
# Теперь всё работает. И с английским тоже.
# Текст из russian.txt
# Привет! Как твои дела,
# Дружище?
# hello!
# принимаемый словарь можно изменять в функции
def addTasks(dictionary: dict) -> None:
    day = (input("Введите нужный день недели: ").strip()).lower()
    if day in dictionary:

        try:
            dictionary[day].remove("задачи отсутствуют")
        except ValueError:
            pass

        tasks = ((input("Введите задачи через пробел: ").strip()).lower()).split()

        for case in tasks:
            dictionary[day].append(case)
    
    else:
        print('Такого дня не существует')

def removeTasks(dictionary: dict) -> None:

    day = (input("Введите нужный день недели: ").strip()).lower()
    if day in dictionary:

        tasks = ((input("Введите задачи через пробел: ").strip()).lower()).split()

        for case in tasks:
            try:
                dictionary[day].remove(case)
            except ValueError:
                pass
        
        if len(dictionary[day])==0:
            dictionary[day].append("задачи отсутствуют")
    
    else:
        print('Такого дня не существует')
from tools.processTasks import *
from tools.output import *

def main() -> None:

    days = {
        "понедельник" : ["задачи отсутствуют"],
        "вторник" : ["задачи отсутствуют"],
        "среда" : ["задачи отсутствуют"],
        "четверг" : ["задачи отсутствуют"],
        "пятница" : ["задачи отсутствуют"],
        "суббота" : ["задачи отсутствуют"],
        "воскресенье" : ["задачи отсутствуют"],
    }

    while True:
        print('1 - просмотреть список задач на неделю')
        print('2 - добавить задачи на конкретный день')
        print('3 - удалить задачи конкретного дня')
        print('4 - выйти из меню')
        choice = int(input('Впишите выбранную цифру: ').strip())
        if choice==1:
            #print(days) # будет выглядить некрасиво
            printDict(days) 
        elif choice==2:
            addTasks(days)
        elif choice==3:
            removeTasks(days)
        elif choice==4:
            break

main()
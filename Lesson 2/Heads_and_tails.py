# Теперь напишем игру используя функции. 

import random

def choices() -> tuple[str,str]:
    coin = random.choice(  ['орёл','решка'] )
    player = (input("Орёл или решка? ").strip()).lower()
    return player,coin

def ChooseWinner(player:str,coin:str) -> None:
    if player.find('орёл')!=-1 and coin.find('орёл')!=-1:
        print('Игрок победил')
    elif player.find('решка')!=-1 and coin.find('решка')!=-1:
        print('Игрок победил')
    else:
        print('Игрок проиграл')

def main() -> None:
    player,coin = choices()
    ChooseWinner(player,coin)

main()
# main - Основная функция является точкой входа в программу.
# Это место, где начинается выполнение кода программы.
# задачи main - вызывать все нужные функции,
# распределять возвращаемые данные между другими функциями.

# a=choices()
# print(a,type(a))
# tuple - неизменяемая индексируемая последовательность
# a=tuple([1,2,3,4])
# print(a)
# a[0]='5' # ошибка
# print(a[0])
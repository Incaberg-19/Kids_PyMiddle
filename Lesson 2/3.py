# Напишем игру "Орёл и Решка". Сначала без функций.

import random

coin = random.choice(  ['орёл','решка'] )
player = (input("Орёл или решка? ").strip()).lower()
# strip() - убирает пробелы в начале и в конце

# -1 это возвращаемый индекс. Если подстрока 'орёл' не нашлась
# в строке player, то вернётся -1. Если -1 не вернулся, то
# вернулась позиция с которой начинается подстрока 'орёл'.
if player.find('орёл')!=-1 and coin.find('орёл')!=-1:
    print('Игрок победил')
elif player.find('решка')!=-1 and coin.find('решка')!=-1:
    print('Игрок победил')
else:
    print('Игрок проиграл')

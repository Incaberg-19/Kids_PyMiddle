from modules.func import definePlayers
from modules.arena import Arena

class Game:
    def __init__(self,countOfPlayers):

        self.classes={
            'Рыцарь':[[150,200],[50,100]],
            'Маг':[[100,150],[75,125]],
            'Ополченец':[[50,100],[20,50]],
        }
        self.players=definePlayers(self.classes,countOfPlayers)
        self.arena = Arena(self.players)
    
    def startGame(self):
        while True:
            if len(self.players)!=1:
                f1,f2=self.arena.chooseFighter()
                print('Дерутся')
                print(self.players[f1].getInfo())
                print(self.players[f2].getInfo())
                print(self.arena.processFight(f1,f2))
                print()
                for player in self.players:
                    print(player.getInfo())
            else:
                print('Победитель')
                print(self.players[0].getInfo())
                break

            input() # для заддержки


#print(__name__) # выдаёт __main__, но имя файла game.py. Всё потому что game.py является файлом запуска.
# файл запуска (тот файл который мы запускаем по нажатию кнопки) - всегда называется __main__
#definePlayers(1,2) # выдаёт modules.func, ведь он вызвался (запустился) из нашего __main__

if __name__ == "__main__":
    game=Game(10)
    game.startGame()

# Теперь код файла 2.py будет исполнен только в том случае, когда запускается именно файл main.py
from random import randint,choice

class Arena:
    def __init__(self, players):
        self.players=players
        self.keys=list(range(len(self.players)))

    def chooseFighter(self):
        self.keys=list(range(len(self.players))) # каждый раз обновляем список ключей поторму что
        # после удаления пользователя этот список меняется
        Indexfighter1=choice(self.keys)
        Indexfighter2=choice(self.keys)
        while Indexfighter2==Indexfighter1:
            Indexfighter2=choice(self.keys)
        return Indexfighter1,Indexfighter2
    
    def processFight(self,Indexfighter1,Indexfighter2):
        while True:
            firstStrike=randint(1,2)
            if firstStrike==1:
                health=self.players[Indexfighter2].getHealth() - self.players[Indexfighter1].getDamage()
                self.players[Indexfighter2].setHealth(health)
            else:
                health=self.players[Indexfighter1].getHealth() - self.players[Indexfighter2].getDamage()
                self.players[Indexfighter1].setHealth(health)

            if self.players[Indexfighter1].getHealth()<0:
                winner = f'{self.players[Indexfighter2].getName()} победил!'
                self.players.pop(Indexfighter1)
                self.keys.remove(Indexfighter1)
                return winner
            
            elif self.players[Indexfighter2].getHealth()<0:
                winner = f'{self.players[Indexfighter1].getName()} победил!'
                self.players.pop(Indexfighter2)
                self.keys.remove(Indexfighter2)
                return winner
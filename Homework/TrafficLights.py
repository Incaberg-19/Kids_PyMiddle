class Traffic_lights:
    def __init__(self,states,times):
        self.times=times
        self.states=states
        self.indexState=0
        self.currentState=self.states[self.indexState]
        self.timer=0
    def changeState(self):
        self.indexState=self.indexState+1
        if self.indexState==len(self.states):
            self.indexState=0
        self.currentState=self.states[self.indexState]
    def changeStateByTimer(self):
        if self.timer>=self.times[self.indexState]:
            self.timer=0
            self.changeState()
        else:
            self.timer+=1

sCars=Traffic_lights(['Красный','Жёлтый','Зелёный'],[10,5,10])
sHumans=Traffic_lights(['Красный','Зелёный'],[15,11])
sHumans.changeState()
while True:
    sCars.changeStateByTimer()
    sHumans.changeStateByTimer()
    print(f'Для машин: {sCars.currentState}\nДля людей: {sHumans.currentState}')
    input()

    
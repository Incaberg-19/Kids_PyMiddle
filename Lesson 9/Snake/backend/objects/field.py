from pygame import Rect

class Field:
    def __init__(self,window_x,window_y,width,height):

        self._rects = []

        for x in range(0,window_x+1,width):
            for y in range(0,window_y+1,height):
                self._rects.append(Rect(x, y, width, height))

    def getListRects(self):
        return self._rects
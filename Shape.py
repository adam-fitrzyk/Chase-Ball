from pygame import Rect, Vector2
from math import pi

class Shape:
    '''Abstract Shape class. '''

    def __init__(self, rect:Rect, expr=None) -> None:
        '''Constructor Method of Shape Class. '''
        self.setRect(rect)
        self.setExpr(expr)

    def setRect(self, rect:Rect) -> None:
        self.__rect = rect
    
    def setExpr(self, expr) -> None:
        self.__expr = expr

    def getRect(self) -> Rect:
        return self.__rect
    
    def getExpr(self):
        return self.__expr

    def getCenter(self) -> Vector2:
        return Vector2(self.__rect.center)
    
    def getXRadius(self) -> int:
        return self.__rect.center[0] - self.__rect.left
    
    def getYRadius(self) -> int:
        return self.__rect.center[1] - self.__rect.top
    
    def findAngleTo(self, pos:tuple|Vector2) -> float:
        '''Returns an angle (in radians) from the center of the shape to some position using east as 0 rads and going anticlockwise. '''
        return (pos - self.getCenter()).angle_to((1, 0)) * pi/180
    
   
def main() -> None:
    pass

if __name__ == "__main__":
    main()
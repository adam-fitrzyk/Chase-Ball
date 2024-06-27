from pygame import Vector2, key, K_w, K_s, K_a, K_d
import GraphicsEngine as GE
from math import sqrt, sin, cos, pi
from pygame.time import Clock

class PhysEngine():
    '''Physics Engine Class that calculates velocities and inputs '''
 
    def __init__(self, acceleration:int=None, friction:int=None, bounce:int=None, start_pos:tuple[int,int]=None, radius:int=None):
        '''Constructor Method of the Physics Engine Class '''
        self.setAcc(acceleration)
        self.setFric(friction)
        self.setBoun(bounce)
        self.setStartPos(start_pos)
        self.setRadius(radius)
        self.__x_veloc = 0
        self.__y_veloc = 0
        self.__speed = 0
        self.__dt = 0
        self.__pos = Vector2(self.getStartPos())
        self.__clock = Clock()
        try: 
            self.__FPS = GE.GraphicsEngine.getFPS()
        except:
            self.__FPS = 60

    # Getters / Setters ---------------------------------

    def setAcc(self, acceleration=None) -> None:
        self.__acceleration = acceleration

    def setFric(self, friction=None) -> None:
        self.__friction = friction

    def setBoun(self, bounce=None) -> None:
        self.__bounce = bounce

    def setStartPos(self, start_pos=None) -> None:
        self.__start_pos = start_pos

    def setRadius(self, radius=None) -> None:
        self.__radius = radius

    def getAcc(self) -> int:
        return self.__acceleration
    
    def getFric(self) -> int:
        return self.__friction
    
    def getBoun(self) -> int:
        return self.__bounce
    
    def getStartPos(self) -> tuple[int, int]:
        '''Returns a tuple of coordinates (x, y) of starting position '''
        return self.__start_pos
    
    def getDt(self) -> float:
        return self.__dt

    def getVelocX(self) -> float:
        return self.__x_veloc
    
    def getVelocY(self) -> float:
        return self.__y_veloc
    
    def getPos(self) -> Vector2:
        return self.__pos
    
    def getSpeed(self) -> float:
        return self.__speed
    
    # Functional ------------------------------------------------

    def applyFric(self) -> None:
        '''Removes speed in accordance to the friction value. '''
        if self.getVelocX() > 0:
            self.__x_veloc -= self.getVelocX() * self.getFric()
        elif self.getVelocX() < 0:
            self.__x_veloc -= self.getVelocX() * self.getFric()

        if self.getVelocY() > 0:
            self.__y_veloc -= self.getVelocY() * self.getFric()
        elif self.getVelocY() < 0:
            self.__y_veloc -= self.getVelocY() * self.getFric()

    def wallColl(self) -> bool:
        '''Checks if entity has collided with a wall, and adjusts speed according to bounce value. Returns true if there was a collision with the wall. '''
        if self.getPos().x > GE.GraphicsEngine.getScreenWidth() - self.__radius:
            self.__x_veloc = -self.getVelocX() * self.__dt * self.getBoun() - self.getAcc()
            collision_x = True
        elif self.getPos().x < self.__radius:
            self.__x_veloc = -self.getVelocX() * self.__dt * self.getBoun() + self.getAcc()
            collision_x = True
        else:
            collision_x = False
        if self.getPos().y > GE.GraphicsEngine.getScreenHeight() - self.__radius:
            self.__y_veloc = -self.getVelocY() * self.__dt * self.getBoun() - self.getAcc()
            return True
        elif self.getPos().y < self.__radius:
            self.__y_veloc = -self.getVelocY() * self.__dt * self.getBoun() + self.getAcc()
            return True
        if collision_x:
            return True
        else:
            return False
        
    def moveTowards(self, pos:Vector2) -> None:
        '''Accelerates entity towards given position '''
        direction: Vector2 = pos - self.__pos
        angle = direction.angle_to((1, 0))
        self.__x_veloc += self.__acceleration * cos(-pi/180 * angle)
        self.__y_veloc += self.__acceleration * sin(-pi/180 * angle)
        
    def checkKeyPress(self) -> None:
        '''Checks if w, a, s or d key has been pressed and accelerates accordingly '''
        keys = key.get_pressed()
        if keys[K_w] and keys[K_d]:
            self.__x_veloc += 1/sqrt(2) * self.getAcc()
            self.__y_veloc -= 1/sqrt(2) * self.getAcc()
        elif keys[K_w] and keys[K_a]:
            self.__x_veloc -= 1/sqrt(2) * self.getAcc()
            self.__y_veloc -= 1/sqrt(2) * self.getAcc()
        elif keys[K_s] and keys[K_d]:
            self.__x_veloc += 1/sqrt(2) * self.getAcc()
            self.__y_veloc += 1/sqrt(2) * self.getAcc()
        elif keys[K_s] and keys[K_a]:
            self.__x_veloc -= 1/sqrt(2) * self.getAcc()
            self.__y_veloc += 1/sqrt(2) * self.getAcc()
        elif keys[K_w]:
            self.__y_veloc -= self.getAcc()
        elif keys[K_s]:
            self.__y_veloc += self.getAcc()
        elif keys[K_a]:
            self.__x_veloc -= self.getAcc()
        elif keys[K_d]:
            self.__x_veloc += self.getAcc()

    def stepTime(self) -> bool | None:
        '''Updates velocity and positions, returns True if there was a collision in current frame. '''
        self.__pos.x += self.__x_veloc * self.__dt
        self.__pos.y += self.__y_veloc * self.__dt
        self.__speed = sqrt(self.__x_veloc**2 + self.__y_veloc**2)
        self.applyFric()
        was_wall_coll = self.wallColl()
        # limits FPS
        # dt is delta time in seconds since last frame, used for framerate independent physics.
        self.__dt = self.__clock.tick(self.__FPS) / 1000
        return was_wall_coll


def main() -> None:
    pass

if __name__ == "__main__":
    main()
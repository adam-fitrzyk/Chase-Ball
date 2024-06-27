from pygame import Rect, Vector2
from Shape import Shape
from math import sqrt, sin, cos
from sympy import symbols, solve_poly_system, sqrt, sin, cos
import GraphicsEngine as GE

x, y = symbols('x y')

class Circle(Shape):
    '''Circle Shape Child Class with . '''
    
    def __init__(self, rect:Rect) -> None:
        '''Constructor Method for Circle Class. '''
        super().__init__(rect)
        r = self.getXRadius()
        x0 = self.getCenter().x
        y0 = GE.GraphicsEngine.getScreenHeight() - self.getCenter().y
        expr = (x - x0)**2 + (y - y0)**2 - r**2 # Equation of the circle -> must equal zero
        self.setExpr(expr)

    def findPointByAngle(self, angle) -> Vector2:
        '''Returns the point on the circle's surface corresponding to the given angle (measured in radians). '''
        x = self.getCenter()[0] + (self.getYRadius() * self.getXRadius() * cos(angle))/sqrt(sin(angle)**2 * self.getXRadius()**2 + cos(angle)**2 * self.getYRadius()**2)
        y = self.getCenter()[1] - (self.getYRadius() * self.getXRadius() * sin(angle))/sqrt(sin(angle)**2 * self.getXRadius()**2 + cos(angle)**2 * self.getYRadius()**2)
        return Vector2(x, y)
    
    def findIntersection(self, shape_eq) -> bool:
        '''Returns True if given point is inside the circle, otherwise return False. '''
        """
        outer_point = self.findPointByAngle(self.findAngleTo(shape.getCenter()))
        shape_point = shape.findPointByAngle(shape.findAngleTo(self.getCenter()))
        if outer_point.distance_to(self.getCenter()) >= shape_point.distance_to(self.getCenter()):
            return True
        else:
            return False
        """
        try:
            solutions = solve_poly_system([self.getExpr(), shape_eq], [x, y])
            for solution in solutions:
                if solution[0].is_real and solution[1].is_real:
                    return True
        except:
            return False
        else:
            return False

class Ellipse(Shape):
    '''Ellipse Shape Child Class. '''

    def __init__(self, rect:Rect):
        '''Constructor Method for Ellipse Class. '''
        super().__init__(rect)
        a = self.getXRadius()
        b = self.getYRadius()
        x0 = self.getCenter().x
        y0 = GE.GraphicsEngine.getScreenHeight() - self.getCenter().y
        expr = b**2*(x - x0)**2 + a**2*(y - y0)**2 - a**2*b**2 # Equation of the ellipse -> must equal zero
        self.setExpr(expr)

    def findPointByAngle(self, angle) -> Vector2:
        '''Returns the point on the ellipse's surface corresponding to the given angle (measured in radians). '''
        x = self.getCenter()[0] + (self.getYRadius() * self.getXRadius() * cos(angle))/sqrt(sin(angle)**2 * self.getXRadius()**2 + cos(angle)**2 * self.getYRadius()**2)
        y = self.getCenter()[1] - (self.getYRadius() * self.getXRadius() * sin(angle))/sqrt(sin(angle)**2 * self.getXRadius()**2 + cos(angle)**2 * self.getYRadius()**2)
        return Vector2(x, y)
    
    def findIntersection(self, shape:Shape) -> bool:
        '''Returns True if given point is inside the ellipse, otherwise return False. '''
        
        outer_point = self.findPointByAngle(self.findAngleTo(shape.getCenter()))
        shape_point = shape.findPointByAngle(shape.findAngleTo(self.getCenter()))
        if outer_point.distance_to(self.getCenter()) >= shape_point.distance_to(self.getCenter()):
            return True
        else:
            return False
        
        """
        if type(shape) == Circle:
            t = symbols('t')
            new_eq = self.getExpr().subs([(x, shape.getCenter().x + shape.getXRadius()*(1 - t**2)/(1 + t**2)), (y, shape.getCenter().y + shape.getXRadius()*(2*t)/(1+t**2))])
            try:
                solutions = solve_poly_system([new_eq], t)
                print(solutions)
                for solution in solutions:
                    if solution[0].is_real and solution[1].is_real:
                        return True
            except:
                print("solver failed... ")
                return False
            else:
                return False
        else:
            try:
                solutions = solve_poly_system([self.getExpr(), shape.getExpr()], [x, y])
                for solution in solutions:
                    if solution[0].is_real and solution[1].is_real:
                        return True
            except:
                return False
            else:
                return False
        """


def main() -> None:
    pass

if __name__ == "__main__":
    main()
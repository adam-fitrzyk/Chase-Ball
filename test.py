#import pygame
from time import sleep, time

'''
mydict = {'hi': 2, 3: 'three'}

for key in mydict:
    print(key, mydict[key])

pygame.init()
screen = pygame.display.set_mode((1280, 720))
sleep(1)
pygame.display.quit()

v1 = pygame.Vector2((2, 1))
v2 = (-1, -3)
v3 = v2 - v1
print(v3)
print('v3 angle =', v3.angle_to((1, 0)))

if (None, None):
    print('empty tuple is a value')

screen = pygame.display.set_mode((1280, 720))
screen.fill('purple')
pygame.display.flip()
sleep(1)
screen = pygame.display.set_mode((1280, 720))
sleep(0.01)
screen.fill('purple')
pygame.display.flip()
sleep(1)

pygame.Rect
'''



from sympy import *

x, y = symbols('x y')

'''
(x - a)**2 + (y - b)**2 - r**2 - x**2*d**2 - y**2*c**2 - c**2*d**2
'''

'''
x in terms of y =
1:
(-a - sqrt(a**2*d**2 + b**2*d**2 - b**2 - 2*b*d**2*y + 2*b*y + c**2*d**4 - c**2*d**2*y**2 - c**2*d**2 + c**2*y**2 - d**2*r**2 + d**2*y**2 + r**2 - y**2))/(d**2 - 1)
2:
(-a + sqrt(a**2*d**2 + b**2*d**2 - b**2 - 2*b*d**2*y + 2*b*y + c**2*d**4 - c**2*d**2*y**2 - c**2*d**2 + c**2*y**2 - d**2*r**2 + d**2*y**2 + r**2 - y**2))/(d**2 - 1)


ANSWER:
1: y =
(-b*d**2 + b - sqrt(a**2*c**2*d**4 - 2*a**2*c**2*d**2 + a**2*c**2 - a**2*d**4 + 2*a**2*d**2 - a**2 - 2*a*c**2*d**2 + 2*a*c**2 + 2*a*d**2 - 2*a + b**2*c**2*d**4 - 2*b**2*c**2*d**2 + b**2*c**2 + c**4*d**6 - 2*c**4*d**4 + c**4*d**2 - c**2*d**6 - c**2*d**4*r**2 + 2*c**2*d**4 + 2*c**2*d**2*r**2 - 2*c**2*d**2 - c**2*r**2 + c**2 + d**4*r**2 - 2*d**2*r**2 + d**2 + r**2 - 1))/(c**2*d**2 - c**2 - d**2 + 1)
1: x =
c*sqrt((-a**2*c**2*d**2 + a**2*c**2 + a**2*d**2 - a**2 + 2*a*c**2 - 2*a - b**2*c**2*d**2 + b**2*c**2 - b**2*d**2 + b**2 - 2*b*sqrt(a**2*c**2*d**4 - 2*a**2*c**2*d**2 + a**2*c**2 - a**2*d**4 + 2*a**2*d**2 - a**2 - 2*a*c**2*d**2 + 2*a*c**2 + 2*a*d**2 - 2*a + b**2*c**2*d**4 - 2*b**2*c**2*d**2 + b**2*c**2 + c**4*d**6 - 2*c**4*d**4 + c**4*d**2 - c**2*d**6 - c**2*d**4*r**2 + 2*c**2*d**4 + 2*c**2*d**2*r**2 - 2*c**2*d**2 - c**2*r**2 + c**2 + d**4*r**2 - 2*d**2*r**2 + d**2 + r**2 - 1) - c**2*d**4 + c**2*d**2*r**2 + c**2*d**2 - c**2*r**2 + c**2 + d**4 - d**2*r**2 - d**2 + r**2 - 1)/(d**2 - 1))/(d*(c**2 - 1))
2: x =
-c*sqrt(-(a**2*c**2*d**2 - a**2*c**2 - a**2*d**2 + a**2 - 2*a*c**2 + 2*a + b**2*c**2*d**2 - b**2*c**2 + b**2*d**2 - b**2 + 2*b*sqrt(a**2*c**2*d**4 - 2*a**2*c**2*d**2 + a**2*c**2 - a**2*d**4 + 2*a**2*d**2 - a**2 - 2*a*c**2*d**2 + 2*a*c**2 + 2*a*d**2 - 2*a + b**2*c**2*d**4 - 2*b**2*c**2*d**2 + b**2*c**2 + c**4*d**6 - 2*c**4*d**4 + c**4*d**2 - c**2*d**6 - c**2*d**4*r**2 + 2*c**2*d**4 + 2*c**2*d**2*r**2 - 2*c**2*d**2 - c**2*r**2 + c**2 + d**4*r**2 - 2*d**2*r**2 + d**2 + r**2 - 1) + c**2*d**4 - c**2*d**2*r**2 - c**2*d**2 + c**2*r**2 - c**2 - d**4 + d**2*r**2 + d**2 - r**2 + 1)/(d**2 - 1))/(d*(c**2 - 1))
 --> These two x values are the same just + or -

2: y =
(-b*d**2 + b + sqrt(a**2*c**2*d**4 - 2*a**2*c**2*d**2 + a**2*c**2 - a**2*d**4 + 2*a**2*d**2 - a**2 - 2*a*c**2*d**2 + 2*a*c**2 + 2*a*d**2 - 2*a + b**2*c**2*d**4 - 2*b**2*c**2*d**2 + b**2*c**2 + c**4*d**6 - 2*c**4*d**4 + c**4*d**2 - c**2*d**6 - c**2*d**4*r**2 + 2*c**2*d**4 + 2*c**2*d**2*r**2 - 2*c**2*d**2 - c**2*r**2 + c**2 + d**4*r**2 - 2*d**2*r**2 + d**2 + r**2 - 1))/(c**2*d**2 - c**2 - d**2 + 1)
 --> The two y values are the same but root is + or -
1: x =
-c*sqrt((-a**2*c**2*d**2 + a**2*c**2 + a**2*d**2 - a**2 + 2*a*c**2 - 2*a - b**2*c**2*d**2 + b**2*c**2 - b**2*d**2 + b**2 + 2*b*sqrt(a**2*c**2*d**4 - 2*a**2*c**2*d**2 + a**2*c**2 - a**2*d**4 + 2*a**2*d**2 - a**2 - 2*a*c**2*d**2 + 2*a*c**2 + 2*a*d**2 - 2*a + b**2*c**2*d**4 - 2*b**2*c**2*d**2 + b**2*c**2 + c**4*d**6 - 2*c**4*d**4 + c**4*d**2 - c**2*d**6 - c**2*d**4*r**2 + 2*c**2*d**4 + 2*c**2*d**2*r**2 - 2*c**2*d**2 - c**2*r**2 + c**2 + d**4*r**2 - 2*d**2*r**2 + d**2 + r**2 - 1) - c**2*d**4 + c**2*d**2*r**2 + c**2*d**2 - c**2*r**2 + c**2 + d**4 - d**2*r**2 - d**2 + r**2 - 1)/(d**2 - 1))/(d*(c**2 - 1))
2: x =
c*sqrt((-a**2*c**2*d**2 + a**2*c**2 + a**2*d**2 - a**2 + 2*a*c**2 - 2*a - b**2*c**2*d**2 + b**2*c**2 - b**2*d**2 + b**2 + 2*b*sqrt(a**2*c**2*d**4 - 2*a**2*c**2*d**2 + a**2*c**2 - a**2*d**4 + 2*a**2*d**2 - a**2 - 2*a*c**2*d**2 + 2*a*c**2 + 2*a*d**2 - 2*a + b**2*c**2*d**4 - 2*b**2*c**2*d**2 + b**2*c**2 + c**4*d**6 - 2*c**4*d**4 + c**4*d**2 - c**2*d**6 - c**2*d**4*r**2 + 2*c**2*d**4 + 2*c**2*d**2*r**2 - 2*c**2*d**2 - c**2*r**2 + c**2 + d**4*r**2 - 2*d**2*r**2 + d**2 + r**2 - 1) - c**2*d**4 + c**2*d**2*r**2 + c**2*d**2 - c**2*r**2 + c**2 + d**4 - d**2*r**2 - d**2 + r**2 - 1)/(d**2 - 1))/(d*(c**2 - 1))
 --> These two x values are the same just + or -
'''
start = time()
a = 1
b = 4
r = 2
c = 2
d = 1
e = 1
f = 1
eq1 = (x - a)**2 + (y - b)**2 - r**2
eq2 = d**2*(x - e)**2 + c**2*(y - f)**2 - c**2*d**2
print(eq1, eq2, sep='\n')

#a, b, r, c, d = symbols('a b r c d')
sols = solve_poly_system([eq1, eq2], [x, y])
print(sols)
print("Solutions: ")
for sol in sols:
    if sol[0].is_real and sol[1].is_real:
        print(f'x: {sol[0]}\n -> {N(sol[0])}')
        print(f'y: {sol[1]}\n -> {N(sol[1])}')
end = time()
print(f'Time taken: {end - start} seconds')

start = time()
t = symbols('t')
new_eq = eq2.subs([(x, a + r*(1 - t**2)/(1 + t**2)), (y, b + r*(2*t)/(1+t**2))])
print(new_eq)
sols = solve([new_eq], t, dict=True)
print(sols)
print("Solutions: ")
for sol in sols:
    if sol[t].is_real:
        print(f't: {sol[t]}\n -> {N(sol[t])}')
end = time()
print(f'Time taken: {end - start} seconds')
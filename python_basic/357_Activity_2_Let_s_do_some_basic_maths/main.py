'''
    Geometry (Complex and Polar)
    Author: Saksham Rathi
'''
import math

# import the classes
from complex import Complex
from polar import Polar

def modulus(c:Complex):
    '''return modulus of the complex number'''
    modsq= (c.x)*(c.x) + (c.y)*(c.y)
    mod= float(math.sqrt(modsq))
    return mod

def arg(c:Complex):
    '''return arg (angle) of the complex number'''
    angle = math.atan2(c.y,c.x)
    return angle

def abscissa(p:Polar):
    '''return abscissa of the polar point'''
    return (p.r * math.cos(p.t))

def ordinate(p:Polar):
    '''return ordinate of the polar point'''
    return (p.r * math.sin(p.t))

def distance(z1:Complex, z2:Complex):
    '''distance between points'''
    dissq = (z2.y-z1.y)**2 + (z2.x-z1.x)**2
    dis = math.sqrt(dissq)
    return dis

if __name__ == '__main__':

    # you can use this area of code to check all the functions manually
    # one example of using the functions has been shown
    # run this using "python3 main.py"
    a = Complex(1,2)
    b = Complex(2,2)
    z = a + b # uses the overloaded add
    print(z)
    print(modulus(z)) # you can call after you implement
    x = Polar(2,math.pi/3) # uses the overloaded power
    print(x ** 2)

from abc import ABC , abstractmethod
import math
# 1
# class Animal:
#     def eat():
#         return "Animal is eating..."
#     def sleep():
#         return "Animal is sleeping..."
    
# class Bird(Animal):
#     def __init__(self):
#         Animal.sleep()
#     def eat():
#         return "Bird is pecking at its food..."
#     def fly():
#         return "Bird is flying..."
    
# class Fish(Animal):
#     def __init__(self):
#         Animal.sleep()
#     def swim():
#         return "Fish is swimming.."
    
# bird = Bird
# fish = Fish

# print(bird.eat())
# print(bird.fly())
# print(bird.sleep())
# print(fish.swim())
# print(fish.sleep())

#2
class Shape(ABC):
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def perimeter(self):
        print("Perimeter is:", end = " ")

    @abstractmethod
    def area(self):
        print("Area is:", end = " ")

class Circle(Shape):
    def __init__(self, r):
        if r < 0:
            return "Wrong radius"
        self.r = r
        Shape.area
        Shape.__init__
        Shape.perimeter

    def perimeter(self):
        return 2 * math.pi * self.r
    
    
    def area(self):
        return math.pi * (self.r**2)
    
class Rect(Shape):
    def __init__(self, a , b):
        if a < 0 or b < 0:
            return "Wrong length or width"
        self.a = a
        self.b = b
        Shape.area
        Shape.__init__
        Shape.perimeter

    def perimeter(self):
        return 2 * self.a + 2 * self.b
    
    
    def area(self):
        return self.a * self.b
    
class Triangle(Shape):
    def __init__(self, *args):
        self.__ind = None
        self.__ind1 = True
        try :
            a, b, c = args
            self.a = a
            self.b = b
            if a + b > c and a + c > b and c + b > a:
                self.c = c
                self.__ind = True
            else:
                self.angle = c
                self.__ind = False
        except ValueError:
            try:
                a, h = args
                self.a = a
                self.h = h
            except ValueError:
                print( "Please enter 3 sides, one side and height or 2 sides and angle")
                self.__ind1 = False
            
        Shape.area
        Shape.__init__
        Shape.perimeter

    def perimeter(self):
        if self.__ind1 is False:
                return "Please enter 3 sides, one side and height or 2 sides and angle"
        if self.__ind is None:
            return "Can't calculate perimeter with 1 side and height"
        elif self.__ind is True:
            return self.a + self.b + self.c
        elif self.__ind is False:
            return "Can't calculate perimeter with 2 side and angle"
        
    
    
    def area(self):
        if self.__ind1 is False:
                return "Please enter 3 sides, one side and height or 2 sides and angle"
        if self.__ind is None:
            return self.a * self.h/2
        elif self.__ind is True:
            p = self.perimeter()/2
            return (p * (p-self.a) * (p-self.b) * (p-self.c)) ** 0.5
        elif self.__ind is False:
            return 0.5 * self.a * self.b * math.sin(math.radians(self.angle))


c1 = Circle(5)
print(c1.perimeter())
print(c1.area())
r1 = Rect(2, 5)
print(r1.perimeter())
print(r1.area())
tr1 = Triangle(3, 4, 5)
print("Perimeter:", tr1.perimeter()) 
print("Area:", tr1.area())
tr2 = Triangle(4, 5)
print("Perimeter:", tr2.perimeter()) 
print("Area:", tr2.area())
tr2 = Triangle(7, 8, 90)
print("Perimeter:", tr2.perimeter()) 
print("Area:", tr2.area())

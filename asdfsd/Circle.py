
class Circle:
    def __init__(self,radius,pi=3.14):
        self.radius=radius
        self.pi=3.14
    def area(self):
        return self.pi*(self.radius*self.radius)

    def circumference(self):
        return 2*self.pi*self.radius
circle1=Circle(radius=int(input('whats the radius? ')))
print(circle1.area())
print(circle1.circumference())

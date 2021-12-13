from random import randint
import turtle

class Point:
    """Point class - to create a point having x & y coordinate
    
    Attributes:
        x: horizontal x-axis
        y: vertial y-axis
        
    Methods:
        falls_in_rectangle: return true if point exists inside rectangle and if not return false.
    """
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:
    """rectangle class - made of two points i.e point1 & point2
    
    Attributes:
        point1: a point object
        point2: another point object
    
    Methods:
        area: return the area of the rectangle formed by those two points.
    """
    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2
    
    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class GraphicalRectangle(Rectangle):
    """creates a new window - for the rectangle"""
    def draw(self, canvas):

        # move from origin to point1
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        # from point1 start drawing 
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GraphicalPoint(Point):
    """creates a graphival point in window"""
    def draw(self, canvas, size = 10, color= 'red'):
        canvas.penup()
        canvas.goto(self.x, self.y)

        canvas.pendown()
        canvas.dot(size, color)

x = float(input("Enter x: "))
y = float(input("Enter y: "))

pointA = GraphicalPoint(x, y)


rectanglex = GraphicalRectangle(Point(randint(5, 90), randint(5, 90)), Point(randint(50, 200), randint(50, 200)))
# rectanglex = GraphicalRectangle(Point(50, 100), Point(100,200))
print(f"Rectangle point1: {rectanglex.point1.x}, {rectanglex.point1.y}")
print(f"Rectangle point2: {rectanglex.point2.x}, {rectanglex.point2.y}")

guessed_area = float(input("Guess area of rectangle: "))

print("Area of rectangle: ", rectanglex.area())

if not pointA.falls_in_rectangle(rectanglex):
    print(f"Area off by: {rectanglex.area() - guessed_area}")
else:
    print("Point is present inside rectangle")


myturtle = turtle.Turtle()
rectanglex.draw(canvas=myturtle)
pointA.draw(canvas=myturtle)

turtle.done()






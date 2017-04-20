import math

class Point:
    """Point class for representing and manipulating x, y coordinates."""
    def __init__(self, initx, inity):
        """Create a new point at the given coordinates."""
        self.x = initx
        self.y = inity

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        """Finds the distance a point is from the origin (0,0)"""
        return math.sqrt((self.x**2) + (self.y**2))

    def __str__(self):
        return "(x=" + str(self.x) + ",y=" + str(self.y) + ")"

    def halfway(self, target):
        """Finds the coordinates of a point between two given points"""
        mx = (self.x + target.x) / 2
        my = (self.y + target.y)/ 2

        return Point(mx, my)

    def distanceFromPoint(self, otherp):
        """Find the distance between two points"""
        
        xdiff = (otherp.getX() - self.x)
        ydiff = (otherp.getY() - self.y)

        return math.sqrt(xdiff**2 + ydiff**2)

    def reflect_x(self):
        """ Creates a new point by reflecting the original about the x-axis"""
        
        rx = self.getX()
        ry = self.getY() * -1

        return Point(rx, ry)

    def find_centre_radius(self, p2, p3):
        """Finds the centre and radius of a circle when given three points that are on the circumference."""

        a = self.halfway(p2)
        b = p2.halfway(p3)

        centre = Point(a.getX(), b.getY())
        radius = centre.distanceFromPoint(p2)

        return "centre: {}, radius{}".format(centre, radius)

    def slope_from_origin(self):
        """Gives the slope of a line that joins the origin to a point """
        if self.x == 0:
            return "Slope is undefined"
        else:
            return (self.y/ self.x)

    def get_line_to(self, otherp):
        """This method produces the equation of the line connecting two points """
            
        a = (otherp.getY() - self.y)/ (otherp.getX() - self.x)
        b = otherp.getY() - (a*otherp.getX())

        return "y={}x + {}".format(a, b)

    def move(self, dx, dy):
        """ Move a given points coordinates a specified number of units"""
        
        self.x = self.x + dx
        self.y = self.y + dy

    
class Rectangle:
    def __init__(self, initialp, width, height):
        self.initial = initialp
        self.width = width
        self.height = height

    def getWidth(self):

        return self.width

    def getHeight(self):

        return self.height

    def __str__(self):

        return "initial point:"+ str(self.initial) + "\n" + "width:" + str(self.width) + "height:" + str(self.height)

    def area(self):
        return self.width * self.height

    def perimeter(self):

        return 2*(self.width + self.height)

    def transpose(self):

        temp = self.width
        self.width = self.height
        self.height = temp

    def contains(self, otherp):

        """ verifies whether a given point resides within a rectangle; the x and y upperbounds are open"""

        if self.initial.getX() <= otherp.getX() < self.getWidth() and self.initial.getY() <= otherp.getY() < self.getHeight():
            return True
        else:
            return False

    def diagonal(self):

        d = math.sqrt((self.width**2 + self.height**2))

        return d
        


r = Rectangle(Point(6,2), 3, 4)

print("We have a pythagorian triple this time: ", r.diagonal())





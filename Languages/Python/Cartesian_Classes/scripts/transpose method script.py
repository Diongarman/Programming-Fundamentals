

p = Rectangle(Point(10, 10), 10, 5)
r = Rectangle(Point(0,0), 10, 5)

print(p.getWidth())
print(p.getHeight())

print(r.getWidth())
print(r.getHeight())

p.transpose()
r.transpose()

print("P Width: ", p.getWidth())
print("P Height: ", p.getHeight())

print("R Width: ", r.getWidth())
print("R Height: ", r.getHeight())

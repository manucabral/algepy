from algepy import Vector, Plot, Point

a = Vector(x=1, y=2, z=3)
b = Vector(x=0, y=2, z=5)

plot = Plot(name='Cross product', projection='3d', range=[-5, 5])

cross = a.cross(b)

plot.add_vector(vector=a, origin=Point(x=0, y=0, z=0), color='red')
plot.add_vector(vector=b, origin=Point(x=0, y=0, z=0), color='blue')
plot.add_vector(vector=cross, origin=Point(x=0, y=0, z=0), color='green')

plot.show()
from algepy import Vector, Point, Plot

# Definimos el origen de los vectores
p = Point(x=1, y=2, z=3)

# Declaramos los vectores
a = Vector(x=1, y=2, z=3)
b = Vector(x=2, y=3, z=4)

# Creamos el gráfico y especificamos que será 3d
plot = Plot(name='Punto', projection='3d')

# Agregamos los vectores y el origen
plot.add_point(point=p, color='red')

#plot.show()
plot.save(path='testplotpoint.png')
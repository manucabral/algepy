from algepy import Point

# Definimos los dos puntos
R = Point(x=1, y=1, z=4)
S = Point(x=3, y=0, z=2)

# Obtenemos el vector mediante los dos puntos
RS = R + S

print('Distancia: ', RS.magnitude())
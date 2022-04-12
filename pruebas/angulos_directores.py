from algepy import Vector

# Vector de 3 dimensiones
a = Vector(x=2, y=0, z=-2, dimension=3)

# Obtendremos los angulos directores en grados
# Ángulo director respecto al eje x
ax = a.direction_cosine(axis='x', degrees=True)

# Ángulo director respecto al eje y
a.direction_cosine('y', degrees=True)

# Ángulo director respecto al eje z
a.direction_cosine('z', degrees=True)

print('Angulo director x:', ax)
print('Angulo director y:', ay)
print('Angulo director z:', az)
# algepy
Libreria de Python que te permite manipular vectores de hasta 3 dimensiones, te puede ser útil para calcular o verificar los resultados de tus operaciones.

Este proyecto todavía se encuentra en desarrollo y no está completamente desarrollado, puede tener algunos bugs o fallos.

- [Instalación](#instalacion)
- [Vector](#vector)
  - [Operaciones básicas](#vector-operaciones-basicas)
  - [Opuesto](#vector-opuesto)
  - [Módulo o norma](#vector-norma)
  - [Ángulos directores](#vector-directores)
  - [Ángulo entre dos vectores](#vector-angulos)
  - [Producto escalar](#vector-escalar)
  - [Perpendicularidad](#vector-perpendicular)
  - [Proyección de vectores](#vector-proyeccion)
  - [Producto vectorial](#vector-producto-vectorial)
  - [Producto mixto](#vector-producto-mixto)
- [Punto](#punto)
  - [Operaciones básicas](#punto-operaciones-basicas)
  - [Vector a partir de dos puntos](#punto-vector)
- [Contribuciones](#contribucion)

<a name="instalacion"></a>
## Instalación
- El paquete todavía no está subido a PyPI así que para probarlo necesitas clonar el repositorio y probarlo manualmente.
```bash
git clone https://github.com/manucabral/algepy.git
cd algepy
```

<a name="vector"></a>
## Vector
Para definir un vector simplemente necesitas instanciar la clase Vector con sus componentes (x, y, z)

Por defecto tendrá 3 dimensiones pero puedes especificarle la dimensión como en el siguiente ejemplo.
```py
from algepy import Vector
v = Vector(x=1, y=1, z=1)
u = Vector(x=1, y=1, z=1, dimension=2) # ignorará el eje z
```

<a name="vector-operaciones-basicas"></a>
### Operaciones básica
Para sumar y restar solamente tienes que utilizar el operador + y -, las dos operaciones devuelve un vector.
```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=2, z=3)
>>> v = Vector(x=0, y=2, z=5)
>>> u + v
(1,4,8)
>>> u - v
(1,0,-2)
```

<a name="vector-opuesto"></a>
### Opuesto
Para obtener el opuesto de un vector hay que utilizar su método `opposite`, este método devuelve un nuevo vector.
```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=2, z=3)
>>> u.opposite()
(-1,-2,-3)
```

<a name="vector-norma"></a>
### Módulo o norma
Para obtener el módulo o la norma del vector hay que utilizar su método `magnitude`, este método devuelve un número decimal.
```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=2, z=3)
>>> u.magnitude()
3.7416573867739413
```

<a name="vector-directores"></a>
### Ángulos directores
Para obtener los ángulos directores de un vector hay que utilizar el método `direction_cosine`, este método requiere que le especifiques el eje obligatoriamente (x, z,  y).

El método devuelve por defecto en radianes pero lo puedes cambiar a grados mediante el parámetro `degrees`, aplica lo mismo con el parámetro `decimals`.
```py
>>> from algepy import Vector
>>> a = Vector(x=2, y=0, z=-2)
>>> a.direction_cosine(axis='x', degrees=True) # ángulo director respecto al eje x
45.0
>>> a.direction_cosine(axis='y', degrees=True) # ángulo director respecto al eje y
90.0
>>> a.direction_cosine(axis='z', degrees=True) # ángulo director respecto al eje z
135.0
```

<a name="vector-angulos"></a>
### Ángulo entre dos vectores
Para obtener el ángulo que se forma entre dos vectores hay que utilizar el método conmutativo `angle`.

El método devuelve por defecto en radianes pero lo puedes cambiar a grados mediante el parámetro `degrees`, aplica lo mismo con el parámetro `decimals`.
```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=1, z=3)
>>> v = Vector(x=-1, y=0, z=4)
>>> u.angle(v, degrees=True, decimals=3) # resultado en grados con 3 decimales
36.448
>>> u.angle(v) # resultado en radianes
0.6361
```

<a name="vector-escalar"></a>
### Producto escalar
Para obtener el producto escalar entre dos vectores hay que utilizar el operador * (no confundir este operador con el producto vectorial) esta operación devuelve un número escalar.
```py
>>> from algepy import Vector
>>> u = Vector(x=-3, y=5, z=8)
>>> v = Vector(x=1, y=1, z=1)
>>> u * v
10
```

<a name="vector-perpendicular"></a>
### Perpendicularidad
Para saber si un vector es perpendicular a otro hay que utilizar el método `perpendicular`, este método devuelve un valor booleano (True o False)
```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=1, z=3)
>>> v = Vector(x=-1, y=0, z=4)
>>> u.perpendicular(v)
False
```
<a name="vector-proyeccion"></a>
### Proyección de vectores
Para obtener la proyección de un vector en la dirección de otro hay que utilizar el método `projection`, este método devuelve una lista con dos vectores.

`w:` vector principal (u) proyectado en otro vector (v)

`n:` otro vector (v) proyectado en el vector principal (u)

El vector principal es el vector al que le aplicamos el método `projection`.
```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=2, z=1)
>>> v = Vector(x=0, y=1, z=-1)
>>> w, n = u.proyection(v)
>>> w
(0.0,0.4999999999999999,-0.4999999999999999) # vector u proyectado en v
>>> n
(1.0,1.5,1.5) # vector v proyectado en u
```

<a name="vector-producto-vectorial"></a>
### Producto vectorial
Para obtener el producto vectorial entre dos vectores hay que utilizar el método `cross`, este método devuelve el vector resultado del producto vectorial.

Tener en cuenta que el producto vectorial no es conmutativo, ya que si cambiamos el orden de los vectores se conservan la dirección y el módulo del producto vectorial pero se invierte el sentido.
```py
>>> from algepy import Vector
>>> a = Vector(x=1, y=2, z=3)
>>> b = Vector(x=0, y=2, z=5)
>>> v = a.cross(b)
>>> v
(4,-5,2) # producto vectorial
>>> v.perpendicular(a), v.perpendicular(b)
True, True
```

<a name="vector-producto-mixto"></a>
### Producto mixto
Para obtener el producto mixto hay que utilizar el método `triple`, este método devuelve un escalar y no es conmutativo así que hay que tener en cuenta lo siguiente.

Definidos `u`, `v` y `w`
Cuando se utiliza el método en `u`.triple(`v`,`w`) se aplicará primero el producto vectorial entre `v` y `w` para después calcular el producto escalar `u`(`v`x` w`)

```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=2, z=3)
>>> v = Vector(x=0, y=2, z=5)
>>> w = Vector(x=0, y=0, z=2)
>>> u.triple(v, w)
4
>>> u * v.cross(w) # equivalente
```

<a name="punto"></a>
## Punto
Para definir un punto simplemente necesitas instanciar la clase Point con sus componentes (x, y, z).

Por ahora solamente puedes utilizar puntos de 3 dimensiones.
```py
from algepy import Point
>>> R = Point(x=1, y=1, z=4)
>>> S = Point(x=3, y=0, z=2)
```
<a name="punto-operaciones-basicas"></a>
### Operaciones básicas
No hay ejemplos que mostrar, todavía en desarrollo.

<a name="punto-vector"></a>
### Vector a partir de dos puntos
Para obtener un vector a partir de dos puntos simplemente hay que usar el operador +, es obligatorio que se utilicen dos puntos.

El resultado de esa operación nos devolverá un vector.
```py
from algepy import Point
>>> R = Point(x=1, y=1, z=4)
>>> S = Point(x=3, y=0, z=2)
>>> R + S
(2,-1,-2)
```

<a name="contribucion"></a>
## Contribución
Todas las contribuciones, reportes o arreglos de bugs e ideas es bienvenido. Para esto puedes dirigirte al apartado de issues y aportar tu ayuda.

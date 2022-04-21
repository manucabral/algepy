# algepy
<details>
  <summary>English readme version, click to spand.</summary>

## What is Algepy?
Algepy is a Python Package that allows you to manipulate vectors, it can be useful to calculate or verify the results of your operations.

This project is still under development and is not fully developed, it may have some bugs or failures.

- [Installation](#instalacion)
- [Vector](#vector)
  - [Basic operations](#vector-operaciones-basicas)
  - [Opposite](#vector-opuesto)
  - [Magnitude](#vector-norma)
  - [Direction Cosine](#vector-directores)
  - [Angle between two vectors](#vector-angulos)
  - [Dot product](#vector-escalar)
  - [Perpendicular](#vector-perpendicular)
  - [Proyection](#vector-proyeccion)
  - [Cross product](#vector-producto-vectorial)
  - [Triple product](#vector-producto-mixto)
- [Point](#punto)
  - [Basic operations](#punto-operaciones-basicas)
  - [Midpoint](#punto-medio)
  - [Find the vector between two points](#punto-vector)
- [Plot](#grafico)
  - [Vector](#grafico-vectores)
  - [Point](#grafico-puntos)
- [Contributions](#contribucion)

<a name="instalacion"></a>
## Instalación
> Using [Python Package Index (PyPI)](https://pypi.org/project/algepy/)
```bash
pip install algepy
```
> Manually
```bash
git clone https://github.com/manucabral/algepy.git
cd algepy
```

<a name="vector"></a>
## Vector
To create a vector you simply need to instantiate the Vector class with its components (x, y, z)

By default it will have 3 dimensions but you can specify the dimension as in the following example.
```py
from algepy import Vector
v = Vector(x=1, y=1, z=1)
u = Vector(x=1, y=1, z=1, dimension=2)
```

<a name="vector-operaciones-basicas"></a>
### Basic operations
To add and subtract you just have to use the + and - operator, both operations returns a vector.
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
### Opposite
To get the opposite of a vector you have to use its `opposite` method, this method returns a new vector.
```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=2, z=3)
>>> u.opposite()
(-1,-2,-3)
```

<a name="vector-norma"></a>
### Magnitude
To get magnitude of the vector, you have to use `magnitude` method, this method returns a decimal number.
```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=2, z=3)
>>> u.magnitude()
3.7416573867739413
```

<a name="vector-directores"></a>
### Direction Cosine
To get the direction angles of a vector you have to use the `direction_cosine` method, this method requires that you specify the axis (x, z, y).

The method returns radians by default but you can change it to degrees using the `degrees` parameter, the same applies with the `decimals` parameter.
```py
>>> from algepy import Vector
>>> a = Vector(x=2, y=0, z=-2)
>>> a.direction_cosine(axis='x', degrees=True)
45.0
>>> a.direction_cosine(axis='y', degrees=True)
90.0
>>> a.direction_cosine(axis='z', degrees=True)
135.0
```

<a name="vector-angulos"></a>
### Angle between two vectors
To get the angle between two vectors, use the commutative method `angle`.

The method returns radians by default but you can change it to degrees using the `degrees` parameter, the same applies with the `decimals` parameter.
```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=1, z=3)
>>> v = Vector(x=-1, y=0, z=4)
>>> u.angle(v, degrees=True, decimals=3)
36.448
>>> u.angle(v) # resultado en radianes
0.6361
```

<a name="vector-escalar"></a>
### Dot product
To get the dot product between two vectors, use the * operator (do not confuse this operator with the cross product), this operation returns a scalar number.
```py
>>> from algepy import Vector
>>> u = Vector(x=-3, y=5, z=8)
>>> v = Vector(x=1, y=1, z=1)
>>> u * v
10
```

<a name="vector-perpendicular"></a>
### Perpendicular
To know if a vector is perpendicular to another you have to use the `perpendicular` method, this method returns a boolean value (True or False)
```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=1, z=3)
>>> v = Vector(x=-1, y=0, z=4)
>>> u.perpendicular(v)
False
```
<a name="vector-proyeccion"></a>
### Proyection
To get the projection of one vector in the direction of another you have to use the `projection` method, this method returns a list with two vectors.

`w:` main vector (u) projected on another vector (v)

`n:` other vector (v) projected on main vector (u)

The main vector is the vector to which we apply the `projection` method.

```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=2, z=1)
>>> v = Vector(x=0, y=1, z=-1)
>>> w, n = u.proyection(v)
>>> w
(0.0,0.4999999999999999,-0.4999999999999999) # u on v
>>> n
(1.0,1.5,1.5) # v on u
```

<a name="vector-producto-vectorial"></a>
### Cross product
To get the cross product between two vectors, you must use the `cross` method, this returns the vector resulting from the cross product.

Bear in mind that the vector product is not commutative, since if we change the order of the vectors, the direction and the magnitude of the vector product are preserved, but the sense is reversed.
```py
>>> from algepy import Vector
>>> a = Vector(x=1, y=2, z=3)
>>> b = Vector(x=0, y=2, z=5)
>>> v = a.cross(b)
>>> v
(4,-5,2) # cross product
>>> v.perpendicular(a), v.perpendicular(b)
True, True
```

<a name="vector-producto-mixto"></a>
### Triple product
To get the triple product you have to use the `triple` method, this returns a number and isn't commutative.

Defined `u`, `v` and `w`
When using the method on `u`.triple(`v`, `w`) the cross product between `v` and `w` will be applied and then the dot product between `u`(`v`x` w`)
```py
>>> from algepy import Vector
>>> u = Vector(x=1, y=2, z=3)
>>> v = Vector(x=0, y=2, z=5)
>>> w = Vector(x=0, y=0, z=2)
>>> u.triple(v, w)
4
>>> u * v.cross(w) # equivalent
```

<a name="punto"></a>
## Point
To create a point you simply need to instantiate the Point class with its (x,y,z) components.

You can only use 3-dimensional points.
```py
from algepy import Point
>>> R = Point(x=1, y=1, z=4)
>>> S = Point(x=3, y=0, z=2)
```
<a name="punto-operaciones-basicas"></a>
### Basic operations
To add and subtract you just have to use the + and - operator, both operations return a point.

<a name="punto-medio"></a>
### Midpoint
To get the midpoint between two points, use the `midpoint` method, it returns a vector with the components of the midpoint.
```py
from algepy import Point
>>> r = Point(x=1, y=2, z=3)
>>> s = Point(x=3, y=-1, z=2)
>>> r.midpoint(s)
(2.0,0.5,2.5)
```

<a name="punto-vector"></a>
### Find the vector between two points
To get a vector from two points you have to use the `find_vector` method, this returns a vector formed from the two points.

```py
from algepy import Point
>>> r = Point(x=1, y=1, z=4)
>>> s = Point(x=3, y=0, z=2)
>>> r.find_vector(s)
(2,-1,-2)
```

<a name="grafico"></a>
## Plot
Algepy uses pyplot from matplotlib so for this module to work, you need to have this package installed.

For now the plot only supports 3 dimensions, you can try others dimensions but you will have errors.
```py
plot = Plot(name='Example', projection='3d')
plot.show()
```

<a name="grafico-vectores"></a>
### Plot a vector
To add a vector to our plot we need to use the `add_vector` method and also have an origin point for the vector.

Once this is done we can show the graph with the `show` method.
```py
origin = Point(x=0, y=0, z=0)
a = Vector(x=1, y=2, z=3)
plot = Plot(name='Vector', projection='3d')
plot.add_vector(origin=origin, vector=a)
plot.show()
```
<img src="https://github.com/manucabral/algepy/blob/main/assets/testplot.png?raw=true" title="testplot">

<a name="grafico-puntos"></a>
### Plot a point
To add a point to our plot we need to use the `add_point` method.

Once this is done we can show the graph with the `show` method.
```py
p = Point(x=1, y=2, z=3)
plot = Plot(name='Point', projection='3d')
plot.add_point(point=p, color='red')
plot.show()
```
<img src="https://github.com/manucabral/algepy/blob/main/assets/testplotpoint.png?raw=true" title="testplotpoint">

<a name="contribucion"></a>
## Contributions
All contributions, reports or bug fixes and ideas are welcome. You can go to the issues section and provide your help.

</details>

<details>
  <summary>Versión español, click para expander.</summary>

## ¿Qué es algepy?
Algepy es una libreria de python que te permite manipular vectores de hasta 3 dimensiones, te puede ser útil para calcular o verificar los resultados de tus operaciones.

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
  - [Punto medio](#punto-medio)
  - [Vector a partir de dos puntos](#punto-vector)
- [Gráfico](#grafico)
  - [Vector](#grafico-vectores)
  - [Punto](#grafico-puntos)
- [Contribuciones](#contribucion)

<a name="instalacion"></a>
## Instalación
> Utilizando [Python Package Index (PyPI)](https://pypi.org/project/algepy/)
```bash
pip install algepy
```
> Manualmente
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
Para sumar y restar solamente tienes que utilizar el operador + y -, las dos operaciones devuelve un punto.

<a name="punto-medio"></a>
### Punto medio
Para obtener el punto medio entre dos puntos hay que utilizar el método `midpoint`, este devuelve un vector con los componentes del punto medio.
```py
from algepy import Point
>>> r = Point(x=1, y=2, z=3)
>>> s = Point(x=3, y=-1, z=2)
>>> r.midpoint(s)
(2.0,0.5,2.5)
```

<a name="punto-vector"></a>
### Vector a partir de dos puntos
Para obtener un vector a partir de dos puntos hay que utilizar el método `find_vector`, este devuelve un vector formado a partir de los dos puntos.

```py
from algepy import Point
>>> r = Point(x=1, y=1, z=4)
>>> s = Point(x=3, y=0, z=2)
>>> r.find_vector(s)
(2,-1,-2)
```
<a name="grafico"></a>
## Gráfico
Algepy utiliza pyplot de matplotlib así que para que este módulo te funcione necesitas tener instalado este paquete.

Por ahora el gráfico solamente soporta 3 dimensiones, puedes intentar con otras pero corres el riesgo de obtener varios errores.
```py
plot = Plot(name='Ejemplo', projection='3d')
plot.show()
```
<a name="grafico-vectores"></a>
### Gráfico de un vector
Para agregar un vector a nuestro gráfico necesitamos utilizar el método `add_vector` y además tener un punto de origen para el vector.

Una vez realizado esto podemos mostrar el gráfico con el método `show`

```py
origen = Point(x=0, y=0, z=0)
a = Vector(x=1, y=2, z=3)
plot = Plot(name='Vector', projection='3d')
plot.add_vector(origin=origen, vector=a)
plot.show()
```
<img src="https://github.com/manucabral/algepy/blob/main/assets/testplot.png?raw=true" title="testplot">

<a name="grafico-puntos"></a>
### Gráfico de un punto
Para agregar un punto a nuestro gráfico necesitamos utilizar el método `add_point`

Una vez realizado esto podemos mostrar el gráfico con el método `show`
```py
p = Point(x=1, y=2, z=3)
plot = Plot(name='Punto', projection='3d')
plot.add_point(point=p, color='red')
plot.show()
```
<img src="https://github.com/manucabral/algepy/blob/main/assets/testplotpoint.png?raw=true" title="testplotpoint">

<a name="contribucion"></a>
## Contribución
Todas las contribuciones, reportes o arreglos de bugs e ideas es bienvenido. Para esto puedes dirigirte al apartado de issues y aportar tu ayuda.
</details>

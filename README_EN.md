# algepy
A Python Package that allows you to manipulate vectors, it can be useful to calculate or verify the results of your operations.

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
- [Point](#punto)
  - [Basic operations](#punto-operaciones-basicas)
  - [Find the vector between two points](#punto-vector)
- [Contributions](#contribucion)

<a name="instalacion"></a>
## Installation
- The package is not yet uploaded to PyPI so to test it you need to clone the repository and test it manually.
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
No examples, still in development.

<a name="punto-vector"></a>
### Find the vector between two points
To get a vector from two points, simply use the + operator, it is required that two points be used.

The result of that operation will returns a vector.
```py
from algepy import Point
>>> R = Point(x=1, y=1, z=4)
>>> S = Point(x=3, y=0, z=2)
>>> R + S
(2,-1,-2)
```

<a name="contribucion"></a>
## Contributions
All contributions, reports or bug fixes and ideas are welcome. You can go to the issues section and provide your help.

import math

class Vector:
    def __init__(self, **kwargs) -> None:
        if kwargs is None:
            return self.null()
        self.axes = ['x', 'y', 'z']
        self.dimension = kwargs.get('dimension', 3)
        self.check_axes(kwargs)

    def check_axes(self, kwargs: dict) -> None:
        for axis in self.axes:
            if axis in kwargs:
                setattr(self, axis, kwargs[axis])
            else:
                setattr(self, axis, 0)

    def null(self) -> None:
        self.x = self.y = self.z = 0
        self.dimension = 3
    
    def magnitude(self) -> float:
        _sum = 0
        for axis in self.axes[0: self.dimension]:
            _sum += getattr(self, axis) ** 2
        return math.sqrt(_sum)

    def opposite(self) -> 'Vector':
        return Vector(x=-self.x, y=-self.y, z=-self.z, dimension=self.dimension)

    def isnull(self) -> bool:
        return self.magnitude() >= 0 and self.magnitude() == 0

    def direction_cosine(self, axis: str, degrees: bool = False, decimals: int = 2) -> 'Radians or Degrees':
        if axis not in self.axes:
            raise ValueError('Axis must be x, y or z')
        value = getattr(self, axis)
        radians = math.acos(value/self.magnitude())
        return math.degrees(radians).__round__(decimals) if degrees else radians
    
    def perpendicular(self, other: 'Vector') -> bool:
        if self.dimension != other.dimension:
            raise ValueError('Dimensions must be equal')
        if other.isnull() or self.isnull():
            raise ValueError('Cannot calculate perpendicular with null vector')
        return self * other == 0

    def angle(self, other: 'Vector', degrees: bool = False, decimals: int = 2) -> 'Radians or Degrees':
        if self.dimension != other.dimension:
            raise ValueError('Dimensions must be equal')
        if other.isnull() or self.isnull():
            raise ValueError('Cannot calculate angle with null vector')
        radians = math.acos(self * other / (self.magnitude() * other.magnitude()))
        return math.degrees(radians).__round__(decimals) if degrees else radians

    def projection(self, other: 'Vector') -> ['self->other', 'other->self']:
        if self.dimension != other.dimension:
            raise ValueError('Dimensions must be equal')
        if other.isnull() or self.isnull():
            raise ValueError('Cannot calculate proyection with null vector')
        product_scalar = self * other
        other_magnitude = other.magnitude() ** 2
        projection_magnitude = product_scalar / other_magnitude
        projection = other * projection_magnitude
        return projection, self - projection

    def __eq__(self, other: 'Vector') -> bool:
        if self.dimension != other.dimension:
            raise ValueError('Dimensions must be equal')
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self) -> str:
        values = '('
        for axis in self.axes[0: self.dimension]:
            values += f'{getattr(self, axis)},'
        return values[:-1] + ')'
    
    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y}, {self.z})'

    def __add__(self, other: 'Vector') -> 'Vector':
        if self.dimension != other.dimension:
            raise ValueError('Dimensions must be equal')
        return Vector(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z, dimension=self.dimension)

    def __sub__(self, other: 'Vector') -> 'Vector':
        if self.dimension != other.dimension:
            raise ValueError('Dimensions must be equal')
        return Vector(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z, dimension=self.dimension)

    def __mul__(self, other: 'Vector' or float) -> 'Vector':
        if isinstance(other, Vector):
            if self.dimension != other.dimension:
                raise ValueError('Dimensions must be equal')
            if other.isnull() or self.isnull():
                return 0
            return self.x * other.x + self.y * other.y + self.z * other.z
        return Vector(x=self.x * other, y=self.y * other, z=self.z * other, dimension=self.dimension)
    
    def __truediv__(self, scalar: float) -> 'Vector':
        return Vector(x=self.x / scalar, y=self.y / scalar, z=self.z / scalar, dimension=self.dimension)

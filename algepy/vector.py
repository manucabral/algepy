import math

class Vector:
    def __init__(self, **kwargs) -> None:
        """
            Initialize a vector with x, y and z coordinates.
            
            Params:
                x: x coordinate
                y: y coordinate
                z: z coordinate
                dimension: dimension of the vector. Default is 3
            
            Returns:
                A vector class instance.
            
            Raises:
                None
        """
        if kwargs is None:
            return self.null()
        self.axes = ['x', 'y', 'z']
        self.dimension = kwargs.get('dimension', 3)
        self.check_axes(kwargs)

    def check_axes(self, kwargs: dict) -> None:
        """
            Check if the axes are valid.
            
            Params:
                kwargs: dictionary with the axes.

            Returns:
                None
        """
        for axis in self.axes:
            if axis in kwargs:
                setattr(self, axis, kwargs[axis])
            else:
                setattr(self, axis, 0)

    def null(self) -> None:
        """
            Set all the coordinates to 0.
            
            Params:
                None
            
            Returns:
                None
        """
        self.x = self.y = self.z = 0
        self.dimension = 3
    
    def magnitude(self) -> float:
        """
            Calculate the magnitude of the vector.
                
            Params:
                None
                
            Returns:
                Magnitude of the vector as a float.
        """
        _sum = 0
        for axis in self.axes[0: self.dimension]:
            _sum += getattr(self, axis) ** 2
        return math.sqrt(_sum) if _sum > 0 else 0

    def opposite(self) -> 'Vector':
        """
            Return the opposite vector.

            Params:
                None
            
            Returns:
                A vector with the opposite coordinates of the original vector.
        """
        return Vector(x=-self.x, y=-self.y, z=-self.z, dimension=self.dimension)

    def isnull(self) -> bool:
        """
            Check if the vector is null.
                
            Params:
                None
                
            Returns:
                True if the vector is null, False otherwise.
        """
        return self.magnitude() >= 0 and self.magnitude() == 0

    def direction_cosine(self, axis: str, degrees: bool = False, decimals: int = 2) -> 'Radians or Degrees':
        """
            Calculate the direction cosine of the vector.

            Params:
                axis: axis to calculate the direction cosine.
                degrees: if True, return the result in degrees.
                decimals: number of decimals to round the result.
            
            Returns:
                Direction cosine of the vector as a radian or degree.
        """
        if axis not in self.axes:
            raise ValueError('Axis must be x, y or z')
        value = getattr(self, axis)
        radians = math.acos(value/self.magnitude())
        return math.degrees(radians).__round__(decimals) if degrees else radians
    
    def perpendicular(self, other: 'Vector') -> bool:
        """
            Check if the vector is perpendicular to the other vector.

            Params:
                other: other vector to check.
            
            Returns:
                True if the vector is perpendicular to the other vector, False otherwise.
        """ 
        if self.dimension != other.dimension:
            raise ValueError('Dimensions must be equal')
        if other.isnull() or self.isnull():
            raise ValueError('Cannot calculate perpendicular with null vector')
        return self * other == 0

    def angle(self, other: 'Vector', degrees: bool = False, decimals: int = 2) -> 'Radians or Degrees':
        """
            Calculate the angle between the vectors.
            
            Params:
                other: other vector to calculate the angle.
                degrees: if True, return the result in degrees.
                decimals: number of decimals to round the result.
            
            Returns:
                Angle between the vectors as a radian or degree.
        """
        if self.dimension != other.dimension:
            raise ValueError('Dimensions must be equal')
        if other.isnull() or self.isnull():
            raise ValueError('Cannot calculate angle with null vector')
        radians = math.acos(self * other / (self.magnitude() * other.magnitude()))
        return math.degrees(radians).__round__(decimals) if degrees else radians

    def projection(self, other: 'Vector') -> ['self->other', 'other->self']:
        """
            Calculate the projection of the vector on the other vector.

            Params:
                other: other vector to calculate the projection.
            
            Returns:
                A tuple with the projection:
                    - self->other: projection of the vector on the other vector.
                    - other->self: projection of the other vector on the vector.
        """
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
        """
            Check if the vectors are equal.

            Params:
                other: other vector to check.
            
            Returns:
                True if the vectors are equal, False otherwise.
        """
        if self.dimension != other.dimension:
            raise ValueError('Dimensions must be equal')
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self) -> str:
        """
            Return the vector as a string.

            Params:
                None
            
            Returns:
                Vector as a string in the form of (x, y, z).
        """
        values = '('
        for axis in self.axes[0: self.dimension]:
            values += f'{getattr(self, axis)},'
        return values[:-1] + ')'
    
    def __repr__(self) -> str:
        """
            Return the vector as a string.

            Params:
                None
            
            Returns:
                Vector as a string in the form of Vector(x, y, z).
        """
        return f'Vector({self.x}, {self.y}, {self.z})'

    def __add__(self, other: 'Vector') -> 'Vector':
        """
            Add two vectors.

            Params:
                other: other vector to add.
            
            Returns:
                A vector with the sum of the two vectors.
        """
        if self.dimension != other.dimension:
            raise ValueError('Dimensions must be equal')
        return Vector(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z, dimension=self.dimension)

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
            Subtract two vectors.

            Params:
                other: other vector to subtract.

            Returns:
                A vector with the difference of the two vectors.
        """
        if self.dimension != other.dimension:
            raise ValueError('Dimensions must be equal')
        return Vector(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z, dimension=self.dimension)

    def __mul__(self, other: 'Vector' or float) -> 'Vector':
        """
            Multiply a vector by a scalar or another vector.

            Params:
                other: scalar or vector to multiply.

            Returns:
                A vector with the product of the vector and the scalar or a vector.
        """
        if isinstance(other, Vector):
            if self.dimension != other.dimension:
                raise ValueError('Dimensions must be equal')
            if other.isnull() or self.isnull():
                return 0
            return self.x * other.x + self.y * other.y + self.z * other.z
        return Vector(x=self.x * other, y=self.y * other, z=self.z * other, dimension=self.dimension)
    
    def __truediv__(self, scalar: float) -> 'Vector':
        """
            Divide a vector by a scalar.

            Params:
                scalar: scalar to divide.

            Returns:
                A vector with the division of the vector by the scalar.
        """
        return Vector(x=self.x / scalar, y=self.y / scalar, z=self.z / scalar, dimension=self.dimension)

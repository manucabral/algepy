from .vector import Vector

class Point:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'
    
    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y}, {self.z})'
    
    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __add__(self, other: 'Point') -> Vector:
        return Vector(x=other.x - self.x, y=other.y - self.y, z=other.z - self.z)
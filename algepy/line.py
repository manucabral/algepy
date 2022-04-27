from .point import Point
from .vector import Vector


class Line:
    """
        Line definition
    """

    def __init__(self, **kwargs):
        """
            Initialize a Line object.

            Params:
                point (Point): point on the line
                vector (Vector): a direction vector of the line

            Returns:
                A line class instance.

            Raises:
                ValueError if no arguments given
        """
        if not kwargs:
            raise ValueError('No arguments given.')
        self.point = kwargs.get('point', Point(x=0, y=0, z=0))
        self.vector = kwargs.get('vector', Vector(x=0, y=0, z=0))

    def __repr__(self):
        return f'Line(point={self.point}, vector={self.vector})'

    def __str__(self):
        return f'L: λ{self.vector} + {self.point}'

from algepy import Vector

u = Vector(x=1, y=1, z=3)
v = Vector(x=-1, y=0, z=4)

angle = u.angle(v, degrees=True)
print(f'{u} y {v} son perpendiculares: {u.perpendicular(v)}')
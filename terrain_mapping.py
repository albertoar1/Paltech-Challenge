import sys

class Point:
    def __init__(self, x, y, z) -> None:
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __str__(self) -> str:
        return (f"Intersection at {self.x},{self.y},{self.z}")
    
    def vector(self, point: object):
        return Vector(self.x-point.x, self.y-point.y, self.z-point.z)
    
class Vector:
    def __init__(self, vx, vy, vz) -> None:
        self.x = float(vx)
        self.y = float(vy)
        self.z = float(vz)

    def __str__(self) -> str:
        return f"Direction: (x: {self.x}, y: {self.y}, z: {self.z}"

    def __eq__(self, value: object) -> bool:
        return self.x/value.x == self.y/value.y == self.z/value.z

    def direction(self, other: object, L: int, R: int):
        if self.x + self.y < other.x + other.y:
            return L+1,R
        else:
            return L,R-1
    
def to_point(line:str):
    line = line.strip()
    line = line.split(' ')
    return Point(line[0],line[1],line[2])

_, x, y, z, vx, vy, vz = sys.argv

vpoint = Point(x,y,z)

vector = Vector(vx,vy,vz)

with open('dem.txt','r') as file:
    dem = file.readlines()

dem = map(to_point, dem)
# Sort by x and y
dem = list(dem)
dem.sort(key= lambda point: point.x+point.y)


L = 0
R = len(dem) - 1
intersect = False

# Binary search for intersection
while L <= R:
    point = (L+R)//2
    # print(dem[point])
    d_vector = dem[point].vector(vpoint)
    # print(d_vector)

    if d_vector!=vector:
        L,R = vector.direction(d_vector,L,R)

    else:
        print(dem[point])
        intersect = True
        break

if not intersect:
    print("There is no intersection")

# for d in dem:
#     if d.vector(vpoint)==vector:
#         print(dem)
#         break
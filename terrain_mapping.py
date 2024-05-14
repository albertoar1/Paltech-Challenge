import sys

class Point:
    # This class defines a point
    # It is used to create vectors and print the intersection point
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self) -> str:
        return (f"Intersection at {self.x},{self.y},{self.z}")
    
    def vector(self, point: object):
        return Vector(self.x-point.x, self.y-point.y, self.z-point.z)
    
class Vector:
    # This class defines a vector
    # It is used to compare vectors and move the binary search
    def __init__(self, vx: float, vy: float, vz: float) -> None:
        self.x = vx
        self.y = vy
        self.z = vz

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
    # Function to map dem.txt lines to Points
    line = line.strip()
    line = line.split(' ')
    return Point(line[0],line[1],line[2])

_, x, y, z, vx, vy, vz = sys.argv
# We check the type of the arguments
# We do not check for 
try:
    x = float(x)
    y = float(y)
    z = float(z)

except ValueError:
    print("Origin point contains non numeric values")
    sys.exit(1)

try:
    vx = float(vx)
    vy = float(vy)
    vz = float(vz)

except ValueError:
    print("Direction vector contains non numeric values")
    sys.exit(1)

vpoint = Point(x,y,z)

vector = Vector(vx,vy,vz)

with open('dem.txt','r') as file:
    dem = file.readlines()

dem = map(to_point, dem)
# Sort by x and y
dem = list(dem)
dem.sort(key= lambda point: point.x+point.y)

# Use of binary search to find the point
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
        # Print intersection point and exit program
        print(dem[point])
        intersect = True
        sys.exit(0)
        break

if not intersect:
    print("There is no intersection")

# for d in dem:
#     if d.vector(vpoint)==vector:
#         print(dem)
#         break
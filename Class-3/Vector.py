class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # on class request
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    # HW - 1 how to divide two vectors

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
v4 = v1 * v2

print(v3)
print(v4)
# Output: (6, 8) -> v3
# Output: (8, 15) -> v4

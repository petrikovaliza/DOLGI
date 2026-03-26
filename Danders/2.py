class Vector:
    def __init__(self, *components):
        self.components = list(components)
    
    def __str__(self):
        return f"Vector({', '.join(str(c) for c in self.components)})"
    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have same length")
        return Vector(*(self.components[i] + other.components[i] for i in range(len(self.components))))
    
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have same length")
        return Vector(*(self.components[i] - other.components[i] for i in range(len(self.components))))
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(c * other for c in self.components))
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have same length")
            return sum(self.components[i] * other.components[i] for i in range(len(self.components)))
        raise TypeError("Unsupported operand type")
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __pow__(self, power):
        if isinstance(power, (int, float)):
            return sum(c ** power for c in self.components)
        raise TypeError("Power must be a number")


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(3 * v1)
print(v1 * v2)
print(v1 ** 2)
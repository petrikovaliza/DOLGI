class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
    
    def __str__(self):
        result = []
        for row in self.data:
            result.append("[" + " ".join(f"{x:4}" for x in row) + "]")
        return "\n".join(result)
    
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same dimensions")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)
    
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Cannot multiply: columns of first must match rows of second")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)
            result.append(row)
        return Matrix(result)
    
    def __matmul__(self, other):
        return self.__mul__(other)
    
    def __pow__(self, power):
        if power == 0:
            result = [[1 if i == j else 0 for j in range(self.rows)] for i in range(self.rows)]
            return Matrix(result)
        if power == 1:
            return self
        result = self
        for _ in range(power - 1):
            result = result * self
        return result


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print("Matrix 1:")
print(m1)
print("\nMatrix 2:")
print(m2)
print("\nMatrix 1 + Matrix 2:")
print(m1 + m2)
print("\nMatrix 1 * Matrix 2:")
print(m1 * m2)
print("\nMatrix 1 @ Matrix 2 (same as multiply):")
print(m1 @ m2)
print("\nMatrix 1 ^ 2:")
print(m1 ** 2)
print("\nMatrix 1 ^ 3:")
print(m1 ** 3)
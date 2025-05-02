class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __add__(self, other):
        return Rectangle(self.length + other.length, self.breadth + other.breadth)

    def __eq__(self, other):
        return self.length == other.length and self.breadth == other.breadth

    def __lt__(self, other):
        return (self.length * self.breadth) < (other.length * other.breadth)

    def __le__(self, other):
        return (self.length * self.breadth) <= (other.length * other.breadth)

    def __gt__(self, other):
        return (self.length * self.breadth) > (other.length * other.breadth)

    def __ge__(self, other):
        return (self.length * self.breadth) >= (other.length * other.breadth)

    def __str__(self):
        return f"Length is {self.length} and Breadth is {self.breadth}"

# Example
r1 = Rectangle(10, 5)
r2 = Rectangle(20, 6)
r3 = r1 + r2
print(r3)
print("r1 == r2:", r1 == r2)
print("r1 < r2:", r1 < r2)

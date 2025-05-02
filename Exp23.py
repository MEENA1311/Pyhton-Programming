class Student:
    def __init__(self, regno, name, cgpa):
        self.regno = regno
        self.name = name
        self.cgpa = cgpa

    def __str__(self):
        return f"RegNo: {self.regno}, Name: {self.name}, CGPA: {self.cgpa}"

# Example
s1 = Student("URK24CS1001", "John", 9.1)
s2 = Student("URK24CS1002", "Arun", 8.7)
print(s1)
print(s2)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        total = sum(self.marks)
        average = total/len(self.marks)
        return (self.name, average)


marks = []
n = int(input())
name = input("")
for i in range(n):
    m = int(input())
    marks.append(m)

s1 = Student(name, marks)
i, j = s1.average()
print(
    f"the name of the student is {i} and he got {j} percent in 10th exam")

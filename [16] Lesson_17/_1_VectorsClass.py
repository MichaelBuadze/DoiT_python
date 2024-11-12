class Vector:
    def __init__(self, x, y):
        # ინიციალიზაცია: ვექტორის x და y მნიშვნელობები
        self.x = x
        self.y = y

    def __add__(self, other):
        # ვექტორების დამატება
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        # ვექტორის სტრიქონულ ფორმატში დაბრუნება
        return f"({self.x}, {self.y})"

# გამოყენება დავალებაში მოცემული მაგალითის მიხედვით
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: (5, 7)

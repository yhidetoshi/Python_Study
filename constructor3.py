class Example():

    def __init__(self, a, b, c):
        self.num1 = a
        self.num2 = b
        self.num3 = c

    def print_total(self):
        total = self.num1 + self.num2 + self.num3
        print(total)

myinstance = Example(1, 2, 3)
myinstance.print_total()

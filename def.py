# ex1
def hello():
    print('Hello!')

hello()

# ex2
def add(a, b):
    c = a+b
    print(c)
    return c
print(add(1,2))

# ex3
def score(a):
    if a > 60:
        return True
    else:
        return False

print(score(70))
print(score(50))

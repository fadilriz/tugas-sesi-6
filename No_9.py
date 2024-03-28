a = 1
b = 1
c = 0

for i in range(10):
    for j in range(a):
        print("*", end="")
    print()
    c = a + b
    a = b
    b = c
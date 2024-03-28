n = 5
for i in range(n, 0, -1):
    for j in range(n):
        if j >= i - 1:
            print(j + 1, end=" ")
        else:
            print("+", end=" ")
    print()

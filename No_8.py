for i in range(5):
    for j in range(5 - i):
        if (i + j) % 2 == 0:
            print("S", end=" ")
        else :
            print("O", end=" ")
    print()
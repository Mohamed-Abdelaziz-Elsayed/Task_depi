height = 6
width = 6 
for i in range(height):
    for j in range(width):
        if j == 0 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")  
    for j in range(width):
        if j == width-1 or j == width-1-i:
            print("*", end="")
        else:
            print(" ", end="")

    print()
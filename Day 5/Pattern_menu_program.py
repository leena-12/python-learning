# The Pattern menu program

print("Choose a pattern:")
print("1. Right triangle")
print("2. Inverted triangle")
print("3. Pyramid")
print("4. Number triangle")

choice = int(input("Enter choice (1-4): "))
rows = int(input("Enter number of rows: "))

if choice == 1:
    for i in range(1, rows + 1):
        for j in range(1, i+1):
         print("*",end =" ")
        print()

elif choice == 2:

    for i in range(rows,0,-1):
        for j in range(1, i+1):
         print("*",end =" ")
        print()


elif choice == 3:
    for i in range(rows):
        print(" " * (rows - i - 1), end=" ")
        print("*" * (2 * i + 1))

elif choice == 4:
    for i in range(1, rows + 1):
        for j in range(i, rows):
         print(" ", end=" ")
        
        for j in range(1, i+1):
         print(j,end =" ")
        print()

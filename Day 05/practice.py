# print the following output.
"""
*
* *
* * *
* * * *
* * * * *
"""

n = int(input("Enter the number :"))
for i in range(1,n):
    for j in range (1, i+1):
        print("*", end = " ")
    print()




# print the following output.
"""
* * * * *
* * * *
* * *
* * 
* 
"""
n = int(input("Enter the number :"))
for i in range(n,0,-1):
    for j in range (1, i+1):
        print("*", end = " ")
    print()



# print the following output.
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""


n = 6
for i in range(1,6):
    for j in range(1 ,i + 1):
        print(j, end =" ")
    print()




#print the pyramid.

n = 6
for i in range (n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range (i):
        print("*", end = " ")
    for j in range(i+1):
        print("*",end=" ")
    print()


#print the reverse pyramid.


n = 6
for i in range (n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range (i,n-1):
        print("*", end = " ")
    for j in range(i,n):
        print("*",end=" ")
    print()

 #print the diamond pattern.

n = 6
for i in range (n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range (i):
        print("*", end = " ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range (n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range (i,n-1):
        print("*", end = " ")
    for j in range(i,n):
        print("*",end=" ")
    print()

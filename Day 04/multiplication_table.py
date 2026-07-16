# print the multiplication table of number n



n = int(input("Enter the number:"))
i =1
while i<= 10 :
    print(n*i)
    i+= 1


# print the elements of the following list using loop :
#[1,4,9,16,25,36,49,64,81,100]

num = [1,4,9,16,25,36,49,64,81,100]

i = 0
while i < len(num):
    print(num[i])
    i +=1



# search for a number x in this tuple using this loop
#[1,4,9,16,25,36,49,64,81,100]


num = (1,4,9,16,25,36,49,64,81,100)
x = 49
i = 0
while i < len(num):
    if(num[i] == x):
       print("FOUND THE NUMBER x at index:",i)
    i +=1

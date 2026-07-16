# print the elements of the following list using for loop :
#[1,4,9,16,25,36,49,64,81,100]

num = [1,4,9,16,25,36,49,64,81,100]

for el in num :
    print(el)



# search for a number x in this tuple using this loop
#[1,4,9,16,25,36,49,64,81,100]


num = (1,4,9,16,25,36,49,64,81,100)
x = 49
i = 0

for el in num :
    if(el == x):
       print("FOUND THE NUMBER x at index:",i)
    i +=1
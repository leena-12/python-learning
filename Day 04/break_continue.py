i = 0
while i<=10 :
    print(i)
    i +=1  
    if(i == 6):
        break
print("End of loop!")



i = 1
while i<= 10 :
    if(i%2 == 0):
       i += 1
       continue #skip
    print(i)
    i +=1
print("End of loop!")
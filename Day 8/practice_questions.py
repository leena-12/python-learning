#Create a list of five favourite programming languages.
#Print:
#First language
#Last language
#Total number of languages

languages = ["python", "C++", "java", "CSS", "HTML"]
print(" The first language entered is:", end =" ") 
print (languages[0])
print(" The last language entered is:", end =" ") 
print (languages[-1])
print(" The length of list is:", end =" ") 
print(len(languages))



#Take five numbers from the user.
#Store them in a list.
#Print the complete list.

values = input("Enter five numbers separated by spaces: ").split()
numbers = [int(v) for v in values]
print(numbers)


#Find:
#Largest number
#Smallest number
#Without using max() or min().

numbers = [12,64,75,98,97,4]
numbers.sort()
print(numbers)
print(" The largest number in the list is:", end =" ") 
print(numbers[-1])
print(" The smallest number in the list is:", end =" ") 
print(numbers[0])


#Count how many even numbers exist in a list.


def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 ==0 :
            count +=1
    return count
if __name__ == "__main__":

  numbers = [int(x) for x in input("enter the numbers separated by spaces:").split()]
result = count_even(numbers)

print(f"the even numbers present in the entered list are:{result}")



#Create a list.
#Remove duplicate values

def remove_duplicates(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


if __name__ == "__main__":
    numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    result = remove_duplicates(numbers)
    print(f"List after removing duplicates: {result}")


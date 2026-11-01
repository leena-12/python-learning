# Student Grade Calculator

marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("The student has A grade.")
elif marks >= 80 and marks < 90:
    print("The student has B grade.")
elif marks >= 70 and marks < 80:
    print("The student has C grade.")
elif marks >= 0 and marks < 70:
    print("The student has D grade.")
else:
    print("Invalid marks. Please enter marks between 0 and 100.")
#  how to check if a string is valid keyword
import keyword

str1 = "Ali"
if keyword.iskeyword(str1):
    print("Ali is a keyword in python")
else:
    print("Ali is not a keyword in python")

str5 = "break"
if keyword.iskeyword(str5):
    print("break is a keyword in python")
else:
    print("break is not a keyword in python")

#Assigning a value to a variable
a = 9
moon = 4
_class = 5
print(a, moon, _class)

#Assigning values to multiple variable
x, y, z = "mamoona", "shamraiz", "4th"
print(x,y,z) 

#How to print without newlinw in python
#by default
print("Maaz is angrybird")
print("He is also cute boy")
#without newline
print("I am a cute girl", end = " ")
print("not aurat")

#sys module
import sys

sys.stdout.write("Ayesha is a good girl ")
sys.stdout.write("She is also hardworking.")

#Decision making 
#if stayement
cgpa = 3
if cgpa > 2:
    print("You can enroll in next semester.")

#if else statement
marks = 35
if marks > 33:
    print("pass")
else:
    print("fail.")

#if elif else statement
cgpa = 2
if cgpa > 3:
    print("Exellent")
elif cgpa == 3:
    print("V good")
elif cgpa > 2:
    print("Good")
else:
    print("poor")

#Nested if statement
hieght = 'true'
weight = 'true'
if hieght == 'true':
    print("You are tall")
    if weight == 'true':
        print("You are fat.")
    else:
        print("You are a skiny person.")
else:
    print("You are tall nor fat.")

#Basic calculator program 
num1 = float(input("Enter  first number : "))
num2 = float(input("Enter second number : "))
print("Please select operation -\n","1. Add\n","2. Subtract\n","3. Multiply\n","4. Divide\n","5. Modulus\n")
choice = int(input("Choose an operation 1, 2, 3, 4, 5: "))
if choice== 1:
    print("The result is: ",num1 + num2)
elif choice == 2:
    print("The result is: ",num1 - num2)
elif choice == 3:
    print("The result is: ",num1 * num2)
elif choice == 4:
    print("The result is: ",num1 / num2)
elif choice == 5:
    print("The result is: ",num1 % num2)
else:
    print("Invalid choice")


#python language advantages and applications




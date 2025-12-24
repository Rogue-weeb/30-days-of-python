print("Hello world, watch me become fucking amazing")
print()
print()
# Day 1 - 30 days of python
name = input("What is your name: ")
print('Hello', name)
try:
    age = int(input("How old are you: "))  # User enters "twenty"
except ValueError:
    print("Please enter a valid number")   # Error message shown
    age = 0                                 # age is now 0 (default value)

# Later in your code:
if age > 18:  # This won't crash because age exists (it's 0)
    print("You are an adult")
else:
    print("You are a minor")  # This will print since age = 0
print()

#i am now writing on the same line with end=''
print('Hello again world' , end='')
print('this is not a new line')
print()
print()

#Checking mathematical Calculations
print(3 + 2) #addition
print(3 - 2) #subtraction
print(3 * 2) #multiplication
print(6 / 2) #division
print(6 % 2) #modulus
print(6 // 2) #floor division
print(6 ** 2) #exponentiation   

print("Hello world, watch me become fucking amazing")
print()
print()
# Day 1 - 30 days of python
name = input("What is your name: ")
print('Hello', name)
while True:
    try:
        age = int(input("How old are you: "))
        break  # valid number, exit the loop
    except ValueError:
        print("Enter a fucking number")   # Error message shown, ask again

# Later in your code:
if age > 18:  # This won't crash because age exists (it's 0)
    print("You are an adult, get in")
else:
    print("get out of here you minor")  # This will print since age = 0
print()

#i am now writing on the same line with end=''
print('Hello again world', end='')
print(' this is not a new line')
print()
print()

#Checking mathematical Calculations




print(3 + 2) #addition
print(3 - 2) #subtraction
print(3 * 2) #multiplication
print(int(6 / 2)) #division
print(7 % 2) #modulus
print(6 // 2) #floor division
print(6 ** 2) #exponentiation   
print((3 + 2) * 4)      # combining operations
print(7 / 3)            # normal division (float)
print(7 // 3)           # floor division (integer result)
print(7 % 3)            # remainder
print(abs(-5))          # absolute value
print(round(3.14159, 2)) # rounding to 2 decimal places
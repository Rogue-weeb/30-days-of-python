print("Hello, world")

name = input("What is your name: ").strip()
print(f"Hello, {name}")

correct_password = "1020"

for _ in range(3): 
    password = input("please enter your password:")
    if password == correct_password:
        print("correct")
        break
    else: 
        print('incorrect') 
else:
    print("Too many tries")        


 
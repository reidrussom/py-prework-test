# Social media age verification program

name = input('Enter your name: ')
age = int(input('Enter your age: '))
if age >=16:
    print("Hello " + name + "! You are "+ str(age) + ", so you may create an account.")
else:
    print("Hello " + name + "! You are "+ str(age) + " so you are not eligible to create an account.")

# Example Run 1
# Input: Reid, 30
# Output: Hello Reid! You are 30, so you may create an account.
# Example Run 2
# Input: Reid, 12
# Output: Hello Reid! You are 12 so you are not eligible to create an account.

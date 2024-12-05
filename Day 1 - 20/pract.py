
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 18:
    print(f"Hello {name}, you are a minor.")
else:
    print(f"Hello {name}, you are an adult.")

print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

def check_even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

num = int(input("\nEnter a number to check if it's even or odd: "))
result = check_even_or_odd(num)
print(f"The number {num} is {result}.")

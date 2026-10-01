while True:
    note = input("Enter a note: ")
    if note != "done":
        with open("notes.txt", "a") as file:
            file.write(f"{note}\n")
    else:
        break
with open("notes.txt", "r") as file:
    content = file.read()
print(content)

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Choose an operator(From +, -, *, /): ")
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1/num2)
    else:
        print("Please enter a valid operation.")
except ValueError:
    print("Plese enter a valid number.")
except ZeroDivisionError:
    print("Zero can not be a denominator.")

for i in range(5):
    num = int(input("Enter an integer number: "))
    with open("numbers.txt", "a") as file:
        file.write(f"{num}\n")
with open("numbers.txt", "r") as file:
    content = file.read()
print(content)

name = input("Enter your name: ")
with open("names.txt", "a") as file:
    file.write(f"\n{name}")
with open("names.txt", "r") as file:
    content = file.read()
print(content)
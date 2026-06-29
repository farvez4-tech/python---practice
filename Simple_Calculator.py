print("------Simple Calculator------")
print("1.  Addition")
print("2.  Subtraction")
print("3.  Multiplication")
print("4.  Divition")
choice = input("Enter yiur choice (1 - 4):  ")
try:
    num1 = float(input("Enter first Number:  "))
    num2 = float(input("Enter second Number:  "))
    if choice == "1":
        print(f"Answer = {num1 + num2}")
    elif choice == "2":
        print(f"Answer = {num1 - num2}")
    elif choice == "3":
        print(f"Answer = {num1 *  num2}")
    elif choice == "4":
        print(f"Answer = {num1 / num2}")
except ValueError:
        print("Please enter a Integer Value!!!")
except ZeroDivisionError:
        print("Sorry! The number cannot Divided by Zero. ")
                            
                            
                    
        
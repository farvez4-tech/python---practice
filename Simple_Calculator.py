 
try:
    while True:
        print("------Simple Calculator------")
        print("1.  Addition")
        print("2.  Subtraction")
        print("3.  Multiplication")
        print("4.  Divition")
        print("5.  Exit")
        choice = input("Enter your choice (1 - 4):  ")
        
        
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
        again = input("Do you want to continue ? (yes / no)")
        if again.lower() == "no":
                print("Thank you for using the calculator!")
                break
                
except ValueError:
        print("Please enter a Integer Value!!!")
except ZeroDivisionError:
        print("Sorry! The number cannot Divided by Zero. ")
                            
                            
                    
        
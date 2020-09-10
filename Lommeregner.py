import Divider
import Gange
import Plus
import Minus
while(True):
    print("[1] Divider")
    print("[2] Gange")
    print("[3] Plus")
    print("[4] Minus")
    Choice = input("Please choose an option")
    if Choice == "1":
        number1 = int(input("Choose the first number"))
        number2 = int(input("Choose the second number"))
        result = Divider.divider(number1, number2)
        break
    elif Choice == "2":
        number1 = int(input("Choose the first number"))
        number2 = int(input("Choose the second number"))
        result = Gange.gange(number1, number2)
        break
    elif Choice == "3":
        number1 = int(input("Choose the first number"))
        number2 = int(input("Choose the second number"))
        result = Plus.plus(number1, number2)
        break
    elif Choice == "4":
        number1 = int(input("Choose the first number"))
        number2 = int(input("Choose the second number"))
        result = Minus.minus(number1, number2)
        break
    else:
        print("Please enter a correct number")
print(result)
import Divider
import Gange
import Plus
import Minus

print("[1] Divider")
print("[2] Gange")
print("[3] Plus")
print("[4] Minus")
Choice = int(input("Please choose an option"))

if Choice == 1:
    number1 = int(input("Choose the first number"))
    number2 = int(input("Choose the second number"))
    Divider.divider(number1, number2)
elif Choice == 2:
    number1 = int(input("Choose the first number"))
    number2 = int(input("Choose the second number"))
    Gange.gange(number1, number2)
elif Choice == 3:
    number1 = int(input("Choose the first number"))
    number2 = int(input("Choose the second number"))
    Plus.plus(number1, number2)
elif Choice == 4:
    number1 = int(input("Choose the first number"))
    number2 = int(input("Choose the second number"))
    Minus.minus(number1, number2)
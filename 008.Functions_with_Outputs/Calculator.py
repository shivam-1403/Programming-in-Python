# Here is a calculator

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

from art import logo


def calculator():
    print(logo)
    stop = False

    num1 = float(input("What's the first number ? : "))

    for symbols in operations :
        print(symbols)

    while not stop :
        operation_symbol = input("Pick an operation from the line above : ")

        num2 = float(input("What's the next number ? : "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Enter 'y' to continue with {answer} or 'n' to exit or 'r' to restart the calculator : ")
        if choice == "y" : 
            num1 = answer
        elif choice == "r" :
            stop = True
            calculator()
        else : 
            stop = True
            exit

calculator()
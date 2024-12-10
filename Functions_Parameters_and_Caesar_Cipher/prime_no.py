# We'll check whether a number is prime or not.

def prime(number):
    is_prime = True
    for i in range(2,number-1):
        if number%i == 0:
            is_prime = False
    if is_prime:
        print("Number is Prime")
    else:
        print("Number is not Prime")

n=int(input("Enter a number to check if it is prime or not : "))
prime(number=n)
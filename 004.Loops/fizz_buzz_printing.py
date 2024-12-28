# Print all numbers between 1 to 100 in turn
# if the number is divisible by 3, instead of number print Fizz
# if the number is divisible by 5, instead of number print Buzz
# if the number is divisible by 3 and 5 both, instead of number print FizzBuzz

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
def add(*num):
    sum = 0
    for n in num:
        sum+=n
    return sum

# print(add(1,2,3,4,5))


# **kwargs -->

def calculate(n, **kwargs):
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
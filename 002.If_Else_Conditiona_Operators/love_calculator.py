# This will take two names as input, find the no. of times the words, T,R,U,E and L,O,V,E comes in them, add them respectively and join them

name1=input("Enter first name : ")
name2=input("Enter second name : ")
str1=name1+name2
str2=str1.lower()
t=str2.count('t')
r=str2.count('r')
u=str2.count('u')
e=str2.count('e')
l=str2.count('l')
o=str2.count('o')
v=str2.count('v')
e=str2.count('e')
true=t+r+u+e
love=l+o+v+e
res=int(str(true)+str(love))
if (res < 10) or (res > 90):
    print(f"Your Love Score is {res} %, you go together like coke and mentos !")
elif (res >= 40) and (res <= 50):
    print(f"Your Love Score is {res} %, you are all right together !")
else:
    print(f"Your Love Score is {res} %")
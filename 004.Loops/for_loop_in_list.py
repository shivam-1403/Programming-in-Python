# Calculate average height, without using sum and len functions.

student_height=input("Enter the heights of student : ").split()
for n in range(0, len(student_height)):
    student_height[n]=int(student_height[n])

add=0
for height in student_height:
    add+=height

num=0
for student in student_height:
    num+=1

avg=float(add/num)
print("Average Height is : ",round(avg))
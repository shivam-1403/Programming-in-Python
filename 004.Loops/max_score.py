score_list=input("Enter the Scores : ").split()
for n in range(0, len(score_list)):
    score_list[n]=int(score_list[n])

maximum=0
for score in score_list:
    if score>maximum:
        maximum=score

print("The Maximum Score is : ",maximum)
# You are going to write a virtual coin toss program.
# It will randomly tell the user, "Heads" or "Tails" (Output should be exactly like this).
# Generate a random number, 0 or 1, where,
# 1 means Heads and 0 means Tails
# Create your own seed to generate number.

import random

test_seed=int(input("Enter seed number : "))
random.seed(test_seed)
random_res=random.randint(0,1)

if random_res == 0:
    print("Tails")
else:
    print("Heads")
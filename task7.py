import random
import math

def myfunction():
    num_list = []  
    for _ in range(5): 
        num = random.randint(20, 50) 
        num_list.append(num) 
    print("Squares of random numbers:")
    for num in num_list: 
        if num % 2 == 0:
            print(math.pow(num, 2)) 
myfunction()
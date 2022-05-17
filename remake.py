import math
import time
import random as rnd

name = input("please enter your name \n")
age = int(input(f"Hello {name} how old are you \n"))
select = int(input("1. Addition  | 2. Subtraction | 3. Multiplication  | 4. Division \n"))

if select == 1:
    questions = int(input("How Many questions do you want \n"))
    for q in range(questions):
        n1 = rnd.randint(1, 100)
        n2 = rnd.randint(1, 100)
        print("What is " + str(n1) + " + " + str(n2) + "?")
        computer_answer = n1 + n2
        anwser = int(input())
        if anwser == computer_answer:
            print ("Correct")
            q+=1
        else:
            print ("wrong")
            q+=1

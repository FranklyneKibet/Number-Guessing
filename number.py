import random

flag = True
while flag:
    num = input("Please input a number for upper bound: ")
    
    if num.isdigit():
        print("let's play!")
        num = int(num)
        flag = False
    else: 
        print("Invalid Input! Try Again!")

secret = random.randint(1, num)
        
guess = None
count = 1 

while guess != secret:
    guess = input("please type a number between 1 and " + str(num) +  ":")
    if guess.isdigit():
        guess = int(guess)
        
    if guess == secret: 
        print("You got it right")
    else:
        print("Please try again")
        count += 1
        
print('it took you', count, 'guesses' )
## Name: Joshua Santillan
## Date: 2/18/20
## Email: santillanj125821@student.vvc.edu
## Class: cis83 spr-2020
## Description: simulating dice rolls while concatenating strings
import random

#start at two, two die will never make 1.
print("Welcome to Josh's Double Dice Game ™")
print("⤷ ⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋⥋ ⤴")

streak = 0
menu = 1
balance = 100.00
print("Initial Balance: $", balance)
num_rolls = int(input('Enter number of rolls: '))
while menu == 1:
    win = 20
    num_twos = ""
    num_threes = ""
    num_fours = ""
    num_fives = ""
    num_sixes = ""
    num_sevens = ""
    num_eights = ""
    num_nines = ""
    num_tens = ""
    num_elevens = ""
    num_twelves = ""
    #num_rolls = 2

    counter = 0
    Gamble = int(input("How many 12's will hit in this number of rolls: "))
   # Gamble = 5
    if num_rolls >= 1:
        for i in range(num_rolls):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            roll_total = die1 + die2

            if roll_total == 2:
                num_twos = num_twos + "*";
            elif roll_total == 3:
                num_threes = num_threes + "*";            
            elif roll_total == 4:
                num_fours = num_fours + "*";
            elif roll_total == 5:
                num_fives = num_fives + "*";
            elif roll_total == 6:
                num_sixes = num_sixes + "*";
            elif roll_total == 7:
                num_sevens = num_sevens + "*";            
            elif roll_total == 8:
                num_eights = num_eights + "*";       
            elif roll_total == 9:
                num_nines = num_nines + "*";
            elif roll_total == 10:
                num_tens = num_tens + "*";
            elif roll_total == 11:
                num_elevens = num_elevens + "*";          
            elif roll_total == 12:
                num_twelves = num_twelves + "*";
                counter +=1             
            #print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

        print('\nDice roll statistics:')
        print('2s:', num_twos)
        print('3s:', num_threes)
        print('4s:', num_fours)
        print('5s:', num_fives)
        print('6s:', num_sixes)
        print('7s:', num_sevens)
        print('8s:', num_eights)
        print('9s:', num_nines)
        print('10s:', num_tens)
        print('11s:', num_elevens)
        print('12s:', num_twelves)
    else:
        print('Invalid number of rolls. Try again.')

    if Gamble == counter:
        print("\n------------")
        print("***Winner***")
        print("------------")
        streak += 1
        balance += (win * streak*2)
        print("»New Balance« $", balance)
    else:
        streak = 0
        print("\n------------")
        print("***Loser***")
        print("------------")
        balance -= win
        if balance < 1:
            print("Broke Go Home")
            menu == 0
        print("»New Balance« $",balance)
    print("Current win streak:", streak)


    ans = input("\nPlay again?(y,n): ")
    if ans == "y":
      menu == 1
    else:
      menu = 0
    if balance < 1:
        print("loser.")
        menu == 0


      

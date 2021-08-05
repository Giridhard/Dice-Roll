from random import randint
def diceroll():
    dice1=randint(1,6)
    dice2=randint(1,6)
    print(f'value of dice1 = {dice1} \nvalue of dice2 = {dice2}')
    total=dice1+dice2
    print(f'Total value is {total}')
    if dice1==6 and dice2==6:
        print(f'**Both dice1 and dice2 are 6,so you got another chance to roll the dice**')
        a=input(f'Type enter to continue: ')
        if a=='enter':
            diceroll()

user_input=input("Enter 'roll' to roll the dice: ").lower()

if user_input=="roll":
    diceroll()

else:
    print("Wrong commad")

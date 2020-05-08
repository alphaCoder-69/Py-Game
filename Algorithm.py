import random                                                           #Importing random module
def star(func):                                                         #DECORATORS
    def body(*args,**kwargs):
        print("*"*20)
        func(*args,**kwargs)
        print("*"*20)
    return body
def per(func):
    def body(*args,**kwargs):
        print("%"*20)
        func(*args,**kwargs)
        print("%"*20)
    return body
@per
@star
def printer(msg): print(msg)
printer("      WELCOME")
def initial():                                                          #The user's choice are stored here
    print("This is a stone, paper and scissors game. Be ready to play the game.\n     The rules are simple :-\n       **Rock vs Paper - Paper wins\n       **Scissors vs Paper - Scissors wins\n       **Rock vs Scissors - Rock wins\n1. Stone\n2. Paper\n3. Scissors\nNow its your turn. Select a number")
    user_input=int(input("Your Choice : "))                              
    return user_input
def gen():                                                              #Function to generate the Opponents input
   opp_choice=random.randint(1,3)
   if(opp_choice==1):return "stone"
   elif(opp_choice==2):return "paper"
   else:return "scissors" 
def Cardinal():                                                         #The head function of the game Cardinal
    userInput=initial()                                                  
    if(userInput==1):user_choice= "stone"
    elif(userInput==2):user_choice="paper"
    elif(userInput==3):user_choice="scissors"
    else: Error()
    opponent=gen()
    print("Your Choice:-",user_choice,"\nOpponent's Choice:-",opponent,"\n# ",user_choice," vs ",opponent)
    if(user_choice != opponent):
        if((user_choice== "stone" and opponent=="paper") or (user_choice== "paper" and opponent=="scissors") or (user_choice== "scissors" and opponent=="stone")):
            print("\nYou Lose. Opponent wins the game.\n")
        elif((user_choice== "stone" and opponent=="scissors") or (user_choice== "paper" and opponent=="stone") or (user_choice== "scissors" and opponent=="paper")):
            print("\nYou have won the game.\n")
        print("\nDo want to play again? (yes/no)")
        again=input()
        if (again=="yes"):Cardinal()
        else : return
    else:
        print("\nThe game is draw.Play again\n\n")
        Cardinal()
def Error():                                                                #This error message is displyed when you gve an invalid input
    print("\nYou have entered an invalid input. Please try again\n")
    Cardinal()
Cardinal()
# Developed by Swaroop Kumar Sahu

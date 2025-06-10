def start_game():  
    print("You are insdie your house during the aftermath of an apocalyptic fallout.")
    print("Would you like to leave to grab spare supplies or stay inside?")

    choice1 = input("What will you do? (leave/stay)")

    if choice1 == "leave":
        leave()
    elif choice1 == "stay":
        stay()
    else:
        print("Not a valid input. Try again")
        
        
def leave():
    print("You leave home and manage to find supplies. Along the way you find someone who could use some help.")
    
    choice2 = input("What will you do? (share/keep)")
    
    if choice2 == "share":
        share()
    elif choice2 == "keep":
        keep()
    else:
        print("Not a valid input. Try again.")
        
def share():
    print("You share your belongings and they run off somewhere. As you walk home, you encounter a raider.")
    
    choice3 = input("What will you do? (fight/run)")
    
    if choice3 == "fight":
        fight()
    elif choice3 == "run":
        run()
    else:
        print("Not a valid input. Try again.")

def fight():
    print("The person comes back to help you fight off the raider. You thank the person and go home.")
    print("You win!")
    
def run():
    print("The raider catches up to you and kills you.")
    print("You lose.")
    
def stay():
    print("You decide to stay home. After a while you start to hear banging on your door. Raiders are outside trying to break in.")
    
    choice4 = input("What will you do? (confront/hide)")
    
    if choice4 == "confront":
        confront()
    elif choice4 == "hide":
        hide()
    else:
        print("Not a valid input. Try again.")
        
def confront():
    print("They overwhelm and brutally murder you.")
    print("You lose")
    
def hide():
    print("You hide in a closet and they break in. As they search your house, you see an opening to sneak out and escape.")
    
    choice5 = input("What will you do? (stay/sneak)")
    
    if choice5 == "stay":
        stay_2()
    elif choice5 == "sneak":
        sneak()
    else:
        print("Not a valid input. Try again.")
        
def
        
        
        
        
        
        
        
        
        
start_game()

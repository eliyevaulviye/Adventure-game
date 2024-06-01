#3.adventure game


import time

def flush_text(text, time_delay=0.1):
    for i in text:
        print(i, end='', flush=True) 
        time.sleep(time_delay)
    print()


flush_text("Welcome to the Adventure Game!")  
flush_text("You find yourself in a dark and mysterious forest.")
flush_text("Your goal is to navigate through the forest and reach the treasure at the end.")
flush_text("You walk in the dark. Then you come across a fork in the path")

choice1=input("You have to decide between taking the left or the right path: ")

if choice1=="left":
    flush_text("There was a serial killer, and you died!")
    print("Game Over")

elif choice1=="right":
    flush_text("You cautiously feel your way through the darkness.")
    flush_text("After a while, you hear a cracking sound coming from the corner.")
    flush_text("A dark figure lanuches at you, knocking you unconcious")
    choice2=input("Do you want to approach the figure to fight with it or do you want to turn to leave: ")
    if choice2=="approach":
        print("You wake up in your bed. It all was a dream.")
    elif choice2=="turn to leave":
        print("On the way back you saw the hidden treasure. So you win. Congratulations! ")  
    else:
        print("Invalid choice. Please enter a valid choice.")      
else:
    print("Invalid choice. Please enter a valid choice.")



#tutorial 36 my little game

from sys import exit
import os

my_items = ["cell phone", "wallet"]

def show_inventory():
    print"""    -------------------------------
    You have:"""
    
    if "cell phone" in my_items:
        print "\t- cell phone"
        
    if "wallet" in my_items:
        print "\t- wallet"
        
    if "knife" in my_items:
        print "\t- knife"
    
    if "cigarettes" in my_items:
        print "\t- cigarettes"

def stars():
    print "\t\t\t\t***"

def defeated_guy(looked_at_pockets):
    print"""Somehow you managed to win the fight. Your foe is lying with no 
conscience, what you're gonna do?\n"""
        
    if looked_at_pockets == False:
        print "(1) Take a look on his pockets."
        if "knife" not in my_items:
            print "(2) Take his knife."
        
        print "(3) Go away."
        show_inventory()
        guy_defeated_choice = raw_input("> ")
        
        if guy_defeated_choice == "1":
            looked_at_pockets = True
            os.system('clear')
            print "You managed to fing some cigaretes in his pockets."
            print "You didn't want to take a risk and decided to go away."
            my_items.append("cigarettes")
            stars()
            road()
        
        elif guy_defeated_choice == "2":
            os.system('clear')
            print "You took his knife from the ground."
            print "You didn't want to take a risk and decided to go away."
            my_items.append("knife")
            stars()
            road()
        elif guy_defeated_choice == "3":
            os.system('clear')
            print "You decided to go away as fast as you could."
            stars()
            road()
        else:
            os.system('clear')
            defeated_guy(looked_at_pockets)
        
    show_inventory()
    

def district():
    print """You're moving through a very dangerous district. Suddenly a big guy with 
a knife comes from nowhere and asks you to give him your wallet.
What you're gonna do?"""

    print """
    (1) Start a fight.
    (2) Give him a wallet.
    (3) Give him your cell phone.
    (4) Run away."""
    show_inventory()
    
    district_choice = raw_input("> ")
    os.system('clear')
    
    if district_choice == "1":
        looked_at_pockets = False
        defeated_guy(looked_at_pockets)    
    elif district_choice == "2":
        print """You've decided to give your wallet. That's good you didn't have much
money in there."""
        
        my_items.remove("wallet")
        stars()
        road()
        
    elif district_choice == "3":
        print"""You've decided to give your cell phone. It's quite old and doesn't 
work properly. The big guy took your phone and walked away."""
        
        my_items.remove("cell phone")
        stars()
        road()
    elif district_choice == "3":
        print"""You've decided to run away. It's a shame you won't be able to tell 
anyone how that morran throw a knife in your back..."""
        exit(0)
    else:
        os.system('clear')
        district()
        
def road():
    print"""You left that awful place and now you at the bus stop. Some old man
has fallen on the ground, it seems, he doesn't feel good. It's late night
no one except you see him."""
    
    if "cell phone" not in my_items:
        print "\"I could use a cell phone right now!\" - you told to yourself."
    
    print "What you're gonna do?\n"
    
    if "cell phone" in my_items:
        print "(1) Call an ambulance using cell phone"
        
    if "wallet" in my_items:
        print "(2) Pay a taxi driver to take the old man to the hospital"
    
    print "(3) Walk away"
    
    show_inventory()
     
    road_choice = raw_input("> ")

    os.system('clear')

    if road_choice == "1":
        if "cell phone" in my_items:
            print"""Ambulance came very fast. They took an old man and went away 
as fast as they could. """
            stars()
            home(road_choice)
        else:
            os.system('clear')
            road()
    elif road_choice == "2":
        if "wallet" in my_items:
            print"""A taxi driver was happy to make some fast money at night. 
You gave him all your money, hoping he will take granpa to the hospital in time.""" 
            my_items.remove("wallet")
            stars()
            home(road_choice)
        else:
            os.system('clear')
            road()
    elif road_choice == "3":
            print """\"He's probably drunk\" - you thought."""
            stars()
            home(road_choice)
    else:
        os.system('clear')
        road()
        
def home(road_choice):
    
    if road_choice == "1":
        print "You waited for half an hour and you didn't see any bus or taxi."
    elif road_choice == "2":
        print "As long as you spent all money for an old man, there was no"
        print "sense in staying on the bus stop."
        
    print "Somehow you managed yo get your way to home. Sleep a bit, "
    print "you've earned the rest... :)"
    print "\n\n\t\t\t THE END"
    exit(0)

os.system('clear')       
district()

import time

def start():
    # Storyline prompts
    print("Airports were the first to close once the outbreak started")
    time.sleep(2)
    print("soon all major motorways were barricaded off, that was a week ago")
    time.sleep(2)
    print("Satellite towers are all down.")
    time.sleep(4)


    print("We were all looking forward to our camping trip")
    time.sleep(2)
    print("me and Jess wanted to do something nice with Joseph before he started reception")
    time.sleep(2)
    print("Glad jess likes to be prepared, if it wasn’t for the amount of camping supplies and resources,")
    time.sleep(2)
    print("we wouldn’t of lasted this long.  But we are all but out now and running out of options.")
    time.sleep(2)
    print("With refuge camps being overrun the last announcement ")
    time.sleep(2)
    print("was for survivors to remain barricaded indoors and wait for rescue.")
    time.sleep(2)
    print("Its been days since the last transmission and no sign of any help.")
    time.sleep(2)
    print("Its time I need to make a choice, stay and hope for rescue")
    time.sleep(2)
    print("or leave and look for supplies and make it to one of the remaining camps.")
    time.sleep(2)
    print("Stay or Leave")

    answer = input(">").lower().strip()
    if answer == "stay":
        # take player to cross_roads
        stay()
    elif answer == "leave":
        # take player to play_again()
        leave()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either stay or leave. To quit the game press 1")
        answer = input(">").lower().strip()
        if answer == "stay":
        # take player to cross_roads
            stay()
        elif answer == "leave":
        # take player to play_again()
            leave()
        elif answer == "1":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()
    
def leave():
    print("You pack up all remaining food and supplies, wait for it to be clear outside before making your move.")
    time.sleep(2)
    print("Do you take the car which has a full tank of petrol ready from the camping trip")
    time.sleep(2)
    print("or go out the back way which leads to a now unused railway line.")
    time.sleep(2)
    print("Car or Back")

    answer = input(">").lower().strip()
    if answer == "car":
        # take player to cross_roads
        car()
    elif answer == "back":
        # take player to play_again()
        back()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either car or back. To quit the game press 1")
        answer = input(">").lower().strip()
        if answer == "car":
        # take player to cross_roads
            car()
        elif answer == "back":
        # take player to play_again()
            back()
        elif answer == "1":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()

def car():
    print("You load the supplies into the car, jess straps Joseph into his car seat.")
    time.sleep(2)
    print("Still no sign of any zombies.")
    time.sleep(2)
    print("You turn the key in the ignition, the car wont start. You try again still nothing.")
    time.sleep(2)
    print("Jess begins to panic and shouts “hurry up, come on we have to go”.")
    time.sleep(2)
    print("“Im trying” you snap back. This causes joseph to cry.")
    time.sleep(2)
    print("With all the commotion you don’t see the zombies approach the car and")
    time.sleep(2)
    print("CRASH they smash through your drivers window.")
    time.sleep(2)
    print("Do you kick the door open pushing the zombies back")
    time.sleep(2)
    print("or reach for your crowbar under the drivers seat.")
    time.sleep(2)
    print("Kick or Crowbar")

def back():
    print("hello") 

def stay():
    print("hello")

start()

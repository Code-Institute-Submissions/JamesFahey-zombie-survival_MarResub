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
            print("Doubt you would of got far")
            # exit()
    
def leave():
    print("hello")

def stay():
    print("hello")

start()

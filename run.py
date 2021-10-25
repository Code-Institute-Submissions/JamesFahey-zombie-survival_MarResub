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
    print("Do you take the car which could attrack nearby zombies")
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

    answer = input(">").lower().strip()
    if answer == "kick":
        # take player to cross_roads
        kick()
    elif answer == "crowbar":
        # take player to play_again()
        crowbar()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either car or back. To quit the game press 1")
        answer = input(">").lower().strip()
        if answer == "kick":
        # take player to cross_roads
            kick()
        elif answer == "crowbar":
        # take player to play_again()
            crowbar()
        elif answer == "1":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()

def crowbar():
    print("You reach under your chair, frantically trying to grab your crowbar.")
    time.sleep(2)
    print("Jess and Joseph are screaming, 4 arms are reaching through the window pulling at you")
    time.sleep(2)
    print("Your fingers brush against the crowbar as teeth sink into your neck.")
    time.sleep(2)
    print("Jess wails in horror just as the growing group of zombies smash the passenger window...")
    time.sleep(2)
    print("You did not survive the zombie outbreak")
    time.sleep(4)
    play_again()

def kick():
    print("The door crashes open with the impact of your kick knocking the zombies to the ground.") 
    time.sleep(2)
    print("You try the ignition again, the engine starts and you manage to get away. /n") 
    time.sleep(2)
    print("'We have been driving for nearly 2 hours,") 
    time.sleep(2)
    print("anywhere we could stop for supplies and resources,") 
    time.sleep(2)
    print("Were overcrowded with those things, we had to keep going.") 
    time.sleep(2)
    print("Our only option now is make it to A camp and hope theres someone that can help us” /n") 
    time.sleep(2)
    print("As you are making you way to a refuge camp you see a car in a ditch") 
    time.sleep(2)
    print("with smoke coming from the bonnet and what looks to be a full boot") 
    time.sleep(2)
    print("As you stop the car, “what are you doing” jess asks.") 
    time.sleep(2)
    print("“there could be something useful in there, we need supplies” you answer.") 
    time.sleep(2)
    print("“its not worth it we need to keep going” jess pleads.") 
    time.sleep(2)
    print("Get out or keep going. ( g or k )") 
    time.sleep(2)

    answer = input(">").lower().strip()
    if answer == "g":
        # take player to cross_roads
        get_out()
    elif answer == "k":
        # take player to play_again()
        keep_going()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either g or k. To quit the game press 1")
        answer = input(">").lower().strip()
        if answer == "g":
        # take player to cross_roads
            get_out()
        elif answer == "k":
        # take player to play_again()
            keep_going()
        elif answer == "1":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()

def keep_going():
    print("You avoid cities to stay clear of the hoards as the miles tick by and night falls.")
    time.sleep(2)
    print("Resources are low with no options to stop. The car begins to chug as you use the last of the fuel")
    time.sleep(2)
    print("As jess and Joseph sleep the crowd moves in…")
    time.sleep(2)
    print("You did not survive the zombie outbreak")
    time.sleep(4)
    play_again()

def get_out():
    print("As you approach the car you notice 2 bodies. The driver, his head pressed against the steering wheel.")
    time.sleep(2)
    print("The passenger has gone head first through the windscreen.")
    time.sleep(2)
    print("Your attention turns to the boot off the car, they have food, bottled water and more.")
    time.sleep(2)
    print("You grab as much as you can carry, as you turn to head back to your car")
    time.sleep(2)
    print('"help me" the weak voice came from the driver.')
    time.sleep(2)
    print('"Please help me. Me and my wife.. Oh my god my wife"')
    time.sleep(2)
    print("You look back at your car and Joseph in the back, then turn your attention back to the injured driver.")
    time.sleep(2)
    print('"Please help me, I think my arm is broke"')
    time.sleep(2)
    print("Help the driver or walk away (help or walk)")
    time.sleep(2)
    
    answer = input(">").lower().strip()
    if answer == "help":
        # take player to cross_roads
        help_driver()
    elif answer == "walk":
        # take player to play_again()
        walk_away()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either g or k. To quit the game press 1")
        answer = input(">").lower().strip()
        if answer == "help":
        # take player to cross_roads
            help_driver()
        elif answer == "walk":
        # take player to play_again()
            walk_away()
        elif answer == "1":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()

def help_driver():
    print("You want to turn and run but can't leave him there to die.")
    time.sleep(2)
    print('"Fuckin ell"')
    time.sleep(2)
    print("You help the driver out of the car and into your own.")
    time.sleep(2)
    print("You put him in the front seat and jess goes to sit with Joseph.")
    time.sleep(2)
    print("You finish loading the supplies and are ready to go.")
    time.sleep(2)
    print('"Wait, by my wife, we had some spare fuel in a tank."')
    time.sleep(2)
    print("You reach over a grab the fuel and get on your way.")
    time.sleep(2)
    print("You avoid the cities as the miles tick by.")
    time.sleep(2)
    print("He hasn't said much since we rescued him from the crash.He's slept most of the time, probably due to the blow to the head.")
    time.sleep(2)
    print("What would you even say to someone who's just lost his wife, I don't know what I would do if something happened to jess or Joseph.")
    time.sleep(2)
    print("It isn't long before you need the fuel the driver told you about. Without it you would of been stranded.")
    time.sleep(2)
    print("As you get back in the car you notice sweat pouring from the driver's forehead.")
    time.sleep(2)
    print("He has a fever. You begin look him over trying to not alert jess to issue. Then you see it, on his left shoulder, bite marks.")
    time.sleep(2)
    print('"I was trying to get her help before she turned" the driver says panting')
    time.sleep(2)
    print('You jump back in shock. "So thats how you ended in the ditch, you should of told us you were bitten"')
    time.sleep(2)
    print('"Please. Were nearly at the camp, someone could help" His voice getting weaker, his eyes closed again.')
    time.sleep(2)
    print('"You need to get out now".... He doesnt respond or move. Just lies motionless in his seat.')
    time.sleep(2)
    print("ou need to get him out of the car do you reach across and open the door, or get out and walk around. (reach or around)")
    time.sleep(2)

    answer = input(">").lower().strip()
    if answer == "reach":
        # take player to cross_roads
        reach_across()
    elif answer == "around":
        # take player to play_again()
        walk_around()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either g or k. To quit the game press 1")
        answer = input(">").lower().strip()
        if answer == "reach":
        # take player to cross_roads
            reach_across()
        elif answer == "around":
        # take player to play_again()
            walk_around()
        elif answer == "1":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()

def reach_across():
    print("You reach across slowly trying not to disturb the driver. You pull on the handle and push open the passenger door.")
    time.sleep(2)
    print("The drivers eyes open blood shot and yellow and sinks his teeth into your arm.")
    time.sleep(2)
    print('"Arggghhh" you yell out in pain and push the driver back in his seat.')
    time.sleep(2)
    print("Jess grabs the crowbar from bellow your seat and strikes the driver repeatedly in the head")
    time.sleep(2)
    print("until his skull bursts and the driver is dead.")
    time.sleep(4)
    print("Not much is said for the rest of the journey, you see the camp ahead and pull over.")
    time.sleep(2)
    print("The bite on your arm is throbbing and tiredness is starting to take over.")
    time.sleep(2)
    print("Jess gets Joseph out of the car and you stand opposite them. You give them a long hug and a kiss and say your goodbyes.")
    time.sleep(2)
    print('"Are you not coming too dad" Joseph asks confused')
    time.sleep(2)
    print('"Ill catch ypus up mate, Ive just need to grab something first " you reply trying to remain strong.')
    time.sleep(2)
    print("You watch them walk up to the camp soldiers approach with guns. You wait until you see them brought inside then turn and walk away.")
    time.sleep(2)
    print("You didn't survive the zombie outbreak but you did get your family to safety.")
    time.sleep(4)
    play_again()

def walk_around():
    print("You do not risk reaching across the driver. You get out and start walking round to the other side.")
    time.sleep(2)
    print('"Ahhhhhhh"')
    time.sleep(2)
    print("The driver lundged towards the back of the car. You race to the rear door a swing it open")
    time.sleep(2)
    print('"Nooo" you cry out in anguish')
    time.sleep(2)
    print("As you drive to the camp you look in the rear view mirror at the blood stained seats and an empty child seat. A reminder of what you lost.")
    time.sleep(4)
    print("You arrive at the camp. Soldiers meet you and once they are satisfied you aren't bitten. Allow you to enter")
    time.sleep(2)
    print("You survived the zombie apocalypse but lost everything.")
    time.sleep(4)
    play_again()

def walk_away():
    print("You turn and walk to the car not looking back. You quickly load the supplies in in car and get moving.")
    time.sleep(2)
    print('"Everything OK" asks jess')
    time.sleep(2)
    print('"Everything is fine" You answer trying to hide your guilt.')
    time.sleep(2)
    print("You avoid cities to stay clear of the hoards as the miles tick by and night falls.")
    time.sleep(2)
    print("Resources are low with no options to stop. The car begins to chug as you use the last of the fuel")
    time.sleep(2)
    print("As jess and Joseph sleep the crowd moves in…")
    time.sleep(2)
    print("You did not survive the zombie outbreak")
    time.sleep(4)
    play_again()

def back():
    print("hello") 

def stay():
    print("hello")

def play_again():
    print("Want to try and survive the zombie outbreak again? Y or N")
    # convert the player's input to lower_case
    answer = input(">").lower().strip()
    if answer == "y":
        # take player to start()
        start()
    elif answer == "n":
        # exit() the program
        print("Too scared to see if you would of made it?")
        print("Doubt you would of got far anyway")
        # exit()
    else:
        # return to start()
        start()

start()

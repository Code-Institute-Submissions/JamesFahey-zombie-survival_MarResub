import time
import random
import os

a = 2
b = 3
c = 4

def clear_console():
    """
    Clears the console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    clear_console()
    print("Welcome to Zombie Survival.")
    time.sleep(a)
    print("\nYou and your family are doing what you can to survive the horror.")
    print("Can you make the right choices")
    print("to get you and your family to safety?")
    time.sleep(a)
    print("\nDo you think you have what it takes to survive? Y or N")
    time.sleep(a)

    answer = input(">").lower().strip()
    if answer == "y":
        # take player to intro()
        print("You are ready... Good luck")
        time.sleep(b)
        intro()
    elif answer == "n":
        # else return player to start()
        print("Too scared to see if you would of made it?")
        print("Doubt you would of got far anyway")
        time.sleep(a)
        start()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either y or n.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "y":
            # take player to intro
            intro()()
        elif answer == "n":
            # take player to start()
            start()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def intro():
    # Storyline prompts
    clear_console()
    print("\nAirports were the first to close once the outbreak started")
    time.sleep(a)
    print("soon all major motorways were barricaded off, that was a week ago")
    time.sleep(a)
    print("Satellite towers are all down.")
    time.sleep(c)
    print()

    print('\n"We were all looking forward to our camping trip')
    time.sleep(a)
    print("me and Jess wanted to do something nice with Joseph before he")
    time.sleep(a)
    print("started nursery. Glad Jess likes to be prepared, if it ")
    time.sleep(a)
    print("wasn’t for the amount of camping supplies and resources, we")
    time.sleep(a)
    print("wouldn’t of lasted this long.  But we are all but out now")
    time.sleep(a)
    print("and running out of options. With refuge camps being overrun")
    time.sleep(a)
    print("the last announcement was for survivors to remain barricaded")
    time.sleep(a)
    print("indoors and wait for rescue. Its been days")
    time.sleep(a)
    print("since the last transmission and no sign of any help.")
    time.sleep(a)
    print("Its time I need to make a choice, stay and hope for rescue")
    time.sleep(a)
    print('or leave for supplies and make it to one of the remaining camps."')
    time.sleep(a)
    print("Stay or Leave")

    answer = input(">").lower().strip()
    if answer == "stay":
        # take player to stay()
        stay()
    elif answer == "leave":
        # take player to leave()
        leave()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either stay or leave.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "stay":
            # take player to stay()
            stay()
        elif answer == "leave":
            # take player to leave()
            leave()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()
    
    
def leave():
    print("\nYou pack up all remaining food and supplies,")
    time.sleep(a)
    print("then wait for it to be clear outside before making your move.")
    time.sleep(a)
    print("Do you take the car which could attract nearby zombies")
    time.sleep(a)
    print("or go out the back way which leads to a now unused railway line.")
    time.sleep(a)
    print("Car or Back")

    answer = input(">").lower().strip()
    if answer == "car":
        # take player to car()
        car()
    elif answer == "back":
        # take player to back()
        back()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either car or back.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "car":
            # take player to car()
            car()
        elif answer == "back":
            # take player to back()
            back()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def car():
    print("\nYou load the supplies into the car,")
    time.sleep(a)
    print("jess straps Joseph into his car seat.")
    time.sleep(a)
    print("Still no sign of any zombies.")
    time.sleep(a)
    print("You turn the key in the ignition, the car wont start.")
    time.sleep(a)
    print("You try again still nothing.")
    time.sleep(a)
    print("Jess begins to panic and shouts “hurry up, come on we have to go”.")
    time.sleep(a)
    print("“Im trying” you snap back. This causes joseph to cry.")
    time.sleep(a)
    print("With all the commotion you don’t see the zombies approach the car")
    time.sleep(a)
    print("CRASH they smash through your drivers window.")
    time.sleep(a)
    print("Do you kick the door open pushing the zombies back")
    time.sleep(a)
    print("or reach for your crowbar under the drivers seat.")
    time.sleep(a)
    print("Kick or Crowbar")

    answer = input(">").lower().strip()
    if answer == "kick":
        # take player to kick()
        kick()
    elif answer == "crowbar":
        # take player to crowbar()
        crowbar()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either kick or crowbar.")
        print("\n To quit the game press q")
        
        answer = input(">").lower().strip()
        if answer == "kick":
            # take player to kick()
            kick()
        elif answer == "crowbar":
            # take player to crowbar()
            crowbar()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def crowbar():
    print("\nYou reach under your chair,")
    time.sleep(a)
    print("frantically trying to grab your crowbar.")
    time.sleep(a)
    print("Jess and Joseph are screaming,")
    time.sleep(a)
    print("4 arms are reaching through the window pulling at you")
    time.sleep(a)
    print("Your fingers brush against the crowbar as teeth sink into your")
    time.sleep(a)
    print("neck. Jess wails in horror just as the growing group of zombies ")
    time.sleep(a)
    print("smash the passenger window...")
    time.sleep(b)
    print("\nYou did not survive the zombie outbreak")
    time.sleep(a)
    play_again()


def kick():
    print("\nThe door crashes open with the impact of your kick knocking") 
    time.sleep(a)
    print("the zombies to the ground. You try the ignition again,") 
    time.sleep(a)
    print("the engine starts and you manage to get away.") 
    time.sleep(a)
    print('\n"We have been driving for nearly 2 hours,') 
    time.sleep(a)
    print("anywhere we could stop for supplies and resources,") 
    time.sleep(a)
    print("Were overcrowded with those things, we had to keep going.") 
    time.sleep(a)
    print('Our only option now is make it to a camp') 
    time.sleep(a)
    print('and hope theres someone that can help us"') 
    time.sleep(a)
    print("\nAs you are making you way to a refuge camp") 
    time.sleep(a)
    print("you see a car in a ditch") 
    time.sleep(a)
    print("smoke coming from the bonnet and what looks to be a full boot") 
    time.sleep(a)
    print("As you stop the car, “what are you doing” jess asks.") 
    time.sleep(a)
    print("“there could be something useful in there,") 
    time.sleep(a)
    print('we need supplies” you answer.') 
    time.sleep(a)
    print("“its not worth it we need to keep going” jess pleads.") 
    time.sleep(a)
    print("Get out or keep going. ( g or k )") 
    time.sleep(a)

    answer = input(">").lower().strip()
    if answer == "g":
        # take player to get_out()
        get_out()
    elif answer == "k":
        # take player to keep_going()
        keep_going()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either g or k.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "g":
            # take player to get_out()
            get_out()
        elif answer == "k":
            # take player to keep_going()
            keep_going()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def keep_going():
    print("\nYou avoid cities to stay clear of the hoards")
    time.sleep(a)
    print("as the miles tick by and night falls.")
    time.sleep(a)
    print("Resources are low with no options to stop.")
    time.sleep(a)
    print("The car begins to chug as you use the last of the fuel")
    time.sleep(a)
    print("As jess and Joseph sleep the crowd moves in…")
    time.sleep(a)
    print("You did not survive the zombie outbreak")
    time.sleep(c)
    play_again()


def get_out():
    print("\nAs you approach the car you notice 2 bodies.")
    time.sleep(a)
    print("The driver, his head pressed against the steering wheel.")
    time.sleep(a)
    print("The passenger has gone head first through the windscreen.")
    time.sleep(a)
    print("Your attention turns to the boot off the car,")
    time.sleep(a)
    print("they have food, bottled water and more.")
    time.sleep(a)
    print("You grab as much as you can carry,")
    time.sleep(a)
    print("as you turn to head back to your car")
    time.sleep(a)
    print('"help me" the weak voice came from the driver.')
    time.sleep(a)
    print('"Please help me. Me and my wife.. Oh my god my wife"')
    time.sleep(a)
    print("You look back at your car and Joseph in the back,")
    time.sleep(a)
    print("then turn your attention back to the injured driver.")
    time.sleep(a)
    print('"Please help me, I think my arm is broke"')
    time.sleep(a)
    print("Help the driver or walk away (help or walk)")
    time.sleep(a)
    
    answer = input(">").lower().strip()
    if answer == "help":
        # take player to help_driver()
        help_driver()
    elif answer == "walk":
        # take player to walk_away()
        walk_away()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either help or walk.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "help":
            # take player to help_driver()
            help_driver()
        elif answer == "walk":
            # take player to walk_away()
            walk_away()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def help_driver():
    print("You want to turn and run but can't leave him there to die.")
    time.sleep(a)
    print('"Fuckin ell"')
    time.sleep(a)
    print("You help the driver out of the car and into your own.")
    time.sleep(a)
    print("You put him in the front seat and jess goes to sit with Joseph.")
    time.sleep(a)
    print("You finish loading the supplies and are ready to go.")
    time.sleep(a)
    print('"Wait, by my wife, we had some spare fuel in a tank."')
    time.sleep(a)
    print("You reach over a grab the fuel and get on your way.")
    time.sleep(a)
    print("You avoid the cities as the miles tick by.")
    time.sleep(a)
    print("\nHe hasn't said much since we rescued him from the crash.")
    time.sleep(a)
    print("He's slept most of the time, probably due to the blow to the head.")
    time.sleep(a)
    print("What would you even say to someone who's just lost his wife,")
    time.sleep(a)
    print("I don't know what I would do if something")
    time.sleep(a)
    print("happened to jess or Joseph.")
    time.sleep(a)
    print("\nIt isn't long before you need the fuel the driver told you about")
    time.sleep(a)
    print("Without it you would of been stranded.")
    time.sleep(a)
    print("As you get back in the car you notice sweat pouring")
    time.sleep(a)
    print("from the driver's forehead. He has a fever.")
    time.sleep(a)
    print("You begin look him over trying to not alert jess to issue.")
    time.sleep(a)
    print("Then you see it, on his left shoulder, bite marks.")
    time.sleep(a)
    print('"I was trying to get her help before she turned"')
    time.sleep(a)
    print('the driver says panting. You jump back in shock.')
    time.sleep(a)
    print('"So thats how you ended in the ditch,')
    time.sleep(a)
    print('you should of told us you were bitten"')
    time.sleep(a)
    print('"Please. Were nearly at the camp, someone could help"')
    time.sleep(a)
    print('His voice getting weaker, his eyes closed again.')
    time.sleep(a)
    print('"You need to get out now".... He doesnt respond or move.')
    time.sleep(a)
    print('Just lies motionless in his seat.')
    time.sleep(a)
    print("You need to get him out of the car")
    time.sleep(a)
    print("do you reach across and open the door,")
    time.sleep(a)
    print("or get out and walk around. (reach or around)")
    time.sleep(a)

    answer = input(">").lower().strip()
    if answer == "reach":
        # take player to reach_across()
        reach_across()
    elif answer == "around":
        # take player to walk_around()
        walk_around()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either reach or around.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "reach":
            # take player to reach_across()
            reach_across()
        elif answer == "around":
            # take player to walk_around()
            walk_around()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def reach_across():
    print("\nYou reach across slowly trying not to disturb the driver.")
    time.sleep(a)
    print("\You pull on the handle and push open the passenger door.")
    time.sleep(a)
    print("The drivers eyes open blood shot and yellow")
    time.sleep(a)
    print("and sinks his teeth into your arm.")
    time.sleep(a)
    print('"Arggghhh" you yell out in pain')
    time.sleep(a)
    print('and manage to push the driver back in his seat.')
    time.sleep(a)
    print("Jess grabs the crowbar from bellow your seat")
    time.sleep(a)
    print("and strikes the driver repeatedly in the head")
    time.sleep(a)
    print("until his skull bursts and the driver is dead.")
    time.sleep(c)
    print("\nNot much is said for the rest of the journey,")
    time.sleep(a)
    print("you see the camp ahead and pull over.")
    time.sleep(a)
    print("The bite on your arm is throbbing")
    time.sleep(a)
    print("tiredness is starting to take over.")
    time.sleep(a)
    print("Jess gets Joseph out of the car and you stand opposite them.")
    time.sleep(a)
    print("You give them a long hug and a kiss and say your goodbyes.")
    time.sleep(a)
    print('"Are you not coming too dad" Joseph asks confused')
    time.sleep(a)
    print('"Ill catch you up mate, I just need to grab something first "')
    time.sleep(a)
    print('you reply trying to remain strong.')
    time.sleep(a)
    print("You watch them walk up to the camp soldiers approach with guns.")
    time.sleep(a)
    print("You wait until you see them brought inside then turn and walk away")
    time.sleep(a)
    print("You didn't survive the zombie outbreak")
    print("but you did get your family to safety.")
    time.sleep(c)
    play_again()


def walk_around():
    print("\nYou do not risk reaching across the driver.")
    time.sleep(a)
    print("You get out and start walking round to the other side.")
    time.sleep(a)
    print('"Ahhhhhhh"')
    time.sleep(a)
    print("The driver lundged towards the back of the car.")
    time.sleep(a)
    print("You race to the rear door a swing it open")
    time.sleep(a)
    print('"Nooo" you cry out in anguish')
    time.sleep(c)
    print("\nAs you drive to the camp you look in the rear view mirror ")
    time.sleep(a)
    print("at the blood stained seats and an empty child seat.")
    time.sleep(a)
    print("A reminder of what you lost.")
    time.sleep(a)
    print("You arrive at the camp. Soldiers meet you,")
    time.sleep(a)
    print("and once they are satisfied you aren't bitten. Allow you to enter")
    time.sleep(a2)
    print("You survived the zombie apocalypse but lost everything.")
    time.sleep(c)
    play_again()


def walk_away():
    print("\nYou turn and walk to the car not looking back.")
    time.sleep(a)
    print("You quickly load the supplies in in car and get moving.")
    time.sleep(a)
    print('"Everything OK" asks jess')
    time.sleep(a)
    print('"Everything is fine" You answer trying to hide your guilt.')
    time.sleep(a)
    print("\nYou avoid cities to stay clear of the hoards.")
    time.sleep(a)
    print("As the miles tick by and night falls.")
    time.sleep(a)
    print("Resources are low with no options to stop.")
    time.sleep(a)
    print("The car begins to chug as you use the last of the fuel")
    time.sleep(a)
    print("As Jess and Joseph sleep the crowd moves in…")
    time.sleep(a)
    print("You did not survive the zombie outbreak")
    time.sleep(c)
    play_again()


def back():
    print('\n"Progress has been slow, but at least')
    time.sleep(a)
    print('its quiet and no sign of danger.')
    time.sleep(a)
    print("It's going to be dark soon so well have to stop and set up camp.")
    time.sleep(a)
    print("There's another one of those signs promising shelter and safety,")
    time.sleep(a)
    print("it could be better than camping in the woods or by the tracks")
    time.sleep(a)
    print('but Im just not sure"')
    time.sleep(a)
    print('"Theres another one of those signs" Jess acknowledges')
    time.sleep(a)
    print('"I think we should check it out')
    time.sleep(a)
    print('its not far and we cant risk camping out here by ourselves"')
    time.sleep(a)
    print("Camp alone or follow the sign to shelter (camp or follow)")
    time.sleep(a)

    answer = input(">").lower().strip()
    if answer == "camp":
        # take player to camp()
        camp()
    elif answer == "follow":
        # take player to follow_signs()
        follow_signs()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either camp or follow.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "camp":
            # take player to camp()
            camp()
        elif answer == "follow":
            # take player to follow_signs()
            follow_signs()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def camp():
    print("\nThe night is long and full of sounds, everyone has you on edge.")
    time.sleep(a)
    print("You lie closest to the door with Joseph inbetween you and Jess.")
    time.sleep(a)
    print("He sleeps peacefully forgetting all the horror he has seen")
    time.sleep(a)
    print("for a small period of time.")
    time.sleep(a)
    print("The next day continues the same as the previous.")
    time.sleep(a)
    print("Progress being slow but quiet.")
    time.sleep(a)
    print("You are just about to stop for lunch")
    time.sleep(a)
    print("when you see an abandoned train up ahead.")
    time.sleep(a)
    print('"Do you think we can get it going" Jess asks')
    time.sleep(a)
    print('"Its definitely worth a go"')
    time.sleep(a)
    print('you reply as your steps begin to speed up to a near jog.')
    time.sleep(a)
    print("\nYou walk towards the train alone to ensure its safe. ")
    time.sleep(a)
    print("You climb into the engine cabin and are greeted")
    time.sleep(a)
    print("with the complicated console and your hope fades.")
    time.sleep(a)
    print('"How am I supposed to work out how to get this train started,')
    time.sleep(a)
    print('theres too many dials and levers I dont know where to start"')
    time.sleep(a)
    print("You stare out of the cabin window wondering if you will")
    time.sleep(a)
    print("ever catch a break. You let your guard down for a moment")
    time.sleep(a)
    print("then in the reflection you see movement")
    time.sleep(a)
    print("As you spin round the zombie dives at you")
    time.sleep(a)
    print("Do you jump back or kick out at the zombie (j or k")
    time.sleep(a)

    answer = input(">").lower().strip()
    if answer == "j":
        # take player to jump_back()
        jump_back()
    elif answer == "k":
        # take player to kick_zombie()
        kick_zombie()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either j or k.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "j":
            # take player to jump_back()
            jump_back()
        elif answer == "k":
            # take player to kick_zombie()
            kick_zombie()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def jump_back():
    print("\nYou jump back but the small confinement")
    time.sleep(a)
    print("of the engine cabin restricts your movement")
    time.sleep(a)
    print("and you can't get out of reach of the zombie.")
    time.sleep(a)
    print("It bites your neck and drags you to the ground.")
    time.sleep(a)
    print("You lie there unable to cry out for help")
    time.sleep(a)
    print("unable to break free from the zombie.")
    time.sleep(a)
    print("You did not survive the zombie outbreak")
    time.sleep(c)
    play_again()


def kick_zombie():
    print("\nYou quickly react and kick the zombie back")
    time.sleep(a)
    print("knocking it to the ground.")
    time.sleep(a)
    print("You grab a spanner by the console and repeatedly hit")
    time.sleep(a)
    print("the zombie in the head till it stops moving.")
    time.sleep(a)
    print("You search the cabin for anything that")
    time.sleep(a)
    print("could help get the engine started.")
    time.sleep(a)
    print("In a cabinet you come across a note pad.")
    time.sleep(a)
    print('It looks brand new, hardly any pages used and still stiff.')
    time.sleep(a)
    print('Amongst the notes is " first shift 17th October 21."')
    time.sleep(a)
    print("That was just 2 days before the outbreak started.")
    time.sleep(a)
    print("On the next page was a step by step guide to start the engine.")
    time.sleep(a)
    print("\nYou race back to get Jess and Joseph,")
    time.sleep(a)
    print("then start up the train following the process in the notes.")
    time.sleep(a)
    print("As you race along the tracks you look across the open fields")
    time.sleep(a)
    print("then back at your family")
    time.sleep(a)
    print("for a brief moment you allow yourself to feel safe")
    time.sleep(a)
    print("and share a smile with Jess.")
    time.sleep(a)
    print("\nYou reach an army blockade who rush you back to the refuge camp")
    time.sleep(a)
    print("Congratulations you and your family survived the zombie apocalypse")
    time.sleep(c)
    play_again()


def follow_signs():
    print("\nAgainst your better judgment you make a turn up ahead")
    time.sleep(a)
    print("following the signs promising shelter and safety.")
    time.sleep(a)
    print("You approach an old train yard with fencing all around")
    time.sleep(a)
    print("and spot someone patrolling the top of the main gate.")
    time.sleep(a)
    print("You continue warily and conceal your camping knife in your sock.")
    time.sleep(a)
    print('As you get closer the guard shouts')
    time.sleep(a)
    print('“quick there’s a hoard on the way, get inside.”')
    time.sleep(a)
    print('Panic takes over and you sprint towards the gate')
    time.sleep(a)
    print('as it begins to open.')
    time.sleep(a)
    print("You make it inside the gate and the relief begins to hit…")
    time.sleep(a)
    print("then everything goes black.")
    time.sleep(c)
    print("\nYou begin to come round")
    time.sleep(a)
    print("as they drag you into what looks like a slaughter room.")
    time.sleep(a)
    print("You see a body on a table being dismembered")
    time.sleep(a)
    print("you are placed on your knees in front of what looks like a")
    time.sleep(a)
    print("large public sink with your hands tied behind your back.")
    time.sleep(a)
    print("Jess in placed to your left along with three others.")
    time.sleep(a)
    print("You edge your knife from your sock")
    time.sleep(a)
    print("and begin to work on your constraints.")
    time.sleep(a)
    print("\nA man with a bat and another with a butcher knife begin to walk")
    time.sleep(a)
    print("towards the person furthest away from you on your left.")
    time.sleep(a)
    print("Without warning the man with the bat")
    time.sleep(a)
    print("strikes him in the back of the head")
    time.sleep(a)
    print("and the second slit his throat draining his blood into the sink.")
    time.sleep(a)
    print("They move onto the next")
    time.sleep(a)
    print("repeating the process getting closer to Jess.")
    time.sleep(a)
    print("You force yourself not to panic")
    time.sleep(a)
    print("and continue to try and cut yourself loose.")
    time.sleep(a)
    print("As the bat is about to make impact for the third time")
    time.sleep(a)
    print("there is a loud bang.The room begins to shake")
    time.sleep(a)
    print("knocking everyone to the ground")
    time.sleep(a)
    print("During the commotion you break free from your constraints")
    time.sleep(a)
    print("Do you attack the guards or free Jess (attack or free")
    time.sleep(a)

    answer = input(">").lower().strip()
    if answer == "attack":
        # take player to attack_guard()
        attack_guard()
    elif answer == "free":
        # take player to free_jess()
        free_jess()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either attack or free.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "attack":
            # take player to attack_guard()
            attack_guard()
        elif answer == "free":
            # take player to free_jess()
            free_jess()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def attack_guard():
    print("\nYou dive at the man with bat before he has a chance to react")
    time.sleep(a)
    print("and stab him in the throat")
    time.sleep(a)
    print("The other drops his knife a begs you not to hurt him. ")
    time.sleep(a)
    print('“Where is my son” you demand')
    time.sleep(a)
    print('“Hes in the other room, we haven’t touched him I swear”')
    time.sleep(a)
    print('he stutters back')
    time.sleep(a)
    print("Let him live or kill him (live or kill")
    time.sleep(a)

    answer = input(">").lower().strip()
    if answer == "live":
        # take player to let_live()
        let_live()
    elif answer == "kill":
        # take player to kill()
        kill()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either live or kill.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "live":
            # take player to let_live()
            let_live()
        elif answer == "kill":
            # take player to kill()
            kill()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def let_live():
    print("\nYou punch the guard in the face knocking him unconscious")
    time.sleep(a)
    print("You quickly free Jess and rush to get Joseph")
    time.sleep(a)
    print("He is in the next room as the guard said, unharmed surrounded")
    time.sleep(a)
    print("by butchered human bodies hung up like pigs.")
    time.sleep(a)
    print('“Who the hell are these people” jess asks in disbelief.')
    time.sleep(a)
    print('“These aren’t people” you answer in disgust.')
    time.sleep(a)
    print('You grab harry and turn to run,')
    time.sleep(a)
    print("do you leave via the main doors or down the corridor to the left")
    time.sleep(a)
    print("Main or Corridor")
    time.sleep(a)

    answer = input(">").lower().strip()
    if answer == "main":
        # take player to main_doors()
        main_doors()
    elif answer == "corridor":
        # take player to corridor()
        corridor()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either main or corridor.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "main":
            # take player to main_doors()
            main_doors()
        elif answer == "corridor":
            # take player to play_again()
            corridor()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def kill():
    print("\nYou don’t say another word")
    time.sleep(a)
    print("and thrust your knife into his stomach multiple times")
    time.sleep(a)
    print("You quickly free Jess and rush to get Joseph")
    time.sleep(a)
    print("He is in the next room as the guard said, unharmed surrounded")
    time.sleep(a)
    print("by butchered human bodies hung up like pigs.")
    time.sleep(a)
    print('“Who the hell are these people” Jess asks in disbelief.')
    time.sleep(a)
    print('“These aren’t people” you answer in disgust.')
    time.sleep(a)
    print('You grab harry and turn to run')
    time.sleep(a)
    print("do you leave via the main doors or down the corridor to the left")
    time.sleep(a)
    print("Main or Corridor")
    time.sleep(a)

    answer = input(">").lower().strip()
    if answer == "main":
        # take player to main_doors()
        main_doors()
    elif answer == "corridor":
        # take player to corridor()
        corridor()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either main or corridor.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "main":
            # take player to main_doors()
            main_doors()
        elif answer == "corridor":
            # take player to corridor()
            corridor()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def main_doors():
    print("\nYou burst through the main doors, leading to the front gate")
    time.sleep(a)
    print("straight into a hoard of zombies")
    time.sleep(a)
    print("The explosion blew a hole in the yards fences")
    time.sleep(a)
    print("allowing the hoard to enter.")
    time.sleep(a)
    print("You try and push Jess and Joseph free but to no avail")
    time.sleep(a)
    print("You did not survive the zombie outbreak")
    time.sleep(c)
    play_again()


def corridor():
    print("\nYou make your way down the corridor.")
    time.sleep(a)
    print("Occupants of the facility can be heard panicking and screaming.")
    time.sleep(a)
    print("Then you see it")
    time.sleep(a)
    print("the window looking over the main courtyard reveals")
    time.sleep(a)
    print("it has been overrun with a hoard of zombies.")
    time.sleep(a)
    print("The explosion blew a hole in the yards fences")
    time.sleep(a)
    print("allowing them to enter. ")
    time.sleep(a)
    print("You scale the back fence avoiding zombies ")
    time.sleep(a)
    print("and any other inhabitants and escape.")
    time.sleep(a)
    print('"From now on we stick to camping" you say to break the silence')
    time.sleep(c)
    print("\nThe next day continues the same as the previous.")
    time.sleep(a)
    print("Progress being slow but quiet.")
    time.sleep(a)
    print("You are just about to stop for lunch")
    time.sleep(a)
    print("when you see an abandoned train up ahead.")
    time.sleep(a)
    print('"Do you think we can get it going" Jess asks')
    time.sleep(a)
    print('"Its definitely worth a go"')
    time.sleep(a)
    print('you reply as your steps begin to speed up to a near jog.')
    time.sleep(a)
    print("\nYou walk towards the train alone to ensure its safe. ")
    time.sleep(a)
    print("You climb into the engine cabin and are greeted")
    time.sleep(a)
    print("with the complicated console and your hope fades.")
    time.sleep(a)
    print('"How am I supposed to work out how to get this train started,')
    time.sleep(a)
    print('theres too many dials and levers I dont know where to start"')
    time.sleep(a)
    print("You stare out of the cabin window wondering if you will")
    time.sleep(a)
    print("ever catch a break. You let your guard down for a moment")
    time.sleep(a)
    print("then in the reflection you see movement")
    time.sleep(a)
    print("As you spin round the zombie dives at you")
    time.sleep(a)
    print("Do you jump back or kick out at the zombie (j or k")
    time.sleep(a)

    answer = input(">").lower().strip()
    if answer == "j":
        # take player to jump_back()
        jump_back()
    elif answer == "k":
        # take player to kick_zombie()
        kick_zombie()
    else:
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either j or k.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "j":
            # take player to jump_back()
            jump_back()
        elif answer == "k":
            # take player to kick_zombie()
            kick_zombie()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


def free_jess():
    print("You rush to jess and begin cutting at her constraints.")
    time.sleep(a)
    print("Just as you manage to get her free you are a struck")
    time.sleep(a)
    print("across the back of the head with the baseball bat")
    time.sleep(a)
    print("crushing your skull.")
    time.sleep(a)
    print("You did not survive the zombie outbreak")
    time.sleep(c)
    play_again()


def stay():
    print("4 more days have past,")
    time.sleep(a)
    print("all rations used and Joseph cant stop crying due to hunger. ")
    time.sleep(a)
    print("Jess having not eaten in 3 days can barely keep awake.")
    time.sleep(a)
    print("The constant crying has attracted a large group of zombies")
    time.sleep(a)
    print("and its just a matter of time before they get in.")
    time.sleep(a)
    print("You sit there motionless staring at a camping rope")
    time.sleep(a)
    print("contemplating what choice to make next …")
    time.sleep(a)
    print()

    outcome = ['You take the rope upstairs and begin to tie the rope around' 
               ' the bannister. Bang Bang Bang. Gunshots come from outside,'
               " you rush downstairs and grap Joseph. The gunshots continue"
               " then it all falls quiet, you start to wake Jess"
               " when an officer wearing a Racoon City uniform bursts in." 
               ' \nHe helps you get Jess and Joseph into his car and '
               ' set off. "Thanks I had given up on anyone showing up" '
               'you say unable to hide your guilt '
               '"Your welcome, I was on my way to the station when I seen '
               'the crowd outside your house, today is supposed to be my '
               'first day with the RPD. My name is Leon"'
               'Congratulations you and your family '
               'survived the zombie apocalypse',
               "You did not survive the zombie outbreak"]
    
    print(random.choice(outcome))
    play_again()


def play_again():
    print("Want to try and survive the zombie outbreak again? Y or N")
    # convert the player's input to lower_case
    answer = input(">").lower().strip()
    if answer == "y":
        # take player to start()
        intro()
    elif answer == "n":
        # exit() the program
        print("Too scared to see if you would of made it?")
        print("Doubt you would of got far anyway")
        start()
    else:
        # return to start()
        # validate incorrect input
        print("\n Incorrect Answer")
        print("\n To continue playing type either y or n.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "y":
            # take player to cross_roads
            intro()
        elif answer == "n":
            # take player to play_again()
            start()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            start()


start()


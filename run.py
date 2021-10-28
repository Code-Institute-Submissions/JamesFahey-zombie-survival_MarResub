import time
import random


def start():
    print("Welcome to Zombie Survival.")
    time.sleep(2)
    print("\nYou and your family are doing what you can to survive the horror.")
    print("Can you make the right choices")
    print("to get you and your family to safety?")
    time.sleep(2)
    print("\nDo you think you have what it takes to survive? Yes or No")
    time.sleep(2)

    answer = input(">").lower().strip()
    if answer == "yes":
        print("You are ready... Good luck")
        time.sleep(3)
        intro()
    elif answer == "No":
        # take player to play_again()
        print("Too scared to see if you would of made it?")
        print("Doubt you would of got far anyway")
        play_again()
    else:
        # else return player to start()
        start()


def intro():
    # Storyline prompts
    print("\nAirports were the first to close once the outbreak started")
    time.sleep(2)
    print("soon all major motorways were barricaded off, that was a week ago")
    time.sleep(2)
    print("Satellite towers are all down.")
    time.sleep(4)
    print()

    print('\n"We were all looking forward to our camping trip')
    time.sleep(2)
    print("me and Jess wanted to do something nice with Joseph before he")
    time.sleep(2)
    print("started nursery. Glad Jess likes to be prepared, if it ")
    time.sleep(2)
    print("wasn’t for the amount of camping supplies and resources, we")
    time.sleep(2)
    print("wouldn’t of lasted this long.  But we are all but out now")
    time.sleep(2)
    print("and running out of options. With refuge camps being overrun")
    time.sleep(2)
    print("the last announcement was for survivors to remain barricaded")
    time.sleep(2)
    print("indoors and wait for rescue. Its been days")
    time.sleep(2)
    print("since the last transmission and no sign of any help.")
    time.sleep(2)
    print("Its time I need to make a choice, stay and hope for rescue")
    time.sleep(2)
    print('or leave for supplies and make it to one of the remaining camps."')
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
        print("\n To continue playing type either stay or leave.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "stay":
            # take player to cross_roads
            stay()
        elif answer == "leave":
            # take player to play_again()
            leave()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()
    
    
def leave():
    print("\nYou pack up all remaining food and supplies,")
    time.sleep(2)
    print("then wait for it to be clear outside before making your move.")
    time.sleep(2)
    print("Do you take the car which could attract nearby zombies")
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
        print("\n To continue playing type either car or back.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "car":
            # take player to cross_roads
            car()
        elif answer == "back":
            # take player to play_again()
            back()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()


def car():
    print("\nYou load the supplies into the car,")
    time.sleep(2)
    print("jess straps Joseph into his car seat.")
    time.sleep(2)
    print("Still no sign of any zombies.")
    time.sleep(2)
    print("You turn the key in the ignition, the car wont start.")
    time.sleep(2)
    print("You try again still nothing.")
    time.sleep(2)
    print("Jess begins to panic and shouts “hurry up, come on we have to go”.")
    time.sleep(2)
    print("“Im trying” you snap back. This causes joseph to cry.")
    time.sleep(2)
    print("With all the commotion you don’t see the zombies approach the car")
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
        print("\n To continue playing type either kick or crowbar.")
        print("\n To quit the game press q")
        
        answer = input(">").lower().strip()
        if answer == "kick":
            # take player to cross_roads
            kick()
        elif answer == "crowbar":
            # take player to play_again()
            crowbar()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()


def crowbar():
    print("\nYou reach under your chair,")
    time.sleep(2)
    print("frantically trying to grab your crowbar.")
    time.sleep(2)
    print("Jess and Joseph are screaming,")
    time.sleep(2)
    print("4 arms are reaching through the window pulling at you")
    time.sleep(2)
    print("Your fingers brush against the crowbar as teeth sink into your")
    time.sleep(2)
    print("neck. Jess wails in horror just as the growing group of zombies ")
    time.sleep(2)
    print("smash the passenger window...")
    time.sleep(3)
    print("\nYou did not survive the zombie outbreak")
    time.sleep(2)
    play_again()


def kick():
    print("\nThe door crashes open with the impact of your kick knocking") 
    time.sleep(2)
    print("the zombies to the ground. You try the ignition again,") 
    time.sleep(2)
    print("the engine starts and you manage to get away.") 
    time.sleep(2)
    print('\n"We have been driving for nearly 2 hours,') 
    time.sleep(2)
    print("anywhere we could stop for supplies and resources,") 
    time.sleep(2)
    print("Were overcrowded with those things, we had to keep going.") 
    time.sleep(2)
    print('Our only option now is make it to a camp') 
    time.sleep(2)
    print('and hope theres someone that can help us"') 
    time.sleep(2)
    print("\nAs you are making you way to a refuge camp") 
    time.sleep(2)
    print("you see a car in a ditch") 
    time.sleep(2)
    print("smoke coming from the bonnet and what looks to be a full boot") 
    time.sleep(2)
    print("As you stop the car, “what are you doing” jess asks.") 
    time.sleep(2)
    print("“there could be something useful in there,") 
    time.sleep(2)
    print('we need supplies” you answer.') 
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
        print("\n To continue playing type either g or k.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "g":
            # take player to cross_roads
            get_out()
        elif answer == "k":
            # take player to play_again()
            keep_going()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()


def keep_going():
    print("\nYou avoid cities to stay clear of the hoards")
    time.sleep(2)
    print("as the miles tick by and night falls.")
    time.sleep(2)
    print("Resources are low with no options to stop.")
    time.sleep(2)
    print("The car begins to chug as you use the last of the fuel")
    time.sleep(2)
    print("As jess and Joseph sleep the crowd moves in…")
    time.sleep(2)
    print("You did not survive the zombie outbreak")
    time.sleep(4)
    play_again()


def get_out():
    print("\nAs you approach the car you notice 2 bodies.")
    time.sleep(2)
    print("The driver, his head pressed against the steering wheel.")
    time.sleep(2)
    print("The passenger has gone head first through the windscreen.")
    time.sleep(2)
    print("Your attention turns to the boot off the car,")
    time.sleep(2)
    print("they have food, bottled water and more.")
    time.sleep(2)
    print("You grab as much as you can carry,")
    time.sleep(2)
    print("as you turn to head back to your car")
    time.sleep(2)
    print('"help me" the weak voice came from the driver.')
    time.sleep(2)
    print('"Please help me. Me and my wife.. Oh my god my wife"')
    time.sleep(2)
    print("You look back at your car and Joseph in the back,")
    time.sleep(2)
    print("then turn your attention back to the injured driver.")
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
        print("\n To continue playing type either help or walk.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "help":
            # take player to cross_roads
            help_driver()
        elif answer == "walk":
            # take player to play_again()
            walk_away()
        elif answer == "q":
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
    print("\nHe hasn't said much since we rescued him from the crash.")
    time.sleep(2)
    print("He's slept most of the time, probably due to the blow to the head.")
    time.sleep(2)
    print("What would you even say to someone who's just lost his wife,")
    time.sleep(2)
    print("I don't know what I would do if something")
    time.sleep(2)
    print("happened to jess or Joseph.")
    time.sleep(2)
    print("\nIt isn't long before you need the fuel the driver told you about")
    time.sleep(2)
    print("Without it you would of been stranded.")
    time.sleep(2)
    print("As you get back in the car you notice sweat pouring")
    time.sleep(2)
    print("from the driver's forehead. He has a fever.")
    time.sleep(2)
    print("You begin look him over trying to not alert jess to issue.")
    time.sleep(2)
    print("Then you see it, on his left shoulder, bite marks.")
    time.sleep(2)
    print('"I was trying to get her help before she turned"')
    time.sleep(2)
    print('the driver says panting. You jump back in shock.')
    time.sleep(2)
    print('"So thats how you ended in the ditch,')
    time.sleep(2)
    print('you should of told us you were bitten"')
    time.sleep(2)
    print('"Please. Were nearly at the camp, someone could help"')
    time.sleep(2)
    print('His voice getting weaker, his eyes closed again.')
    time.sleep(2)
    print('"You need to get out now".... He doesnt respond or move.')
    time.sleep(2)
    print('Just lies motionless in his seat.')
    time.sleep(2)
    print("You need to get him out of the car")
    time.sleep(2)
    print("do you reach across and open the door,")
    time.sleep(2)
    print("or get out and walk around. (reach or around)")
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
        print("\n To continue playing type either reach or around.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "reach":
            # take player to cross_roads
            reach_across()
        elif answer == "around":
            # take player to play_again()
            walk_around()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()


def reach_across():
    print("\nYou reach across slowly trying not to disturb the driver.")
    time.sleep(2)
    print("\You pull on the handle and push open the passenger door.")
    time.sleep(2)
    print("The drivers eyes open blood shot and yellow")
    time.sleep(2)
    print("and sinks his teeth into your arm.")
    time.sleep(2)
    print('"Arggghhh" you yell out in pain')
    time.sleep(2)
    print('and manage to push the driver back in his seat.')
    time.sleep(2)
    print("Jess grabs the crowbar from bellow your seat")
    time.sleep(2)
    print("and strikes the driver repeatedly in the head")
    time.sleep(2)
    print("until his skull bursts and the driver is dead.")
    time.sleep(4)
    print("\nNot much is said for the rest of the journey,")
    time.sleep(2)
    print("you see the camp ahead and pull over.")
    time.sleep(2)
    print("The bite on your arm is throbbing")
    time.sleep(2)
    print("tiredness is starting to take over.")
    time.sleep(2)
    print("Jess gets Joseph out of the car and you stand opposite them.")
    time.sleep(2)
    print("You give them a long hug and a kiss and say your goodbyes.")
    time.sleep(2)
    print('"Are you not coming too dad" Joseph asks confused')
    time.sleep(2)
    print('"Ill catch you up mate, I just need to grab something first "')
    time.sleep(2)
    print('you reply trying to remain strong.')
    time.sleep(2)
    print("You watch them walk up to the camp soldiers approach with guns.")
    time.sleep(2)
    print("You wait until you see them brought inside then turn and walk away")
    time.sleep(2)
    print("You didn't survive the zombie outbreak")
    print("but you did get your family to safety.")
    time.sleep(4)
    play_again()


def walk_around():
    print("\nYou do not risk reaching across the driver.")
    time.sleep(2)
    print("You get out and start walking round to the other side.")
    time.sleep(2)
    print('"Ahhhhhhh"')
    time.sleep(2)
    print("The driver lundged towards the back of the car.")
    time.sleep(2)
    print("You race to the rear door a swing it open")
    time.sleep(2)
    print('"Nooo" you cry out in anguish')
    time.sleep(4)
    print("\nAs you drive to the camp you look in the rear view mirror ")
    time.sleep(2)
    print("at the blood stained seats and an empty child seat.")
    time.sleep(2)
    print("A reminder of what you lost.")
    time.sleep(2)
    print("You arrive at the camp. Soldiers meet you,")
    time.sleep(2)
    print("and once they are satisfied you aren't bitten. Allow you to enter")
    time.sleep(2)
    print("You survived the zombie apocalypse but lost everything.")
    time.sleep(4)
    play_again()


def walk_away():
    print("\nYou turn and walk to the car not looking back.")
    time.sleep(2)
    print("You quickly load the supplies in in car and get moving.")
    time.sleep(2)
    print('"Everything OK" asks jess')
    time.sleep(2)
    print('"Everything is fine" You answer trying to hide your guilt.')
    time.sleep(2)
    print("\nYou avoid cities to stay clear of the hoards.")
    time.sleep(2)
    print("As the miles tick by and night falls.")
    time.sleep(2)
    print("Resources are low with no options to stop.")
    time.sleep(2)
    print("The car begins to chug as you use the last of the fuel")
    time.sleep(2)
    print("As Jess and Joseph sleep the crowd moves in…")
    time.sleep(2)
    print("You did not survive the zombie outbreak")
    time.sleep(4)
    play_again()


def back():
    print('\n"Progress has been slow, but at least')
    time.sleep(2)
    print('its quiet and no sign of danger.')
    time.sleep(2)
    print("It's going to be dark soon so well have to stop and set up camp.")
    time.sleep(2)
    print("There's another one of those signs promising shelter and safety,")
    time.sleep(2)
    print("it could be better than camping in the woods or by the tracks")
    time.sleep(2)
    print('but Im just not sure"')
    time.sleep(2)
    print('"Theres another one of those signs" Jess acknowledges')
    time.sleep(2)
    print('"I think we should check it out')
    time.sleep(2)
    print('its not far and we cant risk camping out here by ourselves"')
    time.sleep(2)
    print("Camp alone or follow the sign to shelter (camp or follow)")
    time.sleep(2)

    answer = input(">").lower().strip()
    if answer == "camp":
        # take player to cross_roads
        camp()
    elif answer == "follow":
        # take player to play_again()
        follow_signs()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either camp or follow.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "camp":
            # take player to cross_roads
            camp()
        elif answer == "follow":
            # take player to play_again()
            follow_signs()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()


def camp():
    print("\nThe night is long and full of sounds, everyone has you on edge.")
    time.sleep(2)
    print("You lie closest to the door with Joseph inbetween you and Jess.")
    time.sleep(2)
    print("He sleeps peacefully forgetting all the horror he has seen")
    time.sleep(2)
    print("for a small period of time.")
    time.sleep(2)
    print("The next day continues the same as the previous.")
    time.sleep(2)
    print("Progress being slow but quiet.")
    time.sleep(2)
    print("You are just about to stop for lunch")
    time.sleep(2)
    print("when you see an abandoned train up ahead.")
    time.sleep(2)
    print('"Do you think we can get it going" Jess asks')
    time.sleep(2)
    print('"Its definitely worth a go"')
    time.sleep(2)
    print('you reply as your steps begin to speed up to a near jog.')
    time.sleep(2)
    print("\nYou walk towards the train alone to ensure its safe. ")
    time.sleep(2)
    print("You climb into the engine cabin and are greeted")
    time.sleep(2)
    print("with the complicated console and your hope fades.")
    time.sleep(2)
    print('"How am I supposed to work out how to get this train started,')
    time.sleep(2)
    print('theres too many dials and levers I dont know where to start"')
    time.sleep(2)
    print("You stare out of the cabin window wondering if you will")
    time.sleep(2)
    print("ever catch a break. You let your guard down for a moment")
    time.sleep(2)
    print("then in the reflection you see movement")
    time.sleep(2)
    print("As you spin round the zombie dives at you")
    time.sleep(2)
    print("Do you jump back or kick out at the zombie (j or k")
    time.sleep(2)

    answer = input(">").lower().strip()
    if answer == "j":
        # take player to cross_roads
        jump_back()
    elif answer == "k":
        # take player to play_again()
        kick_zombie()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either j or k.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "j":
            # take player to cross_roads
            jump_back()
        elif answer == "k":
            # take player to play_again()
            kick_zombie()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()


def jump_back():
    print("\nYou jump back but the small confinement")
    time.sleep(2)
    print("of the engine cabin restricts your movement")
    time.sleep(2)
    print("and you can't get out of reach of the zombie.")
    time.sleep(2)
    print("It bites your neck and drags you to the ground.")
    time.sleep(2)
    print("You lie there unable to cry out for help")
    time.sleep(2)
    print("unable to break free from the zombie.")
    time.sleep(2)
    print("You did not survive the zombie outbreak")
    time.sleep(4)
    play_again()


def kick_zombie():
    print("\nYou quickly react and kick the zombie back")
    time.sleep(2)
    print("knocking it to the ground.")
    time.sleep(2)
    print("You grab a spanner by the console and repeatedly hit")
    time.sleep(2)
    print("the zombie in the head till it stops moving.")
    time.sleep(2)
    print("You search the cabin for anything that")
    time.sleep(2)
    print("could help get the engine started.")
    time.sleep(2)
    print("In a cabinet you come across a note pad.")
    time.sleep(2)
    print('It looks brand new, hardly any pages used and still stiff.')
    time.sleep(2)
    print('Amongst the notes is " first shift 17th October 21."')
    time.sleep(2)
    print("That was just 2 days before the outbreak started.")
    time.sleep(2)
    print("On the next page was a step by step guide to start the engine.")
    time.sleep(2)
    print("\nYou race back to get Jess and Joseph,")
    time.sleep(2)
    print("then start up the train following the process in the notes.")
    time.sleep(2)
    print("As you race along the tracks you look across the open fields")
    time.sleep(2)
    print("then back at your family")
    time.sleep(2)
    print("for a brief moment you allow yourself to feel safe")
    time.sleep(2)
    print("and share a smile with Jess.")
    time.sleep(2)
    print("\nYou reach an army blockade who rush you back to the refuge camp")
    time.sleep(2)
    print("Congratulations you and your family survived the zombie apocalypse")
    time.sleep(4)
    play_again()


def follow_signs():
    print("\nAgainst your better judgment you make a turn up ahead")
    time.sleep(2)
    print("following the signs promising shelter and safety.")
    time.sleep(2)
    print("You approach an old train yard with fencing all around")
    time.sleep(2)
    print("and spot someone patrolling the top of the main gate.")
    time.sleep(2)
    print("You continue warily and conceal your camping knife in your sock.")
    time.sleep(2)
    print('As you get closer the guard shouts')
    time.sleep(2)
    print('“quick there’s a hoard on the way, get inside.”')
    time.sleep(2)
    print('Panic takes over and you sprint towards the gate')
    time.sleep(2)
    print('as it begins to open.')
    time.sleep(2)
    print("You make it inside the gate and the relief begins to hit…")
    time.sleep(4)
    print("then everything goes black.")
    time.sleep(4)
    print("\nYou begin to come round")
    time.sleep(2)
    print("as they drag you into what looks like a slaughter room.")
    time.sleep(2)
    print("You see a body on a table being dismembered")
    time.sleep(2)
    print("you are placed on your knees in front of what looks like a")
    time.sleep(2)
    print("large public sink with your hands tied behind your back.")
    time.sleep(2)
    print("Jess in placed to your left along with three others.")
    time.sleep(2)
    print("You edge your knife from your sock")
    time.sleep(2)
    print("and begin to work on your constraints.")
    time.sleep(2)
    print("\nA man with a bat and another with a butcher knife begin to walk")
    time.sleep(2)
    print("towards the person furthest away from you on your left.")
    time.sleep(2)
    print("Without warning the man with the bat")
    time.sleep(2)
    print("strikes him in the back of the head")
    time.sleep(2)
    print("and the second slit his throat draining his blood into the sink.")
    time.sleep(2)
    print("They move onto the next")
    time.sleep(2)
    print("repeating the process getting closer to Jess.")
    time.sleep(2)
    print("You force yourself not to panic")
    time.sleep(2)
    print("and continue to try and cut yourself loose.")
    time.sleep(2)
    print("As the bat is about to make impact for the third time")
    time.sleep(2)
    print("there is a loud bang.The room begins to shake")
    time.sleep(2)
    print("knocking everyone to the ground")
    time.sleep(2)
    print("During the commotion you break free from your constraints")
    time.sleep(2)
    print("Do you attack the guards or free Jess (attack or free")
    time.sleep(2)

    answer = input(">").lower().strip()
    if answer == "attack":
        # take player to cross_roads
        attack_guard()
    elif answer == "free":
        # take player to play_again()
        free_jess()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either j or k.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "attack":
            # take player to cross_roads
            attack_guard()
        elif answer == "free":
            # take player to play_again()
            free_jess()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()


def attack_guard():
    print("\nYou dive at the man with bat before he has a chance to react")
    time.sleep(2)
    print("and stab him in the throat")
    time.sleep(2)
    print("The other drops his knife a begs you not to hurt him. ")
    time.sleep(2)
    print('“Where is my son” you demand')
    time.sleep(2)
    print('“Hes in the other room, we haven’t touched him I swear”')
    time.sleep(2)
    print('he stutters back')
    time.sleep(2)
    print("Let him live or kill him (live or kill")
    time.sleep(2)

    answer = input(">").lower().strip()
    if answer == "live":
        # take player to cross_roads
        let_live()
    elif answer == "kill":
        # take player to play_again()
        kill()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either j or k.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "live":
            # take player to cross_roads
            let_live()
        elif answer == "kill":
            # take player to play_again()
            kill()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()


def let_live():
    print("\nYou punch the guard in the face knocking him unconscious")
    time.sleep(2)
    print("You quickly free Jess and rush to get Joseph")
    time.sleep(2)
    print("He is in the next room as the guard said, unharmed surrounded")
    time.sleep(2)
    print("by butchered human bodies hung up like pigs.")
    time.sleep(2)
    print('“Who the hell are these people” jess asks in disbelief.')
    time.sleep(2)
    print('“These aren’t people” you answer in disgust.')
    time.sleep(2)
    print('You grab harry and turn to run,')
    time.sleep(2)
    print("do you leave via the main doors or down the corridor to the left")
    time.sleep(2)
    print("Main or Corridor")
    time.sleep(2)

    answer = input(">").lower().strip()
    if answer == "main":
        # take player to cross_roads
        main_doors()
    elif answer == "corridor":
        # take player to play_again()
        corridor()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either j or k.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "main":
            # take player to cross_roads
            main_doors()
        elif answer == "corridor":
            # take player to play_again()
            corridor()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()


def kill():
    print("\nYou don’t say another word")
    time.sleep(2)
    print("and thrust your knife into his stomach multiple times")
    time.sleep(2)
    print("You quickly free Jess and rush to get Joseph")
    time.sleep(2)
    print("He is in the next room as the guard said, unharmed surrounded")
    time.sleep(2)
    print("by butchered human bodies hung up like pigs.")
    time.sleep(2)
    print('“Who the hell are these people” Jess asks in disbelief.')
    time.sleep(2)
    print('“These aren’t people” you answer in disgust.')
    time.sleep(2)
    print('You grab harry and turn to run')
    time.sleep(2)
    print("do you leave via the main doors or down the corridor to the left")
    time.sleep(2)
    print("Main or Corridor")
    time.sleep(2)

    answer = input(">").lower().strip()
    if answer == "main":
        # take player to cross_roads
        main_doors()
    elif answer == "corridor":
        # take player to play_again()
        corridor()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either j or k.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "main":
            # take player to cross_roads
            main_doors()
        elif answer == "corridor":
            # take player to play_again()
            corridor()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()


def main_doors():
    print("\nYou burst through the main doors, leading to the front gate")
    time.sleep(2)
    print("straight into a hoard of zombies")
    time.sleep(2)
    print("The explosion blew a hole in the yards fences")
    time.sleep(2)
    print("allowing the hoard to enter.")
    time.sleep(2)
    print("You try and push Jess and Joseph free but to no avail")
    time.sleep(2)
    print("You did not survive the zombie outbreak")
    time.sleep(4)
    play_again()


def corridor():
    print("\nYou make your way down the corridor.")
    time.sleep(2)
    print("Occupants of the facility can be heard panicking and screaming.")
    time.sleep(2)
    print("Then you see it")
    time.sleep(2)
    print("the window looking over the main courtyard reveals")
    time.sleep(2)
    print("it has been overrun with a hoard of zombies.")
    time.sleep(2)
    print("The explosion blew a hole in the yards fences")
    time.sleep(2)
    print("allowing them to enter. ")
    time.sleep(2)
    print("You scale the back fence avoiding zombies ")
    time.sleep(2)
    print("and any other inhabitants and escape.")
    time.sleep(2)
    print('"From now on we stick to camping" you say to break the silence')
    time.sleep(4)
    print("\nThe next day continues the same as the previous.")
    time.sleep(2)
    print("Progress being slow but quiet.")
    time.sleep(2)
    print("You are just about to stop for lunch")
    time.sleep(2)
    print("when you see an abandoned train up ahead.")
    time.sleep(2)
    print('"Do you think we can get it going" Jess asks')
    time.sleep(2)
    print('"Its definitely worth a go"')
    time.sleep(2)
    print('you reply as your steps begin to speed up to a near jog.')
    time.sleep(2)
    print("\nYou walk towards the train alone to ensure its safe. ")
    time.sleep(2)
    print("You climb into the engine cabin and are greeted")
    time.sleep(2)
    print("with the complicated console and your hope fades.")
    time.sleep(2)
    print('"How am I supposed to work out how to get this train started,')
    time.sleep(2)
    print('theres too many dials and levers I dont know where to start"')
    time.sleep(2)
    print("You stare out of the cabin window wondering if you will")
    time.sleep(2)
    print("ever catch a break. You let your guard down for a moment")
    time.sleep(2)
    print("then in the reflection you see movement")
    time.sleep(2)
    print("As you spin round the zombie dives at you")
    time.sleep(2)
    print("Do you jump back or kick out at the zombie (j or k")
    time.sleep(2)

    answer = input(">").lower().strip()
    if answer == "j":
        # take player to cross_roads
        jump_back()
    elif answer == "k":
        # take player to play_again()
        kick_zombie()
    else:
        # else return player to start()
        print("\n Incorrect Answer")
        print("\n To continue playing type either j or k.")
        print("\n To quit the game press q")
        answer = input(">").lower().strip()
        if answer == "j":
            # take player to cross_roads
            jump_back()
        elif answer == "k":
            # take player to play_again()
            kick_zombie()
        elif answer == "q":
            # allow player to exit
            print("Too scared to see if you would of made it?")
            print("Doubt you would of got far anyway")
            # exit()


def free_jess():
    print("You rush to jess and begin cutting at her constraints.")
    time.sleep(2)
    print("Just as you manage to get her free you are a struck")
    time.sleep(2)
    print("across the back of the head with the baseball bat")
    time.sleep(2)
    print("crushing your skull.")
    time.sleep(2)
    print("You did not survive the zombie outbreak")
    time.sleep(4)
    play_again()


def stay():
    print("4 more days have past,")
    time.sleep(2)
    print("all rations used and Joseph cant stop crying due to hunger. ")
    time.sleep(2)
    print("Jess having not eaten in 3 days can barely keep awake.")
    time.sleep(2)
    print("The constant crying has attracted a large group of zombies")
    time.sleep(2)
    print("and its just a matter of time before they get in.")
    time.sleep(2)
    print("You sit there motionless staring at a camping rope")
    time.sleep(2)
    print("contemplating what choice to make next …")
    time.sleep(2)
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
        # exit()
    else:
        # return to start()
        start()


start()


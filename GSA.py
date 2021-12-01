import sys,time,os
os.system("cls")
print("")
print("\033[1;36;40m _______   _______   _         _______   _______  _________  _______  \n\
(  ____ \ (  ____ \ ( (    /| (  ____ \ (  ____ \ \__   __/ (  ____ \ \n\
| (    \/ | (    \/ |  \  ( | | (    \/ | (    \/    ) (    | (    \/ \n\
| |       | (__     |   \ | | | (__     | (_____     | |    | (_____  \n\
| | ____  |  __)    | (\ \) | |  __)    (_____  )    | |    (_____  ) \n\
| | \_  ) | (       | | \   | | (             ) |    | |          ) | \n\
| (___) | | (____/\ | )  \  | | (____/\ /\____) | ___) (___ /\____) | \n\
(_______) (_______/ |/    )_) (_______/ \_______) \_______/ \_______) \n\
 \n\
 _______   _______   _______   _______   _______  \n\
(  ____ \ (  ____ ) (  ___  ) (  ____ \ (  ____ \ \n\
| (    \/ | (    )| | (   ) | | (    \/ | (    \/ \n\
| (_____  | (____)| | (___) | | |       | (__     \n\
(_____  ) |  _____) |  ___  | | |       |  __)    \n\
      ) | | (       | (   ) | | |       | (       \n\
/\____) | | )       | )   ( | | (____/\ | (____/\ \n\
\_______) |/        |/     \| (_______/ (_______/ \n\
 \n\
 _______   ______              _______   _        _________            _______   _______  \n\
(  ___  ) (  __  \  |\     /| (  ____ \ ( (    /| \__   __/ |\     /| (  ____ ) (  ____ \ \n\
| (   ) | | (  \  ) | )   ( | | (    \/ |  \  ( |    ) (    | )   ( | | (    )| | (    \/ \n\
| (___) | | |   ) | | |   | | | (__     |   \ | |    | |    | |   | | | (____)| | (__     \n\
|  ___  | | |   | | ( (   ) ) |  __)    | (\ \) |    | |    | |   | | |     __) |  __)    \n\
| (   ) | | |   ) |  \ \_/ /  | (       | | \   |    | |    | |   | | | (\ (    | (       \n\
| )   ( | | (__/  )   \   /   | (____/\ | )  \  |    | |    | (___) | | ) \ \__ | (____/\ \n\
|/     \| (______/     \_/    (_______/ |/    )_)    )_(    (_______) |/   \__/ (_______/ \n\
\033[0;0m")
input("\033[1;36;40m                              Press ENTER to start... \033[0;0m")
print("")

intro_story = "The year is 2050 and colonization of other planets has begun.\n\
\n\
Earth is dying and the Human race must do whatever they can to survive. \n\
\n\
The Genesis colony ship was built so the Human race could start to colonize Mars. \n\
\n\
It is also the proof of concept for the colonization project and the newly invented cryogenic sleep pod technology. \n\
\n\
If this mission goes well Earth will build more colony ships and send them out to colonize distant planets in other solar systems. \n\
\n\
It's been 9 months and Genesis has reached Mars, but something has gone wrong... \n\
"
def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.004)
        else:
            time.sleep(0.1)

print("")
typewriter(intro_story)
print("")
input("                             Press ENTER to continue... ")
os.system("cls")
print("")
print("................................................................................ \n\
................................................................................ \n\
................................................................................ \n\
.......................@........................................................ \n\
.........................................................*((((*................. \n\
....................................................@@@(((((((((((((/........... \n\
...............#.................................&@@@@@@((((((((((////.......... \n\
...............#..............................,@@@@@@@@@@@(((((///////*......... \n\
............................................@@@@@@@@@@@@@@@@(//////////......... \n\
..........................................@@@@@@@@@@@@@@@@&&&&&////////......... \n\
........................................@@@@@@#**%%%%**@&&&&&&&&&&&///.......... \n\
......................................*@@@@@@*%%%%%%%(((,&&&&&&&&&&&&........... \n\
.....................................@@@@@@@/*%%%%%(((((,&&&&&&&&&&............. \n\
...................................@@@@@@@@@@*(%(((((((,,&&&&&&&&............... \n\
.........................((((((((@@@@@@@@@@@@@&,,,,,,,*&&&&&&&.................. \n\
......................(((((((((%@@@@@@@@@@@&&&&&&&&&&&&&&&&..................... \n\
....................((((((((((@@@@@@@@@%(&&&&&&&&&&&&&&&........................ \n\
...................(((((((((@@@@@@@@((((&&&&&&&&&&&&#........................... \n\
...........................@@@@@@@(((%&&&&&&&&&&&............................... \n\
..........................%%@@@(((/&&&&&&&&&&#((................................ \n\
.......@................*%%%%((((&&&&&&&&&/((((................................. \n\
.....................(((&&&(((###&&&&&(((((((((.....................&........... \n\
.................../((&&&((&&&##....((((((((((.................................. \n\
.................((((&&&&&&(((.......(((((((.................................... \n\
................(((&&&&((((..........((((....................................... \n\
..............((((((((((........................................................ \n\
.............(((((((*........................................................... \n\
............((((................................................................ \n\
....................................................................,@.......... \n\
................................................................................ \n\
................................................................................ \n\
................................................................................ \n\
")

print("You've been woken from cryogenic sleep. You're head is still a bit foggy.")
def players_name():
    global players_name  
    players_name = input("Do you remember your name? ")
    players_name = players_name.capitalize()
    os.system("cls")
    print(f"Well {players_name} you'd best try to work out what is going on.")


print("")
players_name()
print("")
print("You look over the other pods. The rest of the crew are still in cryogenic sleep.")
print("You can feel the movement of the ship under your feet.")
print("The ship should have made an automated landing on Mars before waking all the crew together.")
print("")
print("")
print("")
print("What would you like to do?")
print("")
print("")

print("A: Leave the room and go to the Communal Area.")
print("B: Check the status of the pods on the computer console.")
print("")

response = ""

while response != "A" or "B":
    response = input("Please choose option A or B: ").upper()
    if response.upper() == "B":
        os.system("cls")
        print("The pods are still working but the ship's A.I network seems to be malfunctioning.")
        print("")
        print("There is an emergency warning showing but the system is locked and won't show you what the emergemcy is.")
        print("")
        print("There is nothing left to do here you decide to leave the room and head to the communal area.")
        print("")
        break
    elif response.upper() == "A":
        break
    else:
        print("I'm sorry i didn't get that. Please try again.")

input("                             Press ENTER to continue... ")
os.system("cls")

print("As the door to the communal area opens it seems to trigger an audible warning from the ship's artificial intelligence")
print("")

print("\033[1;36;40m \n\
This is an automated emergency warning from G.A.I. \n\
Genesis ship engines offline. \n\
Orbit around Mars deteriorating. \n\
Genesis will be destroyed in T-minus 29 minutes and counting. \n\
Emergency crew landing pod system offline. \n\
Please reset G.A.I. to correct all malfunctioning systems. \n\
\033[0;0m")

print("")
print("")
print(f"{players_name} it looks like it's up to you reset G.A.I and save everyone!")
print("")
input("                             Press ENTER to continue... ")

os.system("cls")

print("You enter the communal area and immediately rush over to the door for the coontrol room.")
print("You try the default password but it doesn't work.")
print("Then you remember back to before launch.")
print("Captain Caldwell was reading 'Journey to the Center of the Earth'.")
print("He said 'It's this book that inspired me to join the Mars mission. I think i'll change the control room password in honour of this amazing author'.")
print("")
print("You dont remember the author's name but the Captain was reading the book in this room so it must be around here somewhere!")
print("")
print("Where do you want to search for the book?")
print("")
print("")

print("A: Look on the shelving under the central table.")
print("B: Check the Captain's personal locker.")
print("C: Search the food storage area.")
print("D: Try searching the sofas in the seating area.")
print("")

search_area = ""

while search_area != "A":
    search_area = input("Please choose option A, B, C or D: ").upper()
    if search_area == "A":
        os.system("cls")
        print("")
        print ("You find the book jammed on a shelf next to a container filled with spoons. It's right where the Captain normally sits.")
        print("")
        print ("'Journey to the Center of the Earth' by Jules Verne.")
        print("")
        print ("You hurry over to the sealed door and type in the name. The door lock LED goes green and you hear the door lock disengage.")
        print("")
        break
    elif search_area == "B":
        print("")
        print("All the personal lockers are sealed with a fingerprint code. You keep searching and hope the Captain didn't lock the book away.")
        print("")
    elif search_area == "C":
        print("You check all the cupboards and drawers just in case the book was misplaced. There's no sign of it so you keep searching.")
        print("")
    elif search_area == "D":
        print("")
        print("You check down the sides of the seating cushions. No books here so you keep searching.")
        print("")
    else:
        print("")
        print("I'm sorry i didn't get that. Please try again.")
        print("")

input("                             Press ENTER to continue... ")

os.system("cls")

print("You hurry into the control room and quickly check around for signs of damage.")
print("Everything looks OK as far as you can tell.")
print("You don't remember the A.I reset sequence but there is an emergerncy backup console built into the table in the middle of the room.")
print("Using your fingerprint you access the console and quickly find the instructions to reset the ships A.I.")
print("")
print("As the sequence needs to be entered quickly you take a careful mental note of the four steps.")
print("If you get the sequence wrong you could fry the whole server and make it unusable!")
print("")
print("The reset procedure is as follows:")
print("")
print("\033[1;32;40m \n\
Turn off server. \n\
Manually switch to reset mode. \n\
Restart the server. \n\
Reload G.A.I from backup. \033[0;0m")

print("")
print("")
input("                             Press ENTER to continue... ")

os.system("cls")

reset_procedure = []
print ("You go to the mainframe and get ready to start the reset sequence.")
print("")
print("")

print ("What process do you want to do first?")
print("")
print("A: Reload G.A.I from emergency backup.")
print("B: Restart the Server.")
print("C: Manually switch to reset mode.")
print("D: Turn off the Server.")

reset_procedure.append(input("Please choose option A, B, C or D: ").upper())

os.system("cls")

print ("What process do you want to do second?")
print("")
print("A: Reload G.A.I from emergency backup.")
print("B: Restart the Server.")
print("C: Manually switch to reset mode.")
print("D: Turn off the Server.")

reset_procedure.append(input("Please choose option A, B, C or D: ").upper())

os.system("cls")

print ("What process do you want to do third?")
print("")
print("A: Reload G.A.I from emergency backup.")
print("B: Restart the Server.")
print("C: Manually switch to reset mode.")
print("D: Turn off the Server.")

reset_procedure.append(input("Please choose option A, B, C or D: ").upper())

os.system("cls")

print ("What process do you want to do fourth?")
print("")
print("A: Reload G.A.I from emergency backup.")
print("B: Restart the Server.")
print("C: Manually switch to reset mode.")
print("D: Turn off the Server.")

reset_procedure.append(input("Please choose option A, B, C or D: ").upper())

if reset_procedure == ["D","C","B","A"]:
    print("")
    print("")
    print("You input the correct procedure and the ships computer restarts in moments.")
    print("Before long you hear the reassuring sound of G.A.I.'s voice.")

    print(f"\033[1;36;40m \n\
    Genesis Artificial Initelligence now back online. \n\
    Multiple damaged areas detecting on Genesis. \n\
    Orbit around Mars is now critical. \n\
    Genesis will crash land in T-minus 5 minutes and counting. \n\
    Emergency crew landing pod system now online. \n\
    Crew member {players_name} please return to your sleep pod and I will launch the landing pod. \n\
\033[0;0m")

    print("")
    print("")
    print("You rush back through the communal area and return to your sleep pod as fast as you can.")
    print("The pod closes and you feel yourself getting drowsy as the pod starts working.")
    print("You feel the ship jolt just before losing consciousness...")
    print("")
    print("")
    input("                             Press ENTER to continue... ")

    os.system("cls")


    print("                                                                     \n\
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\
@@@@@@@@@@@/////(((((((////////////////////////////***************@@@/#&@@@@@@@@\n\
@@@@@@@@@@@////((((((((//////////////%%%%%#/////////*************,@@@/(%@@@@@@@@\n\
@@@@@@@@@@@////(((((((///////////%%%&%,,..&&%%%/////***************@@&(%&@@@@@@@\n\
@@@@@@@@@@@////(((((((/////////%%&*@&%,,,...  &%%///***************@@@(%&@@@@@@@\n\
@@@@@@@@@@@////(((((((////////%&*@@/**,,,...   &%%//,*************,@@@/#&@@@@@@@\n\
@@@@@@@@@@@////(((((((///////%%&,,,,,,,.....    &%//***************@@@/#&@@@@@@@\n\
@@@@@@@@@@&////(((((((////////%&.#........     %%%///**************@@@/#%@@@@@@@\n\
@@@@@@@@@@&////(((((((/////////%&(....        &%%////**************@@@/#%@@@@@@@\n\
@@@@@@@@@@@////((((((((/////////%%&&&      &&%%//////,*************@@@/#%@@@@@@@\n\
@@@@@@@@@@@////((((((((/////////////%%%%%%%//////////*************,@@@/#&@@@@@@@\n\
@@@@@@@@@@@/////(((((((//////////////////////////////*************&@@/(%&@@@@@@@\n\
@@@@@@@@@@@/////(((((((//////////%%%%&&&@&&%%%(//////************,@@@/(%&@@@@@@@\n\
@@@@@@@@@@@@////(((((((////////%%&**&%#/,... #%%%////*************@@@/#%@@@@@@@@\n\
@@@@@@@@@@@@/////(((((((//////%%%*@@**,,,...   &%%///,************@@@(#&@@@@@@@@\n\
@@@@@@@@@@@@/////(((((((/////%%&,@%,,,,,....    &%///************#@@/(%&@@@@@@@@\n\
@@@@@@@@@@@@/////(((((((//////%&.%,.......      &%///,***********@@@/(%&@@@@@@@@\n\
@@@@@@@@@@@@@/////((((((//////%%&./....       *&%////************@@@/#%@@@@@@@@@\n\
@@@@@@@@@@@@@/////(((((((///////%%&&        &&%%/////***********/@@%(#&@@@@@@@@@\n\
@@@@@@@@@@@@@//////((((((//////////%%%%%%%%%(////////***********@@@/(%&@@@@@@@@@\n\
@@@@@@@@@@@@@@*////((((((///////////////////////////************@@@@@#@@@@@@@@@@\n\
@@@@@@@@&&&&&%#**,//((((((////////&&&&&&%%#/////////*********,,%&&&&&@@@(%@@@@@@\n\
@@@@@@@&&&&&&##,****((((((///////&&&&&&&&%%##///////,****,,,,,##&&&&&&@@@(%@@@@@\n\
@@@@@@@&&@&&&%##,****(((((//////&&@&&&&&&%%%##//////****,,,,,,#%&&&@&&@@@/#&@@@@\n\
@@@@@@&&@@&&&%##,****(((((/////&&&&&&&&&&%%%###////*,,,,,,,,,##%&&&@@&&@@@(%@@@@\n\
@@@@@@&&@&&&&%%##*****(((((***#&&@&&&&&&&&%%%###***,,,,,,,,,*#%%&&&&@&&@@@/#&@@@\n\
@@@@@@&@@&&&&%%###****(((((**,&&@@&&&&&&&&%%%###***,,,,,,,,,##%%&&&&@@&@@@/(%@@@\n\
@@@@@&&@@&&&&%%%###,**(((((,*(&&@@&&&&&&&&%%%%###*,,,,,,,,,##%%%&&&&@@&&@@@(%&@@\n\
@@@@@&@@@&&&%%%%%###***((((/*&&@@@&&&&&&&&&%%%###*,,,,,,,,##%%%%&&&&@@@&@@@/#&@@\n\
@@@@@&@@@&&&%%%%%%###******,,&&@@&&&&&&####((((((*,,,,,,,#%%%%%%%&&&@@@&@@@/(%@@\n\
@@@@&@@@@&&&%%%%%%%%%#@@@@@@&&@@@&&&&&&####(((((((@@@@@#%%%%%%%%%&&&@@@&&@@@(%&@\n\
@@@@&@@@@&&&%%%%%%%%%%@@@@@@&&@@@&&&&&&####(((((((@@@@@%%%%%%%%%%&&&@@@@&@@@/#&@\n\
@@@&&&&&&&&&%%%%%%%%%%@@@@@&&@@@@&&&&&&#####(%%%###@@@&%%%%%%%%%%&&&&&&&&@@@/(%&\n\
@@@,,,,,&&&&%%%%%%%/,,(@@@@&&&@@@&&&&&&&&&&&%%%%###@@@,,,(%%%%%%%&&&&,,,,(@@((%&\n\
@@@,*****,,,,,,,,,,,,,*@@@@,,,*&&&&&&&&&&&&&%%*,...@@@,.,,,,,,,,,,,,*****/@@#(%&\n\
@@@@@@@@,,,,,,,,,.@@@@@@@@@,,****,,,,,,,,,,,,,,,...@@@@@@@@.,,,,,,,,,@@@@@@@/(%&\n\
@@@@#/@@@@@@@@@@@@@@//((#@@@@@@,,,,,,,,,,,,,,,,@@@@@@//(/@@@@@@@@@@@@@@//((#%%&@\n\
@@@@@@@@@&%%%###%%%%%&&&@@@@(%@@@@@@@@@@@@@@@@@@&//(##%&&@@@&%%%%##%%%%%&&&@@@@@\n\
")
    print("")
    print("You wake up again with no idea how long you were asleep.")
    print("You look around the room and see the other sleep pods opening and the rest of the crew waking up.")
    print("As you leave your pod you check the nearest viewport.")
    print("Red dust is settling down on a very red and rocky planet.")
    print("")
    print("")
    print("              CONGRATULATIONS YOU HAVE WON!")
    print("")
    print("")
else:
    os.system("cls")
    print("You run the procedure and wait....")
    print("Nothing seems to happen.")
    print("You try the procedure again but it doesn't work.")
    print("You hear a crackling sound and start to smell the first signs of an electrical fire.")
    print("")
    print("")
    print("It looks like you entered the wrong procedure and fried the computer.")
    print("")
    print("")
    input("                             Press ENTER to continue... ")

    os.system("cls")
    print("\033[1;31;40m    \n\
                                                                                                    \n\
               ,///////////*       ////////////     /////       .////.  /////////////////           \n\
             **///       ///**   **//*      .///**  /////**,  **/////.  /////                       \n\
             /////              .////,       /////  ////////*////////.  /////                       \n\
             /////  */////////  .////,       /////  /////  .//  ,////.  //////////////,             \n\
             /////       /////  ./////////////////  /////       ,////.  /////                       \n\
             /////       /////  .////,       /////  /////       ,////.  /////                       \n\
               *////////////    .////,       /////  /////       ,////.  /////////////////           \n\
                                                                                                    \n\
                                                                                              ///// \n\
     .////////////     /////       /////  *////////////////*  ///////////////              ,/////// \n\
   /////       *////   /////       /////  *////               /////       /////            ,/////// \n\
   /////       *////   /////       /////  *////               /////       *////          ///////.   \n\
   /////       *////   /////       /////  *//////////////     /////       /////          /////      \n\
   /////       *////     /////  .////,    *////               ///////////////                       \n\
   /////       ,////        ///////       *////               /////     /////       /////           \n\
     .////////////            //*         *///////////////**  /////       *////     /****           \n\
                                                                                                    \n\
                                                                                                    \n\
    \033[0;0m")
    print("                               SORRY, YOU HAVE LOST THE GAME.")
    print("")
    print("")
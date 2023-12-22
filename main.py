import random
import sys


"""
A christmas text adventure game made for the English language support center.
"""

SANTA_IMAGE = """
                               ..,,,,,,,,,,,,,,,,.. 
                        ..,,;;;;;;;;;;;;;;;;;;;;;;;;;;,,. 
                    .,::::;;;;aaaaaaaaaaaaaaaaaaaaaaaaaaa;;,,. 
                .,;;,:::a@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@a, 
              ,;;;;.,a@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@a 
           ,;;;;%;.,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@a, 
        ,;%;;;;%%;,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
     ,;;%%;;;;;%%;;@@@@@@@@@@@@@@'%v%v%v%v%v%v%v%v%v%v%v%v`@@@@@@@@@ 
   ,;;%%;;;;:;;;%;;@@@@@@@@@'%vvvvvvvvvnnnnnnnnnnnnnnnnvvvvvv%`@@@@' 
  ,;%%;;;;;:;;;;;;;;@@@@@'%vvva@@@@@@@@avvnnnnnnnnnnvva@@@@@@@OOov, 
 ,;%;;;;;;:::;;;;;;;@@'OO%vva@@@@@@@@@@@@vvnnnnnnnnvv@@@@@@@@@@@Oov 
 ;%;;;;;;;:::;;;;;;;;'oO%vvn@@%nvvvvvvvv%nnnnnnnnnnnnn%vvvvvvnn%@Ov 
 ;;;;;;;;;:::;;;;;;::;oO%vvnnnn>>nn.   `nnnnnnnnnnnn>>nn.   `nnnvv' 
 ;;;;;;;;;:::;;;;;;::;oO%vvnnvvmmmmmmmmmmvvvnnnnnn;%mmmmmmmmmmmmvv, 
 ;;;;;;;;;:::;;;;;;::;oO%vvmmmmmmmmmmmmmmmmmvvnnnv;%mmmmmmmmmmmmmmmv, 
 ;;;;;;;;;;:;;;;;;::;;oO%vmmmmnnnnnnnnnnnnmmvvnnnvmm;%vvnnnnnnnnnmmmv 
  `;%;;;;;;;:;;;;::;;o@@%vvmmnnnnnnnnnnnvnnnnnnnnnnmmm;%vvvnnnnnnmmmv 
   `;;%%;;;;;:;;;::;.oO@@%vmmnnnnnnnnnvv%;nnnnnnnnnmmm;%vvvnnnnnnmmv' 
     `;;;%%;;;:;;;::;.o@@%vvnnnnnnnnnnnvv%;nnnnnnnmm;%vvvnnnnnnnv%'@a. 
      a`;;;%%;;:;;;::;.o@@%vvvvvvvvvvvvvaa@@@@@@@@@@@@aa%%vvvvv%%@@@@o. 
     .@@o`;;;%;;;;;;::;,o@@@%vvvvvvva@@@@@@@@@@@@@@@@@@@@@avvvva@@@@@%O, 
    .@@@@@Oo`;;;;;;;;::;o@@@@@@@@@@@@@@@@@@@@"""""""@@@@@@@@@@@@@@@@@OO@a 
  .@@@@@@@@@OOo`;;;;;;:;o@@@@@@@@@@@@@@@@"           "@@@@@@@@@@@@@@oOO@@@, 
 .@@@@o@@@@@@@OOo`;;;;:;o,@@@@@@@@@@%vvvvvvvvvvvvvvvvvv%%@@@@@@@@@oOOO@@@@@, 
 @@@@o@@@@@@@@@OOo;::;'oOOooooooooOOOo%vvvvvvvvvvvvvv%oOOooooooooOOO@@@O@@@, 
 @@@oO@@@@@@@@@OOa@@@@@a,oOOOOOOOOOOOOOOoooooooooooooOOOOOOOOOOOOOO@@@@Oo@@@ 
 @@@oO@@@@@@@OOa@@@@@@@@Oo,oO@@@@@@@@@@OOOOOOOOOOOOOO@@@@@@@@@@@@@@@@@@Oo@@@ 
 @@@oO@@@@@@OO@@@@@@@@@@@OO,oO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Oo@@@ 
 @@@@o@@@@@@OO@@@@@@@@@@OOO,oO@@@@@@@@@O@@@@@@@@@@@@@@@@@@@@@o@@@@@@@@@O@@@@ 
 @@@@@o@@@@@OOo@@@@@@@OOOO'oOO@@@@@@@@Oo@@@@@@@@@@@@O@@@@@@@@Oo@@@@@@@@@@@@a 
`@@@@@@@O@@@OOOo`OOOOOOO'oOO@@@@@@@@@O@@@@@@@@@@@@@@@O@@@@@@@@Oo@@@@@@@@@@@@ 
 `@@@@@OO@@@@@OOOooooooooOO@@@@@@@@@@@@@@@@@@@@@@@@@@Oo@@@@@@@Oo@@@@@@oO@@@@ 
   `@@@OO@@@@@@@@@@@@@@@@@@@O@@@@@@@@@@@@@@@@@@@@@@@@Oo@@@@@@@O@@@@@@@oO@@@' 
      `@@`O@@@@@@@@@@@@@@@@@@@Oo@@@@@@@@@@@@@@@@@@@@@@Oo@@@@@@@@@@@@@@@O@@@' 
        `@ @@@@@@@@@@@@@@@@@@@OOo@@@@@@@@@@@@@@@@@@@@@O@@@@@@@@@@@@@@@'@@' 
           `@@@@@@@@@@@@@@@@@@OOo@@@@@@@@@@@@@@@@@@@@O@@@@@@@@@@@@@@@ a' 
               `@@@@@@@@@@@@@@OOo@@@@@@@@@@@@@@@@@@@@@@@@Oo@@@@@@@@' 
                  `@@@@@@@@@@@Oo@@@@@@@@@@@@@@@@@@@@@@@@@Oo@@@@' 
                      `@@@@@@Oo@@@@O@@@@@@@@@@@@@@@@@@@'o@@' 
                          `@@@@@@@@oO@@@@@@@@@@@@@@@@@ a' 
                              `@@@@@oO@@@@@@@@@@@@@@' ' 
                                '@@@o'`@@@@@@@@' 
                                 @'   .@@@@' 
                                     @@' 
                                   @'
"""

TITLE = """
|\ |  _.      _  |_ _|_       |  o  _ _|_
| \| (_| |_| (_| | | |_ \/    |_ | _>  |_
              _|        /
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
"""

BACKGROUND = [
    "Because of SDGs and inflation, coal is very expensive.",
    "So expensive, infact, Santa can no longer give coal to naughty childern.",
    "Santa has gone crazy from having to deliver to 2 billion childern every year",
    "All naughty childern are now on his 'Kill List'."
    "--------------------------------------------",
    "--------------------------------------------",
    "(press enter to continue)"
]

LOCATIONS = {
    # The locations of your head / body
    "beginning": "You open your eyes. Your head is pounding. You realize you are lying on the floor.",
    "brother": "You remember your brother stole his best friend's Nintendo Switch this year, to play Super Mario Wonder",
    "floor": "You see a pool of dark liquid. The room is almost pitch black, but the christmas tree's lights behind you makes a bit of light.",
    "room": "The room is dark. There are carefully wrapped presents under the christmas tree. Next to the tree is a table with a glass of milk and a plate of cookies."
}

ACTIONS = {
    "look": "You take a look around",
    "open": {"inventory": "You open your inventory", "present": "You open a present."},
    "drink-milk": "You drink the milk. The sweet comforting liquid fills your mouth. Your hands begin to steady.",
    "eat-cookies": "You eat the cookies. The sugary goodness tickles your tongue. Your hands begin to steady",
    "stand": "You stand up. Your head is spinning.",
    "recall": "You try to remember the meaning for ",
    "shoot": "You aim and shoot your gun at the man in red.",
    "load": "You load the gun.",
    "forgot": "You can't remember the meaning for ",
}

SANTA = [
    "You hear footsteps above you. Someone is upstares wearing heavy boots.",
    "The footsteps above you are getting louder.",
    "You hear a door opening on the second floor.",
    "You hear footsteps near the top of the stairs.",
    "You hear lound footsteps taking a step down the stairs.",
    "You hear another loud footstep as someone is coming down the stairs." ,
    "You hear another loud step. You see two large black boot at the top of the stairs.",
    "You hear another loud step. You see two large boot and red pants.",
    "You hear another loud step. You see two large boot, red pants, and a black belt.",
    "You hear a few more loud steps. You see two large boot, red pants, a black belt, and a red jacket.",
    "You hear the foot steps behind you."
]
 
SANTA_DEAD = "You've killed Santa... but where is your brother?"
SANTA_KILLS = "You fall to the floor. The loud footsteps get quieter and quieter, as your vision goes black."

WORD_DEFINITIONS = {
    "pounding": "(v) an 'on'/'off' sound or pain. Think of a someone making something with a hammer.",
    "realize": "(v) to become aware. For example, people are laughing at you and you don't know why. You realize you are not wearing pants!",
    "comforting": "(adj) make you feel calmer and less worried",
    "pitch-black": "(ex) very very dark. You can't see anything.",
    "spinning": "(v) going around and around; dizzy",
    "steady": "(v) moving less; to make something move less; to hold something still",
    "footstep": "(n) the sound when someone is walking",
    "footsteps": "(n) the sound when someone is walking",
    "vision": "(n) your ability to see with your eyes",
    "stairs": "(n) something you walk up or down to get to another floor",
    "tickles": "(v) a sometimes good, sometimes bad feeling when something touches you. Think of a feather under your nose.",
    "feather": "(n) a very light part of a bird's wing",
    "glimmer": "(v) reflect light in a pleasant way; shinny.",
    "useful": "(adj) something that you can use for some kind of benifit.",
    "lifeless": "(adj) another word for dead.",
    "handgun": "(n) a small gun you can use with one hand.",
    "soulless": "(adj) no soul and no emotions.",
    "massager": "(n) a device used to relax muscles...",
    "step": "(n/v) one level of a staircase; move your foot forward once",
    "bit": "(n) a very small amount of something.",
}

PRESENTS = {
    "teddy_bear": "It's a teddy bear. You feel it's fluffy fur, as it stares back at you with soulless eyes",
    "hair_dryer": "It's a hairdryer. It's pink and wireless. Amazing technology, but not very useful right now.",
    "toothbrush": "It's a toothbrush. It's soft bristles are not very useful right now.",
    "gun": "It's a Beretta 3032 Tomcat handgun. It's small, but looks useful.",
    "bullets": "It's full of bullets. They glimmer in the dim light, lifeless.",
    "coffee_maker": "It's a coffee maker. My father would love this, but he's sleeping right now?",
    "dog_toy": "It's a dog toy... but we don't have a dog",
    "massager": "It's a massager. The batteries are dead, but I'm sure it's very relaxing."
}

STATE = {
    "lying": True,
    "standing": False,
}

gun_state = {
    "have": False,
    "loaded": False
}

santa_state = {
    "alive": True,
}

inventory = {}
santa_counter = 0
nervousness = 0

def ask_to_play_again():
    answer = ""
    while answer != "yes" or answer != "no":
        answer = input("Would you like to play again?\nYes or No\n").lower()
    return answer

def remember(word):
    if word in WORD_DEFINITIONS.keys():
        print(ACTIONS["recall"] + f"'{word}'" + "... " + WORD_DEFINITIONS[word])
    else:
        print(ACTIONS["forgot"] + f"'{word}'.")


def introduce():
    for i in BACKGROUND:
        print(i)


def open_and_add(command):
    # TODO: Refactor me please
    item = command[1].lower()
    open_message = ACTIONS["open"][item]
    if item == "inventory":
        print(open_message)
        print("------------------")
        for key, val in inventory.items():
            print(f"> {key}")
        print("------------------")
        print("\n")
    elif item == "present":
        random_present_name = random.choice(list(PRESENTS.keys()))
        random_present_message = PRESENTS[random_present_name]
        print("\n")
        print(open_message)
        print(random_present_message)
        match random_present_name:
            case "teddy_bear":
                print("\nYou put the teddy bear in your inventory.\n")
                inventory[random_present_name] = random_present_message
                del PRESENTS[random_present_name]
                return
            case "hair_dryer":
                print("\nYou put the hair dryer in your inventory.\n")
                inventory[random_present_name] = random_present_message
                del PRESENTS[random_present_name]
                return
            case "dog_toy":
                print("\nYou put the dog toy in your inventory.\n")
                inventory[random_present_name] = random_present_message
                del PRESENTS[random_present_name]
                return
            case "coffee_maker":
                print("\nYou put the coffee maker in your inventory.\n")
                inventory[random_present_name] = random_present_message
                del PRESENTS[random_present_name]
                return
            case "gun":
                print(f"\nYou put the {random_present_name} in your inventory.\n")
                inventory[random_present_name] = random_present_message
                gun_state["have"] = True
                del PRESENTS[random_present_name]
                return

        print(f"\nYou put the {random_present_name} in your inventory.\n")
        inventory[random_present_name] = random_present_message
        del PRESENTS[random_present_name]
        

def load_gun():
    if gun_state["have"]:
        if "bullets" in inventory.keys():
            print(ACTIONS["load"])
            gun_state["loaded"] = True
        else:
            print("You don't have any bullets")
    else:
        print("You don't have a gun")
    

def shoot_gun():
    if gun_state["loaded"]:
        print(ACTIONS["shoot"])
        santa_state["alive"] = False
    else: 
        print("Shoot with what?")


while True:
    print(SANTA_IMAGE)
    print(TITLE)
    introduce()
    _ = input()  # Pause before start of game
    print(LOCATIONS["beginning"], LOCATIONS["brother"])
    while True:
        player_command = input().strip().split()
        print("\n")
        try:
            match player_command[0]:
                case "look":
                    print(ACTIONS["look"])
                    if STATE["lying"]:
                        print("You are lying on the floor")
                        print(LOCATIONS["floor"])
                    elif STATE["standing"]:
                        print(LOCATIONS["room"])
                case "open":
                    open_and_add(player_command)
                case "drink":
                    print(ACTIONS["drink-milk"])
                case "eat":
                    print(ACTIONS["eat-cookies"])
                case "stand":
                    print(ACTIONS["stand"])
                    STATE["lying"] = False
                    STATE["standing"] = True
                case "recall":
                    remember(player_command[1])
                case "help":
                    possible_actions_list = list(ACTIONS.keys())
                    possible_actions_list.pop()
                    print("\n")
                    for i in possible_actions_list:
                        if i == "open":
                            print("open present")
                            print("open inventory")
                            continue
                        elif i == "drink-milk":
                            print("drink")
                            continue
                        elif i == "eat-cookies":
                            print("eat")
                            continue
                        print(i)
                    print("\n")
                    continue
                case "load":
                    load_gun()
                case "shoot":
                    shoot_gun()
                case _:
                    print("\n")
                    print("You do nothing.")
        except:
            print("You do nothing")
            print("(Type 'help' for commands.)")

        santa_counter += 1

        if santa_state["alive"] is False:
            print(SANTA_DEAD)
        elif santa_counter == len(SANTA):
            print(SANTA_KILLS)
            break
        else:
            print(SANTA[santa_counter])
            continue
        break
    break






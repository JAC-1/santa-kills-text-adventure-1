import random
import text


"""
A christmas text adventure game made for the English language support center.
"""


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
    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() in ['yes', 'no']:
            return play_again.lower() == 'yes'
        print("Please enter 'yes' or 'no'.")


def remember(word):
    if word in text.WORD_DEFINITIONS.keys():
        print(text.ACTIONS["remember"] + f"'{word}'" + "... " + text.WORD_DEFINITIONS[word])
    else:
        print(text.ACTIONS["forgot"] + f"'{word}'.")


def introduce():
    for i in text.BACKGROUND:
        print(i)

def open_present():
    pass

def open_and_add(command):
    # TODO: Refactor me please
    item = command[1].lower()
    open_message = text.ACTIONS["open"][item]
    if item == "inventory":
        print(open_message)
        print("------------------")
        for key, val in inventory.items():
            print(f"> {key}")
        print("------------------")
        print("\n")
    elif item == "present":
        random_present_name = random.choice(list(text.PRESENTS.keys()))
        random_present_message = text.PRESENTS[random_present_name]
        print("\n")
        print(open_message)
        print(random_present_message)
        match random_present_name:
            case "teddy_bear":
                print("\nYou put the teddy bear in your inventory.\n")
                inventory[random_present_name] = random_present_message
                del text.PRESENTS[random_present_name]
                return
            case "hair_dryer":
                print("\nYou put the hair dryer in your inventory.\n")
                inventory[random_present_name] = random_present_message
                del text.PRESENTS[random_present_name]
                return
            case "dog_toy":
                print("\nYou put the dog toy in your inventory.\n")
                inventory[random_present_name] = random_present_message
                del text.PRESENTS[random_present_name]
                return
            case "coffee_maker":
                print("\nYou put the coffee maker in your inventory.\n")
                inventory[random_present_name] = random_present_message
                del text.PRESENTS[random_present_name]
                return
            case "gun":
                print(f"\nYou put the {random_present_name} in your inventory.\n")
                inventory[random_present_name] = random_present_message
                gun_state["have"] = True
                del text.PRESENTS[random_present_name]
                return

        print(f"\nYou put the {random_present_name} in your inventory.\n")
        inventory[random_present_name] = random_present_message
        del text.PRESENTS[random_present_name]
        

def load_gun():
    if gun_state["have"]:
        if "bullets" in inventory.keys():
            print(text.ACTIONS["load"])
            gun_state["loaded"] = True
        else:
            print("You don't have any bullets")
    else:
        print("You don't have a gun")
    

def shoot_gun():
    if gun_state["loaded"]:
        print(text.ACTIONS["shoot"])
        santa_state["alive"] = False
    elif gun_state["have"] and gun_state["loaded"] is False:
        print("You can't shoot an empty gun")
    else:
        print("You don't have a gun, or something to shoot with.")


while True:
    print(text.SANTA_IMAGE)
    print(text.TITLE)
    introduce()
    _ = input()  # Pause before start of game
    print(text.LOCATIONS["beginning"], text.LOCATIONS["brother"])
    while True:
        player_command = input().strip().split()
        print("\n")
        try:
            match player_command[0]:
                case "look":
                    print(text.ACTIONS["look"])
                    if STATE["lying"]:
                        print("You are lying on the floor")
                        print(text.LOCATIONS["floor"])
                    elif STATE["standing"]:
                        print(text.text.LOCATIONS["room"])
                case "open":
                    open_and_add(player_command)
                case "drink":
                    print(text.ACTIONS["drink-milk"])
                case "eat":
                    print(text.ACTIONS["eat-cookies"])
                case "stand":
                    print(text.ACTIONS["stand"])
                    STATE["lying"] = False
                    STATE["standing"] = True
                case "remember":
                    remember(player_command[1])
                    continue
                case "help":
                    possible_actions_list = list(text.ACTIONS.keys())
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
                        elif i == "remember":
                            print("remember <word you don't know> (eg. remember steady)")
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
            print(text.SANTA_DEAD)
        elif santa_counter == len(text.SANTA):
            print(text.SANTA_KILLS)
            break
        else:
            print(text.SANTA[santa_counter])
            continue
        break
    if ask_to_play_again():
        santa_counter = 0
        continue
    else:
        break


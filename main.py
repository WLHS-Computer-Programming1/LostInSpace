'''
Name: Brandon Smith
Date: 10/3/24
Description: This is a text adventure game called Lost in Space about someone who crash lands on a planet
and tries to find their way around the planet.
'''
import random
import time # for slow scrolling

def print_intro_text():
    # raw text needed for ASCII art, use r in front of '''
    intro_art = r'''
    
                         `. ___
                        __,' __`.                _..----....____
            __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
      _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
    ,'________________                          \`-._`-','
     `._              ```````````------...___   '-.._'-:
        ```--.._      ,.                     ````--...__\-.
                `.--. `-`                       ____    |  |`
                  `. `.                       ,'`````.  ;  ;`
                    `._`.        __________   `.      \'__/`
                       `-:._____/______/___/____`.     \  `
                                   |       `._    `.    \
                                   `._________`-.   `.   `.___
                                                 SSt  `------'`
    '''
    
    print("Welcome to Lost in Space.....")
    # could I slowly scroll an empty screen until the ship appears?
    for i in range(10):
        print(".")
        time.sleep(0.5)
    print(intro_art)

def print_player_status(player_info:dict)->None
    print(f"Your current health is {player_info['health']}")
def crash_landing_scene():
    initial_health = random.randint(50,90)
    player_info = {
        'name':'hal',
        'health': initial_health,
        'inventory':[]
    }
    print("You feel foggy as you slowly wake up to the sound of alarms and the smell of smoke.")
    print("You look down at your suit and see that your name is ")
    print("(Enter your name)")
    player_name = input("> ")
    player_info['name'] = player_name
    print(f"Checking your vitals, you see that your overall health is at {player_info['health']}%")
    print(f"You look around and realize you have crashed on an unknown planet. Stepping outside, you "
          f"see a damaged escape pod, what looks like a signal tower in distance, and a forest.")
    choice_one(player_info)


def choice_one(player_info):
    print(f"Do you\n1) Explore your damaged ship more"
          f"\n2)Investigate the signal tower"
          f"\n3)Examine the damaged pod"
          f"\n4)Enter the forest")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            explore_ship(player_info)
        elif player_choice == 2:
            signal_tower_encounter(player_info)
        elif player_choice == 3:
            damaged_pod_encounter(player_info)
        elif player_choice == 4:
            forest_encounter(player_info)
        else:
            print("Invalid choice")
            continue

def choice_two(player_info:dict)->None:
    print(f"Do you\n1) Go back to the ship"
          f"\n2)Go to the Deserted Settlement"
          f"\n3)Go to Dark Valley")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            explore_ship(player_info)
        elif player_choice == 2:
            deserted_settlement(player_info)
        elif player_choice == 3:
            dark_valley(player_info)
        else:
            print("Invalid choice")
            continue

def choice_three(player_info):
    print(f"Do you\n1) Go back to the ship"
          f"\n2)Explore the Glowing Lake that you see in the distance"
          f"\n3)Approach a nearby alien shrine"
          f"\n4)Explore a promising looking cave")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            explore_ship(player_info)
        elif player_choice == 2:
            glowing_lake(player_info)
        elif player_choice == 3:
            alien_shrine(player_info)
        elif player_choice == 4:
            cave_encounter(player_info)
        else:
            print("Invalid choice")
            continue

def explore_ship(player_info):
    print("You explore your wrecked ship, looking for anything useful")
    for i in range(10):
        print(".")
        time.sleep(0.2)
    print("You find a full survival kit and your health has been replenished.")
    player_info["health"] = 100
    choice_one(player_info)


def signal_tower_encounter(player_info):
    health_drop = random.randint(10,30)
    print("After a long journey, you enter the signal tower.You feel tired and your health has suffered."
          f"You look at your vitals and see your health has dropped {health_drop}%"
          "Inside the signal tower, you see a device"
          "that looks like an electronic book.")
    print("You have basic repair supplies with you and you attempt to repair the device.")
    while True:
        chance_to_repair = random.randint(0,9)
        if chance_to_repair in [0,1,2,3]:
            print("After taking the device apart and analyzing it, you turn a few screws, fix a few wires...")
            for i in range(5):
                time.sleep(0.4)
            print("You flip the switch and the device lights up")
        else:
            print("After taking the device apart and analyzing it, you turn a few screws, fix a few wires...")
            for i in range(5):
                time.sleep(0.4)
            print("When you flip the switch, nothing happens")
        print("On the screen, you see the name of two locations and their coordinates")
        print(f"Deserted Settlement: -54.21,48.23\nDark Valley: 65.48,-23.56")
        choice_two(player_info)


def damaged_pod_encounter(player_info):
    if 'key' in player_info['inventory']:
        print("Come back to this")
    else:
        print("The door to the pod won't open and it looks like it needs a key.")
        choice_one(player_info)

def forest_encounter(player_info):
    print("A short journey takes you what you can only describe as a forest, although the "
          "trees are not like anything you have seen on Earth")
    choice_three()

def glowing_lake(player_info):
    print("The glowing lake looks both eery and peaceful at the same time")
    for i in range(10):
        time.sleep(0.2)
    event_chance1 = random.randint(0,9)
    if player_info['health'] != 100:
        if event_chance1 in [0,1]:
            print("After touching the surface of the water, you feel renewed and refreshed")
            player_info['health'] = 100
            choice_three(player_info)
        if event_chance1 in [2,6]:
            print("After touching the surface of the water, you feel disoriented and fall down.")
            print("You hear voices and chaos and see groups of people running into a cave.")
            choice_three(player_info)
        elif event_chance1 in [7,9]:
            print("After touching the surface of the water, you feel disoriented and fall down.")
            print("A voice emanates from the water and says...")
            print(f"The deeper you go, the darker it gets—not just around you, but within.\n"
                  "Some paths are meant to remain untouched,\n"
                  "for what lies beyond might never let you leave…")
            choice_three(player_info)
    else:
        if event_chance1 in [0,4]:
            print("After touching the surface of the water, you feel disoriented and fall down.")
            print("You hear voices and chaos and see groups of people running into a cave.")
            choice_three(player_info)
        elif event_chance1 in [6,9]:
            print("After touching the surface of the water, you feel disoriented and fall down.")
            print("A voice emanates from the water and says...")
            print(f"The deeper you go, the darker it gets—not just around you, but within.\n"
                  "Some paths are meant to remain untouched,\n"
                  "for what lies beyond might never let you leave…")
            choice_three(player_info)

def deserted_settlement(player_info):
    pass

def dark_valley(player_info):
    pass

def main():
    print_intro_text()
    crash_landing_scene()

if __name__ == '__main__':
    main()






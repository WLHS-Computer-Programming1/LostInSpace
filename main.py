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

def crash_landing_scene():
    initial_health = random.randint(50,90)
    player_info = {
        'name':'hal',
        'health': initial_health
    }
    print("You feel foggy as you slowly wake up to the sound of alarms and the smell of smoke.")
    print("You look down at your suit and see that your name is ")
    print("(Enter your name)")
    player_name = input("> ")
    player_info['name'] = player_name
    print(f"Checking your vitals, you see that your overall health is at {player_info['health']}%")
    print(f"You look around and realize you have crashed on an unknown planet. Stepping outside, you "
          f"see a damaged escape pod, what looks like a signal tower in distance, and a forest.")
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


def explore_ship(player_info):
    pass

def signal_tower_encounter(player_info):
    pass

def damaged_pod_encounter(player_info):
    pass

def forest_encounter(player_info):
    pass




def main():
    print_intro_text()
    crash_landing_scene()

if __name__ == '__main__':
    main()






'''
Name: Brandon Smith
Date: 10/3/24
Description: This is a text adventure game called Lost in Space about someone who crash lands on a planet
and tries to find their way around the planet.
'''

print("Possible Themes".center(40,'-'))
print("Castle")
print("Swamp")
print("Space crash")

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
print(intro_art)
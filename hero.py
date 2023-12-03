# hero.py

import random

from ability import Ability
from armor import armor


class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''

    # we know the name of our hero, so we assign it here
    self.name = name
    # similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health
    
def add_weapon(self, weapon):
        '''Add weapon to self.abilties'''
        self.abilities.append(weapon)

def fight(self, opponent):
  ''' Current Hero will take turns fighting the opponent hero passed in.
  '''
  # TODO: Fight each hero until a victor emerges.
  # Phases to implement:
  #1) randomly choose winner,
  # Hint: Look into random library, more specifically the choice method

def fight(self, opponent):
  winner = random.choice([self, opponent])

  print("f{winner.name} wins the fight!")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    hero1.fight (hero2)



if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  my_hero = Hero("Grace Hopper", 200)
  print(my_hero.name)
  print(my_hero.current_health)
 

def add_ability(self, ability):
  self.abilities.append(ability)

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  ability = Ability("Great Debugging", 50)
  hero = Hero("Grace Hopper", 200)
  hero.add_ability(ability)
  print(hero.abilities)

def add_armor(self, armor):
         self.armors.append(armor)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)
   
def is_alive(self):
   if alive :
        return True
   else : 
      return False

def fight(self, opponent): 
        if not (self.has_abilities() or opponent.has_abilities()):
            print("Draw")
            return
        
        while self.is_alive() and opponent.is_alive():
            # Step 2: The hero (self) and their opponent must attack each other
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())


            if self.is_alive():
                self.kills += 1
                opponent.deaths += 1
                
        
            else:
               opponent.kills += 1
               self.deaths += 1


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
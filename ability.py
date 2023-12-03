import random

class Ability:
    def __init__(self, fly, max_damage):
        self.name = fly
        self.max_damage = max_damage
        return self.name 
        
    #define attack/what it does
    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value

if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
    




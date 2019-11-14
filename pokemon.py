class Pokemon:

    def __init__(self, name, level, element_type, current_health, knocked_out): 
        self.name = name
        self.level = level
        self.element_type = element_type.lower()
        self.maximum_health = level * 20         
        self.current_health = current_health
        self.knocked_out = knocked_out
    
    def __repr__(self):
        return self.name
    
    def knock_out(self):
        self.knocked_out = True
        print(self.name + " has been knocked out!")
    
    def revive(self):
        self.knocked_out = False
        self.current_health = self.maximum_health
        print(self.name + " has been revived and has " + str(self.current_health) + "  health") 
    
    def lose_health(self, lost_health):
        if lost_health >= self.current_health:
            self.current_health = 0
            self.knock_out()
        else:
            self.current_health -= lost_health
            print(self.name + " now has " + str(self.current_health) + " health")
    
    def regain_health(self, gained_health):
        if self.knocked_out:
            print(self.name + " can not gain health, because they are knocked out.")
        else:
            self.current_health = min([self.current_health + gained_health, self.maximum_health])
            print (self.name + " now has " + str(self.current_health) + " health")
    
    def attack(self, attacking_pokemon):
        print(self.name + " is attacking " + attacking_pokemon.name + ".")
        elements = ["fire", "water", "grass"]
        damage_multipliers = [[1/2, 1/2, 2], [2, 1/2, 1/2], [1/2, 2, 1/2]]
        attacking_pokemon.lose_health(self.level * damage_multipliers[elements.index(self.element_type)][elements.index(attacking_pokemon.element_type)])
        print()
charizard = Pokemon("Charizard", 2, "Fire", 20, False)
bulbousaur = Pokemon("Bulbousaur", 4, "Water", 30, False)

charizard.attack(bulbousaur)
bulbousaur.attack(charizard)
bulbousaur.attack(charizard)
bulbousaur.attack(charizard)
bulbousaur.attack(charizard)
bulbousaur.attack(charizard)



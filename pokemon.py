class Pokemon:
    def __init__(self, name, level, element_type, maximum_health, current_health, knocked_out):
        self.name = name
        self.level = level
        self.element_type = element_type
        self.maximum_health = maximum_health
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

test_name = "Pikachu"
test_level = 1
test_element_type = "Electric"
test_maximum_health = 30
test_current_health = 25
test_knocked_out = False

pikachu = Pokemon(test_name, test_level, test_element_type, test_maximum_health, test_current_health, test_knocked_out)
print(pikachu)

pikachu.lose_health(5)
pikachu.lose_health(45)
pikachu.regain_health(25)
pikachu.revive()
pikachu.lose_health(29)
pikachu.regain_health(45)

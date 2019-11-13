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

test_name = "Pikachu"
test_level = 1
test_element_type = "Electric"
test_maximum_health = 30
test_current_health = 25
test_knocked_out = False

pikachu = Pokemon(test_name, test_level, test_element_type, test_maximum_health, test_current_health, test_knocked_out)
print(pikachu)

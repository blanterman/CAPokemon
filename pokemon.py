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

    # Sets the knock out state of the pokemon object to True. Should only be called by lose_health()
    def knock_out(self):
        self.knocked_out = True
        print(self.name + " has been knocked out!")
    
    # Revives (sets the knock out state to False) This should only be called by regain_health()
    def revive(self):
        self.knocked_out = False
        print(self.name + " has been revived.") 
    
    # Takes health away from the pokemon, if there is not enough health to take, the pokemon is knocked out
    def lose_health(self, lost_health):
        if lost_health >= self.current_health:
            self.current_health = 0
            self.knock_out()
        else:
            self.current_health -= lost_health
            print(self.name + " now has " + str(self.current_health) + " health")
    
    # Gives a give amount of health back to the pokemon. If the pokemon is knocked out it is revived 
    def regain_health(self, gained_health):
        if self.knocked_out:
            self.revive()
        self.current_health = min([self.current_health + gained_health, self.maximum_health])
        print (self.name + " now has " + str(self.current_health) + " health")
    
    # Executes the attack of one pokemon on another. How strong the attack is depends on the relative elements of the pokemon.
    def attack(self, attacking_pokemon):
        print(self.name + " is attacking " + attacking_pokemon.name + ".")
        elements = ["fire", "water", "grass"]
        damage_multipliers = [[0.5, 0.5, 2.0], [2.0, 0.5, 0.5], [0.5, 2.0, 0.5]]
        attacking_pokemon.lose_health(self.level * damage_multipliers[elements.index(self.element_type)][elements.index(attacking_pokemon.element_type)])
        print()

class Trainer:
    def __init__(self, name, potion_quantity, active_pokemon, pokemon_list):
        self.name = name
        self.potion_quantity = potion_quantity
        self. active_pokemon = active_pokemon
        self. pokemon_list = pokemon_list

    def __repr__(self):
        return self.name
    
    # Restores a pokemon to full health
    def use_potion(self):
        if self.potion_quantity == 0:
            print(self.name + " does not have any potions to use.")
        else:
            print(self.name + " has healed " + self.pokemon_list[self.active_pokemon].name + " with a potion.")
            self.pokemon_list[self.active_pokemon].regain_health(self.pokemon_list[self.active_pokemon].maximum_health)
            self.potion_quantity -= 1
    
    # Facilitates one trainer's active pokemon attacking the active pokemon of another trainer
    def attack(self, attacked_trainer):
        print(self.name + " uses their " + self.pokemon_list[self.active_pokemon].name + " to attack " + attacked_trainer.name + "\'s " + attacked_trainer.pokemon_list[attacked_trainer.active_pokemon].name)
        self.pokemon_list[self.active_pokemon].attack(attacked_trainer.pokemon_list[attacked_trainer.active_pokemon])
    
    # Selects which pokemon in the trainers list will be the active (attacking/attacked) pokemon
    def switch_active_pokemon(self, new_active_pokemon):
        if (0 > new_active_pokemon) or (new_active_pokemon > len(self.pokemon_list) - 1):
            print("Unable to switch to that pokemon")
        elif self.pokemon_list[new_active_pokemon].knocked_out:
            print("Unable to switch to that pokemon, they are knocked out.")
        else:
            self.active_pokemon = new_active_pokemon
            print(self.name + " has switched pokemons. Now using: " + self.pokemon_list[self.active_pokemon].name + ".")
    
# Prompts the user to choose player 1 and player 2 from the list of players
def choose_players(trainers_list):
    for i in range(len(trainers_list)):
        print(str(i + 1) + " - " + trainers_list[i].name)
    player1 = trainers_list[int(input("Please select (input the number of) a trainer to be player 1:")) - 1]
    print("Player 1 is: " + player1.name)

    player2 = trainers_list[int(input("Please select (input the number of) a trainer to be player 2:")) - 1]
    print("Player 2 is: " + player2.name)
    print("")
    return player1, player2, True

# Initialize variable for the pokemon battles

# Pokemon list 1
charizard = Pokemon("Charizard", 1, "Fire", 20.0, False)
squirtle = Pokemon("Squirtle", 1, "Water", 20.0, False)
tangela = Pokemon("Tangela", 1, "grass", 20.0, False)
brysons_pokemon = [charizard, squirtle, tangela]

#Pokemon list 2
chikorita = Pokemon("Chikorita", 1, "grass", 20.0, False)
vulpix = Pokemon("Vulpix", 1, "fire", 20.0, False)
psyduck = Pokemon("Psyduck", 1, "water", 20.0, False)
shannons_pokemon = [chikorita, vulpix, psyduck]

bryson = Trainer("Bryson", 10, 0, brysons_pokemon)
shannon = Trainer("Shannon", 20, 0, shannons_pokemon)

trainers = [bryson, shannon]

battle_continues = True
players_chosen = False
player1s_turn = True

# Main game loop
while(battle_continues):
    
    if not players_chosen:
        player1, player2, players_chosen = choose_players(trainers)

    attacker = player1 if player1s_turn else player2
    defender = player2 if player1s_turn else player1

    print(attacker.name + "\'s turn:")
    option = int(input(attacker.name + ", would you like to: \n \
1: Attack \n \
2: Switch pokemon (doesn't use a turn) \n \
3: Administer Potion to active pokemon \n \
4: Check inventory \n \
99: Quit \n"))

    if option == 1:
        if attacker.pokemon_list[attacker.active_pokemon].knocked_out:
            print("Can not attack using a knocked out pokemon.\nPlease switch to another pokemon or administer a potion to current active pokemon.")
        else:
            attacker.attack(defender)
            player1s_turn = not player1s_turn
    
    if option == 2:
        print("You currently can choose from: \n")
        for i in range(len(attacker.pokemon_list)):
            if not attacker.pokemon_list[i].knocked_out:
                print(str(i + 1) + ": " + attacker.pokemon_list[i].name)
        new_active_pokemon = int(input("Please choose from the list")) - 1
        attacker.switch_active_pokemon(new_active_pokemon)

    if option == 3:
        attacker.use_potion()
        player1s_turn = not player1s_turn

    if option == 4:
        print("\n" + attacker.name + "\'s inventory:\n \
---------------------------------------------------------\n \
Pokemon:")
        list_num = 1
        for pokemon in attacker.pokemon_list:
            knockout_message = "knocked out" if pokemon.knocked_out else "Ready for battle"
            active_indicator = "*" if attacker.active_pokemon == list_num - 1 else ""
            print(active_indicator + str(list_num) + ": " + pokemon.name + ", Element: " + pokemon.element_type + ", Health: " + str(pokemon.current_health) + ", KO Status: " + knockout_message)
            list_num += 1
        print("Potions: " + str(attacker.potion_quantity))
        print("")

    if option == 99:
        battle_continues = False



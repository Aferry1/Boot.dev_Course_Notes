#LESSON 1: Comparison Operators
def player_1_wins(player_1_score, player_2_score):
    did_player_1_win = player_1_score > player_2_score
    return did_player_1_win

print("====================")
print("Q1 answer:")
print(player_1_wins(10, 8))
print("====================")
#We can print the output of the function by nesting it in a print function
#Extra print statements added for legibility in console


#LESSON 2: Comparison Operator Evaluations
def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = mustang_height == edward_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphonse_same = winry_height == alphonse_height
    
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same
    #Returns 3 boolean values

print("Q2 answer:")
print(compare_heights(5, 5, 7, 5))
print("====================")


#LESSON 3: Comparison Practice
def can_withstand_blow(hero_armor, enemy_damage):
    can_withstand_blow = hero_armor > enemy_damage
    return can_withstand_blow
    #Returns true if the hero armor can withstand the attack

print("Q3 answer:")
print(can_withstand_blow(250, 175))
print("====================")


#LESSON 4: If Statements
def print_status(player_health):
    #If the player's health is 0, print "dead" in the terminal
    if player_health == 0:
        #Note that the if statement does not use parentheses
        print("dead")
    print("status check complete")

def q4test(health):
    print("Q4 answer:")
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("====================")

q4test(0)
q4test(5)


#LESSON 5: If Practice
def check_swords_for_army(number_of_swords, number_of_soldiers):
    #We want an equal number of swords and soldiers
    if number_of_swords == number_of_soldiers:
        print("correct amount")
    if number_of_swords != number_of_soldiers:
        print("incorrect amount")

print("Q5 answer:")
check_swords_for_army(500, 1000)
print("====================")
print("Q5 answer:")
check_swords_for_army(800, 800)
print("====================")


#LESSON 6: If-Else
def player_status(health):
    #Only one of these statements will be printed
    if health <= 0:
        print("dead")
    elif health <= 5:
        print("injured")
    else:
        print("healthy")

print("Q6 answer:")
player_status(0)
print("====================")
print("Q6 answer:")
player_status(4)
print("====================")
print("Q6 answer:")
player_status(6)
print("====================")


#LESSON 7: If-Else Practice
"""
The bug is in line 2 of the sample code.
Change 
if True: 
to 
if current_player_name == high_scoring_player_name:
"""


#LESSON 8: If-Else Practice pt2
def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        print("high")
    elif player_name == low_scoring_player_name:
        print("low")
    else:
        print("neither")

print("Q8 answer:")
check_high_score("ash", "ash", "brock")
print("====================")
print("Q8 answer:")
check_high_score("brock", "ash", "brock")
print("====================")
print("Q8 answer:")
check_high_score("misty", "brock", "ash")
print("====================")


#LESSON 9: Boolean Logic
def does_attack_hit(attack_roll, armor_class):
    #A 1 is always a miss, and a 20 is always a hit
    #Otherwise, the attack roll must be higher than the armor class
    attack_lands = attack_roll != 1 and attack_roll > armor_class
    attack_successful = attack_lands or attack_roll == 20
    return attack_successful
    #Returns a boolean value

print("Q9 answer:")
print(does_attack_hit(17, 18))
print("====================")
print("Q9 answer:")
print(does_attack_hit(20, 25))
print("====================")


#LESSON 11: Should Serve Drinks
def should_serve_customer(customer_age, on_break, time):
    #We're looking at three criteria, all booleans. 
    #If they're all true, the customer should be served.
    customer_is_adult = customer_age >= 21
    bartender_is_working = on_break == False
    pub_is_open = time >= 5 and time <= 10
    
    should_serve_customer = customer_is_adult and bartender_is_working and pub_is_open
    return should_serve_customer
    #Returns boolean value

def q11test(age, worker, time):
    print("Q11 answer:")
    print(should_serve_customer(age, worker, time))
    print("====================")

q11test(22, False, 10)
q11test(41, False, 1)
q11test(14, False, 7)
q11test(23, True, 5)


#CHALLENGE 1: Mount Rental
def check_mount_rental(time_used, time_purchased):
    rental_message = None
    if time_used > time_purchased:
        rental_message = "overtime charged"
    elif time_used <= time_purchased:
        rental_message = "no charges yet"
    
    return rental_message

def c1test(time_used, time_purchased):
    print("Challenge 1 Answer:")
    print(check_mount_rental(time_used, time_purchased))
    print("====================")

c1test(3, 4)
c1test(5, 2)


#CHALLENGE 2: Combat Advantage
def combat_evaluation(player_power, enemy_defense):
    #By default, all of these booleans are false
    advantage, disadvantage, evenly_matched = False, False, False
    
    #If the player is stronger, advantage will be true
    advantage = player_power > enemy_defense
    #If the player is weaked, disadvantage will be true
    disadvantage = player_power < enemy_defense
    #If the player's power equals the enemy's defense, they are evenly matched
    evenly_matched = player_power == enemy_defense

    #Three booleans are returned, only one of which will be true
    return advantage, disadvantage, evenly_matched

def c2test(player_power, enemy_defense):
    print("Challenge 2 Answer:")
    print(combat_evaluation(player_power, enemy_defense))
    print("====================")

c2test(101, 100)
c2test(50, 100)
c2test(100, 100)


#CHALLENGE 3: Round Trip
def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    #Take the total distance divided by the meters per energy to determine the energy needed
    energy_needed = (distance_one_way * 2) / meters_per_energy
    #Does the player have enough energy? Will be a boolean value
    has_enough_energy = energy_available > energy_needed
    return has_enough_energy

def c3test(energy_available, distance_one_way, meters_per_energy):
    print("Challenge 3 Answer:")
    print(has_enough_energy(energy_available, distance_one_way, meters_per_energy))
    print("====================")

c3test(8, 50, 22)
c3test(9, 100, 20)
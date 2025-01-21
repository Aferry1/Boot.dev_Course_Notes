#LESSON 1-2: Loops, Loop Practice
def print_numbers(end):
    #Function doesn't seem to work without an input
    #Makes it more flexible for the input to not be hard-coded
    for i in range(0, end):
        print(i)
    #i is incremented by 1 by default

def q1answer(end):
    print("====================")
    print("Q1-2 answer:")
    print_numbers(end)
    print("====================")

q1answer(10)
#Prompt has the max as 99, but this saves on output space


#LESSON 3: Loops Practice
def print_numbers_from_five(end):
    for i in range(5, end):
    #The lower bound doesn't have to be 0
    #The upper bound is not inclusive, goes up to end-1
        print(i)

def q3answer(end):
    print("Q3 answer:")
    print_numbers_from_five(end)
    print("====================")

q3answer(10)
#Prompt has the max as 99, but this saves on output space


#LESSON 7: Range Continued
def count_down(start, end):
    for i in range(start, end, -1):
    #The third parameter is the increment, in this case decreasing by 1
        print(i)

def q7answer(start, end):
    print("Q7 answer:")
    count_down(start, end)
    print("====================")

q7answer(10, 0)


#LESSON 8: Sum Game
def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

def q8answer(start, end):
    print("Q8 answer:")
    q8result = sum_of_numbers(start, end)
    print(q8result)
    print("====================")

q8answer(0, 10)


#LESSON 9: Sum Game 2
def sum_of_odd_numbers(end):
    total = 0
    for i in range(0, end):
        #Odd numbers are not evenly divisible by 2
        #We only want to add odd numbers to the total
        if i % 2 != 0:
            total += i
    return total

def q9answer(end):
    print("Q9 answer:")
    q9result = sum_of_odd_numbers(end)
    print(q9result)
    print("====================")

q9answer(10)


#LESSON 10: While
def regenerate(current_health, max_health, enemy_distance):
    """
    Only regain health if:
    1) health is not full
    2) if the enemy is far enough away
    The break point is 3 distance away in this example
    """
    while current_health < max_health and enemy_distance > 3:
        #The enemy moves closer as you regenerate health in this example
        current_health += 1
        enemy_distance -= 2
    return current_health

def q10answer(current_health, max_health, enemy_distance):
    print("Q10 answer:")
    q10result = regenerate(current_health, max_health, enemy_distance)
    print(q10result)
    print("====================")

q10answer(2, 110, 50)


#CHALLENGE 1: Match Countdown
def countdown_to_start():
    #Loop countdown to 1; numbers are hard-coded
    for i in range(10, 0, -1):
        countdown_message = f"{i}..."
        #If i is 1, add "Fight!" to the string
        if i == 1:
            countdown_message += "Fight!"  
        #Print the string statement
        print(countdown_message)
    return countdown_message

print("Challenge 1 answer:")
countdown_to_start()
print("====================")


#CHALLENGE 2: Critical Hit
def calculate_flurry_crit(num_attacks, base_damage):
    """
    This calculates the total attack damage assuming it already crits
    Crits do double damage
    The final hit of the flurry attack also does double damage at base
    """
    #Calculate the final hit seperately
    flurry_damage = 2 * base_damage * (num_attacks - 1)
    final_hit_damage = 4 * base_damage 
    #2*2=4, and this is only for 1 hit
    total_damage = flurry_damage + final_hit_damage
    return total_damage

print("Challenge 2 answer:")
print(calculate_flurry_crit(3, 15))
print("====================")


#CHALLENGE 3: Experience Points
def calculate_experience_points(level):
    """
    The experience needed to level up is 5 times the player's current level
    The amount of xp needed increments by 5 with each level
    We want to calculate the total xp the player has gained based on their level
    """
    total_xp = 0
    for i in range(0, level):
        total_xp += (5 * i)

    return total_xp

print("Challenge 3 answer:")
print(calculate_experience_points(1))
print(calculate_experience_points(2))
print(calculate_experience_points(3))
print(calculate_experience_points(4))
print(calculate_experience_points(5))
print("====================")


#CHALLENGE 4: Random Events
def is_prime(number):
    """
    A prime number is only divisble by itself and 1
    0, 1, and any negative number are not prime numbers
    We don't seem to be taking floats into account
    """
    #Conditions are true by default
    #If conditions remain true, is_prime will change to true
    at_least_2 = True
    not_divisble = True
    is_prime = False
    #Condition 1
    if number < 2:
        at_least_2 = False
    #Condition 2
    for i in range(2, number):
        if number % i == 0:
            not_divisble = False
    #is_prime is only true if both conditions are true
    is_prime = at_least_2 and not_divisble
    #Returns a boolean
    return is_prime

print("Challenge 4 answer:")
print(is_prime(-2))
print(is_prime(1))
print(is_prime(7))
print(is_prime(10))
print("====================")


#CHALLENGE 5: Meditate
def meditate(mana, max_mana, energy, energy_drinks):
    """
    While meditating, the character converts energy into mana. 
    They'll stop when their mana is full, or they run out of energy.
    Energy can be replenished with energy drinks.
    """
    #Repeat while mana isn't full and there's energy to use
    while mana != max_mana and (energy > 0 or energy_drinks > 0):
        #When out of energy, consume an energy drink (if possible)
        if energy == 0 and energy_drinks > 0:
            energy += 50
            energy_drinks -= 1
        #Transmute energy into mana (if possible)
        if energy > 0:
            energy -= 1
            mana += 1
        #print(f"Current mana is {mana}")
        #print(f"Current energy is {energy}")
        #print(f"Current energy drinks are {energy_drinks}")
    #Return three integer values
    return mana, energy, energy_drinks

print("Challenge 5 answer:")
print(meditate(0, 10, 9, 0))
print(meditate(0, 12, 0, 1))
print(meditate(1, 100, 99, 2))
print("====================")
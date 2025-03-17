#LESSON 1: Dictionaries
def get_character_record(name, server, level, rank):
    #Takes two strings and two integers as inputs
    character_record = {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}"
    }
    return character_record
    #Returns a dictionary

def q1answer(name, server, level, rank):
    print("====================")
    print("Q1 answer:")
    print(get_character_record(name, server, level, rank))
    print("====================")

q1answer("Mage", "server1", 10, 3)


#LESSON 7: Counting Practice
def count_enemies(enemy_names):
    #Takes a list of strings as input
    #Define an empty dictionary
    enemies_dict = {}
    #FOR EACH ENEMY:
    for enemy_name in enemy_names:
        #If the name isn't present as a key, add it
        if (enemy_name in enemies_dict) == False:
            #Establish a starting value of 0 for the key
            enemies_dict[enemy_name] = 0
        #Increment the corresponding key by 1
        enemies_dict[enemy_name] += 1
    return enemies_dict

def q7answer(enemy_names):
    print("Q2 answer:")
    print(count_enemies(enemy_names))
    print("====================")

q7answer(["slime", "goblin", "witch", "slime"])


#LESSON 8: Iterating over a Dictionary
def get_most_common_enemy(enemies_dict):
    #Takes a dictionary as input (similar to the one from lesson 7)
    #Ouput set to None by default
    most_common_enemy = None
    #Set the max so far to negative infinity, as it's the lowest possible number
    max_so_far = float("-inf")
    #For each key in the dictionary:
    for enemy in enemies_dict:
        enemy_count = enemies_dict[enemy]
        #If a higher count is found, update the variables
        if enemy_count > max_so_far:
            most_common_enemy = enemy
            max_so_far = enemy_count
    return most_common_enemy
    #Returns a string
"""
"Note that this function does not take into account multiple enemies with the same number.
In such cases, only the first one found is returned.
"""

def q8answer(enemies_dict):
    print("Q8 answer:")
    print(get_most_common_enemy(enemies_dict))
    print("====================")

q8answer({
    "slime": 2,
    "goblin": 1,
    "witch": 1
})
q8answer({})


#CHALLENGE 1: Quest Status
def get_quest_status(progress):
    #Takes a dictionary as input
    quest_status = progress["entity"]["character"]["quests"]["bridge_run"]["status"]
    #You can chain dictionary keys together like this, from out to in
    return quest_status
    #Returns a string 

def c1answer(progress):
    print("C1 answer:")
    print(get_quest_status(progress))
    print("====================")

c1answer({
    "entity": {
        "character": {
            "name": "Kaladin",
            "quests": {
                "bridge_run": {
                    "status": "In Progress", # <- The value we're looking for
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        }
    }
})


#CHALLENGE 2: Total Score
def merge(dict1, dict2):
    #Takes two dictionaries as inputs
    score_dict = {}
    for key in dict1:
        score_dict[key] = dict1[key]
    for key in dict2:
        score_dict[key] = dict2[key]
        #If there is a matching key between the two dictionaries, the second value overwrites the first
    return score_dict
    #Returns a dictionary

def total_score(score_dict):
    #Takes a dictionary with integer values as input
    score = 0
    #Return 0 by default
    for key in score_dict:
        score += score_dict[key]
    return score
    #Returns an integer

def c2answer(dict1, dict2):
    print("C2 answer:")
    #Use the nested functions to combine and tally the score
    print(total_score(merge(dict1, dict2)))
    print("====================")

c2answer(
    {"first_quarter": 24, "second_quarter": 31},
    {"third_quarter": 29, "fourth_quarter": 40}
)


#CHALLENGE 3: Vendor
def calculate_total(items_purchased, pinned_list):
    #The item prices are hard-coded in this example
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }

    #UNPURCHASED ITEMS
    #Define an empty list
    unpurchased_items = []
    for desired_item in pinned_list:
        #Assume they don't have the item by default
        purchased = False
        #Look through the list of acquired items
        for acquired_item in items_purchased:
            #If there's a match, set purchased to true
            if desired_item == acquired_item:
                purchased = True
        #If the boolean is still false, add the item to the list of unpurchased items
        if purchased == False:
            unpurchased_items.append(desired_item)
            #The order will follow the order of pinned_list
    
    #RECEIPT
    #Define an empty dictionary
    receipt = {}
    for acquired_item in items_purchased:
        #Set the price based on the matching item name
        #Note that this will not work with items outside of the existing list
        receipt[acquired_item] = item_prices[acquired_item]

    #TOTAL COST
    #Give a default value of 0 for the total
    total_cost = 0
    for aquired_item in items_purchased:
        total_cost += item_prices[aquired_item]

    """
    Returns:
    1) A list of strings
    2) A dictionary of string keys and float values
    3) A float of the total 
    """
    return unpurchased_items, receipt, total_cost

def c3answer(items_purchased, pinned_list):
    print("C3 answer:")
    print(calculate_total(items_purchased, pinned_list))
    print("====================")

c3answer(
    ["health_potion", "mana_potion"], 
    ["health_potion", "mana_potion", "gold_dust"]
)
"""
You could likely combine some of the for loops to make the function more concise.
I decided to seperate the code to make it more legible.
"""
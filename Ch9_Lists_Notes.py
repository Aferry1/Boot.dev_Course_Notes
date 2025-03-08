#LESSON 1: Lists
def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"]
    #This list of strings is not stored in a variable

def q1answer():
    print("====================")
    print("Q1 answer:")
    print(get_inventory())
    print("====================")

q1answer()


#LESSON 5: Indexing Into Lists
def get_leather_scraps():
    inventory = [
        "Healthing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword"
    ]

    item_index = 1
    #Indexing starts at 0, 
    #The value is hard coded for this example
    return inventory[item_index]

def q5answer():
    print("Q5 answer:")
    print(get_leather_scraps())
    print("====================")

q5answer()


#LESSON 6: List Length
def get_last_index(inventory):
    last_item_index = len(inventory) - 1
    #The length of a list is one greater than the index of the last item
    return last_item_index

def q6answer(inventory):
    print("Q6 answer:")
    print(get_last_index(inventory))
    print("====================")

q6answer(["Healing Potion", "Leather Scraps"])
q6answer(["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"])
#Note that the input must be a list


#LESSON 7: List Updates
def smelt_ore(inventory):
    #If the second item in the inventory is Iron Ore, smelt it into an Iron Bar
    #In any other case, do nothing but return the inventory back
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"
    return inventory

def q7answer(inventory):
    print("Q7 Answer:")
    print(smelt_ore(inventory))
    print("====================")

q7answer(["Potion", "Iron Bar", "Iron Sword", "Leather Armor"])
q7answer([None, "Iron Ore", None, "Leather Armor"])


#LESSON 8: Appending in Python
def generate_user_list(num_of_users):
    #An empty list is defined, which we'll fill in later
    player_ids = []
    for i in range(0, num_of_users):
        #Add the value of i to represent each player ID
        #This does mean the first player will have an ID of "0"
        player_ids.append(i)
        #Note that the i is in parentheses, not brackets
    return player_ids

def q8answer(num_of_users):
    print("Q8 answer:")
    print(generate_user_list(num_of_users))
    print("====================")

q8answer(2)
q8answer(5)


#LESSON 9: Pop Values
def clear_inventory():
    #For this example, the inventory is hard coded
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth"
    ]
    print(f"Invntory: {inventory}")
    
    for i in range(0, len(inventory)):
        #Cycle through the inventory, selling each item one at a time
        #Note that no gold or other compensation is given in this example
        item = inventory.pop()
        print(f"Selling: {item}")
        print(f"Inventory: {inventory}")

def q9answer():
    print("Q9 answer:")
    clear_inventory()
    print("====================")

q9answer()


#LESSON 10: Counting the items in a list
def get_item_counts(items):
    #All counts begin at 0
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    for i in range (0, len(items)):
        current_item = items[i]
        #Increment the matching count by 1 for relevant items
        #Note that these comparisons are case sensitive
        if current_item == "Potion":
            potion_count += 1
        elif current_item == "Bread":
            bread_count += 1
        elif current_item == "Shortsword":
            shortsword_count += 1
    
    #Returns three integers
    return potion_count, bread_count, shortsword_count

def q10answer(items):
    print("Q10 answer:")
    print(get_item_counts(items))
    print("====================")

#Input requires a list; list can hold multiple variable types
q10answer(["Bread", "Potion", "Shortsword", "Bread"])
q10answer(["Potion", "Potion", "Shortsword", "Buckler", "Iron Mace"])


#LESSON 13: Find an item in a list
def contains_leather_scraps(items):
    #Found is false by default
    found = False

    #If the item is in the list, change found to true
    for item in items:
        if item == "Leather Scraps":
            found = True
    
    #Returns boolean value
    return found

def q13answer(items):
    print("Q13 answer:")
    print(contains_leather_scraps(items))
    print("====================")

q13answer(["Potion", "Healing Potion", "Iron Breastplate", "Leather Scraps"])
q13answer(["Potion", "Shortsword", "Buckler", "Iron Mace"])


#LESSON 14: Find the increase
def check_character_levels():
    #Both lists are hard coded for this example
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]
    #Correct output should be 2, 3, 7

    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] < new_character_levels[i]:
            print(i)

def q14answer():
    print("Q14 answer:")
    check_character_levels()
    print("====================")

q14answer()


#LESSON 15: Find max
def find_max(nums):
    max_so_far = float("-inf")
    #Negative infinity is the default, as any other number will be larger
    for damage in nums:
        if damage > max_so_far:
            max_so_far = damage
            #If the current value is bigger, update the max
    return max_so_far
    #Returns float variable

def q15answer(nums):
    print("Q15 answer:")
    print(find_max(nums))
    print("====================")

q15answer([1, 2, 3, 4, 5])
q15answer([10, 20, 300, 4, 5])
q15answer([])
"""
We don't use the max() function in this example.
This is to avoid getting an error if the input is an empty list.
Another way to approach this would be to check if the length of the list is at least 1.
"""


#LESSON 16: Modulo operator in Python (%)
def get_odd_numbers(num):
    odd_numbers = []
    #Define an empty list
    for i in range(0, num):
        #Note that this will not include the upper bound, even if odd
        if i % 2 != 0:
        #Only even numbers will have a remainder of 0
            odd_numbers.append(i)
    return odd_numbers
    #Returns a list of integers

def q16answer(num):
    print("Q16 answer:")
    print(get_odd_numbers(num))
    print("====================")

q16answer(10)


#LESSON 17: Slicing Lists
def get_champion_slices(champions):
    #Needs a list as an input
    first_slice = champions[2:]
    second_slice = champions[:-2]
    #Note that index -2 is includes the third index from the end
    third_slice = champions[::2]
    return first_slice, second_slice, third_slice
    #Returns three lists

def q17answer(champions):
    print("Q17 answer:")
    print(get_champion_slices(champions))
    print("====================")

q17answer(["Andy", "Brock", "Cassie", "Donald", "Evan", "Ferdinand"])


#LESSON 18: List operations - concatenate
def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    #Needs three lists as inputs
    player_favorites = favorite_weapons + favorite_armor + favorite_items
    return player_favorites
    #Returns a concatenated list

def q18answer(favorite_weapons, favorite_armor, favorite_items):
    print("Q18 answer:")
    print(concatenate_favorites(favorite_weapons, favorite_armor, favorite_items))
    print("====================")

q18answer(["sword", "dagger"],
        ["bracers", "helmet"],
        ["feather", "iron bars"])


#LESSON 19: List operations - contains
def is_top_weapon(weapon):
    #The list is hard-coded in this example
    top_weapons = ["sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles"]
    search_result = weapon in top_weapons
    return search_result
    #Returns boolean value

def q19answer(weapon):
    print("Q19 answer:")
    print(is_top_weapon(weapon))
    print("====================")

q19answer("sword of justice")
q19answer("bronze mace")


#LESSON 20: List deletion
def trim_strongholds(strongholds):
    #We want to delete the first and last two strongholds in the list
    del strongholds[0]
    del strongholds[-2:]
    return strongholds
    #Returns the modified list

def q20answer(strongholds):
    #Needs a list as input
    print("Q20 answer:")
    print(trim_strongholds(strongholds))
    print("====================")

q20answer([1, 2, 3, 4, 5])


#LESSON 21: Tuples
def get_heroes():
    #List is hard-coded for this example
    heroes = [
        ("Glorfindel", 2093, True),
        ("Gandalf", 1054, False),
        ("Gimli", 389, False),
        ("Aragorn", 87, False)
    ]
    return heroes
    #Returns a list of tuples
#The lesson focused on fixing syntax, so there's no output    

#LESSON 21: First element
def get_first_item(items):
    output = None
    #If there is a first element of the list, return it
    if len(items) > 0:
        output = items[0]
    #Otherwise, return the string "ERROR"
    else:
        output = "ERROR"
    return output

def q22answer(items):
    #Takes a list as an input
    print("Q22 answer:")
    print(get_first_item(items))
    print("====================")

q22answer([1, 2, 3])
q22answer([])


#LESSON 23: Reverse List
def reverse_array(items):
    reverse_list = items[-1: : -1]
    #Start with the last item, move backwards 1 index towards the start
    return reverse_list
    #Returns the new list

def q23answer(items):
    print("Q23 answer:")
    print(reverse_array(items))
    print("====================")

q23answer([1, 2, 3])


#LESSON 24: Filter messages
"""
Note that this function only filters out the word "dang"
Any other bad words are not considered
"""
def filter_messages(messages):
    #Create two empty lists that are returned at the end of the function
    filtered_messages = []
    bad_word_counts = []

    #FOR EACH MESSAGE:
    """
    1) Split the message into a list of words
    2) Create a list to store the non-bad words
    3) Create a counter for the number of bad words
    """
    for message in messages:
        words = message.split()
        safe_words = []
        bad_words_counter = 0

        #FOR EACH WORD:
        """
        1) If the word IS "dang", increment the bad_words_counter variable by 1
        2) If it is IS NOT "dang", add it to the safe_words list
        """
        for word in words:
            if word == "dang":
                bad_words_counter += 1
            else:
                safe_words.append(word)
    
        #ADD RESULTS:
        """
        1) Join the list of non-bad words into a single string
        2) Append the new clean message to the final list of filtered messages
        3) Append the count of bad words removed to its list
        """
        filtered_message = " ".join(safe_words)
        filtered_messages.append(filtered_message)
        bad_word_counts.append(bad_words_counter)

    return filtered_messages, bad_word_counts

def q24answer(messages):
    print("Q24 answer:")
    print(filter_messages(messages))
    print("====================")

q24answer(["oh gosh dang it", "dang dang bang", "safe message"])

#CHALLENGE 1: Evens and Odds
def get_odds_and_evens(numbers):
    #Takes a list as the input
    num_odds = 0
    num_evens = 0

    #Loop through the list, and tally the number of even and odd numbers
    for number in numbers:
        if number % 2 != 0:
            num_odds += 1
        else:
            num_evens += 1

    return num_odds, num_evens
    #Returns two integers

def c1answer(numbers):
    print("C1 answer:")
    print(get_odds_and_evens(numbers))
    print("====================")

c1answer([1, 7, 2, 5, 3, 4])


#CHALLENGE 2: Even Teams
def split_players_into_teams(players):
    #Accepts a list as input
    even_team = players[::2]
    #Take the players with the even indexes
    odd_team = players[1::2]
    #Take the players with the odd indexes
    #Note that in the case of an odd number of players, odd_team will have one more player

    return even_team, odd_team

def c2answer(players):
    print("C2 answer:")
    print(split_players_into_teams(players))
    print("====================")

c2answer(["Amy", "Brian", "Cassie", "Daniel", "Evan", "Gregory"])


#CHALLENGE 3: Alchemy ingredients
def check_ingredient_match(recipe, ingredients):
    #Takes two lists as inputs
    """
    The goal is to:
     1) Calculate the percentage of the recipe that is met
     2) Return a list of the unobtained items
    We are taking into account recipes with multiple copies of the same ingredient
    We must take into account that the items might be equal, but in a different order
    For this example, it's assumed the lists are the same length
    """
    #Define an empty list, and make copies of the input lists
    missing_ingredients = []
    working_recipe = recipe
    working_ingredients = ingredients
    
    #FOR EACH NEEDED INGREDIENT:
    for i in range(0, len(recipe)):
        #Set the boolean to False by default
        matching_ingredient = False
        #Loop through the ingredients to see if the player has it
        for j in range(0, len(ingredients)):
            #If there's a match, mark off the items in the working lists
            if recipe[i] == ingredients[j]:
                matching_ingredient = True
                working_recipe[i] = "USED"
                working_ingredients[j] = "USED"
        #If there was no match, mark the required ingredient as missing
        if matching_ingredient == False:
            missing_ingredients.append(recipe[i])

    #Calculate the percentage of required ingredients (1 - % missing) the player had
    recipe_completion = 1 - (len(missing_ingredients) / len(recipe))

    return recipe_completion, missing_ingredients
    #Returns a float and a list

def c3answer(recipe, ingredients):
    print("C3 answer:")
    print(check_ingredient_match(recipe, ingredients))
    print("====================")

c3answer(
    [
        "Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk", 
        "Mandrake Root","Griffin Feather", "Elf Dust","Goblin Ear"
    ],
    [
        "Dragon Scale", "Goblin Ear", "Phoenix Feather", "Elf Dust",
        "Mandrake Root", "Griffin Feather", "Elf Dust", "Goblin Ear"
    ]
)

"""
This may not be the simplest solution, but it was the one I came up with to address all the edge cases.
There may be some way to take advantage of the fact that the lists are the same length. 
"""


#CHALLENGE 4: Validate Path
def validate_path(expected_path, character_path):
    """
    The function takes two lists as inputs.
    The goal is to compare the charted path to the one the character took
    The first item in the character_path list will always be the character name
    """
    #Define variable for tallying the number of matching waypoints
    matching_waypoints = 0
    for i in range(0, len(expected_path)):
        #If they match, add 1 to the running total
        if expected_path[i] == character_path[i + 1]:
            #The index + 1 is to offset the first index being the character name
            matching_waypoints += 1
    
    character_name = character_path[0]
    accuracy = matching_waypoints / len(expected_path) * 100
    #Multiply by 100 to format the number as a percentage
    return character_name, accuracy

def c4answer(expected_path, character_path):
    print("C4 answer:")
    print(validate_path(expected_path, character_path))
    print("====================")

c4answer(
    ["A", "B", "C", "D", "E"],
    ["Arthur", "A", "X", "C", "D", "E"]
)


#CHALLENGE 5: Double the string
def double_string(string):
#Takes a string as the input
    """
    The goal of this function is to double every character in the string
    For example, "TEST" becomes "TTEESSTT"
    Spaces count as characters, and should be doubled as well
    """
    #Create an empty list that we'll put the characters in
    split_list = []
    #Split up the string
    split_string = string.split()
    #Note that the default delimiter for .split() is a space
    #FOR EACH WORD:
    for word in split_string:
        #Define an empty variable to store the characters
        new_word = []
        #FOR EACH CHARACTER:
        #Note that we can loop through characters in a string
        for character in word:
            new_word.append(character)
            new_word.append(character)
        #Add the new word to the resulting list, then move on to the next word
        split_list.append(new_word)
    """
    Now we have a list of lists, with these properties:
    1) Each index is a word in the original phrase
    2) Each list contains characters doubled from the original word

    To get the desired output, we still need to:
    1) Turn each list into a string, with no spaces
    2) Combine the list of words into one string, with a double space between each word.
    """
    combined_list = []
    #FOR EACH MODIFIED WORD:
    for word in split_list:
        combined_string = "".join(word)
        combined_list.append(combined_string)
    #Rejoin the list as one string, adding two spaces between each word
    resulting_string = "  ".join(combined_list)
    return resulting_string

def c5answer(string):
    print("C5 answer:")
    print(double_string(string))
    print("====================")

c5answer("Hello there")
"""
I'm sure there's a more elegant solution to this last challenge,
but this is what I found worked. 
Perhaps we don't need to split up the string to begin with?
"""

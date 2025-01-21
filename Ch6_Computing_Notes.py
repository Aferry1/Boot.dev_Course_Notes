#Chapter 6: Computing

#LESSON 1: Python Numbers
def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    return total_damage, average_damage



#LESSON 5-6: Changing in Place; Plus Equals
def update_player_score(current_score, increment):
    current_score = current_score + increment
    #current_score += increment is a cleaner way to write this
    #works will all four base operators: +=, -=, *=, /=
    return current_score



#LESSON 7: Scientific Notation
def max_players_on_server():
    small_server_max = 1.024e18
    medium_server_max = 1.024e19
    large_server_max = 1.024e20
    return small_server_max, medium_server_max, large_server_max
    #Function is only meant to return these static values



#LESSON 13: Bitwise '&' Operator
#Define variables
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

#Note:The get_XXX_bits functions only return the bits.
#The test code (not shown) compares the result to the original permission value to see if it matches.
def get_create_bits(user_permissions):
    #user_permissions is a binary number
    result = user_permissions & can_create_guild
    #result variable is a bunary number
    return result

def get_review_bits(user_permissions):
    result = user_permissions & can_review_guild
    return result

def get_delete_bits(user_permissions):
    result = user_permissions & can_delete_guild
    return result

def get_edit_bits(user_permissions):
    result = user_permissions & can_edit_guild
    return result



#LESSON 14: Bitwise '|' Operator
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    #All four inputs are binary numbers
    #Permissions are shared between all members. If one member has a permission, they all do.
    shared_permissions = glorfindel | galadriel | elendil | elrond
    return shared_permissions

#CHALLENGE #1: Damage Meter
def main():
    calculate_dps(8_000_000, 45)
    calculate_dps(10_000_000, 49)
    #Remeber to use underscores as delimiters instead of commas

def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("==========================")

main()

#CHALLENGE #2: Converting Binary
def binary_string_to_int(num_servers, num_players, num_admins):
    num_servers_int = int(num_servers, 2)
    #When looking online, this is the main way to convert this.
    #The second input (2) tells the base. Binary is base 2.
    #Not sure if there's a good way to do this manually. Number of digits in input could vary.
    num_players_int = int(num_players, 2)
    num_admins_int = int(num_admins, 2)
    return num_servers_int, num_players_int, num_admins_int
    
#Chapter 5: Testing and Debugging

#LESSON 1
def total_xp(level, xp_to_add):
	#Each level is 100XP
	total_xp = (level * 100) + xp_to_add
	return total_xp

#LESSON 3
def take_magic_damage(health, resist, amp, spell_power):
	#Calculate max damage first before subtracting resist
    max_damage = spell_power * amp
    total_damage = max_damage - resist
    #Health variable gets updated and replaced
    health -= total_damage
    return health

#LESSON 7
def unlock_achievement(before_xp, ach_xp, ach_name):
    total_xp = before_xp + ach_xp
    achievement_message = "Achievement Unlocked: " + ach_name
    #When debugging, print the values of the two variables we created
    return total_xp, achievement_message

#LESSON 8
def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    return msg
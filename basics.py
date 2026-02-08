# a = 6

# a = a + 2

# print(a)

# print("Hello, World!")


# player_health = 1000
# armor_multiplier = 2

# armored_health = player_health * armor_multiplier

# print(armored_health)
# print(player_health)

# player_health = 100
# poison_damage = -10

# player_poison_health = player_health + poison_damage

# print(player_poison_health)

# this is a single line comment. It can be used to write a brief explanation or note about a specific line of code or a small section of code.
"""
This is a multi-comment block. It can be used to write multiple lines of comments without needing to use the # symbol at the beginning of each line. This is useful for writing longer explanations or notes in your code.
"""

# functions

# def area_of_circle(radius):
#     pie = 3.14
#     area = pie * radius * radius
#     return area

# sword_length = 1.0
# spear_length = 2.0

# sword_area = area_of_circle(sword_length)
# spear_area = area_of_circle(spear_length)

# print(f"Sword area is ${sword_area} meters")
# print(f"Spear area is ${spear_area} meters")

# multiple parameter functions

# def subtract(a, b):
#     return a - b
# # multiple arguments function call
# print(subtract(5, 1))

# hours to seconds

# def hours_to_seconds(hours):
#     minutes = hours * 60
#     seconds = minutes * 60
#     # shorthand
#     # return hours * 60 * 60
#     return seconds

# def test(hours):
#     secs = hours_to_seconds(hours)
#     print(f"{hours}, hours is {secs} seconds")

# test(33)

# multiple item return

# def become_warrior(first_name, last_name, power):
#     # title = first_name + " " + last_name + " " + "the warrior"
#     title = f"{first_name} {last_name} the warrior"
#     new_power = power + 1
#     return title, new_power

# def main():
#     test("Frodo", "Baggins", 5)

# def test(first_name, last_name, power):
#     title, new_power = become_warrior(first_name, last_name, power)
#     print(f"{title}, has a power level of: {new_power}!")
          
# main()

# def get_max_health(modifier, health):
#     return modifier * health

# my_modifier = 5
# my_level = 10

# max_health = get_max_health(my_modifier, my_level)

# print(f"Max health is: {max_health}")

# global scope
player_level = 10

def calculate_health(modifier):
    return player_level * modifier

def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level

print(f"Character has an {calculate_health(10)} max health")
print(f"Character has an {calculate_primary_stats(3, 8)} primary stats")
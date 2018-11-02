types_of_people = 10
x = f"There are {types_of_people} tpyes of types of people."

binary = "binary"
do_not = "don`t"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn`t that joke so funny?!{}"

print(joke_evaluation.format(hilarious))

w = "This is the left sid of..."
e = "a string with a right side."

print(w + e)


tabby_cat = "\tI am tabbed in."
persian_cat = "I am split\non a line."
bachslash_cat = "I am \\ a \\ cat."

fat_cat = """
I will do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(bachslash_cat)
print(fat_cat)


print("How old are u ?", end = ' ')
age = input()
print("How tall are u?", end = ' ')
height = input()

print(f"you r {age} old ,{height} tall")



new_age = input("how old are u?")
print(new_age)

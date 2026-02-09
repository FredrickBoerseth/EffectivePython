# Prefer multiple assignment unpacking over indexing

# in its simpelest form a tuple contains two values, like a key value pair from a dict

snack_calories = {
	'chips': 140,
	'popcorn': 80,
	'nuts': 190,
}
items = tuple(snack_calories.items())
print(items)


# items in a tuple can be accessed using indexing
item = ('Peanut butter', 'Jelly')
first = item[0]
second = item[1]
print(first, 'and', second)


# tuples are immutable.. they can be changed after they are created
pair = ('Chocolate', 'Peanut buttter')
# pair[0] = 'Honey'


item = ('Peanut butter', 'Jelly')
first, second = item # unpacking
print(first, 'and', second)


# can be done, but not reccomended
favorite_snacks = {
	'salty': ('pretzels', 100),
	'sweet': ('cookies', 180),
	'veggie': ('carrots', 20),
}

((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3))) = favorite_snacks.items()


print(f'favorite {type1} is {name1} with {cals1} calories')
print(f'favorite {type2} is {name2} with {cals2} calories')
print(f'favorite {type3} is {name3} with {cals3} calories')
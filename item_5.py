# Write helper functions instead of complex expressions

from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green', keep_blank_values=True)
print(repr(my_values))

print('Red:     ', my_values.get('red'))
print('Green:   ', my_values.get('green'))
print('opacity: ', my_values.get('opacity'))


# for query string 'red=5&blue=0&green'
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print(f'red:       {red!r}')
print(f'green:     {green!r}')
print(f'opacity:   {opacity!r}')

red = int(my_values.get('red', ['']) or 0) # hard to read, to much visual noise


# better for less complicated situations
red_str = my_values.get('red', [''])
red = int(red_str[0]) if red_str[0] else 0


green_str = my_values.get('green', [''])
if green_str[0]:
	green = int(green_str[0])
else:
	green = 0



def get_first_int(values, key, default=0):
	found = values.get(key, [''])
	if found[0]:
		return int(found[0])
	return default

# python makes it easy to write complex code, if this happens use helper function to contain the logic
# this code pulls for a value, and returns empty if equal to false / 0
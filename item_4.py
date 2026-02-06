### problems with c style formatting

a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))

# this works if key comes before value, but not the other way around problem .1
key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted)

pantry = [
('avocados', 1.25),
('bananas', 2.5),
('cherries', 15),
]

# second problem, becomes difficult to read when making small modifications

for i, (item, count) in enumerate(pantry):
	print('#%d: %-10s = %.2f' % (i, item, count))


# third problem, if you want to use the same value.. in this case name, you have to type it several times
template = '%s loves food. See %s cook.'
name = "Max"
formatted = template % (name, name)
print(formatted)



# solutions

#problem 1

key = 'my_var'
value = 1.234

old_way = '%-10s = %.2f' % (key, value)

new_way = '%(key)-10s = %(value).2f' % {'key': key, 'value': value} # Original version

reordered = '%(key)-10s = %(value).2f' % {'value': value, 'key': key} # Swapped version

assert old_way == new_way == reordered

# dictionaries also solve problem number three:

name = 'Max'

template = '%s loves food. See %s cook.'
before = template % (name, name) # tuple

template = '%(name)s loves food. See %(name)s cook.'
after = template % {'name': name} # dictionary

assert before == after

# formatting expressions becomes verbose, and hard to read

for i, (item, count) in enumerate(pantry):
	before = '#%d: %-10s = %d' % (
		i + 1,
		item.title(),
		round(count))

	after = '#%(loop)d: %(item)-10s = %(count)d' % {
	    'loop': i + 1,
	    'item': item.title(),
	    'count': round(count),
	}

	assert before == after

	# using dictionaries is also a problem with c style programming, it becomes verbose.

soup = 'lentil'
formatted = 'Today\'s soup is %(soup)s.' % {'soup': soup}
print(formatted)


menu = {
	'soup': 'lentil',
	'oyster': 'kumamoto',
	'special': 'schnitzel',
}

template = ('Today\'s soup is %(soup)s, buy one get two %(oyster)s oysters, and our special entree is %(special)s.')

formatted = template % menu
print(formatted)

# this shit is kinda disorienting. Your eyes have to switch between whats in the dict to match them up with the template.


#############################

# The format built-in and str.format

#############################


a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

b = 'my string'
formatted = format(b, '^20s')
print(formatted)

key = 'my_var'
value = 1.234

formatted = '{} = {}'.format(key,value)
print(formatted)

formatted = '{:<10} = {:.2f}'.format(key, value)
print(formatted)

formatted = '{1} = {0}'.format(key, value)
print(formatted)

formatted = '{0} loves food. See {0} cook.'.format(name)
print(formatted)



old_template = ('Today\'s soup is %(soup)s, '
	            'buy one get two %(oyster)s oysters, '
	            'and our special entree is %(special)s.')
old_formatted = template % {
	'soup': 'lentil',
	'oyster': 'kumamoto',
	'special': 'schnitzel',
}


new_template = ('Today\'s soup is {soup}, '
	            'buy one get two {oyster} oysters, '
	            'and our special entree is {special}.')
new_formatted = new_template.format(
	soup='lentil',
	oyster='kumamoto',
	special='schnitzel',)

assert old_formatted == new_formatted


#############################

# interpolated format strings

#############################

key = 'my_var'
value = 1.234

formatted = f'{key} = {value}'
print(formatted)

formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)

places = 3
num = 1.23456
print(f'My number is {num:.{places}f}')

# use f strings.. fuck the rest boi
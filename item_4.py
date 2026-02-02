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


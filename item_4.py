a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))

# this works if key comes before value, but not the other way around
key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted)

pantry = [
('avocados', 1.25),
('bananas', 2.5),
('cherries', 15),
]


for i, (item, count) in enumerate(pantry):
	print('#%d: %-10s = %.2f' % (i, item, count))
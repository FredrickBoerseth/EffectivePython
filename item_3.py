# know the differences between bytes and str

a = b'h\x65llo' # instance of bytes
print(list(a))
print(a)

a = 'a\u0300 propos' # instance of str
print(list(a))
print(a)


# helper function, converting stuffs, takes in bytes or str, returns string only
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # Instance of str

print(repr(to_str(b'foo')))
print(repr(to_str('bar')))


# second function, takes bytes or str, returns bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # Instance of bytes

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))

# adding stuffs
print(b'one' + b'two')
print('one' + 'two')

# this wont work thou
# print(b'one' + 'two')
# print('one' + b'two')


# using binary operators lets you compare bytes to bytes, and str to str
assert b'red' > b'blue'
assert 'red' > 'blue'

import locale
print(locale.getpreferredencoding())
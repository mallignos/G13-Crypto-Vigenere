
# Basic Error class
class Error(Exception):
	pass

# Error for Problems during Encoding
class EncodeError(Error):
	pass

# Error for Problems during Decoding
class DecodeError(Error):
	pass

# The maximum value something can have
MAX_INT = 32

# All Legal ints to decode
# returns list
def allInts():
	return list(range(MAX_INT))

# All legal characters to encode
# returns list
def allChars():
	return [decodeInt(i) for i in allInts()]

# Encodes a char into an int
# char c
# return int
def encodeChar(c):
	if 'a' <= c and c <= 'z':
		return (ord(c) - ord('a'))
	elif c == 'å':
		return (26)
	elif c == 'ä':
		return (27)
	elif c == 'ö':
		return (28)
	elif c == ' ':
		return (29)
	elif c == ',':
		return (30)
	elif c == '.':
		return (31)
	else:
		raise EncodeError("Illegal character found: " + str(c))

# Makes a int into a char
# int c
# returns char
def decodeInt(c):
	if 0 <= c and c <= 25:
		return (chr(c + ord('a')))
	elif c == 26:
		return ('å')
	elif c == 27:
		return ('ä')
	elif c == 28:
		return ('ö')
	elif c == 29:
		return (' ')
	elif c == 30:
		return (',')
	elif c == 31:
		return ('.')
	else:
		raise DecodeError("Illegal int found: " + str(c))

# Tests some things from this module.
def _test():
	print('max_int:',MAX_INT)
	print('allInts:',allInts())
	print('allChars:',allChars())
	print('Now testing Exception:')
	decodeInt(MAX_INT + 1)
	print('Can you see this?')

# makes test run if main module
if __name__ == '__main__':
	_test()


# Makes an char into an int
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
		print("Illegal character found: " + str(c))

# Makes a int into a char
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
		print("Illegal character found: " + str(c))
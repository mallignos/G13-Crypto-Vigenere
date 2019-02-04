import encode_decode

fileName = "Words/sv100.txt"

_legalChars = set([encode_decode.decodeInt(i) for i in range(32)])
_wordList   = set()
_has_init = False

def is_sv_word(c):
	if not _has_init:
		_init()
	return c in _wordList

def _init():
	words = open(fileName).read().lower().split("\n")

	for w in words:
		toAdd = True
		for c in w:
			if c not in _legalChars:
				toAdd = False
				break
		if toAdd:
			_wordList.add(w)

	_has_init = True

def main():
	while(True):
		a = str(input("Type a word: "))
		if (is_sv_word(a)):
			print("In the dictionary")
		else:
			print("NOT in the dictionary")

# So that Python starts to run the main.
if __name__ == '__main__':
    main()

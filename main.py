import sys
import json
import encrypt_decrypt
import key_guess
import keylength_guess


# Find the last occurence of char c in string s
# string s the string to check
# char c the char to compare
# return int the index of the last occuring character equal to c
def findLast(s,c):
	for i in range(len(s)-1,-1,-1):
		if s[i] == c:
			return i
	return (-1)

# Remove all characters after the last c from s, including that character
# string s the string to remove from
# char c the char to compare
# return string The string without the characters 
def ignoreLast(s,c):
	i = findLast(s,c)
	if i == (-1):
		return s
	else:
		return s[:i]


# Remove all characters before the last c from s, including that character
# string s the string to remove from
# char c the char to compare
# return string The string without the characters
def ignoreInit(s,c):
	i = findlast(s,c)
	return s[i+1:]

# Makes a file path to output into, so that the file can inherit the name.
# string Path the origenal input path
# string extension A new file extension to use
# return string A path that you can use
def makeOutputPath(Path,extension):
	return 'out/' + ignoreInit(ignoreLast(Path,'.'),'/') + extension

# Handles encrypt command
# returns none
# Side effects: creates/overwrites a file in out/, with the plain from input
def encrypt():
	inputPlainPath = sys.argv[3]
	inputKeyPath   = sys.argv[2]
	outputPath = makeOutputPath(inputPlainPath,".crypto")

	plain = open(inputPlainPath,'r').read()
	key = open(inputKeyPath,'r').read()

	crypto = encrypt_decrypt.encryptString(plain,key,32)

	open(outputPath,'w').write(crypto)

# Handles decrypt command
# returns none
# Side effects: creates/overwrites a file in out/, with the crypto from input
def decrypt():
	inputCryptoPath = sys.argv[3]
	inputKeyPath    = sys.argv[2]
	outputPath = makeOutputPath(inputCryptoPath,".plain")

	crypto = open(inputCryptoPath,'r').read()
	key = open(inputKeyPath,'r').read()

	plain = encrypt_decrypt.decryptString(crypto,key,32)

	open(outputPath,'w').write(plain)

# Handles break command
# returns none
# Side effects: creates/overwrites a file in out/, with the crypto from input
def break_():
	inputCryptoPath = sys.argv[2]
	outputPath = makeOutputPath(inputCryptoPath,".break")


	crypto = open(inputCryptoPath,'r').read()
	freq = json.loads(open("Freqency Text/freq.json",'r').read())

	m = keylength_guess.keylength_guess_most_likely(crypto)
	key = key_guess.guess(crypto,m,freq)

	plain = encrypt_decrypt.decryptString(crypto,key,32)

	open(outputPath,'w').write(key + "\n" + plain)

# Handles if no command was given
# returns none
# Side effects: prints stuff in the terminal
def help() {
	print("Usage: python3 main.py [mode] (...)")
	print("\tRead the readme for more info.")
	print("Availeble [mode]:")
	print("\tpython3 main.py encrypt (path/to/key) (path/to/plain)")
	print("\tpython3 main.py decrypt (path/to/key) (path/to/crypto)")
	print("\tpython3 main.py break (path/to/crypto)")

}

# Main
# desides what function above to run.
def main():
	if sys.argv[1] == 'encrypt':
		encrypt()
	elif sys.argv[1] == 'decrypt':
		decrypt()
	elif sys.argv[1] == 'break':
		break_()
	else:
		help()

# Makes so that main runs if not imported.
if __name__ == '__main__':
	main()
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
	i = findLast(s,c)
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

	crypto = encrypt_decrypt.encryptString(plain,key)

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

	plain = encrypt_decrypt.decryptString(crypto,key)

	open(outputPath,'w').write(plain)

# Handles break command
# returns none
# Side effects: creates/overwrites a file in out/, with the crypto from input
def break_():
	crypto_argc = 2
	kmax = 16
	if sys.argv[2][:2] == '-k':
		kmax = int(sys.argv[2][2:]) 
		crypto_argc = 3
	
	inputCryptoPaths = [sys.argv[crypto_argc]]
	
	break_aux(inputCryptoPaths,kmax)


# Handles break-multiple command
# returns none
# Side effects: creates/overwrites a file in out/, with the crypto from input
def break_multiple():
	crypto_argc = 2
	kmax = 16
	if sys.argv[2][:2] == '-k':
		kmax = int(sys.argv[2][2:]) 
		crypto_argc = 3

	inputCryptoPaths = sys.argv[crypto_argc:]
	break_aux(inputCryptoPaths,kmax)

# Handles break-multiple command
# returns none
# Side effects: creates/overwrites a file in out/, with the crypto from input
def break_aux(inputCryptoPaths,kmax):
	
	cryptos = []
	for path in inputCryptoPaths: 
		cryptos += [open(path,'r').read()]

	freq = json.loads(open("Freqency Text/freq.json",'r').read())

	m = keylength_guess.keylength_guess_most_likely(cryptos,maxi=kmax)
	print("Guessed length:",m)
	key = key_guess.guess(cryptos,m,freq)
	print("Guessed Key   :",key)

	for i in range(len(cryptos)):
		outputPath = makeOutputPath(inputCryptoPaths[i],".break")
		plain = encrypt_decrypt.decryptString(cryptos[i],key)

		open(outputPath,'w').write(key + "\n" + plain)


# Handles if no command was given
# returns none
# Side effects: prints stuff in the terminal
def help():
	print("Usage: python3 main.py [mode] (...)")
	print("\tRead the readme for more info.")
	print("Availeble [mode]:")
	print("\tpython3 main.py encrypt (path/to/key) (path/to/plain)")
	print("\tpython3 main.py decrypt (path/to/key) (path/to/crypto)")
	print("\tpython3 main.py break (path/to/crypto)")


# Main
# desides what function above to run.
def main():
	if sys.argv[1] == 'encrypt':
		encrypt()
	elif sys.argv[1] == 'decrypt':
		decrypt()
	elif sys.argv[1] == 'break':
		break_multiple()
	#elif sys.argv[1] == 'break-multiple':
	#	break_multiple()
	else:
		help()

# Makes so that main runs if not imported.
if __name__ == '__main__':
	main()
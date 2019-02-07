import encode_decode

# Encrypts a single character that has been turned into an int c, key int k
# int c the character to encrypt
# int k the character act as key
# return int the encrypted Character
def encryptInt(c,k):
	return (c + k) % encode_decode.MAX_INT

# Encrypts a single char c, with key char k
# char c the plain char
# char k the key char
# return char the crypto char
def encryptChar(c,k):
	return encode_decode.decodeInt(encryptInt(encode_decode.encodeChar(c),encode_decode.encodeChar(k)))

# Encrypts a string s with key k
# string s the plaintext to encrypt
# string k the key 
# returns string the cryptotext
def encryptString(s,k):
	outString = ""
	for i in range(len(s)):
		outString += encryptChar(s[i],k[i % len(k)])
	
	return outString

# Decrypts a single character that has been turned into an int c, key int k
# int c the character to dectypt
# int k the character act as key
# return int the decrypted character
def decryptInt(c,k):
	return encryptInt(c,(-k)) 

# Decrypts a single char c, with key char k
# char c the crypto char
# char k the key char
# return char the plain char
def decryptChar(c,k):
	return encode_decode.decodeInt(decryptInt(encode_decode.encodeChar(c),encode_decode.encodeChar(k)))

# Decrypts a string s with key k
# string s the cryptotext to decrypt
# string k the key 
# returns string the plaintext
def decryptString(s,k):
	outString = ""
	for i in range(len(s)):
		outString += decryptChar(s[i],k[i % len(k)])
	
	return outString

# Function that tests if the encryption is working.
# Just for testing purposes.
def _main():
	plainString = open("in/vig_group13.plain","r").read().lower()
	keyString   = open("in/vig_group13.key"  ,"r").read().lower()

	codeString  = encryptString(plainString,keyString)
	
	outFile     = open("out/vig_group13.crypto","w")
	outFile.write(codeString)

	print(codeString)

	decodedString = decryptString(codeString,keyString)
	
	print(decodedString)

# So that Python starts to run the main.
if __name__ == '__main__':
    _main()


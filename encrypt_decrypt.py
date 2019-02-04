import encode_decode

# Decrypts a single character that has been turned into an int c, key int k and
# m amount of characters
def encryptInt(c,k,m):
	return (c + k) % m

# Encrypts a string s with key k and m amount of characters.
def encryptString(s,k,m):
	outString = ""
	for i in range(len(s)):
		p_int = encode_decode.fromCharToInt(s[i         ])
		k_int = encode_decode.fromCharToInt(k[i % len(k)])
		c_int = encryptInt(p_int,k_int,m)

		outString += fromIntToChar(c_int)
	
	return outString

# Decrypts a single character that has been turned into an int c, key int k and
# m amount of characters
def decryptInt(c,k,m):
	return encryptInt(c,(-k),m) 

# Decrypts a string s with key k and m amount of characters.
def decryptString(s,k,m):
	outString = ""
	for i in range(len(s)):
		c_int = encode_decode.fromCharToInt(s[i         ])
		k_int = encode_decode.fromCharToInt(k[i % len(k)]) 
		p_int = decryptInt(c_int,k_int,m)

		outString += fromIntToChar(p_int)
	
	return outString

# Encrypts a string, then saves it. Also decrypts the same string back
# to see that the code was correctly implemented.
def main():
	plainString = open("in/vig_group13.plain","r").read().lower()
	keyString   = open("in/vig_group13.key"  ,"r").read().lower()

	codeString  = encryptString(plainString,keyString,32)
	
	outFile     = open("out/vig_group13.crypto","w")
	outFile.write(codeString)

	decodedString = decryptString(codeString,keyString,32)
	
	print(decodedString)

# So that Python starts to run the main.
if __name__ == '__main__':
    main()


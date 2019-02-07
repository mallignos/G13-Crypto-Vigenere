import json
import encode_decode
import operator

import encrypt_decrypt
import keylength_guess

# The string into diffrent substring, depending on their modulo
# string s the string to be split
# int m the amount of splits
# returns [string] the partitioned strings 
def mod_split(s,m):
	out = [""]*m
	for i in range(0,len(s)):
		out[i%m] += s[i]
	return out


# makes a frequency dict of a string p
# string p the string
# returns dict(string,int) how many times any char occurs in the string p
def gen_freq(p):
	chars = [encode_decode.decodeInt(i) for i in range(32)]

	d = dict([(c,0) for c in chars])
	for c in p:
		d[c] += 1
	return d


# Normelises a dictionary d, so that the sum of all values are 1
# dict(T,int) d the dictionary
# returns dict(T,float) normalized dictionary 
def dictNorm(d):
	sum_ = sum(d.values())
	d_out = dict()
	for i in d:
		d_out[i] = d[i] / sum_
	return d_out

# Finds out how different dictionaries are
# 0 means very similar/identical, 1 would be as dissimilar as possible
# Effectially manhattan geometry distance
# dict(T,float) d_a one dict
# dict(T,float) d_a second dict
# returns float distance inbetween them 
def distDict(d_a,d_b):
	sum_ = 0
	for i in d_a:
		sum_ += abs(d_a[i] - d_b[i])

	return sum_

# Slow version of the key guesser
# More accurate than the slow version
# Assumes s is a ceasar cipher.
# Tries every key in a ceasar cipher, and picks the most likely.
# O(C) for C = amount of characters
# string s the encrypted partial string
# dict(char,int) sv_freq the expected character frequency
# returns the best character to be the key.
def slow(s,sv_freq):
	this_f = gen_freq(s)

	best = None
	best_v = float('inf')
	for i in encode_decode.allChars():

		shifted_freq = dict()
		for q in sv_freq:
			shifted_freq[encrypt_decrypt.decryptChar(q,i)] = this_f[q]

		sum_ = distDict(dictNorm(shifted_freq),dictNorm(sv_freq))

		if best_v > sum_:
			best = i
			best_v = sum_

	return best

# Fast version of the keyguesser has been deprecated
# It only succeded 50% of the tests or so
# This means that the plaintext was still unlegible
# O(1)
# def fast(s,most_likely_char):
# (...)
# ---------------------------------------------------------

# guess a keyword based on key length m and string s and frequency table exp_freq
# string s the string to be decrypted
# int m the guessed length of the key
# dict(char,int) exp_freq a dict that acts as a frequency table for the guessed luangage of the cipher.
# return string the guessed key
def guess(s,m,exp_freq):
	parts = mod_split(s,m)
	
	key = ""
	for i in range(m):
		key += slow(parts[i],exp_freq)
	return key


# just some tests
def _main():

	file = open("in/vig_group13.crypto",'r').read()
	exp_freq = json.loads(open("Freqency Text/freq.json",'r').read())

	
	k = keylength_guess.keylength_guess_most_likely(file)
	print(k)
	key = guess(file,k,exp_freq)

	print(key) 
	print(encrypt_decrypt.decryptString(file,key))

		

# runs the tests if not imported.
if __name__ == '__main__':
	_main()
#! /usr/bin/env python3

import encode_decode
from operator import itemgetter

# Analyse a string and return the most likely keylength
# String s the string analysed
# int mini the minimum string length tested
# int maxi the maximum string length tested
# returns int the most likely keylength
def keylength_guess_most_likely(s,mini=2,maxi=16):
	res = []
	for i in range(mini,maxi+1):
		res += [(i,keylength_guess_friedman(s,i))]

	return max(res,key=itemgetter(1))[0]


# The friedman value of the string with keylength m
# String s the string analysed
# int m the tested keylength
# returns float the value
def keylength_guess_friedman(s,m):
	partitions = mod_split(s,m)

	#print(partitions)
	sum_ = 0
	for p in partitions:
		sum_ += IC(p)

	return (sum_/m)

# The string into diffrent substring, depending on their modulo
# string s the string to be split
# int m the amount of splits
# returns [string] the partitioned strings 
def mod_split(s,m):
	out = [""]*m
	for i in range(0,len(s)):
		out[i%m] += s[i]
	return out

# Calculates the index of coincidence for a string p
# string p the substring to be calulated
# returns float the IC value
def IC(p):
	sum_ = 0
	chars = [encode_decode.decodeInt(i) for i in range(32)]
	l = len(p)
	freq = gen_freq(p,chars)
	for i in chars:
		sum_ += freq[i]*(freq[i]-1)/(l*(l-1))
	return sum_

# makes a frequency dict of a string p
# string p the string
# [string] chars reused list of chars because they were already generated somewhere else
# returns dict(string,int) how many times any char occurs in the string p
def gen_freq(p,chars):
	d = dict([(c,0) for c in chars])
	for c in p:
		d[c] += 1
	return d


# Tests the current functions
def main():
	file = open("in/vig_group4.crypto").read()

	for m in range(2,17):
		print(m,end="\t")
		print(keylength_guess_friedman(file,m))

	print("Most likely:",keylength_guess_most_likely(file))

# Runs main() if not imported.
if __name__ == '__main__':
	main()

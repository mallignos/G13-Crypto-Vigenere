#! /usr/bin/env python3

import os
import json

def dict_incr(d,e):
	if e in d:
		d[e] += 1
	else:
		d[e] = 1

def remap(d):
	remap_rules = [ ('\n',None),
					('!','.'),
					('%',None),
					('&',None),
					("'",None),
					('(',None),
					(')',None),
					('*',None),
					('+',None),
					('-',None),
					('0',None),
					('1',None),
					('2',None),
					('3',None),
					('4',None),
					('5',None),
					('6',None),
					('7',None),
					('8',None),
					('9',None),
					(':',None),
					(';',None),
					('=',None),
					('?','.'),
					('[',None),
					(']',None),
					('\u00b0',None), #degree symbol
					('\u00bb',None), # >> symbol
					('\u00bd',None), # 1/2 symbol
					('\u00e0','a'),  # à 
					('\u00e6','a'),  # ae symbol
					('\u00e6','e'),  # ae symbol (again)
					('\u00e8','e'),  # è
					('\u00e9','e'),  # é
					('\u00fc','u')   # ü
					]

	# these two loops cannot be combined, because of the ae-rule
	for (o,n) in remap_rules:
		if n not in d:
			d[n] = 0
		d[n] += d[o]

	for (o,n) in remap_rules:
		if o in d:
			d.pop(o)

	return d

def main():
	freq = dict()
	for i in os.listdir('Text Files/'):
		s = open('Text Files/' + i).read().lower()
		for c in s:
			dict_incr(freq,c)
	remap(freq)
	print("Removed (",freq.pop(None),") diffrent characters")
	js = json.dumps(freq, indent=4,sort_keys=True)
	print(js)
	print("length:",len(freq))
	open("freq.json",'w').write(js)

if __name__ == '__main__':
	main()
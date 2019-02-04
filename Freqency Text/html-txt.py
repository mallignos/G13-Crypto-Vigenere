#! /usr/bin/env python3

import os

class HtmlReadError(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

def clean_tags(f):
	out = ""
	file = open(f,'r').read()
	ignore = False
	for c in file:
		if c == '<':
			if ignore:
				raise HtmlReadError("< found nested")
			else:
				ignore = True
		elif c == '>':
			if ignore:
				ignore = False
			else:
				raise HtmlReadError("> found before <")
		elif not ignore:
			out += c
	return out


def main():
	for i in os.listdir("HTML Files/"):
		s = clean_tags("HTML Files/" + i)
		f = open("Text Files/" + i[:-5] + ".txt",'w')
		f.write(s)
		f.close()

if __name__ == '__main__':
	main()
import os
import json

def dict_incr(d,e):
	if e in d:
		d[e] += 1
	else:
		d[e] = 1

def remap(d):
	pass

def main():
	freq = dict()
	for i in os.listdir('Text Files/'):
		s = open('Text Files/' + i).read().lower()
		for c in s:
			dict_incr(freq,c)
	remap(freq)
	js = json.dumps(freq,sort_keys=True, indent=4)
	print(js)
	open("freq.json",'w').write(js)

if __name__ == '__main__':
	main()
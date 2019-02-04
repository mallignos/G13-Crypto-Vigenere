import encode_decode

# string s, int l (guess length)
def keylength_guess_kasiski(s,l):
	fragments = dict()

	#maybe wrong range?
	for i in range(len(s)):
		
		w = s[i:i+l]
		
		if w in fragments:
			fragments[s[i:i+l]].append(i)
		else:
			fragments[s[i:i+l]] = [i]

	#print(fragments)
	for frag in fragments: 
		if len(fragments[frag]) > 2:
			d = diff(fragments[frag])
			print(frag,d)


def diff(lx):
	out = lx[1:]
	for i in range(len(lx)-1):
		out[i] -= lx[i]
	return out

def mod_split(s,m):
	out = [""]*m
	for i in range(0,len(s)):
		out[i%m] += s[i]
	return out

def keylength_guess_friedman(s,m):
	partitions = mod_split(s,m)

	#print(partitions)
	sum_ = 0
	for p in partitions:
		sum_ += IC(p)

	print(sum_/m)

def IC(p):
	sum_ = 0
	chars = [encode_decode.decodeInt(i) for i in range(32)]
	l = len(p)
	for i in chars:
		sum_ += freqency(p,i)*(freqency(p,i)-1)/(l*(l-1))
	return sum_

def freqency(s,c):
	f = 0
	for i in s:
		if c == i:
			f+=1
	return f


file = open("in/vig_group4.crypto").read()

for m in range(2,17):
	print(m,end="\t")
	keylength_guess_friedman(file,m)
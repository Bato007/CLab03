import random


small = ''
medium = ''
large = ''

def LCG(a, b, N):
	# a ≡ b(mod N)
	bitChain = '' 
	t = 16 # Binary concatenation cycle size
	k = 8 # Individual bitChain size
	size = 128992

	try:
		parse = list(map(int,[a, b, N])) # Parsing Verification
		a = parse[0]
		b = parse[1]
		N = parse[2]
	except:
		return "Something went wrong"
	
	x = random.randrange(200)%N # Randomized initial value

	for i in range(int(size/t)): 
		x = (a*x + b)%N 
		binary = bin(x).replace('b','').zfill(t)
		bitChain += binary

	return bitChain


small = LCG(6,55,11)
medium = LCG(612,5115,7212)
large = LCG(6,55,150)


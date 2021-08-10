import random


def LCG(a, b, N):
	# a ≡ b(mod N)
	bitChain = '' 
	t = 8 # Binary concatenation cycle size
	k = 8 # Individual bitChain size

	try:
		parse = list(map(int,[a, b, N])) # Parsing Verification
		a = parse[0]
		b = parse[1]
		N = parse[2]
	except:
		return "Something went wrong"
	
	x = random.randrange(200)%N # Randomized initial value

	for i in range(t): 
		x = (a*x + b)%N 
		binary = bin(x).replace('b','').zfill(k)
		bitChain += binary

	return bitChain

print(LCG(2,5,11))
print(LCG(6,55,29))
print(LCG(7,47,88))

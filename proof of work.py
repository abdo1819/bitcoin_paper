import string
import random
import hashlib
import time

examp_ch ='YuNkB4aAPeIR629Tj0p6phbYT'

def genration(challenge = examp_ch , size = 25):

	answer = ''.join(random.choice(string.ascii_lowercase +
				       string.ascii_uppercase +
				       string.digits ) for x in range(size)
			 	)
	
	atempt = challenge + answer

	return atempt,answer


def at_atempt():
	found = False

	start = time.time()
	while not found:
		atempt,answer = genration()
		sha = hashlib.sha256(atempt.encode())
		solution =sha.hexdigest()

		if solution.startswith('000'):
			print(solution)
			print('take',time.time()-start)
			
			found = True
	print (atempt)

at_atempt()


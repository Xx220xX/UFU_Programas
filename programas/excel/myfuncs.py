
import random
def gerarNumerosAleatorios(min,max, n):
	lt = []
	for i in range(n):
		lt.append(random.randint(min,max))
	return lt

def sortDict(dic):
	key = list(dic.keys())
	value = list(dic.values())
	for i in range(len(value)-1,0,-1):
		for j in range(i):
			if value[j] > value[j+1] or (value[j] == value[j+1] and key[j] > key[j+1]):
				value[j],value[j+1] = value[j+1],value[j]
				key[j],key[j+1] = key[j+1],key[j]
			
	return {key[i]:value[i] for i in range(len(value))} 
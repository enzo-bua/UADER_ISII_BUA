# prime number calculator: find all primes up to n
from datetime import datetime
#max = int(input("Trova numeri primi fino a quale numero? : "))
max = 20
primeList = []
#for loop for checking each number.
for x in range(2, max + 1):
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
print(primeList, "fecha: ", datetime.now())
#-------------------------------------------------------------
# prime number calculator: find the first n primes
#count = int(input("Trova quanti numeri primi?: "))
mostrar = 3
count = mostrar
primeList = []
x = 2
while len(primeList) < count:
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
	x += 1
print(primeList, "fecha: ", datetime.now())

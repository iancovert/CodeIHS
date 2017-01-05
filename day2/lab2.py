# A first version of the prime function. Are there some special cases where this fails?
def prime(n):
	for i in range(2, n):
		if (n % i == 0):
			return False
	return True

# A faster version of the prime function that doesn't check some unnecessary possible factors
def betterPrime(n):
	if (n == 2):
		return True
	if (n % 2 == 0):
		return False
	m = int(n ** 0.5)
	for i in range(3, m + 1):
		if (n % i == 0):
			return False
	return True

# Testing the prime function
print(prime(17))
print(prime(37))
print(betterPrime(1001))
print(betterPrime(10001))

numbers = [4, 5, 7, 13, 99]
for num in numbers:
    result = betterPrime(num)
    print(result)
# Solution
def calcFib(n):
	if n <= 1:									# Given values
		return n
	else:
		return calcFib(n - 1) + calcFib(n - 2)	# Calculate Fib(n > 1)

# Tests
answers = {\
    0: 0,
	1: 1,
	2: 1,
	3: 2,
	4: 3,
	5: 5,
	6: 8,
	7: 13,
	8: 21,
	9: 34,
	10: 55,
	20: 6765,
}

def testFunc():
	for k,v in answers.items():
		result = calcFib(k)
		if result != v:
			print("Test {} failed. {} was returned, the correct answer is {}".format(k, result, v))
		else:
			print("Fibonacci({}) = {}".format(k, result))

# Run
input = input("Please enter a non-negative integer: ")
try:
	n = int(input)
	if n < 0:
		raise ValueError

	result = calcFib(n)
	print("Fibonacci({}) = {}".format(n, result))
except ValueError:
	print("Sorry, {} is not a positive integer".format(input))

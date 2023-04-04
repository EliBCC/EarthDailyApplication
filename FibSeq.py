# Solution
def calcFib(n):
	if n <= 1:
		return n
	else:
		return calcFib(n - 1) + calcFib(n - 2)

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
	11: 89,
	12: 144,
	13: 233,
}

def testFunc():
	for k,v in answers.items():
		result = calcFib(k)
		if result is not v:
			print("Test {} failed. {} was returned, the correct answer is {}".format(k, result, v))
		else:
			print("The {}th Fibonacci number is {}".format(k, result))

testFunc()
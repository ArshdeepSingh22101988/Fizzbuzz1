#Task 0 which involves printing some words

for fizzBuzz in range(100):
	#takes the integer from 1 to 100
	#checking for the divisibility for both 3 nd 5  using the modulus and prnting the appropriate result
	if fizzBuzz%3 ==0 and fizzBuzz%5==O:
		print("fizzBuzz")
		continue
	#checks for the divisibility for 3 and printing Fizz
	elif fizzBuzz %3 ==0:
		print("Fizz")
		continue
	#checks for the divisibility for 5 and printing Buzz
	elif FizzBuzz%5==0:
		print("Buzz")
		continue
	print("FizzBuzz")

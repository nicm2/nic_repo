def igcd(num1, num2):
    if num1 > num2:
        x = num2
    else:
        x = num1
    for i in range(1, x + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i

    return gcd



class Gcd:
	def __init__(self, num1, num2):
		self.x = num1
		self.y = num2

	def __call__(self):
		if self.x > self.y:
			x = self.y

		if self.y > self.x:
			x = self.x

		for i in range(1, x+1):
			if self.x % i == 0 and self.y % i == 0:
				gcd = i
		return gcd

def tester():
	num = input("Imperative function: -i- or OOP function -o-")
	try:
		if num == 'i':
			print("The gcd of 60 and 48 is : ",end="")
			print(igcd(60,48))
		elif num == 'o':
			f = Gcd(60,48)
			print("The gcd of 60 and 48 is : ",end="")
			print(f())
	except:
		print("Sorry, something went wrong")


if __name__ == "__main__":
    tester()

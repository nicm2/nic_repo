{% include nav.html %}

# Data Structures Project

## Runtime
- [Replit Runtime](https://replit.com/@nicm21/nicrepo-3)
<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@nicm21/nicrepo-3?embed=true"></iframe>

## Key Learning (Tech Talks)
- Recursive sequences/functions are functions that call themselves to loop
- Ex: fibonacci
- While, for, and recursive loops to repeat code (while built in counter, for is specified)

Week 0: 
```py 
      try: 
        f = open("demofile.txt")
        try:
          f.wrtie("Lorum Ipsum")
        except:
          print("Something went wrong when writing to the file")
        finally:
          f.close()
      except:
        print("Something went wrong when opening the file")
  # use except and try to test when an error occur and keep the function running
```
  
Week 1:
```py

# Hack 1: List elements with embedded Dictionary

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "John",  
               "LastName": "Mortensen",  
               "DOB": "October 21",  
               "Residence": "San Diego",  
               "Email": "jmortensen@powayusd.com",  
               "Owns_Cars":["2015 Fusion","2011 Ranger","2003 Excursion","1997 F-350", "1969 Cadillac"]  
              })  

InfoDb.append({  
               "FirstName": "Sunny",  
               "LastName": "Naidu",  
               "DOB": "August 2",  
               "Residence": "San Diego",  
               "Email": "snaidu@powayusd.com",  
               "Owns_Cars":["A","B","C"]  
              })  
```
```py 
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)
        
# this is test driver or code that plays when executed directly, versus import which will not run these statements
def tester():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input
```
Week 2:

```py 
#init() function for classes which is executed when a class is called to assign initial values
class Fibonacci:
    def __init__(self):
        self.fiboSeq = [0, 1]
```
```py
# call function inside a class which makes it able to act as a regular function and call itself
    def __call__(self, n):
        if n < len(self.fiboSeq):
            return self.fiboSeq[n]
        else:
            # Compute the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2) # two recursive calls to self (__call__(self, n))
            self.fiboSeq.append(fib_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.fiboSeq[n]
```

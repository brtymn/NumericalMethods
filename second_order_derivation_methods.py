print("This script takes the second derivative of a function using three methods and showcases the results.\n")

def ForwardDifference(f, x, h):
	return (f(x + h + h) - 2 * f(x + h) + f(x)) / h ** 2

def BackwardDifference(f, x, h):
	return (f(x) - 2 * f(x - h) + f(x - h - h)) / h ** 2

def CentralDifference(f, x, h):
	return (f(x + h) - 2 * f(x) + f(x - h)) / h ** 2

## The function to be derived.
def TheFunction(x):
	return 2 * x ** 3 + 4 * x ** 2 - 5 * x

x = 1 ## This value does not matter. Chosen as "1" for simplicity.
h = 0.1

dydt_f = ForwardDifference(TheFunction, x, h)
dydt_b = BackwardDifference(TheFunction, x, h)
dydt_c = CentralDifference(TheFunction, x, h)


exact_derivation = 12 * x + 8 ## The exact derivation is written here manually to check the results of the difference methods.

print("Forward difference derivation result =", dydt_f)
print("Backward difference derivation result =", dydt_b)
print("Central difference derivation result =", dydt_c)
print("Exact derivation result  =", exact_derivation)

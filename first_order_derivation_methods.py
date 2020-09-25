print("This script takes the derivative of a function using three methods and showcases the results.\n")

def ForwardDifference(f, x, step_height):
	return (f(x + step_height) - f(x)) / step_height

def BackwardDifference(f, x, step_height):
	return (f(x) - f(x - step_height)) / step_height

def CentralDifference(f, x, step_height):
	return (f(x + step_height) - f(x - step_height)) / (2 * step_height)

## The function to be derived.
def TheFunction(x):
	return ((2 * (x ** 3)) + ((4 * (x ** 2)) - 5 * x))

x = 1 ## This value does not matter. Chosen as "1" for simplicity.
step_height = 0.1

dydt_forward = ForwardDifference(TheFunction, x, h)
dydt_backward = BackwardDifference(TheFunction, x, h)
dydt_central = CentralDifference(TheFunction, x, h)

## The exact derivation is written here manually to check the results of the difference methods.
exact_derivation = 6 * (x ** 2) + (8 * x) - 5

print("Forward difference derivation result =", dydt_forward)
print("Backward difference derivation result =", dydt_backward)
print("Central difference derivation result =", dydt_central)
print("Exact derivation result =", exact_derivation)

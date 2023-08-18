import math as m

def get_values(stack):
	b = stack[-1]
	stack.pop()
	a = stack[-1]
	stack.pop()
	return a, b



Operations = input().split()
stack = []

for item in Operations:
	try:
		N = int(item)
		stack.append(N)
	except:
		if item == "add":
			a, b = get_values(stack)
			stack.append(a + b)
		elif item == "sub":
			a, b = get_values(stack)
			stack.append(a - b)
		elif item == "mul":
			a, b = get_values(stack)
			stack.append(a * b)
		elif item == "div":
			a, b = get_values(stack)
			stack.append(a / b)
		elif item == "mod":
			a, b = get_values(stack)
			stack.append(a % b)
		elif item == "sqrt":
			stack[-1] = m.sqrt(stack[-1])


print(int(stack[0]))
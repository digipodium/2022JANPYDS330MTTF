# f(x) = x * 3 -3
# f(10)

# lambda
eq = lambda x: x * 3 - 3
# print(eq(10))


hyp = lambda p,b : (p**2 +b **2) ** .5
# print(hyp(3,4))

def exp(power):
    return lambda l: [i **power for i in l]

eq2 = exp(4)
print(eq2([1,2,3,4,5,6,7]))
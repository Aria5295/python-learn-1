
print(2**3) #2^3

def exp1(base, pow):
    print(base ** pow)

exp1(2, 3)

def exp(base, pow):
    result = 1
    for index in range(pow):
        result = result * base
    return result

print(exp(3,4))
import random

def generate_name(n,s):
    return random.choice(n)+" "+random.choice(s)

names = ['Alex','Helen','Sarah','William']
surnames = ['Chapman','West','Mayer','Shakespeare']

print(generate_name(names,surnames))
print(generate_name(names,surnames))
print(generate_name(names,surnames))
print(generate_name(names,surnames))
print(generate_name(n=names,s=surnames))
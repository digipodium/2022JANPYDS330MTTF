# functions that will display all the factors of a number

# num = 20 
# for i in range(1,num+1):
#     if num % i == 0:
#         print(i,end=',')


def get_factors(num):
    f = []
    for i in range(1,num+1):
        if num % i == 0:
            f.append(i)
    return f

# calling
x = int(input('enter a number:'))
print(f'{x} factors are {get_factors(x)}')
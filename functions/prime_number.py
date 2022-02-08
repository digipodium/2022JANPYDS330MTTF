# number that are only completely divisible by one and themselves

def check_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True
   

# calling the function
print("is number 12 prime?",check_prime(12))
print("is number 13 prime?",check_prime(13))
print("is number 15 prime?",check_prime(15))

out = check_prime(192032)
if out:
    print("great")
else:
    print('meh')
print()


def gcd_fun(x, y): 
    if(y == 0): # it divide every number 
        return x  # return x 
    else: 
        return gcd_fun(y, x % y) 


def find_hcf(a,b): 
    while(b): 
        print(f'На входе {a=} и {b=}')
        a, a = b, a % b 
        print(f'На выходе {a=} и {b=}')
        return a 


a = find_hcf(100, 3)
print(a)


a, b = 10, 17%3

print (a, b)
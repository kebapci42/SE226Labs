import math
# Recursive factorial method
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
        
#print(factorial(5))

# Sin(x) formula
def sine_x():
    n = int(input("Enter an approximation limit (n): "))
    x = int(input("Enter an angle in degrees (x): "))
    x = (x * math.pi) / 180.0 # 180 degrees is pi radians
    res = 0
    for i in range(n+1):
        res += (lambda y : ((-1)**i) * (x**(2*i + 1)) / factorial(2*i + 1))(i)

    return res

#print(sine_x())


# The sum goes to 1/n
ans = 0  # Answer will be added later
def sum_till_one_over_n(n):
    ''' Function takes a positive integer and 
        adds all the numbers (as 1/number) till 1/n,
        and returns nothing for some reasons(?)
    '''
    global ans  # Make ans global
    if n > 0:
        ans += 1 / n
        sum_till_one_over_n(n - 1)


#sum_till_one_over_n(6)
#print(ans)
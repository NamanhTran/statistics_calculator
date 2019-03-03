from math import *

def irq(q3, q1):
    return q3 - q1

def quartiles(arr):
    percent = 0

    arr.sort()

    quarters = []
    
    while percent <= 100:
        temp = (percent / 100) * len(arr)
        if temp.is_integer():
            if temp == len(arr):
                quarters.append(arr[int(temp) - 1])

            elif temp == 0:
                quarters.append(arr[int(temp)])

            else:
                quarters.append(mean([arr[int(temp) - 1], arr[int(temp)]]))

        else:
            quarters.append(arr[ceil(temp) - 1])

        percent = percent + 25
    
    _irq = irq(quarters[3],quarters[1])

    upperFence = quarters[3] + (_irq * 1.5)
    lowerFence = quarters[1] - (_irq * 1.5)

    print(f"Q0: {quarters[0]}\nQ1: {quarters[1]}\nQ2: {quarters[2]}\nQ3: {quarters[3]}\nQ4: {quarters[4]}\nIRQ: {_irq}\nIRQ x 1.5: {_irq*1.5}\nLower Fence: {lowerFence}\nUpper Fence: {upperFence}")

    

def mean(arr):
    size = 0
    total = 0
    for i in arr:
        total = total + i
        size = size + 1
    return total / size

def z_score(x, mew, std_div):
    return (x - mew) / std_div

def choose(a,b):
    return factorial(a)/(factorial(b) * factorial(a - b))

def binom_prob(n, k, p):
    return choose(n, k) * p**k * (1 - p)**(n-k)

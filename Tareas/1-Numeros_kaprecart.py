#from functools import cache, lru_cache
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Process
import time

#@lru_cache(maxsize=10)
def get_digits(x, b):
    digits = []
    while x > 0:
        digits.append(x % b)
        x = x // b
    return digits

def form_number(digits, b):
    result = 0
    for i in range(0, len(digits)):
        result = result * b + digits[i]
    return result

#@cache
#@lru_cache(maxsize=500)
def kaprekar_map(x, b):
    descending = form_number(sorted(get_digits(x, b), reverse=True), b)
    ascending = form_number(sorted(get_digits(x, b)), b)
    return descending - ascending

def kaprekar_cycle(x, b):
    x = int (str(x), b)
    seen = []
    while x not in seen:
        seen.append(x)
        x = kaprekar_map(x, b)
    cycle = []
    while x not in cycle:
        cycle.append(x)
        x = kaprekar_map(x, b)
    return cycle

def execute(i):
    new = []
    new = kaprekar_cycle(i, 10)
    
    return sorted(new)

pool = ThreadPool(16)
def main():
    cycles = []
    new = []
    #for i in range(500000000,999999999): #(10000000,99999999)
    for i in range(100000,999999):
        new.append(i)

    '''
    start = time.time()
    for i in new:
        cycles.append(execute(i))
    end = time.time()
    '''


    start = time.time()
    cycle = pool.map(execute, new)
    end = time.time()

    print(end - start)
    res = []
    [res.append(x) for x in cycles if x not in res]
    print(res)




if __name__ == '__main__':
    main()
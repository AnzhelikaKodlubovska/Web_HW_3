import time
from multiprocessing import Pool, cpu_count

def factorize_sync(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_multi(numbers):
    with Pool(cpu_count()) as pool:
        factors_multi = pool.map(factorize_sync, numbers)
    return factors_multi

def factorize(*numbers):
    return factorize_multi(numbers)

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    start_time = time.time()
    factors_sync = [factorize_sync(num) for num in numbers]
    end_time = time.time()
    print("Час виконання синхронної версії:", end_time - start_time)

    start_time = time.time()
    factors_multi = factorize(*numbers)
    end_time = time.time()
    print("Час виконання версії з використанням багатоядерних процесів:", end_time - start_time)

    a, b, c, d = factors_multi
    assert a == factors_sync[0]
    assert b == factors_sync[1]
    assert c == factors_sync[2]
    assert d == factors_sync[3]

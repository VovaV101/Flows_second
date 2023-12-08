import time
from multiprocessing import Pool, cpu_count

def factorize_sync(numbers):
    result = []
    for num in numbers:
        factors = [i for i in range(1, num + 1) if num % i == 0]
        result.append(factors)
    return result

def factorize_parallel(numbers):
    with Pool(cpu_count()) as pool:
        result = pool.map(factorize_single, numbers)
    return result

def factorize_single(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def factorize(*numbers):
    result = []
    for num in numbers:
        factors = [i for i in range(1, num + 1) if num % i == 0]
        result.append(factors)
    return result

if __name__ == '__main__':
    # Тестові дані (список чисел)
    input_numbers = [128, 255, 99999, 10651060]

    # Вимір часу для синхронної версії
    start_time = time.time()
    result_sync = factorize_sync(input_numbers)
    end_time = time.time()
    execution_time_sync = end_time - start_time

    print("Синхронна версія:")
    print("Результат:", result_sync)
    print("Час виконання:", execution_time_sync, "секунд")

    # Вимір часу для паралельної версії
    start_time = time.time()
    result_parallel = factorize_parallel(input_numbers)
    end_time = time.time()
    execution_time_parallel = end_time - start_time

    print("\nПаралельна версія:")
    print("Результат:", result_parallel)
    print("Час виконання:", execution_time_parallel, "секунд")

    # Перевірка з використанням тестів
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

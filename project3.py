stop_range = int(input())
num_divisors = int(input())

for i in range(10, stop_range): 
    digits_sum = sum([int(digit) for digit in str(i)]) 
    if digits_sum ** 2 == i: 
        print(i) 

for i in range(10, stop_range): 
    div_count = 0 
    for j in range(1, i + 1): 
        if i % j == 0: 
            div_count += 1 
    if div_count == num_divisors: 
        print(i)
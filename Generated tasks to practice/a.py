def sum_even_numbers(n):

    total = 0

    for num in range(2, n+1, +2):
        if num % 2 == 0:
            total += num
        else:
            continue
        
    return total

print(sum_even_numbers(int(input("Please enter a number until all even numbers should be summed: "))))
def most_frequent(numbers):
    if not numbers:
        return None
    freq = {}
    for number in numbers:
        freq[number] = freq.get(number, 0) + 1

    best = numbers[0]
    for numbr in numbers:
        if freq[number] > freq[best]:
            best = number
    return best

num = (most_frequent([2, 5, 2, 8, 2, 5]))  
print(num)              

def move_zeros(numbers):
    pos = 0
    for number in numbers:
        if number != 0:
            numbers[pos] = number
            pos += 1
    while pos < len(numbers):
        numbers[pos] = 0 
        pos += 1

b = [0, 1, 0, 3, 12]
move_zeros(b) 
print(b)              
def insert_sort(numbers):
    """Implementa el algortimo Insertion Sort"""
    
    for pos_key in range(1, len(numbers)):
        key = numbers[pos_key]
        previous_pos = pos_key - 1
        
        while previous_pos >= 0 and numbers[previous_pos] > key:
            numbers[previous_pos + 1] = numbers[previous_pos]
            previous_pos -=1
            
        numbers[previous_pos + 1] = key
    
    return numbers


numbers = insert_sort([6, 2, 1, 7, 5, 2, 3, 4, 56, 12, 14, 13])
print(numbers)
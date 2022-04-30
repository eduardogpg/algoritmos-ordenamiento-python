def bubble_sort(numbers):
    """Implementa el algoritmo de ordenamiento Burbuja"""

    swap = True
    
    while swap:
        
        swap = False
        
        for pos in range(0, len(numbers) -1):
            current_number = numbers[pos]
            next_number = numbers[pos + 1]
            
            if current_number > next_number:
                swap = True
                
                numbers[pos] = next_number
                numbers[pos + 1] = current_number
    
    return numbers
    
numbers = bubble_sort([6, 5, 8, 7, 4])
print(numbers)
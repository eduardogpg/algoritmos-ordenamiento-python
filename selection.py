def selection_sort(numbers):
    """Implementa el Algoritmo Selection Sort"""
    
    for pos_market in range(0, len(numbers) -1):
        
        for pos in range(pos_market + 1, len(numbers)):
            
            if numbers[pos_market] > numbers[pos]:
                numbers[pos_market], numbers[pos] = numbers[pos], numbers[pos_market]
        
    return numbers
        
numbers = selection_sort([6, 8, 7, 1, 0, 15, 12, 2, 3, 4, 5])
print(numbers)
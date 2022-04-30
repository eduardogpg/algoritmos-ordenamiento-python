def quick_sort(numbers):
    """Implementa el algoritmo de ordenamiento Quick Sort"""
    
    if len(numbers) < 2:
        print(numbers)
        return numbers
    
    pivot = numbers[-1]
    smaller, equal, large = [], [], []
    
    for number in numbers:
        
        if number < pivot:
            smaller.append(number)
        
        if number == pivot:
            equal.append(number)
            
        if number > pivot:
            large.append(number)
            
    
    return quick_sort(smaller) + equal + quick_sort(large)


numbers = quick_sort([1, 3, 9, 8, 6, 2, 5])
print(numbers)
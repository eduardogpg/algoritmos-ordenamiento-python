def merge_sort(numbers):
    """Implementa el algoritmo Merge Sort"""
    
    if len(numbers) == 1:
        print(numbers)
        return numbers
    
    mid = len(numbers) // 2
    
    left = numbers[:mid]
    right = numbers[mid:]
    
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    sorted = []
    
    l = 0
    r = 0
    
    while l < len(left) and r < len(right):
        
        if left[l] < right[r]:
            sorted.append(left[l])
            l += 1
        else:
            sorted.append(right[r])
            r += 1
    
    sorted.extend(left[l:])
    sorted.extend(right[r:])
    
    return sorted
    
numbers = merge_sort([6, 3, 8, 1, 4, 7, 10])
print(numbers)
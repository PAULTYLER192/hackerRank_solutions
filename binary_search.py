#recursive binary search
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Base case: Target not found

    mid = (low + high) // 2  # Find the middle index

    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)  # Search right half
    else:
        return binary_search_recursive(arr, target, low, mid - 1)  # Search left half
        
#iterative binary search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half

    return -1  # Target not found
    
    
# Test array (sorted)
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Target to search
targets = [7, 14, 1, 19, 20]

# Iterative Test
print("Iterative Binary Search:")
for target in targets:
    result = binary_search(arr, target)
    print(f"Target {target}: {'Found at index ' + str(result) if result != -1 else 'Not found'}")

# Recursive Test
print("\nRecursive Binary Search:")
for target in targets:
    result = binary_search_recursive(arr, target, 0, len(arr) - 1)
    print(f"Target {target}: {'Found at index ' + str(result) if result != -1 else 'Not found'}")
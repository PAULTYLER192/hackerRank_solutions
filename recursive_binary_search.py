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
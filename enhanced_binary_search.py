def binary_search_with_closest(arr, target):
    if not arr:
        return {"position": -1, "closest": None, "comparisons": 0}

    low, high = 0, len(arr) - 1
    closest, comparisons = None, 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        # Update closest value
        if closest is None or abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]

        if arr[mid] == target:
            return {"position": mid, "closest": arr[mid], "comparisons": comparisons}
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return {"position": -1, "closest": closest, "comparisons": comparisons}

# Test array (sorted)
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Enhanced Test
enhanced_targets = [7, 14, 2, 20]
print("\nEnhanced Binary Search:")
for target in enhanced_targets:
    result = binary_search_with_closest(arr, target)
    print(f"Target {target}: {result}")
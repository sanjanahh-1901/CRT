#Merge Sort
#Merging 2 unsorted subarrays into a single sorted array
def merge(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    # Append any remaining elements from either list
    res.extend(left[i:])
    res.extend(right[j:])
    return res
print(merge([38, 27, 43], [3, 9, 82, 10])) # [3, 9, 10, 27, 38, 43, 82]

#Recursive merge sort function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)
print(merge_sort([38, 27, 43, 3, 9, 82, 10])) # [3, 9, 10, 27, 38, 43, 82]





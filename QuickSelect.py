#QuickSelect.py
#This algorithm is supposed to find the nth smallest element in a list.

def partition(arr, start, end, n):
    # For simplicity, let's make the pivot the last element
    # this is right from quicksort.
    pivot = arr[end]
    follower = leader = start
    # Leader will move faster than the follower. Therefore, this is the break condition
    while leader < end:
        if arr[leader] <= pivot:
            arr[follower], arr[leader] = arr[leader], arr[follower]
            follower += 1
        leader += 1

    arr[follower], arr[end] = arr[end] , arr[follower]
    return follower # this is the index where the partition is now. To the left, everything is smaller and vice versa

def quickSelect(arr, left, right, n):
    if left == right:
        # This is the base case.
        # Here, there is nothing to select, so we return the element within the bounds
        return arr[left]

    if arr == None or len(arr) < 1:
        return None
    part = partition(arr, left, right, n)

    if n == part:
        # Return the partition as the partition is in the right spot in the list
        return arr[part]
    elif n < part:
        return quickSelect(arr, left, part-1, n)
    else:
        return quickSelect(arr, part + 1, right, n - part)

# This is just an easy interface to use quick select.
# n is now the nth element, not index (i.e. 1 is the smallest)
def nthSmallest(arr, n):
    if n < 1 or arr == None or len(arr) < n:
        return None
    return quickSelect(arr, 0, len(arr) - 1, n - 1)

print(nthSmallest([5,2,3,1], 0))







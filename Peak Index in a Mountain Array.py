#arr = [0, 10, 50, 2]

def fun(arr):
    left = 0 
    right = len(arr) - 1
    while left < right :
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
print(fun([0, 10, 50, 20, 51, 10]))
n, key = map(int, input().split())
array = []
for _ in range(n):
    element = int(input())
    array.append(element)
def binary_search(array, key):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == key:
            return mid
        elif key < array[mid]:
             high = mid - 1
        else:
            low = mid + 1
    return -1
result = binary_search(array, key)
if result == -1:
    print(f"{key} is not found in the array.")
else:
    print(f"{key} is found at index {result}.")
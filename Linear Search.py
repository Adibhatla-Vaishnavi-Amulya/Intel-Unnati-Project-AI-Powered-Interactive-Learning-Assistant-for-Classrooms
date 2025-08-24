n, key = map(int, input().split())
array = []
for _ in range(n):
    element = int(input())
    array.append(element)
def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1
result = linear_search(array, key)
if result == -1:
    print(f"{key} is not found in the given array.")
else:
    print(f"{key} is found at index {result}.")
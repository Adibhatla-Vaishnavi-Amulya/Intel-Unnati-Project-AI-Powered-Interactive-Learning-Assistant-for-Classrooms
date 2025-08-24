n = int(input())
array = []
for _ in range(n):
    element = int(input())
    array.append(element)
def selection_sort(array):
    for i in range (len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j] <  array[min]:
                min = j
        if min != i:
            array[i], array[min] = array[min], array[i]
    return array
print(f"Sorted array is {selection_sort(array)}.")
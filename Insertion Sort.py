n = int(input())
array = []
for _ in range(n):
    element = int(input())
    array.append(element)
def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp
    return array
print(f"Sorted array is {insertion_sort(array)}.")
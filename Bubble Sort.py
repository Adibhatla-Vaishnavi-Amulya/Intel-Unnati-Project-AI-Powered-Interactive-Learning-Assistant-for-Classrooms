n = int(input())
array = []
for _ in range(n):
    element = int(input())
    array.append(element)
def bubble_sort(array):
    for i in range(len(array)-1):
        flag = False
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        if flag == False:
            break
    return array
print(f"Sorted array is {bubble_sort(array)}.")
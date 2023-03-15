import time

########### Selection Sort #############
def selection_sort(arr):
    for step in range(len(arr)):
        min_idx = step
        for i in range(step + 1, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])

########### Insertion Sort #############
def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr;

########### Bubble Sort #############
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1, i, -1):
            if arr[i]>arr[j]:
                aux = arr[j]
                arr[j] = arr[i]
                arr[i] = aux
    return arr

########### Merge Sort #############
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

########### Quick Sort #############
def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[r]) = (arr[r], arr[i + 1])
    return i + 1

def quick_sort(arr, l, r):
    if l < r:
        pi = partition(arr, l, r)
        quick_sort(arr, l, pi - 1)
        quick_sort(arr, pi + 1, r)

########### Heap Sort #############
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)

########### Counting Sort #############
def counting_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(0, len(arr)):
        count_arr[arr[i] - min_element] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
    return arr

########### Radix Sort #############
def counting_sort_radix(arr, digit):
    size = len(arr)
    output = [0] * size
    count = [0] * 10
    for i in range(size):
        ind = arr[i] // digit
        count[ind % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        ind = arr[i] // digit
        output[count[ind % 10] - 1] = arr[i]
        count[ind % 10] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

def radix_sort(arr):
    max_element = max(arr)
    digit = 1
    while max_element // digit > 0:
        counting_sort_radix(arr, digit)
        digit *= 10

########### Bucket Sort #############
def bucket_sort(arr):
    nrbuck = 10
    max_ele = max(arr)
    min_ele = min(arr)
    vals = (max_ele - min_ele) / nrbuck
    temp = []
    for i in range(nrbuck):
        temp.append([])
    for i in range(len(arr)):
        aux = (arr[i] - min_ele) / vals - int((arr[i] - min_ele) / vals)
        if (aux == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele) / vals) - 1].append(arr[i])
        else:
            temp[int((arr[i] - min_ele) / vals)].append(arr[i])
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
    k = 0
    for list in temp:
        if list:
            for i in list:
                arr[k] = i
                k = k + 1

###### Main ######
arr=[]
with open("list44.txt", "r") as f:
    line = f.readline()
    cn = line.split(" ")
    for i in cn:
        arr.append(int(i))
tstart = time.time()
ptstart = time.process_time()

#### function call #####
bucket_sort(arr)
########################


tend = time.time()
ptend = time.process_time()
tres = tend - tstart
ptres = ptend - ptstart
with open("listout.txt", "w") as fout:
    for i in arr:
        fout.write(str(i)+" ")
with open("listout.txt", "a") as fout:
    fout.write("\n")
    fout.write("Time: {:.7f}\n".format(tres))
    fout.write("Process Time: {:.7f}\n".format(ptres) )

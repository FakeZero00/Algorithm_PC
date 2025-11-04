array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227,
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3,
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92,
       83,     100,      94,      40,       5,     458,     364,      26,      64,     635,
       90,     489,      72,     504,      88,      97,     226,     218,     186,     268,
]

def sort_bubble(arr):
    print('=' * 60)
    print(f'before: {arr}')

    length = len(arr)
    for count in range(length - 1):
        for i in range(length - count - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print(f'after : {arr}')

def sort_select(arr):
    print('=' * 60)
    print(f'before: {arr}')

    length = len(arr)
    count = 0
    while count < length:
        min = count
        for i in range(count + 1, length):
            if arr[i] < arr[min]:
                min = i
        arr[min], arr[count] = arr[count], arr[min]
        count += 1

    print(f'after : {arr}')

def sort_insert(arr):
    print('=' * 60)
    print(f'before: {arr}')

    length = len(arr)
    for count in range(1, length):
        temp = arr[count]
        i = count
        while i > 0:
            if arr[i - 1] > temp:
                arr[i] = arr[i - 1]
            else:
                break
            i -= 1
        arr[i] = temp

    print(f'after : {arr}')

def sort_shell(arr):
    print('=' * 60)
    print(f'before: {arr}')

    GAPS = [23, 10, 4, 1]
    length = len(arr)
    for gap in GAPS:
        for start in range(gap, length):
            temp = arr[start]
            temppos = start
            while temppos >= gap:
                if arr[temppos - gap] > temp:
                    arr[temppos] = arr[temppos - gap]
                    temppos -= gap
                else:
                    break
            arr[temppos] = temp

    print(f'after : {arr}')

def heapify(root, size, arr):
    left_child = 2 * root + 1
    if left_child >= size: return
    compare_child = left_child

    right_child = 2 * root + 2
    if right_child < size:
        if arr[left_child] < arr[right_child]:
            compare_child = right_child

    if arr[root] < arr[compare_child]:
        arr[root], arr[compare_child] = arr[compare_child], arr[root]
        heapify(compare_child, size, arr)

def sort_heap(arr):
    print('=' * 60)
    print(f'before: {arr}')

    length = len(arr)
    last_parent_index = length // 2 - 1
    for i in range(last_parent_index, -1, -1):
        heapify(i, length, arr)

    last_sort_index = length - 1
    for i in range(last_sort_index, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(0, i, arr)

    print(f'after : {arr}')

def merge(arr, left, right, end):
    merged = []
    l, r = left, right
    while l < right and r <= end:
        if arr[l] <= arr[r]:
            merged.append(arr[l])
            l += 1
        else:
            merged.append(arr[r])
            r += 1

    while l < right:
        merged.append(arr[l])
        l += 1

    while r <= end:
        merged.append(arr[r])
        r += 1

    arr[left : end + 1] = merged

def sort_merge(arr, left, end):
    if left >= end: return

    middle = (left + end) // 2
    sort_merge(arr, left, middle)
    sort_merge(arr, middle + 1, end)
    merge(arr, left, middle + 1, end)

def partition(arr, left, right):
    arr[0], arr[(left + right) // 2] = arr[(left + right) // 2], arr[0]

    l, r = left, right + 1
    while True:
        while True:
            l += 1
            if l > r: break
            if l > right or arr[l] > arr[0]: break

        while True:
            r -= 1
            if r < l: break
            if r < left or arr[r] < arr[0]: break

        if l >= r: break
        arr[l], arr[r] = arr[r], arr[l]

    if left != r:
        arr[0], arr[r] = arr[r], arr[0]

    return r

def sort_quick(arr, left, right):
    if left >= right: return

    pivot = partition(arr, left, right)
    sort_quick(arr, left, pivot)
    sort_quick(arr, pivot + 1, right)

def main():
  sort_bubble(array[:])
  sort_insert(array[:])
  sort_select(array[:])
  sort_shell(array[:])
  sort_heap(array[:])
  sort_merge(array[:], 0, len(array) - 1)
  sort_quick(array[:], 0, len(array) - 1)

if __name__ == '__main__':
  main()
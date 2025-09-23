array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227,
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3,
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92,
       83,     100,      94,      40,       5,     458,     364,      26,      64,     635,
       90,     489,      72,     504,      88,      97,     226,     218,     186,     268,
]


def Heapify(root, size, arr):
    left_child = 2 * root + 1
    if left_child >= size: return
    compare_child = left_child

    right_child = 2 * root + 2
    if right_child < size:
        if arr[right_child] > arr[left_child]:
            compare_child = right_child

    if arr[root] < arr[compare_child]:
        arr[root], arr[compare_child] = arr[compare_child], arr[root]
        Heapify(compare_child, size, arr)


def HeapSort(arr):
    print(f"before : {arr}")

    count = len(arr)
    last_parent_index = count // 2 - 1
    for n in range(last_parent_index, -1, -1):
        Heapify(n, count, arr)

    last_sort_index = count - 1
    while last_sort_index > 0:
        arr[0], arr[last_sort_index] = arr[last_sort_index], arr[0]
        Heapify(0, last_sort_index, arr)
        last_sort_index -= 1

    print(f"after : {arr}")

def CountSort(arr):
    print(f"before : {arr}")

    max_value = max(arr)
    count = [0] * (max_value + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(max_value):
        count[i + 1] += count[i]

    result = [None] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        value = arr[i]
        at = count[value] - 1
        count[value] -= 1
        result[at] = value

    print(f"after : {result}")

if __name__ == '__main__':
    HeapSort(array[:])
    CountSort(array[:])
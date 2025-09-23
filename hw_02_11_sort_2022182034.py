array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,     635, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,     268, 
]

def heapify(root, size, arr):
    left_child = 2 * root + 1
    if left_child >= size: return
    compare_child = left_child

    right_child = 2 * root + 2
    if right_child < size:
        if arr[right_child] > arr[left_child]:
            compare_child = right_child

    if arr[compare_child] > arr[root]:
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
    while last_sort_index > 0:
        arr[0], arr[last_sort_index] = arr[last_sort_index], arr[0]
        heapify(0, last_sort_index, arr)
        last_sort_index -= 1

    print(f'after : {arr}')

def main():
  sort_heap(array[:])

if __name__ == '__main__':
  main()


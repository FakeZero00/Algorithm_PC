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
  for count in range(length - 1):
      min = arr[count]
      for i in range(count + 1, length):
          if arr[i] < min:
              min = arr[i]
              arr[i], arr[count] = arr[count], arr[i]
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
            i = start
            while i >= gap:
                if arr[i - gap] > temp:
                    arr[i] = arr[i - gap]
                    i -= gap
                else:
                    break
            arr[i] = temp

    print(f'after : {arr}')

def main():
  sort_bubble(array[:])
  sort_insert(array[:])
  sort_select(array[:])
  sort_shell(array[:])

if __name__ == '__main__':
  main()


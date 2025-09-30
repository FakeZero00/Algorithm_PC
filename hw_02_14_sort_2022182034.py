from _pyrepl.commands import end

names = [

    "임성진",

    "김민준", "이도현", "박서준", "정현우", "최지호",

    "장우진", "윤태현", "조민성", "오준호", "한시우",

    "김서연", "이지민", "박하윤", "정다은", "최예린",

    "장수아", "윤지아", "조하늘", "오소율", "한은채",

    "서지후", "배도윤", "임하람", "강유진", "노은서",

    "문채린", "신예준", "류아린", "홍지호", "곽서현"

]

def sort_insert(arr, start, end_inclusive):
    length = end_inclusive + 1
    for count in range(start + 1, length):
        temp = arr[count]
        i = count
        while i > 0:
            if arr[i - 1] > temp:
                arr[i] = arr[i - 1]
            else:
                break
            i -= 1
        arr[i] = temp

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

def sort_merge(arr, start, end_inclusive):
    if end_inclusive <= start: return
    if end_inclusive == start + 5:
        sort_insert(arr, start, end_inclusive)
        return

    middle = (start + end_inclusive) // 2
    sort_merge(arr, start, middle)
    sort_merge(arr, middle + 1, end_inclusive)
    merge(arr, start, middle + 1, end_inclusive)

def partition(arr, left, right):
    middle = (left + right) // 2
    pivot = middle
    if arr[left] > arr[middle]:
        if arr[middle] > arr[right] : pivot = middle
        elif arr[left] > arr[right] : pivot = right
        else : pivot = left
    else:
        if(arr[left] > arr[right]) : pivot = left
        elif(arr[middle] > arr[right]) : pivot = right
        else : pivot = middle
    pivot_data = arr[pivot]

    p, q = left, right + 1

    while True:
        while True:
            p += 1
            if p > right or arr[p] > pivot_data: break

        while True:
            q -= 1
            if q < left or arr[q] < pivot_data: break

        if p >= q: break

        

def sort_quick(arr, start, end_inclusive):
    if end_inclusive <= start: return
    if end_inclusive == start + 5:
        sort_insert(arr, start, end_inclusive)
        return

    pivot = partition(arr, start, end_inclusive)
    sort_quick(arr, start, pivot - 1)
    sort_quick(arr, pivot + 1, end_inclusive)

def main():
    last = len(names) - 1
    sort_insert(names[:], 0, last)

    arr = names[:]
    print('=' * 60)
    print(f'ME< {arr}')
    sort_merge(arr, 0, last)
    print(f'ME> {arr}')

    arr = names[:]
    print('=' * 60)
    print(f'QU< {arr}')
    sort_quick(arr, 0, last)
    print(f'QU> {arr}')

    print(f'My name index = {arr.index(names[0])}')

if __name__ == '__main__':
  main()


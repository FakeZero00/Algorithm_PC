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
  print('=' * 60)
  print(f'before: {arr}')
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
  print(f'after : {arr}')

def main():
    last = len(names) - 1
    sort_insert(names[:], 0, last)

if __name__ == '__main__':
  main()


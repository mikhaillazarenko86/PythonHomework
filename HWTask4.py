s = int(input())
if s % 6 == 0:
    j = ((s // 6), ((s // 6) * 4), (s // 6))
    print(j)
else:
    print('Неверное s')
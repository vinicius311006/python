a = []
b = []
for contador in range(10):
     a.append(int(input('digite um numero: ')))
     if contador % 2 == 0:
          b.append(a[contador] * 5)
     else:
          b.append(a[contador] + 5)     

for contador in range(len(a)):
     print(f'{a[contador]} = {b[contador]}')


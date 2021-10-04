"""exemplu 1
"""
n = int(input("Introdu n: \n"))
s=0
for i in range(1,n+1):
  p=1
  for j in range(1,i+1):
    p *= j
  s += p
print('Suma = ', s)
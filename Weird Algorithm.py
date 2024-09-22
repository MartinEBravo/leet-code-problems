n = int(input())
list = []
while n != 1:
    list.append(n)
    if n % 2 == 0:
        n = n / 2
    else:
        n = n*3 + 1
list.append(1)
secuencia = ''
for i in list:
    secuencia += str(int(i)) + ' '
print(secuencia[:-1])

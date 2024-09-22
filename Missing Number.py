a = int(input())
b = input()
b = b.split(' ')
b.sort()
num = list(range(1,a+1))
lista = list(map(str,num))
for i in range(a):
    if b[i] != lista[i]:
        print(lista[i])
        break

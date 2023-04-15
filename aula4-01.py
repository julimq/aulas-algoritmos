ant = 0
preant = 1
n = int(input("Escreva seu numero: "))
for n in range(1,n+1):
    num = preant + ant
    preant = ant 
    ant = num
    print(num)

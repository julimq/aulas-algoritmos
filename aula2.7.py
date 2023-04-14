num = int(input("Escolha um número: "))
if num < 2:
    print(num, "Não é um número primo.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "Esse número não é primo.")
            break
    else:
         print(num, "Esse número é primo.") 
       
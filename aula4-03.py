n = int(input("Digite o número de termos desejados: "))

soma = 0 

m = 1 

for i in range(1, n+1):
    soma += i / m 
    m += 2
    
print("A soma dos", n, "termos da série é: ", soma)

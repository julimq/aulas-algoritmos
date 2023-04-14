SALARIO_INICIAL = float(input("Seu salário inical: "))
ANO_INICIAL = 2005
ANO_ATUAL = 2023

salario_2006 = SALARIO_INICIAL * 1.015


percentual_aumento = 0.03 
salario_anterior = salario_2006
ano_atual = 2007

while ano_atual <= ANO_ATUAL:
    salario_atual = salario_anterior * (1 + percentual_aumento)
    percentual_aumento *= 2 
    salario_anterior = salario_atual
    ano_atual += 1


print(f"O salário atual do funcionário é de R${salario_atual:.2f}")
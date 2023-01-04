import math

avista = float(input('Informe o valor a vista: '))
capital = float(input('Informe o valor a prazo: '))
taxa = (float(input('Informe a taxa de juros anual: '))/ 12) / 100
tempo = 1 # 1 mês = 1 ano / 12 meses
juros = 0
vezes = int(input('Informe a quantidade de vezes a prazo (se for sem juros): '))

divisao = capital / vezes
diferenca =  capital - avista

for i in range(vezes):
    montante = capital * math.pow((1 + taxa), tempo)
    juros = juros + (montante - capital)
    capital -= divisao

print('')
    
if juros > diferenca:
    print('Vale a pena comprar a prazo')
    print(f'Comprando a prazo você economizaria {round(juros - diferenca, 2)} reais')
else:
    print('Vale a pena comprar a vista')
    print(f'Comprando a vista você economizaria {round(diferenca - juros, 2)} reais')

print('O valor da diferença é de:', round(diferenca, 2))
print('O valor de juros é de:', round(juros, 2))
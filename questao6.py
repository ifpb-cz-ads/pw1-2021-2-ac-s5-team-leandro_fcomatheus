valorCasa = float(input('Informe o valor da casa:'))
salario = float(input('Informe o seu salário:'))
anos = float(input('Informe a quantidade de anos para pagar:'))
limitePrestacao = (salario*30)/100
meses = 12*anos
valorPrestacao = valorCasa/meses
if valorPrestacao>limitePrestacao:
    print('Seu empréstimo não pode ser aprovado, pois o valor da prestação supera 30% do seu salário!')
else:
    print('Empréstimo aprovado, as prestações ficaram no valor de %.1f'%valorPrestacao)

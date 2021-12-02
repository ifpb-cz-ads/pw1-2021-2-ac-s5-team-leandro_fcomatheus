numero1 = float(input('Informe um número:'))

numero2 = float(input('Informe outro número:'))
operacao = str(input('Escolha uma operação:\n'
                     '+'
                     '\n-'
                     '\n*'
                     '\n/'))
if operacao == '+':
    resultado = numero1+numero2
    print('O soma é: %.1f' % resultado)
if operacao == '-':
   resultado = numero1-numero2
   print('A subtração é: %.1f'%resultado)
if operacao == '*':
 resultado = numero1*numero2
 print('O produto é: %.1f' % resultado)
if operacao == '/':
 resultado = numero1/numero2
 print('A divisão é: %.1f' % resultado)

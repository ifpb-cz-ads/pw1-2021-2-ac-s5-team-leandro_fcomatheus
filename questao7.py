kwh = float(input('Informe  a quantidade kwh consumida:'))
instalacao = input('Informe o tipo de instalação:\n'
                   'R para residêncial\n'
                   'I para indústrial\n'
                   'C para comercial')
if instalacao == 'R' and kwh<=500:
    valorPagar = kwh*0.40
    print('O valor a pagar é %.1f reais'%valorPagar)

if instalacao == 'R' and kwh>500:
    valorPagar = kwh*0.65
    print('O valor a pagar é %.1f reais'%valorPagar)

if instalacao == 'C' and kwh<=1000:
    valorPagar = kwh*0.55
    print('O valor a pagar é %.1f reais'%valorPagar)

if instalacao == 'C' and kwh>1000:
    valorPagar = kwh*0.60
    print('O valor a pagar é %.1f reais'%valorPagar)

if instalacao == 'I' and kwh<=5000:
    valorPagar = kwh*0.55
    print('O valor a pagar é %.1f reais'%valorPagar)

if instalacao == 'I' and kwh>5000:
    valorPagar = kwh*0.40
    print('O valor a pagar é %.1f reais'%valorPagar)

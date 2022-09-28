
def calcularSalario():
    salario = float(input('Digite seu salario: '))
    print(f'O salario sem reajuste: R${salario:.2f}')

    if salario <= 280:
        taxa = 0.2
        salarioAjuste = salario + salario*taxa
    elif salario > 280 and salario <= 700:
        taxa = 0.15
        salarioAjuste = salario + salario*taxa
    elif salario > 700 and salario <= 1500:
        taxa = 0.1
        salarioAjuste = salario + salario*taxa
    else:
        taxa = 0.05
        salarioAjuste = salario + salario*taxa
    print(f'O salario ajustado: R${salarioAjuste:.2f}')
    print(f'A taxa de aumento foi de {taxa*100}%')
    print(f'O aumento aplicado foi de {salarioAjuste - salario}')
  

calcularSalario()
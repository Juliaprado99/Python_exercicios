valor_hora = int(input('Quanto vale a sua hora?'))

horas_trabalhadas = int(input('Quantas horas você trabalhou nesse mês?'))

def calcularSalario():
    salario_bruto = horas_trabalhadas * valor_hora
    sindicato = salario_bruto * 0.03
    FGTS = salario_bruto * 0.11
    INSS = salario_bruto * 0.1
    if salario_bruto < 900:
        taxa = '0'
    elif salario_bruto > 900 and salario_bruto <= 1500:
        taxa = 0.05
    elif salario_bruto > 1500 and salario_bruto <= 2500:
        taxa = 0.1
    else:
        taxa = 0.2

    print(f'Salário Bruto: ({valor_hora} * {horas_trabalhadas}) = R${salario_bruto:.2f}')
    print(f'(-) IR ({taxa * 100}%) = R${(taxa) * salario_bruto}')
    print(f'(-) INSS (10%) = R${INSS}')
    print(f'FGTS (11%) = R${salario_bruto * .11}')
    print(f'Total dos Descontos: R${INSS + (taxa * salario_bruto)}')
    print(f'Salário Liquido: R${salario_bruto - INSS - (taxa * salario_bruto)}')

    

calcularSalario()

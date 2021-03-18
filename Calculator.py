def calculator():
    operation = input('Qual é a operação? + , - , * ou / ?: ')
    num1 = int(input('Primeiro numero: '))
    num2 = int(input('Segundo numero: '))
    if operation == '+':
        print('{} + {} ='.format(num1, num2), num1 +num2)
    elif operation == '-':
        print('{} - {} ='.format(num1, num2), num1 - num2)
    elif operation == '*':
        print('{} * {} ='.format(num1, num2), num1 *num2)
    elif operation == '/':
        print('{} / {} ='.format(num1, num2), num1 /num2)
    else:
        print('Operação inexistente.')
    again()

def again():
    novamente = input('Quer calcular novamente? Y para sim, N para não.')
    if novamente.upper() == "Y":
        calculator()
    elif novamente.upper() =="N":
        print('Sayonara.')
    else:
        again()
calculator()
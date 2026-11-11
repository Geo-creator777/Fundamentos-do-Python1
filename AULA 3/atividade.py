# if aninhado - ninho de ifs 

if  x > 5:
    if y > 10:
        print('teste finalizado')

if x > 5 and y  > 10:
    print('Teste finalizado')
    
    
if not x  > 5 or x > 10:
    print('finalizado')
    
    
    # 1 VERIFICAÇÃO DE UM NUMERO POSITIVO

numero = int(input('digite um numero: '))

if numero >  0:
    print('POSITIVO')
elif numero < 0:
    print('NEGATIVO')
else:
    print('Zero')
    
    
    lado1 = float(input('lado 1: '))
lado2 = float(input('lado 2: '))
lado3 = float(input('lado 3: '))

if lado1 == lado2 == lado3 == lado1:
    print('Equilatero')
elif  lado1 != lado2 != lado3 != lado1:
    print('Escaleno')
else:
    print('Isoceles')
    
    
   
idade = int(input('Idade >> '))

if idade >= 18:
    print('Acesso permitido')
else:
    print('Menor de idade, acesso negado') 

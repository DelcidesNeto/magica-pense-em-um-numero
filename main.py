from time import sleep
numero_de_montes = int(input('Quantos montes você quer adicionar? '))
print('\n')
montes = []
espelhoMontes = {}
ultimoNumeroAdicionado = 0
opcoesStr = ''
for monte in range(0, numero_de_montes):
    monteAtual = []
    for numero in range(0, numero_de_montes):
        ultimoNumeroAdicionado += 1
        monteAtual.append(ultimoNumeroAdicionado)  
    montes.append(monteAtual)  

for i, monte in enumerate(montes):
    espelhoMontes[i] = monte[0]
opcoesStr = '['
for i, monte in enumerate(montes):
    opcoesStr += f'{i+1}, '
    print(f'------Monte {i+1}------')
    for numero in monte:
        print(f'\t{numero}')
    print('\n')

opcoesStr = opcoesStr[:-2]+']'
monteEscolhido = int(input(f'Escolha um monte: {opcoesStr}: '))


print(f'------Monte {monteEscolhido}------')
for numero in montes[monteEscolhido-1]:
    print(f'\t{numero}')
print('\n')

input('Decore um dos números e aperte ENTER para continuar')
print('\n')
print('Embaralhando os números', end='')
sleep(0.3)
print('.', end='')
sleep(0.3)
print('.', end='')
sleep(0.3)
print('.')
print('\n')
novosMontes = []
for monteAntigo in range(1, numero_de_montes+1):
    monteAtual = []
    for numero in range(1, numero_de_montes+1):
        monteAtual.append(montes[numero-1][-1])
        montes[numero-1].pop()
    novosMontes.append(monteAtual)
for i, monte in enumerate(novosMontes):
    print(f'------Monte {i+1}------')
    for numero in monte:
        print(f'\t{numero}')
    sleep(0.5)
    print('\n')
ondeEsta = int(input(f'Qual monte está o número que você pensou? {opcoesStr}: '))
for i, monte in enumerate(novosMontes):
    if espelhoMontes[monteEscolhido-1] in monte:
        indexMonte = monte.index(espelhoMontes[monteEscolhido-1])
        print(novosMontes[ondeEsta-1][indexMonte])
        break

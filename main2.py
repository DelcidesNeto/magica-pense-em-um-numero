# Importa a biblioteca pandas e dá o apelido 'pd' para facilitar o uso
import pandas as pd

# Lista para armazenar as vendas
vendas = []

# Função para cadastrar uma venda
def cadastrar_venda():
    cliente = input('Nome do Cliente: ')
    produto = input('Produto: ')
    valor = float(input('Valor (R$): ').replace(',','.'))

    # Salva a venda como um dicionário dentro da lista
    venda = {
        'cliente': cliente,
        'produto': produto,
        'valor': valor
    }
    vendas.append(venda)
    print('Venda cadastrada com sucesso!\n')

# Função para listar todas as vendas
def listar_vendas():
    if not vendas:
        print('Nenhuma venda cadastrada.\n')
        return

    print('=== VENDAS ===')
    for i, venda in enumerate(vendas, start=1):
        print(f"{i}. Cliente: {venda['cliente']}, Produto: {venda['produto']}, valor: R${venda['valor']:.2f}")

# Função para exportar as vendas para Escel
def exportar_para_excel():
    if not vendas:
        print('Nenhuma venda para exportar.\n')
        return

    # Cria um DataFrame do pandas a partir da lista vendas
    df = pd.DataFrame(vendas)

    # Salva o DataFrame em um arquivo Excel na mesma pasta do projeto
    df.to_excel('relatorio_vendas.xlsx', index=False)

    # Confirma que o arquivo foi criado
    print('Relatório exportado com sucesso"\n')

# Loop principal do programa
while True:
    print('Selecione uma opção válida:')
    print('1 - Cadastrar venda')
    print('2 - Listar vendas')
    print('3 - Exportar para Excel')
    print('4 - Sair')

    opcao = input('Escolha uma opção')

    if opcao == '1':
        cadastrar_venda()
    elif opcao == '2':
        listar_vendas()
    elif opcao == '3':
        exportar_para_excel()
    elif opcao == '4':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida! Tente novamente.\n')

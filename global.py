#Julia Souza Costa Schiavi RM: 562418
#Thayna Ferreira Lopes RM: 566349
#Leonardo Grosskopf Martins RM: 562255


print("\nBem-vindo ao GeoChuva!")
print("--------------------------------")

# Função para forçar o usuário a digitar uma das opções da lista fornecida
def forca_escolha(msg, lista_opcoes):
    opcoes_str = ' , '.join(lista_opcoes)
    escolha = input(f'{msg}\n {opcoes_str}\n--> ')
    while escolha not in lista_opcoes:
        escolha = input(f'Opção inválida. {msg}\n {opcoes_str}\n--> ')
    return escolha

lista_zona = ['zona central', 'zona norte', 'zona sul', 'zona oeste', 'zona leste']

# Utilizando um Dicionário aninhado com listas para facilitar o código
bairros_zona = {
    'zona central': ['centro', 'república', 'sé'],
    'zona norte': ['tucuruvi', 'santana', 'casa Verde'],
    'zona sul': ['santo amaro', 'capao redondo', 'jabaquara'],
    'zona oeste': ['pinheiros', 'butanta', 'lapa'],
    'zona leste': ['itaquera', 'tatuape', 'mooca']
}

# Lista dos riscos de cada bairro, utilizando o Dicionário aninhado
risco_bairros = {
    'centro': 'ALTO',
    'republica': 'MUITO ALTO',
    'sé': 'MODERADO',
    'tucuruvi': 'MODERADO',
    'santana': 'ALTO',
    'casa Verde': 'MUITO ALTO',
    'santo amaro': 'MUITO ALTO',
    'capao redondo': 'ALTO',
    'jabaquara': 'MODERADO',
    'pinheiros': 'MODERADO',
    'butanta': 'ALTO',
    'lapa': 'ALTO',
    'itaquera': 'MUITO ALTO',
    'tatuape': 'MODERADO',
    'mooca': 'ALTO'
}

# Repetir o código indefinidamente, permitindo o usuário fazer várias consultas sem precisar reiniciar o programa.
while True:
    opcao_zona = forca_escolha("Escolha qual Zona de sua preferência:", lista_zona)
    print(f"\nVocê escolheu: {opcao_zona}")

    print("--------------------------------")
    lista_bairros = bairros_zona[opcao_zona]
    opcao_bairro = forca_escolha(f"Escolha um bairro da {opcao_zona}:", lista_bairros)
    
    print(f"\nVocê mora na {opcao_zona}, no bairro {opcao_bairro}.")
    # Utilizando o .get pois se o bairro estiver no dicionário, ele retorna o risco real;
    # Se não estiver, ele não dá erro — só retorna a palavra "desconhecido".
    risco = risco_bairros.get(opcao_bairro, "desconhecido")
    print(f"Nível de risco de alagamento para {opcao_bairro}: {risco}.")
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    
    # Adicionando parte para encerrar o programa ou voltar para o início
    repetir = input("\nDeseja fazer outra consulta? (s/n): ")
    if repetir != 's': 
        print("GeoChuva agradece. Até logo!")
        break




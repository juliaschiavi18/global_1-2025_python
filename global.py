#Julia Souza Costa Schiavi RM: 562418
#Thayna Ferreira Lopes RM: 566349
#Leonardo Grosskopf Martins RM: 562255


print("\nBem-vindo ao GeoChuva!")
print("--------------------------------")
#função para forçar o usuario a digitar uma das opcoes da lista de zona
def forca_zona(msg, lista_zona):
    zona = ' , '.join(lista_zona)
    escolha = input(f'{msg}\n {zona}\n--> ')
    while escolha not in lista_zona:
        escolha = input(f'Opção inválida. {msg}\n {zona}\n--> ')
    return escolha
#função para forçar o usuario a digitar uma das opcoes da lista de bairros
def forca_bairro(msg, lista_bairro):
    bairros = ' , '.join(lista_bairro)
    escolha = input(f'{msg}\n {bairros}\n--> ')
    while escolha not in lista_bairro:
        escolha = input(f'Opção inválida. {msg}\n {bairros}\n--> ')
    return escolha
lista_zona = ['zona central', 'zona norte', 'zona sul', 'zona oeste', 'zona leste']

#utilizando um Dicionario aninhado com listas para facilitar o codigo, em vez de fazer varias variaveis com as respectivas listas
bairros_zona = {
    'zona central': ['centro', 'república', 'sé'],
    'zona norte': ['tucuruvi', 'santana', 'casa Verde'],
    'zona sul': ['santo amaro', 'capao redondo', 'jabaquara'],
    'zona oeste': ['pinheiros', 'butanta', 'lapa'],
    'zona leste': ['itaquera', 'tatuape', 'mooca']
}


#lista dos riscos de cada bairro, utilizando o Dicionario aninhado
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
#repetir o código indefinidamente,  permitindo o usuário 
# fazer várias consultas sem precisar reiniciar o programa.
while True:
    
    opcao_zona = forca_zona("Escolha qual Zona de sua preferência:", lista_zona)
    print(f"\nVocê escolheu: {opcao_zona}")


    print("--------------------------------")
    lista_bairros = bairros_zona[opcao_zona]
    opcao_bairro = forca_bairro(f"Escolha um bairro da {opcao_zona}:", lista_bairros)

   
    print(f"\nVocê mora na {opcao_zona}, no bairro {opcao_bairro}.")
#utilizando o .get pois se o bairro estiver no dicionário, ele retorna o risco real;
#Se não estiver, ele não dá erro — só retorna a palavra "desconhecido".
    risco = risco_bairros.get(opcao_bairro, "desconhecido")
    print(f"Nível de risco de alagamento para {opcao_bairro}: {risco}.")
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    
#adicionando parte para encerrar o programa ou voltar para o inicio
   
    repetir = input("\nDeseja fazer outra consulta? (s/n): ")
    if repetir != 's':
        print("GeoChuva agradece. Até logo!")
        break




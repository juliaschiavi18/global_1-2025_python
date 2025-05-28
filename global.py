print("Bem vindo ao GeoChuva!")
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
#lista dos bairros
bairros_zona = {
    'zona central': ['Centro', 'República', 'Sé'],
    'zona norte': ['Tucuruvi', 'Santana', 'Casa Verde'],
    'zona sul': ['Santo Amaro', 'Capão Redondo', 'Jabaquara'],
    'zona oeste': ['Pinheiros', 'Butantã', 'Lapa'],
    'zona leste': ['Itaquera', 'Tatuapé', 'Mooca']
}

# pedindo para o usuario escolher uma zona

opcao_zona = forca_zona("Escolha qual Zona de sua preferência:", lista_zona)
print(f"\nVocê escolheu: {opcao_zona}")

# pedindo pro usuario escolher um bairro de acordo com a zona que ele escolheu

lista_bairros = bairros_zona[opcao_zona]
opcao_bairro = forca_bairro(f"Escolha um bairro da {opcao_zona}:", lista_bairros)
print(f"\nVocê mora na {opcao_zona}, no bairro {opcao_bairro}.")
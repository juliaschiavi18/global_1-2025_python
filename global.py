# GeoChuva - Sistema de Consulta de Risco de Enchentes
# Desenvolvido por: Julia Souza Costa Schiavi RM: 562418
# Thayna Ferreira Lopes RM: 566349
# Leonardo Grosskopf Martins RM: 562255

from unidecode import unidecode

print("\n🌧️ Bem-vindo ao GeoChuva - Monitoramento de Riscos de Enchentes 🌧️")
print("---------------------------------------------------------------")

# Função para normalizar strings
def normaliza(texto):
    return unidecode(texto).lower().strip()

# Função para garantir uma escolha válida, mesmo com variações
def forca_escolha(msg, lista_opcoes):
    opcoes_normalizadas = {normaliza(opcao): opcao for opcao in lista_opcoes}
    opcoes_str = ' | '.join(lista_opcoes)
    
    while True:
        escolha = input(f'\n{msg}\n({opcoes_str})\n--> ')
        chave_normalizada = normaliza(escolha)
        
        if chave_normalizada in opcoes_normalizadas:
            return opcoes_normalizadas[chave_normalizada]
        
        print("❌ Opção inválida. Tente novamente.")

# Zonas e seus bairros associados
lista_zona = ['zona central', 'zona norte', 'zona sul', 'zona oeste', 'zona leste']

bairros_zona = {
    'zona central': ['centro', 'república', 'sé'],
    'zona norte': ['tucuruvi', 'santana', 'casa verde'],
    'zona sul': ['santo amaro', 'capão redondo', 'jabaquara'],
    'zona oeste': ['pinheiros', 'butantã', 'lapa'],
    'zona leste': ['itaquera', 'tatuapé', 'mooca']
}

# Níveis de risco por bairro
risco_bairros = {
    'centro': 'ALTO',
    'república': 'MUITO ALTO',
    'sé': 'MODERADO',
    'tucuruvi': 'MODERADO',
    'santana': 'ALTO',
    'casa verde': 'MUITO ALTO',
    'santo amaro': 'MUITO ALTO',
    'capão redondo': 'ALTO',
    'jabaquara': 'MODERADO',
    'pinheiros': 'MODERADO',
    'butantã': 'ALTO',
    'lapa': 'ALTO',
    'itaquera': 'MUITO ALTO',
    'tatuapé': 'MODERADO',
    'mooca': 'ALTO'
}

# Função para mostrar o risco do bairro escolhido
def exibe_risco(zona, bairro):
    risco = risco_bairros.get(bairro, "DESCONHECIDO")
    print("\n📍 Localização selecionada:")
    print(f"Zona: {zona.title()} | Bairro: {bairro.title()}")
    print(f"⚠️ Nível de risco de alagamento: {risco}")
    print("================================================")

# Loop principal
while True:
    opcao_zona = forca_escolha("Escolha uma zona da cidade", lista_zona)
    lista_bairros = bairros_zona[opcao_zona]
    opcao_bairro = forca_escolha(f"Escolha um bairro da {opcao_zona.title()}", lista_bairros)

    exibe_risco(opcao_zona, opcao_bairro)

    repetir = input("\n🔁 Deseja fazer outra consulta? (s/n): ").strip().lower()
    if repetir != 's':
        print("\n✅ GeoChuva agradece a sua consulta. Fique seguro e bem informado!")
        break
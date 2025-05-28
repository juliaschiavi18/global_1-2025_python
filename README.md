# GeoChuva💧💻

## 🌧️ Sobre o Projeto

O GeoChuva é um script Python simples e interativo que permite aos usuários consultar o **nível de risco de alagamento** em diferentes bairros da cidade, divididos por zonas geográficas. O objetivo principal é fornecer uma ferramenta rápida para verificar a suscetibilidade de alagamentos em áreas específicas.

## ✨ Funcionalidades

* **Seleção de Zona:** O usuário pode escolher entre diferentes zonas da cidade (Central, Norte, Sul, Oeste, Leste).
* **Seleção de Bairro:** Após selecionar a zona, o script apresenta uma lista de bairros pertencentes àquela zona para o usuário escolher.
* **Consulta de Risco:** Para o bairro selecionado, o sistema informa o nível de risco de alagamento (**MODERADO**, **ALTO**, **MUITO ALTO**).
* **Validação de Entrada:** A função **`forca_escolha`** garante que o usuário digite apenas opções válidas, evitando erros.
* **Loop de Consulta:** O programa permite que o usuário faça múltiplas consultas sem a necessidade de reiniciar o script.

---

## 🚀 Como Usar

1.  **Execute o script:**
    ```bash
    python seu_arquivo.py
    ```
    (Substitua `seu_arquivo.py` pelo nome do arquivo onde você salvou o código.)

2.  **Siga as instruções:** O programa irá guiá-lo para escolher a zona e, em seguida, o bairro desejado.

3.  **Visualize o risco:** O nível de risco de alagamento será exibido para o bairro escolhido.

4.  **Faça novas consultas:** Ao final de cada consulta, você será perguntado se deseja realizar outra. Digite `s` para continuar ou `n` para encerrar o programa.

---

## ⚙️ Estrutura do Código

* **`forca_escolha(msg, lista_opcoes)`:** Função unificada que solicita ao usuário que escolha uma opção de uma lista predefinida (seja zona ou bairro), garantindo uma entrada válida.
* **`lista_zona`:** Uma lista de strings contendo as zonas disponíveis.
* **`bairros_zona`:** Um **dicionário aninhado** que mapeia cada zona a uma lista de bairros correspondentes. Isso facilita a organização e recuperação dos bairros por zona.
* **`risco_bairros`:** Um dicionário que associa cada bairro ao seu respectivo nível de risco de alagamento. O método `.get()` é usado para retornar o risco real do bairro ou "desconhecido" caso o bairro não esteja mapeado.
* **Loop `while True`:** Permite que o programa seja executado continuamente, oferecendo múltiplas consultas ao usuário.

---

## 🤝 Contribuições

Sinta-se à vontade para fazer sugestões, relatar problemas ou contribuir com melhorias para este projeto.

## 👩‍💻Desenvolvedora
### Julia Schiavi
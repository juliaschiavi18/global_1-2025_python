# GeoChuva💧💻

## 🌧️ Sobre o Projeto

O GeoChuva é um script Python simples e interativo que permite aos usuários consultar o **nível de risco de alagamento** em diferentes bairros da cidade, divididos por zonas geográficas. O objetivo principal é fornecer uma ferramenta rápida para verificar a suscetência de alagamentos em áreas específicas.

## ✨ Funcionalidades

* **Seleção de Zona:** O usuário pode escolher entre diferentes zonas da cidade (Central, Norte, Sul, Oeste, Leste).
* **Seleção de Bairro:** Após selecionar a zona, o script apresenta uma lista de bairros pertencentes àquela zona para o usuário escolher.
* **Consulta de Risco:** Para o bairro selecionado, o sistema informa o nível de risco de alagamento (MODERADO, ALTO, MUITO ALTO).
* **Validação de Entrada:** As funções `forca_zona` e `forca_bairro` garantem que o usuário digite apenas opções válidas, evitando erros.
* **Loop de Consulta:** O programa permite que o usuário faça múltiplas consultas sem a necessidade de reiniciar o script.

## 🚀 Como Usar

1.  **Execute o script:**
    ```bash
    python seu_arquivo.py
    ```
    (Substitua `seu_arquivo.py` pelo nome do arquivo onde você salvou o código.)

2.  **Siga as instruções:** O programa irá guiá-lo para escolher a zona e, em seguida, o bairro desejado.

3.  **Visualize o risco:** O nível de risco de alagamento será exibido para o bairro escolhido.

4.  **Faça novas consultas:** Ao final de cada consulta, você será perguntado se deseja realizar outra. Digite `s` para continuar ou `n` para encerrar o programa.

## ⚙️ Estrutura do Código

* **`forca_zona(msg, lista_zona)`:** Função que solicita ao usuário que escolha uma zona de uma lista predefinida, garantindo uma entrada válida.
* **`forca_bairro(msg, lista_bairro)`:** Função similar à `forca_zona`, mas para a seleção de bairros.
* **`lista_zona`:** Uma lista de strings contendo as zonas disponíveis.
* **`bairros_zona`:** Um **dicionário aninhado** que mapeia cada zona a uma lista de bairros correspondentes. Isso facilita a organização e recuperação dos bairros por zona.
* **`risco_bairros`:** Um dicionário que associa cada bairro ao seu respectivo nível de risco de alagamento.
* **Loop `while True`:** Permite que o programa seja executado continuamente, oferecendo múltiplas consultas ao usuário.

## 🤝 Contribuições

Sinta-se à vontade para fazer sugestões, relatar problemas ou contribuir com melhorias para este projeto.

## 👩‍💻Desenvolvedora
### Julia Schiavi
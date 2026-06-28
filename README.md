# Sistema de Gerenciamento de Biblioteca

Projeto desenvolvido para a disciplina de Algoritmos e Programação no 1º período do curso de Bacharelado em Inteligência Artificial do Piauí Instituto de Tecnologia (PIT).

## Descrição do Projeto

O sistema realiza o gerenciamento do acervo e dos empréstimos de uma biblioteca por meio de uma aplicação web interativa criada com Streamlit. A aplicação permite cadastrar, listar, atualizar e remover livros e registros, mantendo todos os dados salvos em um arquivo JSON local.
O projeto implementa um CRUD completo (Create, Read, Update e Delete) utilizando estruturas de dados em Python (como dicionários e listas) e persistência de dados no arquivo biblioteca.json

## Funcionalidades

* Cadastrar Livro/Usuário: Registra novas obras no acervo com informações detalhadas e controle de ID.
* Listar Acervo: Exibe todos os livros cadastrados, seus autores, status de empréstimo e categorias.
* Atualizar Registro: Permite alterar dados de livros cadastrados ou modificar o status de disponibilidade.
* Remover Livro: Exclui uma obra do acervo de forma segura através da interface gráfica.
* Persistência de Dados: Salva automaticamente todas as alterações no arquivo biblioteca.json.

## Tecnologias Utilizadas

* Python 3: Linguagem principal utilizada no desenvolvimento da lógica de negócios.
* Streamlit: Framework utilizado para construir a interface web responsiva e os componentes visuais.
* JSON: Formato leve de intercâmbio de dados escolhido para o armazenamento do acervo.
* Biblioteca json: Módulo nativo do Python usado para a leitura e escrita segura dos arquivos.

## Como Executar o Projeto

1. Instale as dependências necessárias:
   bash
   pip install streamlit

2. Execute a aplicação a partir do terminal:
   Bash
   streamlit run menu.py

3. Ira abrir automaticamente uma página no navegador:
   ```Bash
   o endereço local exibido pelo Streamlit (geralmente http://localhost:8501).

 
## Estrutura do Projeto

Sistema-de-Biblioteca-main/
├── sistema de biblioteca/
│   ├── menu.py
│   ├── funcoes.py
│   └── biblioteca.json
└── README.md

### `menu.py` 
Arquivo principal responsável por renderizar a interface web no Streamlit, gerenciar a navegação lateral e chamar os componentes visuais.

### ` funcoes.py`
Módulo que centraliza a lógica do CRUD e as funções de manipulação do arquivo JSON (carga, escrita e modificação de registros).

### `biblioteca.json`
Banco de dados local em formato JSON gerado dinamicamente para manter os dados salvos entre as execuções.

## Uso de Inteligência Artificial

A IA foi utilizada como apoio para adaptar o projeto para Streamlit e organizar a documentação.

## Prompts Utilizados

Modularização do código:

"Transforme meu sistema de biblioteca em uma aplicação Streamlit."

"O sistema utiliza Python e JSON (biblioteca.json) para armazenar livros com os campos: id, titulo, autor, ano e disponivel."

"A aplicação deve permitir:
- Adicionar livros
- Listar livros
- Buscar livros por título
- Atualizar livros
- Remover livros"

"Utilize menu lateral (sidebar), interface simples e moderna, mensagens de sucesso/erro e mantenha a persistência dos dados no arquivo JSON.":

"Quero que continue separado os codigos" 

## Links do Projeto

* Repositório no GitHub: https://github.com/Kelly1788/Sistema-de-Biblioteca

## Equipe:

* Jennifer Kelly Cunha Santos - Kellyjenni1001@gmail.com

* Karina Lira de Almeida - liradealmeidakarina@gmail.com

* Paula Beron Silva Cardoso - paulacardosoof@gmail.com

# Referências

## Materiais da Disciplina (PIT)

* Fundamentos de Lógica e Python.

* Estruturas Condicionais e de Repetição.

* Manipulação de Listas, Dicionários e Funções.

* Persistência de Arquivos e Formato JSON.

## Python e JSON
* PYTHON SOFTWARE FOUNDATION. The Python Tutorial: Data Structures. Disponível em: https://docs.python.org/3/tutorial/datastructures.html. Acesso em: 27 jun. 2026.

* PYTHON SOFTWARE FOUNDATION. json - JSON encoder and decoder. Disponível em: https://docs.python.org/3/library/json.html. Acesso em: 27 jun. 2026.

## Streamlit
* STREAMLIT. Main Concepts & API Reference. Disponível em: https://docs.streamlit.io/. Acesso em: 27 jun. 2026.

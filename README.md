# Sistema de Biblioteca

Sistema de gerenciamento de biblioteca via linha de comando, desenvolvido em Python. Permite cadastrar, listar, buscar, atualizar e remover livros, com persistência de dados em arquivo JSON.

## Funcionalidades

- **Adicionar livro** — cadastra título, autor e ano de publicação; gera ID automaticamente
- **Listar livros** — exibe todos os livros com status de disponibilidade (Disponível / Emprestado)
- **Buscar livro** — pesquisa por título (sem diferenciar maiúsculas/minúsculas)
- **Atualizar livro** — edita título, autor ou ano de um livro pelo ID
- **Remover livro** — exclui um livro da coleção pelo ID

## Tecnologias

- Python 3.7+
- Biblioteca padrão (`json`, `os`) — sem dependências externas

## Estrutura do Projeto

```
sistema de biblioteca/
├── menu.py           # Ponto de entrada — menu interativo
├── funcoes.py        # Lógica de negócio (CRUD)
└── biblioteca.json   # Banco de dados local (criado automaticamente)
```

## Como Executar

**Pré-requisito:** Python 3.7 ou superior instalado.

```bash
# Entre na pasta do projeto
cd "sistema de biblioteca"

# Execute o programa
python menu.py
```

O menu será exibido no terminal. Digite o número da opção desejada e pressione Enter.

```
=== Sistema de Biblioteca ===
1. Adicionar livro
2. Listar livros
3. Buscar livro
4. Atualizar livro
5. Remover livro
0. Sair
```

## Formato dos Dados

Os livros são armazenados em `biblioteca.json` com a seguinte estrutura:

```json
[
  {
    "id": 1,
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano": 1899,
    "disponivel": true
  }
]
```

| Campo       | Tipo    | Descrição                          |
|-------------|---------|-------------------------------------|
| `id`        | inteiro | Identificador único gerado automaticamente |
| `titulo`    | texto   | Título do livro                     |
| `autor`     | texto   | Nome do autor                       |
| `ano`       | inteiro | Ano de publicação                   |
| `disponivel`| booleano| `true` = Disponível / `false` = Emprestado |

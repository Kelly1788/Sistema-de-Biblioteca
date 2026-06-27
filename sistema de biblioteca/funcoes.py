import json
import streamlit as st

ARQUIVO = "biblioteca.json"

def carregar_dados():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
    
        st.info("Arquivo não encontrado. Criando um novo arquivo.")
        return []

def salvar_dados(biblioteca):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(biblioteca, f, ensure_ascii=False, indent=4)  

def adicionar_livro(biblioteca):
    st.header('ADICIONAR UM LIVRO')
    st.markdown('---')
    
    with st.form("form_adicionar", clear_on_submit=True):
        titulo = st.text_input('Digite o título do livro:')
        autor = st.text_input('Digite o nome do autor:')
        ano = st.number_input('Digite o ano da publicação do livro:', min_value=0, max_value=2026, value=2024, step=1)
        
        botao_salvar = st.form_submit_button('Salvar Livro')
        
        if botao_salvar:
            if titulo.strip() == "" or autor.strip() == "":
                st.error("Erro: Preencha o título e o autor.")
            else:
                if biblioteca:
                    id_novo = biblioteca[-1]['id'] + 1
                else:
                    id_novo = 1
                livro_novo = {
                    "id": id_novo,
                    "titulo": titulo,
                    "autor": autor,
                    "ano": int(ano),
                    "disponivel": True
                }
                biblioteca.append(livro_novo)
                salvar_dados(biblioteca)
                st.success(f"Livro '{titulo}', adicionado com sucesso!!")
                st.rerun()

def lista(biblioteca):
    st.header('LISTA DOS LIVROS')
    st.markdown('---')
    
    if not biblioteca:
        st.warning("Nenhum livro cadastrado")
        return
    
    for livro in biblioteca:
        if livro["disponivel"]: 
            status = "Disponível"
            cor = "green"
        else:
            status = "Emprestado"
            cor = "red"
            
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### **{livro['titulo']}**")
                st.markdown(f"**Autor:** {livro['autor']} | **Ano:** {livro['ano']}")
                st.caption(f"ID: {livro['id']}")
            with col2:
                st.markdown(f"<span style='color:{cor}; font-weight:bold;'>● {status}</span>", unsafe_allow_html=True)

def buscar(biblioteca):
    st.header('BUSCAR LIVROS')
    st.markdown('---')

    titulo = st.text_input('Digite o título do livro: ')
    
    if titulo:
        title_digitado = titulo.lower()
        for livro in biblioteca:
            title_livro = livro["titulo"].lower()
            
            if title_digitado in title_livro:
                with st.chat_message("book", avatar="📖"):
                    st.markdown(f"**ID:** {livro['id']}")
                    st.markdown(f"**Título:** {livro['titulo']}")
                    st.markdown(f"**Autor:** {livro['autor']}")
                    st.markdown(f"**Ano:** {livro['ano']}")
                return

        st.error('LIVRO NÃO ENCONTRADO')

def atualizar(biblioteca):
    st.header('ATUALIZAR LIVROS')
    st.markdown('---')

    if not biblioteca:
        st.warning("Nenhum livro cadastrado para atualizar.")
        return

    opcoes = {f"ID {l['id']} - {l['titulo']}": l for l in biblioteca}
    escolha = st.selectbox("Selecione o livro que deseja atualizar:", list(opcoes.keys()))
    livro_encontrado = opcoes[escolha]

    with st.form("form_atualizar"):
        st.write(f"Livro encontrado!! | Titulo atual: {livro_encontrado['titulo']}")
        novo_titulo = st.text_input('Digite o novo título:', value=livro_encontrado['titulo'])
        novo_autor = st.text_input('Digite o novo autor:', value=livro_encontrado['autor'])
        novo_ano = st.number_input('Digite o novo ano:', min_value=0, max_value=2026, value=livro_encontrado['ano'], step=1)
        novo_status = st.checkbox("Disponível", value=livro_encontrado['disponivel'])
        
        if st.form_submit_button('Confirmar Alteração'):
            livro_encontrado['titulo'] = novo_titulo
            livro_encontrado['autor'] = novo_autor
            livro_encontrado['ano'] = int(novo_ano)
            livro_encontrado['disponivel'] = novo_status
            salvar_dados(biblioteca)
            st.success('Atualizado com sucesso!!')
            st.rerun()

def remover(biblioteca):
    st.header('REMOVER LIVROS')
    st.markdown('---')

    if not biblioteca:
        st.warning("Nenhum livro cadastrado para remover.")
        return

    opcoes = {f"ID {l['id']} - {l['titulo']}": l for l in biblioteca}
    escolha = st.selectbox("Selecione o livro que deseja remover:", list(opcoes.keys()))
    livro_encontrado = opcoes[escolha]

    st.warning(f"Tem certeza que deseja remover o livro '{livro_encontrado['titulo']}'?")
    if st.button('Sim, Remover', type="primary"):
        biblioteca.remove(livro_encontrado)
        salvar_dados(biblioteca)
        st.success('Livro removido com sucesso!')
        st.rerun()
#te
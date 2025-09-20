import streamlit as st
from codigo import chain

st.set_page_config(page_title="LinguaChain - Tradutor", page_icon="🌎")

st.title("🌎 LinguaChain")
st.subheader("Seu tradutor inteligente com LangChain + OpenAI")

st.write("Digite o texto abaixo e escolha o idioma para traduzir:")

# Entrada de texto
texto = st.text_area("Texto para traduzir", placeholder="Escreva aqui...")

# Idioma destino
idioma = st.text_input("Idioma de destino", "inglês")

# Botão de tradução
if st.button("Traduzir"):
    if texto.strip():
        resultado = chain.invoke({"idioma": idioma, "texto": texto})

        try:
            st.success(f"**Tradução ({idioma})**  \n{resultado}")
        except:
            st.success(f"**Tradução ({idioma})**  \n{resultado.content}")
        
    else:
        st.warning("⚠️ Por favor, insira um texto para traduzir.")
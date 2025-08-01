
import streamlit as st
import pandas as pd

# Dados
frutas = {
    "alho": 39.90,
    "chuchu": 5.90,
    "beterraba": 4.99,
    "batata doce": 5.90,
    "batata doce branca": 8.90,
    "cenoura": 5.90,
    "tomate saladete": 8.90,
    "batata lavada": 7.90,
    "repolho verde": 5.90,
    "repolho roxo": 6.90,
    "cebola branca": 5.90,
    "coco verde": 5.90
}

# Converter para DataFrame só para organização (opcional)
df_frutas = pd.DataFrame(list(frutas.items()), columns=['Produto', 'Preço'])
st.markdown("HORTIFRUTI")
st.title("consultor de preços 🍅🥕🧄")
st.subheader("Clique no nome do produto para ver o preço:")

# Mostrar os produtos como botões
for produto in df_frutas['Produto']:
    if st.button(produto.title()):
        preco = frutas[produto]
        st.success(f"O preço de *{produto.title()}* é R$ {preco:.2f}")

# Se quiser exibir toda a tabela também
# st.dataframe(df_frutas)
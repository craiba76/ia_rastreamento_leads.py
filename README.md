# ia_rastreamento_leads.py
import streamlit as st
import pandas as pd
from datetime import datetime

# Simulador de dados encontrados (futuramente virá do scraping/API)
leads = [
    {
        "Nome": "@mariafit",
        "Produto": "Colágeno Hidrolisado",
        "Rede Social": "Instagram",
        "Link": "https://instagram.com/mariafit",
        "Data": datetime.today().strftime('%d/%m/%Y'),
        "Status": "Novo"
    },
    {
        "Nome": "rafael.saude",
        "Produto": "Ômega 3",
        "Rede Social": "OLX",
        "Link": "https://olx.com.br/perfil/rafael.saude",
        "Data": datetime.today().strftime('%d/%m/%Y'),
        "Status": "Novo"
    },
    {
        "Nome": "@nutrimarcia",
        "Produto": "Vitamina D3",
        "Rede Social": "Instagram",
        "Link": "https://instagram.com/nutrimarcia",
        "Data": datetime.today().strftime('%d/%m/%Y'),
        "Status": "Novo"
    }
]

# Converte para DataFrame
df = pd.DataFrame(leads)

st.set_page_config(page_title="LICITA360 Leads", layout="wide")
st.title("🔍 IA Rastreadora de Compradores - Nicho: Saúde")

# Filtros
filtro_nicho = st.selectbox("Escolha o Nicho", ["Saúde", "Beleza", "Pet", "Casa", "Tecnologia"])
filtro_status = st.selectbox("Status", ["Todos", "Novo", "Abordado"])

# Aplicar filtros
if filtro_status != "Todos":
    df = df[df["Status"] == filtro_status]

st.dataframe(df, use_container_width=True)

# Botão para exportar
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("📄 Baixar CSV", data=csv, file_name="leads_encontrados.csv", mime="text/csv")

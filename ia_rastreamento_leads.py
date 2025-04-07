import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="IA Rastreadora de Compradores", layout="wide")

# Dados simulados para múltiplos nichos
dados = {
    "Saúde": [
        {"Nome": "@mariafit", "Produto": "Colágeno Hidrolisado", "Rede Social": "Instagram", "Link": "https://instagram.com/mariafit", "Data": "07/04/2025", "Status": "Novo"},
        {"Nome": "rafael.saude", "Produto": "Ômega 3", "Rede Social": "OLX", "Link": "https://olx.com.br/perfil/rafael.saude", "Data": "07/04/2025", "Status": "Novo"},
        {"Nome": "@nutrimarcia", "Produto": "Vitamina D3", "Rede Social": "Instagram", "Link": "https://instagram.com/nutrimarcia", "Data": "07/04/2025", "Status": "Novo"},
    ],
    "Beleza": [
        {"Nome": "@carol.makeup", "Produto": "Base Líquida", "Rede Social": "Instagram", "Link": "https://instagram.com/carol.makeup", "Data": "07/04/2025", "Status": "Novo"},
        {"Nome": "@dicasdebeleza", "Produto": "Hidratante Facial", "Rede Social": "Instagram", "Link": "https://instagram.com/dicasdebeleza", "Data": "07/04/2025", "Status": "Novo"},
    ],
    "Pet": [
        {"Nome": "@petfeliz", "Produto": "Ração Premium", "Rede Social": "Instagram", "Link": "https://instagram.com/petfeliz", "Data": "07/04/2025", "Status": "Novo"},
        {"Nome": "petshop_bahia", "Produto": "Areia_

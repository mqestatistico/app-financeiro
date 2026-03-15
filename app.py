import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Configuração da Página
st.set_page_config(page_title="Dashboard ATCG Finance", layout="wide")

st.title("📊 Monitor de Mercado")
st.markdown("---")

# 1. Sidebar para Inputs
st.sidebar.header("Configurações")
periodo = st.sidebar.selectbox("Período", ["1mo", "3mo", "6mo", "1y", "5y"])

# 2. Definição dos Ativos (Ibovespa e Dólar)
ativos = {"IBOVESPA": "^BVSP", "DÓLAR/REAL": "USDBRL=X"}

# 3. Layout em Colunas para Métricas
cols = st.columns(len(ativos))

for i, (nome, ticker) in enumerate(ativos.items()):
    # Usamos progress=False para não sujar o log do Streamlit
    dados = yf.download(ticker, period=periodo, progress=False)
    
    if not dados.empty:
        # .item() extrai o valor numérico de uma Series de um único elemento
        ultimo_fechamento = float(dados['Close'].iloc[-1])
        primeiro_fechamento = float(dados['Close'].iloc[0])
        
        variacao = ((ultimo_fechamento / primeiro_fechamento) - 1) * 100
        
        with cols[i]:
            # Agora os valores são floats puros e a formatação funcionará
            st.metric(label=nome, value=f"{ultimo_fechamento:,.2f}", delta=f"{variacao:.2f}%")
            
            # Gráfico de Linha
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=dados.index, y=dados['Close'], mode='lines', name=nome))
            fig.update_layout(height=300, margin=dict(l=0, r=0, t=0, b=0))
            st.plotly_chart(fig, use_container_width=True)
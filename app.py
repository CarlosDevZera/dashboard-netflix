import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# DADOS: Carregar o conjunto de dados
df_netflix = pd.read_csv('netflix_titles.csv')

# --- PREPARANDO OS DADOS: LIMPEZA INICIAL E CONVERSÃO DE TIPOS ---

# 1. Preencher valores nulos
df_netflix = df_netflix.fillna('Não informado')

# 2. Converter a coluna de datas para o formato datetime
df_netflix['date_added'] = pd.to_datetime(df_netflix['date_added'], format='mixed', errors='coerce')

# 3. Extrair o ano da data
df_netflix['ano_adicionado'] = df_netflix['date_added'].dt.year

# 4. Preencher nulos com 0 e converter para int
df_netflix['ano_adicionado'] = df_netflix['ano_adicionado'].fillna(0).astype(int)

# 5. Limpar a coluna de país de forma definitiva
# (Ajuste final para lidar com vírgulas e espaços)
df_netflix['country'] = df_netflix['country'].str.replace(', ', ',').str.replace(',', ', ').fillna('Não informado')

# CONSTRUINDO O DASHBOARD
st.title('Análise do Catálogo da Netflix')

# --- ADICIONANDO FILTROS NA BARRA LATERAL ---
st.sidebar.header('Filtros')

# Criar um filtro para o tipo de conteúdo (Filme ou Série)
tipo_conteudo = st.sidebar.selectbox(
    'Selecione o tipo de conteúdo:',
    ['Todos', 'Movie', 'TV Show']
)

# Adicionar a uma lista de países únicos
paises_disponiveis = df_netflix['country'].str.split(', ').explode().unique()
paises_disponiveis = [pais.strip() for pais in paises_disponiveis if pais.strip() != '']
paises_disponiveis = sorted(paises_disponiveis)
paises_disponiveis = ['Todos'] + paises_disponiveis

# Criar o filtro para país
pais_selecionado = st.sidebar.selectbox(
    'Selecione o país de produção:',
    paises_disponiveis
)

# --- FILTRAR O DATAFRAME COM BASE NA SELEÇÃO ---
df_filtrado = df_netflix.copy()
if tipo_conteudo != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['type'] == tipo_conteudo]

if pais_selecionado != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['country'].str.contains(pais_selecionado)]


# --- VERIFICA SE O DATAFRAME FILTRADO NÃO ESTÁ VAZIO ---
if df_filtrado.empty:
    st.warning('Nenhum resultado encontrado para os filtros selecionados.')
else:
    # SEPARAR E CONTAR GÊNEROS (PARA O GRÁFICO)
    generos_contagem = df_filtrado['listed_in'].str.split(', ').explode().value_counts()
    df_generos_contagem = generos_contagem.head(10).reset_index()
    df_generos_contagem.columns = ['genero', 'contagem']

    # GRÁFICO: Top 10 Gêneros
    st.subheader('Top 10 Gêneros')
    st.write('Gráfico de barras mostrando os gêneros com o maior número de títulos.')

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='contagem', y='genero', data=df_generos_contagem, ax=ax)
    ax.set_title(f'Top 10 Gêneros na Netflix ({tipo_conteudo}, {pais_selecionado})')
    ax.set_xlabel('Número de Títulos')
    ax.set_ylabel('Gênero')
    st.pyplot(fig)
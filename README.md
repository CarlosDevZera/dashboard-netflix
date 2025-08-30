# dashboard-netflix

### Análise Interativa do Catálogo da Netflix

Este projeto é um dashboard interativo construído com **Python** e **Streamlit** para analisar a estratégia de conteúdo da Netflix em diferentes países. Ele permite explorar o catálogo, filtrando por tipo de conteúdo e país de produção, para descobrir insights sobre o comportamento da plataforma em mercados globais.

---

## O Problema

A base de dados do catálogo da Netflix é grande e cheia de informações valiosas, mas, em seu estado bruto, não é fácil de ser analisada. O objetivo deste projeto foi transformar esses dados em uma ferramenta visual e intuitiva para extrair informações estratégicas de forma rápida.

---

## Principais Insights

O dashboard revela que a Netflix adota uma estratégia de produção regionalizada. Ao comparar diferentes países, é possível notar como o foco muda drasticamente:

* **Estados Unidos:** A estratégia é de volume massivo, com um foco em gêneros tradicionais como **"Dramas"** e **"Comedies"**, que são o coração de Hollywood.
* **Espanha:** A estratégia é de criar hits globais a partir de um mercado regional, com um foco em gêneros como **"International Movies"** e **"Dramas"** que se tornam fenômenos em escala mundial, como **"La Casa de Papel"**.

---

## Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Pandas:** Para manipulação e limpeza dos dados.
* **Streamlit:** Para a construção do dashboard interativo.
* **Matplotlib** e **Seaborn:** Para a criação dos gráficos de visualização.

---

## Como Rodar o Projeto Localmente

1.  Certifique-se de ter o Python e o Streamlit instalados.
2.  Clone este repositório.
3.  Instale as dependências usando:
    ```
    pip install -r requirements.txt
    ```
4.  Execute a aplicação com o comando:
    ```
    streamlit run app.py
    ```

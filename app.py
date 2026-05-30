import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="AutoCar",
    page_icon="lulafoto",
    layout="wide"
)

# Dados de exemplo
carros = [
    {
        "Modelo": "Toyota Corolla",
        "Ano": 2023,
        "Preço": 145000,
        "Combustível": "Flex",
        "Imagem": "https://images.unsplash.com/photo-1549399542-7e3f8b79c341"
    },
    {
        "Modelo": "Honda Civic",
        "Ano": 2024,
        "Preço": 165000,
        "Combustível": "Flex",
        "Imagem": "https://images.unsplash.com/photo-1552519507-da3b142c6e3d"
    },
    {
        "Modelo": "BMW 320i",
        "Ano": 2023,
        "Preço": 320000,
        "Combustível": "Gasolina",
        "Imagem": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7"
    },
    {
        "Modelo": "Tesla Model 3",
        "Ano": 2024,
        "Preço": 350000,
        "Combustível": "Elétrico",
        "Imagem": "https://images.unsplash.com/photo-1560958089-b8a1929cea89"
    }
]

df = pd.DataFrame(carros)

# Título
st.title("lulafoto AutoCar")
st.subheader("Encontre o carro ideal para você")

# Sidebar
st.sidebar.header("Filtros")

combustivel = st.sidebar.selectbox(
    "Combustível",
    ["Todos"] + list(df["Combustível"].unique())
)

preco_max = st.sidebar.slider(
    "Preço Máximo (R$)",
    50000,
    400000,
    400000,
    10000
)

# Aplicar filtros
filtrado = df[df["Preço"] <= preco_max]

if combustivel != "Todos":
    filtrado = filtrado[filtrado["Combustível"] == combustivel]

# Mostrar resultados
st.write(f"### {len(filtrado)} carros encontrados")

for _, carro in filtrado.iterrows():
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(carro["Imagem"], use_container_width=True)

    with col2:
        st.subheader(carro["Modelo"])
        st.write(f" Ano: {carro['Ano']}")
        st.write(f" Combustível: {carro['Combustível']}")
        st.write(f" Preço: R$ {carro['Preço']:,.2f}")

        if st.button(
            f"Ver detalhes - {carro['Modelo']}",
            key=carro["Modelo"]
        ):
            st.success(
                f"Você selecionou o {carro['Modelo']}"
            )

    st.divider()

# Rodapé
st.markdown("---")
st.caption("© 2025 AutoCar - Catálogo de veículos")
import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="AutoCar",
    page_icon="🚗",
    layout="wide"
)


def criar_carro(modelo, ano, preco, combustivel, imagem=""):
    if ano <= 2010:
        categoria = "Carro antigo / clássico"
        descricao = "Modelo mais antigo, bom para quem gosta de carro clássico ou usado barato."
    else:
        categoria = "Carro moderno"
        descricao = "Modelo mais novo, com visual atual e mais tecnologia."

    return {
        "Modelo": modelo,
        "Ano": ano,
        "Preço": preco,
        "Combustível": combustivel,
        "Imagem": imagem,
        "Categoria": categoria,
        "Detalhes": descricao
    }


carros = [
    criar_carro("Toyota Corolla", 2023, 145000, "Flex"),
    criar_carro("Honda Civic", 2024, 165000, "Flex"),
    criar_carro("BMW 320i", 2023, 320000, "Gasolina"),
    criar_carro("Tesla Model 3", 2024, 350000, "Elétrico"),
    criar_carro("Volkswagen Golf GTI", 2022, 210000, "Gasolina"),
    criar_carro("Chevrolet Onix", 2024, 89000, "Flex"),
    criar_carro("Hyundai HB20", 2024, 92000, "Flex"),
    criar_carro("Fiat Argo", 2023, 78000, "Flex"),
    criar_carro("Jeep Renegade", 2023, 125000, "Flex"),
    criar_carro("Volkswagen T-Cross", 2024, 155000, "Flex"),
    criar_carro("Chevrolet Tracker", 2024, 148000, "Flex"),
    criar_carro("Nissan Kicks", 2023, 135000, "Flex"),
    criar_carro("Honda HR-V", 2024, 165000, "Flex"),
    criar_carro("Toyota Hilux", 2023, 290000, "Diesel"),
    criar_carro("Ford Ranger", 2024, 310000, "Diesel"),
    criar_carro("Chevrolet S10", 2023, 275000, "Diesel"),
    criar_carro("Mitsubishi L200 Triton", 2024, 300000, "Diesel"),
    criar_carro("BYD Dolphin", 2024, 150000, "Elétrico"),
    criar_carro("Volvo XC40 Recharge", 2024, 330000, "Elétrico"),
    criar_carro("Audi A3", 2023, 260000, "Gasolina"),
    criar_carro("Mercedes-Benz C180", 2023, 285000, "Gasolina"),
    criar_carro("Porsche Macan", 2022, 390000, "Gasolina"),
    criar_carro("Fiat Pulse", 2024, 115000, "Flex"),
    criar_carro("Renault Kwid", 2024, 72000, "Flex"),

    # Carros antigos de 1990 até 2010
    criar_carro("Volkswagen Gol CL", 1990, 14000, "Gasolina"),
    criar_carro("Chevrolet Monza SL/E", 1991, 18000, "Gasolina"),
    criar_carro("Fiat Uno Mille", 1992, 12000, "Gasolina"),
    criar_carro("Ford Escort XR3", 1993, 25000, "Gasolina"),
    criar_carro("Volkswagen Santana", 1994, 22000, "Gasolina"),
    criar_carro("Chevrolet Kadett", 1995, 19000, "Gasolina"),
    criar_carro("Fiat Tempra", 1996, 17000, "Gasolina"),
    criar_carro("Volkswagen Parati", 1997, 21000, "Gasolina"),
    criar_carro("Chevrolet Corsa Wind", 1998, 16000, "Gasolina"),
    criar_carro("Volkswagen Kombi", 1999, 35000, "Gasolina"),
    criar_carro("Fiat Palio", 2000, 15000, "Gasolina"),
    criar_carro("Renault Clio", 2001, 17000, "Gasolina"),
    criar_carro("Peugeot 206", 2002, 18000, "Gasolina"),
    criar_carro("Toyota Corolla XEi", 2003, 32000, "Gasolina"),
    criar_carro("Honda Civic LX", 2004, 34000, "Gasolina"),
    criar_carro("Chevrolet Astra", 2005, 26000, "Flex"),
    criar_carro("Fiat Siena", 2006, 22000, "Flex"),
    criar_carro("Volkswagen Golf", 2007, 38000, "Gasolina"),
    criar_carro("Honda Fit", 2008, 36000, "Flex"),
    criar_carro("Mitsubishi Pajero TR4", 2010, 52000, "Flex")
]

df = pd.DataFrame(carros)


def formatar_preco(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


st.title("Carros")
st.subheader("Encontre o carro ideal para você")


st.sidebar.header("Filtros")

busca = st.sidebar.text_input("Buscar carro pelo nome")

combustivel = st.sidebar.selectbox(
    "Combustível",
    ["Todos"] + sorted(list(df["Combustível"].unique()))
)

ano_minimo = int(df["Ano"].min())
ano_maximo = int(df["Ano"].max())

ano_inicio, ano_fim = st.sidebar.slider(
    "Ano do carro",
    min_value=ano_minimo,
    max_value=ano_maximo,
    value=(ano_minimo, ano_maximo),
    step=1
)

preco_minimo = int(df["Preço"].min())
preco_maximo = int(df["Preço"].max())

valor_min, valor_max = st.sidebar.slider(
    "Faixa de preço",
    min_value=preco_minimo,
    max_value=preco_maximo,
    value=(preco_minimo, preco_maximo),
    step=10000
)

st.sidebar.write(f"Valor mínimo: {formatar_preco(valor_min)}")
st.sidebar.write(f"Valor máximo: {formatar_preco(valor_max)}")

# Aplicar filtros
filtrado = df[
    (df["Preço"] >= valor_min) &
    (df["Preço"] <= valor_max) &
    (df["Ano"] >= ano_inicio) &
    (df["Ano"] <= ano_fim)
]

if combustivel != "Todos":
    filtrado = filtrado[filtrado["Combustível"] == combustivel]

if busca:
    filtrado = filtrado[
        filtrado["Modelo"].str.contains(busca, case=False, na=False)
    ]

# Mostrar resultados
st.write(f"### {len(filtrado)} carros encontrados")

if filtrado.empty:
    st.warning("Nenhum carro encontrado com esses filtros.")

for _, carro in filtrado.iterrows():
    col1, col2 = st.columns([1, 2])

    with col1:
        imagem = str(carro["Imagem"]).strip()

        if imagem:
            st.image(imagem, use_container_width=True)
        else:
            st.info("Foto ainda não adicionada")

    with col2:
        st.subheader(f"{carro['Modelo']} - {carro['Ano']}")
        st.write(f"**Preço:** {formatar_preco(carro['Preço'])}")
        st.write(f"**Combustível:** {carro['Combustível']}")

        with st.expander("🔎 Ver detalhes do carro"):
            st.write(f"**Modelo:** {carro['Modelo']}")
            st.write(f"**Ano:** {carro['Ano']}")
            st.write(f"**Categoria:** {carro['Categoria']}")
            st.write(f"**Combustível:** {carro['Combustível']}")
            st.write(f"**Preço anunciado:** {formatar_preco(carro['Preço'])}")
            st.write(f"**Descrição:** {carro['Detalhes']}")

            st.info(
                "Para colocar foto, cole o link da imagem no campo imagem do carro."
            )

    st.divider()


st.markdown("---")
st.caption("Thigas.com")
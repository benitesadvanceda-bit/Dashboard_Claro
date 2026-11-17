import streamlit as st

from db import conectar, consultar

st.set_page_config(page_title="Dashboard Claro", layout="wide")
st.title("Dashboard Claro")


@st.cache_resource
def conexao():
    return conectar()


try:
    conn = conexao()
    st.success(f"Conectado ao Oracle {conn.version}")
except Exception as e:  # noqa: BLE001
    st.error(f"Falha ao conectar ao Oracle: {e}")
    st.stop()

sql = st.text_area(
    "Consulta SQL (somente leitura)",
    "SELECT table_name FROM user_tables ORDER BY table_name",
)
if st.button("Executar"):
    try:
        st.dataframe(consultar(conn, sql), use_container_width=True)
    except Exception as e:  # noqa: BLE001
        st.error(str(e))

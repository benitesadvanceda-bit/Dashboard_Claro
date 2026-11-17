"""Conexão com o Oracle usando python-oracledb (thin por padrão; thick se ORACLE_CLIENT_LIB_DIR estiver definida)."""
import os

import oracledb
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Modo thick (Oracle Instant Client): necessário quando o banco usa recursos que o
# modo thin não suporta, ex.: DPY-3015 (verificador de senha antigo 10G).
_lib_dir = os.getenv("ORACLE_CLIENT_LIB_DIR")
if _lib_dir:
    oracledb.init_oracle_client(lib_dir=_lib_dir)


def conectar() -> oracledb.Connection:
    faltando = [v for v in ("ORACLE_USER", "ORACLE_PASSWORD", "ORACLE_DSN") if not os.getenv(v)]
    if faltando:
        raise RuntimeError(f"Variáveis de ambiente ausentes: {', '.join(faltando)}")
    return oracledb.connect(
        user=os.environ["ORACLE_USER"],
        password=os.environ["ORACLE_PASSWORD"],
        dsn=os.environ["ORACLE_DSN"],
    )


def consultar(conn: oracledb.Connection, sql: str, params: dict | None = None) -> pd.DataFrame:
    with conn.cursor() as cur:
        cur.execute(sql, params or {})
        colunas = [c[0] for c in cur.description]
        return pd.DataFrame(cur.fetchall(), columns=colunas)


if __name__ == "__main__":
    # Teste rápido: python db.py
    with conectar() as conn:
        print("Conectado! Versão do Oracle:", conn.version)
        print(consultar(conn, "SELECT USER AS usuario, SYSDATE AS agora FROM dual"))

"""Conexão com o Oracle usando python-oracledb (modo thin, sem Oracle Client)."""
import os

import oracledb
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


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

# Dashboard Claro

Dashboard em Python + Streamlit conectado a um banco Oracle via `python-oracledb` (modo thin — não precisa instalar o Oracle Client).

## Como rodar

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # preencha usuário, senha e DSN
python db.py                # testa a conexão
streamlit run app.py        # abre o dashboard
```

O arquivo `.env` contém credenciais e **não** deve ser commitado (já está no `.gitignore`).

`ORACLE_DSN` usa o formato `host:porta/service_name`, ex.: `oracle.empresa.com:1521/ORCLPDB1`.

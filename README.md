# 🔍 Crawler de Vagas no LinkedIn

Projeto de **web scraping automatizado** com Selenium para coleta de vagas de emprego publicadas no LinkedIn. Os dados são processados e armazenados em um banco de dados PostgreSQL, com foco em robustez, testes e boas práticas de desenvolvimento.

## Funcionalidades

- 🔎 **Busca automatizada de vagas** com `Selenium` com base em palavra-chave (ex: "Python remoto").
- 🧼 **Limpeza e normalização** dos dados com `Pandas`.
- 🧠 **Verificação de duplicatas** com SQLAlchemy ORM, utilizando `filtros e consultas otimizadas`.
- 🗃️ **Armazenamento estruturado em PostgreSQL**, usando `SQLAlchemy ORM`.
- 🧪 **Testes unitários** com `pytest` e `unittest.mock`.   
- 📁 **`Logs**` persistentes** para rastrear execuções e erros.
- 📒  **`Notebook*` Jupyter adaptativo**, criado para facilitar o desenvolvimento incremental do crawler com Selenium. Permite executar etapas isoladamente. Ideal para estudo, debugging e reprocessamento controlado de dados sem comprometer o fluxo principal.


## Como Executar o Projeto 

### 1. Clonar o repositório

```
git clone https://github.com/Joao-Dias-10/crawler_de_vagas.git
cd crawler_de_vagas
```

### 2. Criar e ativar o ambiente virtual

```
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
```

### 3. Instalar as dependências

```
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente (.env)

```
DATABASE_URL=postgresql://usuario:senha@localhost:port/nome_do_banco
USER_LINKEDIN=seu_email
PASSWORD_LINKEDIN=sua_senha
```




# 🔍 Crawler de Vagas no LinkedIn

Este projeto realiza scraping de vagas de emprego publicadas no LinkedIn com base em uma palavra-chave (ex: "Python remoto"). As vagas são processadas, limpas e salvas automaticamente em um banco de dados PostgreSQL.

---

## 🚀 Como funciona

1. **Coleta** vagas usando automação com Selenium.
2. **Limpa** os dados extraídos (removendo duplicatas e normalizando campos).
3. **Armazena** no banco de dados com SQLAlchemy, evitando registros duplicados.
4. **Registra logs** de execução e possíveis erros.

---

## 🧪 Execução

```bash
python main.py
# crawler_de_vagas

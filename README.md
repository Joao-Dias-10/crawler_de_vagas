# 🔍 Crawler de Vagas no LinkedIn

Este é um projeto automatizado para **mineração de dados** (web scraping) que coleta vagas de emprego publicadas no LinkedIn, utilizando a automação do Selenium para garantir a extração eficiente e precisa das informações.

As vagas são coletadas com base em uma palavra-chave (ex: "Python remoto"), processadas, limpas e armazenadas automaticamente em um banco de dados **PostgreSQL**. O sistema foi desenvolvido para ser **eficiente**, **escalável** e **sem duplicações**.

## 🚀 Funcionalidades

- **Coleta automatizada**: O crawler utiliza o **Selenium** para navegar nas páginas do LinkedIn e coletar as vagas mais recentes relacionadas à palavra-chave configurada.
- **Limpeza de dados**: Usando **Pandas**, o sistema trata e normaliza os dados coletados, removendo duplicatas e garantindo a qualidade das informações.
- **Banco de dados PostgreSQL**: As vagas são armazenadas de maneira otimizada no **PostgreSQL**, com tabelas criadas automaticamente através de **SQLAlchemy** e verificações de duplicação para manter a integridade dos dados.
- **Execução eficiente**: O sistema foi projetado para ser rápido e eficaz, garantindo que apenas as vagas mais recentes e relevantes sejam coletadas, sem registros duplicados.
- **Logs de execução**: O sistema registra logs detalhados de cada execução, facilitando a identificação de erros e o monitoramento do desempenho.

## 🧑‍💻 Como Executar o Projeto

### 1. **Instalar as dependências**

Primeiro, você precisa instalar as dependências necessárias para o projeto. Certifique-se de ter o **Python 3.8 ou superior** instalado em sua máquina. Depois, instale as dependências do projeto:

```bash
pip install -r requirements.txt

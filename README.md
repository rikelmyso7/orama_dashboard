# Orama Dashboard

## Sobre o Projeto

Este projeto é uma solução completa de automação e visualização de relatórios, com foco em tornar a análise de dados **mais interativa, rápida e confiável**.

Atualmente, ele realiza duas grandes tarefas:

- **Automação de Relatórios**: Utilizando **RPA com Selenium**, o sistema acessa uma plataforma web (SmartPOS), realiza login automático, busca as vendas do período selecionado, coleta todas as informações relevantes e gera um arquivo Excel (.xlsx) organizado.

- **Visualização Interativa**: Após gerar o relatório, o sistema oferece um **Dashboard Streamlit** moderno e responsivo. Nele, o usuário pode visualizar os dados reais em **gráficos interativos** (Plotly) que facilitam a interpretação dos resultados e apoiam a tomada de decisão.

---

## Objetivo
Esta solução foi desenvolvida com os seguintes propósitos:

- Melhorar a forma como a empresa conduzia reuniões de apresentação de resultados.
- Tornar os relatórios **mais claros, objetivos e profissionais**.
- Automatizar processos manuais de outro setor, otimizando tempo e reduzindo erros humanos.
- Facilitar o acesso a dados em tempo real para tomadas de decisão mais rápidas e embasadas.

---

## Como Rodar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

---

pip install -r requirements.txt

### 3. Configure as variáveis de ambiente
- Crie um arquivo .env na raiz do projeto com:

# ex:
- EMAIL=seu_email_no_smartpos
- SENHA=sua_senha_no_smartpos

### 4. Gerar o Relatório (.xlsx)
- Execute o scraper:

make gerar-relatorio

### 5. Rodar o Dashboard
- Após gerar o relatório:

make dashboard


### Tecnologias Usadas

Python
Streamlit
Selenium
Plotly Express
Pandas
OpenPyXL
PyAutoGUI
dotenv

---

![vendas19_05](https://github.com/user-attachments/assets/68ee242b-9d6d-41ea-a480-3a4d01f66788)
![produtos19_05](https://github.com/user-attachments/assets/9faf06ab-5aa3-4283-8ee7-55d8a8432558)

### Projeto desenvolvido para Orama Brasil, focado em otimizar análises internas e melhorar a gestão de dados.

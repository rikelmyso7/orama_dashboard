# Variáveis
PYTHON=python
STREAMLIT=streamlit

# Comandos
install:
	pip install -r requirements.txt

gerar-relatorio:
	$(PYTHON) -m gerar_planilha.run_scraper

dashboard:
	$(STREAMLIT) run main_app.py

env-example:
	echo "EMAIL=seu_email@exemplo.com" > .env.example && echo "SENHA=sua_senha" >> .env.example

clean-pyc:
	find . -type f -name "*.pyc" -delete

clean-cache:
	find . -type d -name "__pycache__" -exec rm -r {} +

clean:
	make clean-pyc
	make clean-cache


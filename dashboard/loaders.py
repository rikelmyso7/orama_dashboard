import pandas as pd

def load_excel(filepath: str) -> pd.DataFrame:
    try:
        return pd.read_excel(filepath)
    except FileNotFoundError:
        raise Exception(f"Arquivo não encontrado: {filepath}")
    except Exception as e:
        raise Exception(f"Erro ao carregar o arquivo {filepath}: {str(e)}")

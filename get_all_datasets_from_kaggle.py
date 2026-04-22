import kagglehub
import pandas as pd
import shutil
from pathlib import Path

from config_paths import PATH_RAW_FILES
from config_tables import TABLES

# Baixa para o cache e copia para o projeto
cache = Path(kagglehub.dataset_download("olistbr/brazilian-ecommerce"))

for arquivo in cache.glob("*.csv"):
    shutil.copy(arquivo, PATH_RAW_FILES / arquivo.name)

dfs = {}

for nome, (arquivo, encoding) in TABLES.items():
    df = pd.read_csv(PATH_RAW_FILES / arquivo, encoding=encoding)
    dfs[nome] = df
    print(f"{nome}: {df.shape[0]} linhas, {df.shape[1]} colunas")
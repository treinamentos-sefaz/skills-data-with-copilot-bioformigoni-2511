"""Módulo 2 — Manipulação de DataFrames com pandas.

Complete cada função com o apoio do GitHub Copilot. Prefira operações
vetorizadas e evite alterar o DataFrame original (use ``.copy()``).

Valide com:  ``python lab/check.py --module pandas``
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def load_wines(path: str) -> pd.DataFrame:
    """Leia o CSV em ``path`` e retorne um DataFrame do pandas."""
    # Prompt sugerido: "Leia o arquivo CSV em path com pandas e retorne o DataFrame."
    return pd.read_csv(path)


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Converta a coluna ``rating`` para numérico e remova as linhas cujo
    ``rating`` seja nulo. Retorne o DataFrame limpo."""
    # Prompt sugerido:
    # "Crie uma cópia de df com .copy(), converta a coluna rating para numérico
    #  usando pd.to_numeric(..., errors='coerce') e remova as linhas com rating
    #  nulo usando dropna(subset=['rating']). Retorne o DataFrame limpo."
    return (
        df.copy()
        .assign(rating=lambda d: pd.to_numeric(d["rating"], errors="coerce"))
        .dropna(subset=["rating"])
    )


def top_varieties_by_avg_rating(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Retorne as ``n`` variedades com maior média de ``rating`` (colunas:
    variety, avg_rating), ordenadas da maior para a menor."""
    # Prompt sugerido:
    # "Agrupe df por variety, calcule a média de rating nomeando a coluna como
    #  avg_rating, ordene por avg_rating em ordem decrescente e retorne um
    #  DataFrame com as n primeiras linhas contendo as colunas variety e avg_rating."
    return (
        df.groupby("variety", as_index=False)
        .agg(avg_rating=("rating", "mean"))
        .sort_values("avg_rating", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )


def add_rating_category(df: pd.DataFrame) -> pd.DataFrame:
    """Adicione a coluna ``rating_category`` com as faixas: "Baixa" (< 85),
    "Média" (85 a 90) e "Alta" (> 90). Dica: use ``pd.cut``."""
    # Prompt sugerido:
    # "Crie uma cópia de df com .copy() e adicione a coluna rating_category usando
    #  pd.cut sobre a coluna rating com os labels ['Baixa', 'Média', 'Alta'], onde
    #  'Baixa' é < 85, 'Média' é de 85 a 90 (inclusivo) e 'Alta' é > 90."
    # pd.cut não consegue fechar 85 e 90 no mesmo lado do intervalo, então usa-se np.select.
    rating = df["rating"]
    conditions = [rating < 85, rating <= 90, rating > 90]
    labels = ["Baixa", "Média", "Alta"]
    return df.copy().assign(
        rating_category=np.select(conditions, labels, default=None)
    )


def enrich_with_country(df: pd.DataFrame) -> pd.DataFrame:
    """Adicione a coluna ``country`` extraindo o último trecho após a vírgula de
    ``region`` (ex.: "Mendocino, California" -> "California")."""
    # Prompt sugerido:
    # "Crie uma cópia de df com .copy() e adicione a coluna country extraindo o
    #  último trecho após a vírgula da coluna region usando str.split(',').str[-1].str.strip()."
    return df.copy().assign(
        country=lambda d: d["region"].str.split(",").str[-1].str.strip()
    )

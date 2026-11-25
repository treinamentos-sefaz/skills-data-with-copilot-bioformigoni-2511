"""Módulo 4 — Visualização de Dados.

Complete cada função com o apoio do GitHub Copilot. Cada função deve **gerar um
gráfico e salvá-lo** no caminho ``out_path`` (formato PNG). Use ``matplotlib`` e
``seaborn``. Em ambientes sem interface gráfica (CI), mantenha o backend "Agg".

Valide com:  ``python lab/check.py --module viz``
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # backend sem interface gráfica (funciona no CI)
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402


def _salvar_figura(fig, out_path: str):
    """Ajusta o layout, salva a figura em PNG (dpi=100), fecha e a retorna."""
    fig.tight_layout()
    fig.savefig(out_path, dpi=100)
    plt.close(fig)
    return fig


def plot_rating_distribution(df: pd.DataFrame, out_path: str):
    """Histograma da distribuição da coluna ``rating``. Inclua título e labels em
    português e salve a figura em ``out_path``."""
    # Prompt sugerido:
    # "Crie um histograma da coluna rating com 20 bins usando plt.subplots(),
    #  adicione título e labels de eixos em português, salve a figura em out_path
    #  como PNG (dpi=100), feche com plt.close(fig) e retorne fig."
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["rating"].dropna(), bins=20, color="#722f37", edgecolor="white")
    ax.set_title("Distribuição das avaliações (rating)")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Quantidade de vinhos")
    return _salvar_figura(fig, out_path)


def plot_top_varieties(df: pd.DataFrame, out_path: str):
    """Gráfico de barras horizontais com as 10 variedades (``variety``) com maior
    quantidade de vinhos. Salve a figura em ``out_path``."""
    # Prompt sugerido:
    # "Gere um gráfico de barras horizontais (ax.barh) com as 10 variedades mais
    #  frequentes de df['variety'].value_counts().head(10), ordenadas por quantidade,
    #  com título e labels de eixos em português, salve em out_path como PNG
    #  (dpi=100), feche com plt.close(fig) e retorne fig."
    contagens = df["variety"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(contagens.index, contagens.values, color="#722f37")
    ax.invert_yaxis()  # maior quantidade no topo
    ax.set_title("As 10 variedades com mais vinhos")
    ax.set_xlabel("Quantidade de vinhos")
    ax.set_ylabel("Variedade")
    return _salvar_figura(fig, out_path)


def plot_boxplot_by_variety(df: pd.DataFrame, out_path: str):
    """Boxplot de ``rating`` para as 5 variedades mais frequentes. Salve a figura
    em ``out_path``."""
    # Prompt sugerido:
    # "Filtre df para manter apenas as 5 variedades mais frequentes da coluna variety
    #  e gere um boxplot de rating por variety usando sns.boxplot(data=..., x='variety',
    #  y='rating', ax=ax), com título e labels de eixos em português. Salve em out_path
    #  como PNG (dpi=100), feche com plt.close(fig) e retorne fig."
    top5 = df["variety"].value_counts().head(5).index
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(
        data=df[df["variety"].isin(top5)],
        x="variety",
        y="rating",
        order=top5,
        ax=ax,
    )
    ax.set_title("Distribuição de rating nas 5 variedades mais frequentes")
    ax.set_xlabel("Variedade")
    ax.set_ylabel("Rating")
    return _salvar_figura(fig, out_path)

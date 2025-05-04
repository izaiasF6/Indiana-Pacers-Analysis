import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
from pandas import DataFrame


def vertical_bar_chart(
        dataframe: DataFrame,
        columns: list[str],
        reverse=False
) -> Figure:
    """Cria uma figura com gráficos de barras verticais, destacando sempre o Indiana Pacers

    Parâmetros:
        dataframe (DataFrame): dataframe com os dados
        columns (list[str]): lista com as colunas (estatísticas) do dataframe a serem visualizadas
        reverse (booleano): se True, ordena o gráfico de forma crescente. Se False, decrescente.

    Returns:
        Figure: Objeto Figure contendo gráficos de barras verticais
    """

    # Cria a figura
    fig, axes = plt.subplots(nrows=2,
                             ncols=int(len(columns) / 2),
                             figsize=(30, 15)
    )
    axes = axes.flatten()  #Transforma matriz de axes em lista para iteração

    # Itera sobre cada métrica informada em "columns", criando um gráfico
    for i, column in enumerate(columns):
        ax = axes[i]
        media = dataframe[column].mean()  # Calcula a média da métrica atual

        # Ordena o dataframe pela métrica atual
        dataframe = dataframe.sort_values(by=column, ascending=reverse).reset_index(drop=True)

        # Cria uma lista com os 8 melhores times e outra com suas métricas
        bar_points = dataframe[column].head(8).astype(float).tolist()
        bar_team = dataframe["team"].head(8).tolist()

        # Verifica se o Indiana Pacers está entre os 8 primeiros, e se não estiver, adiciona-o
        if "Indiana Pacers" not in bar_team:
            index = dataframe.query("team == 'Indiana Pacers'").index[0]
            bar_team[-1] = "Indiana Pacers"
            bar_points[-1] = dataframe.loc[dataframe["team"] == "Indiana Pacers", column].values[0]
        else:
            index = bar_team.index("Indiana Pacers") + 1

        # Cria os rótulos das barras
        eixo_labels = [
            f"{idx + 1}° {team.split()[-1]}"
            if team != "Indiana Pacers" else f"{index}° {team.split()[-1]}"
            for idx, team in enumerate(bar_team)
        ]

        # Gera o gráfico com coloração amarela para Indiana e azul para os demais
        sns.set_style("darkgrid")
        sns.barplot(
            y=bar_points,
            x=eixo_labels,
            data=dataframe.head(8),
            ax=ax,
            hue="team",
            palette=["#FDBB30" if team == "Indiana Pacers" else "#002D62" for team in bar_team],
            legend=False,
        )

        # Ajusta as posições dos rótulos no eixo x para evitar sobreposição
        for i, label in enumerate(ax.get_xticklabels()):
            if i % 2:
                label.set_y(-0.03)

        # Adiciona os valores dos times no topo
        for bar in ax.patches:
            ax.annotate(
                f"{bar.get_height():.1f}",
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                fontsize=10,
                color="black",
                va="bottom",
                ha="center",
                xytext=(0, 3),
                textcoords="offset points"
            )

        # Define os títulos, rótulos das barras e configurações visuais
        ax.axhline(y=media, color='red', linestyle='--', linewidth=1.2, label=f"Média ({media:.2f}")
        ax.set_title(f"Melhores times em {column}")
        ax.set_xlabel("Times")
        ax.set_ylabel(f"{column} por jogo")
        ax.spines[["top", "right"]].set_visible(False)

    return fig


def horizontal_bar_chart(dataframe: DataFrame,
                                filtered_df: DataFrame,
                                columns: list[str],

) -> Figure:
    """Cria uma figura com gráficos de barras horizontais

    Parâmetros:
        dataframe (DataFrame): DataFrame com os dados
        columns (list[str]): lista com as colunas (estatísticas) do dataframe a serem visualizadas

    Returns:
        Figure: Objeto Figure contendo gráficos de barras horizontais
    """

    # Cria a figura
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(30, 12))
    axes = axes.flatten()

    # Itera sobre cada métrica informada em "columns", criando um gráfico
    for i, column in enumerate(columns):
        ax = axes[i]

        # Ordena o dataframe pela métrica atual
        dataframe = dataframe.sort_values(by=column, ascending=False)

        # Calcula a média da métrica
        league_mean = filtered_df[column].mean()

        # Gera o gráfico com o estilo definido
        sns.set_style("darkgrid")
        sns.barplot(
            y="Player",
            x=column,
            data=dataframe,
            ax =ax,
            hue="Player",
            palette=sns.blend_palette(["#002D62", "#D1E5F0"], n_colors=22),
            orient="h",
            legend=False,
        )

        # Adiciona os valores dos jogadores ao lado da barra
        for bar in ax.patches:
            ax.annotate(
                f"{bar.get_width():.1f}",
                (bar.get_width(), bar.get_y() + bar.get_height() / 2),
                fontsize=8,
                color="black",
                va="center",
                ha="left",
                xytext=(3, 0),
                textcoords="offset points",
            )

        # Define os títulos, rótulos das barras e configurações visuais
        ax.axvline(x=league_mean,
                   color='red',
                   linestyle='--',
                   linewidth=1.2,
                   label=f"Média ({league_mean:.2f})"
        )
        ax.set_title(f"{column} per Game", fontsize=12)
        ax.set_xlabel(None)
        ax.set_ylabel(None)
        ax.spines[["top", "right"]].set_visible(False)

    return fig


def scatter(dataframe: DataFrame,
                       columns: list[str],
                       title: str,
                       xlabel: str,
                       ylabel: str
) -> Figure:
    """Cria uma figura com um dispersograma com base em duas estatísticas fornecidas

    Parâmetros:
        dataframe (DataFrame): dataframe com os dados
        columns (list[str]): lista com duas strings, representando eficiência (%) e tentativas
        title (string): título do gráfico

    Returns:
        Figure: Objeto Figure contendo um gráfico de dispersão
    """

    # Cria a figura
    fig, ax = plt.subplots(figsize=(15, 6))

    # Gera o gráfico de dispersão
    sns.set_style("darkgrid")
    sns.scatterplot(
        data=dataframe,
        x=columns[0],
        y=columns[1],
        s=100,
        ax=ax,
        color="#002D62"
    )

    # Adiciona o nome dos jogadores
    for index, txt in enumerate(dataframe["Player"]):
        plt.annotate(
            txt,
            (dataframe.iloc[index][columns[0]], dataframe.iloc[index][columns[1]]),
            fontsize=8,
            textcoords="offset points",
            xytext=(6, -3),
            ha="left"
        )

    # Define os títulos, rótulos dos pontos e configurações visuais
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.tight_layout()

    return fig


def plot_radar_charts(
        subjects_1: list[str],
        subjects_2: list[str],
        stats_1,
        stats_2,
        player_stats_1,
        player_stats_2,
        label_media: str,
        label_player: str
) -> Figure:
    """Cria uma figura com dois gráficos de radar

    Parâmetros:
        subjects_1 (list of strings):
        stats_1:
        subjects_2 (list of strings):
        stats_2:
        player_stats:
        label_media (string): nome da média para usar na legenda
        label_player (string): nome do jogador para usar na legenda

    Returns:
        Figure: Objeto Figure contendo dois gráficos de radar
    """

    # Cria uma figura com dois subplots polares lado a lado
    fig, axs=plt.subplots(
        1, 2,
        subplot_kw={"polar": True},
        figsize=(12, 8)
    )

    # Gráfico 1: Estatísticas Acumulativas

    # Define os ângulos igualmente espaçados para cada eixo (um para cada atributo)
    angles_1 = np.linspace(0, 2 * np.pi, len(subjects_1), endpoint=False)
    angles_1 = np.concatenate(
        (angles_1, [angles_1[0]])
    )  # Adiciona o primeiro valor ao final do array para fechar o gráfico

    # Fecha os dados adicionando o primeiro valor ao final de cada array
    stats_1 = np.concatenate((stats_1, [stats_1[0]]))
    player_stats_1 = np.concatenate((player_stats_1, [player_stats_1[0]]))
    subjects_1 = subjects_1 + [subjects_1[0]]

    # Plota a linha média e preenche com azul
    axs[0].plot(angles_1, stats_1, color="#002D62",
                label=label_media, marker="o", markersize=4
    )
    axs[0].fill(angles_1, stats_1, color="#002D62", alpha=0.6)

    # Plota a linha do jogador e preenche com amarelo
    axs[0].plot(angles_1, player_stats_1, color="#FDBB30",
                label=label_player, marker='o', markersize=4
    )
    axs[0].fill(angles_1, player_stats_1, color="#FDBB30", alpha=0.5)

    # Define o rótulo e título
    axs[0].set_thetagrids(angles_1 * 180 / np.pi, subjects_1)
    axs[0].set_title("Estatísticas Acumulativas", pad=35, fontsize=14)

    # Gráfico 2: Estatísticas percentuais

    # Repete os processos para construír o segundo gráfico com outros dados
    angles_2 = np.linspace(0, 2 * np.pi, len(subjects_2), endpoint=False)
    angles_2 = np.concatenate((angles_2, [angles_2[0]]))
    stats_2 = np.concatenate((stats_2, [stats_2[0]]))
    player_stats_2 = np.concatenate((player_stats_2, [player_stats_2[0]]))
    subjects_2 = subjects_2 + [subjects_2[0]]

    axs[1].plot(angles_2, stats_2, color="#002D62",
                label=label_media, marker="o", markersize=4
    )
    axs[1].fill(angles_2, stats_2, color="#002D62", alpha=0.6)
    axs[1].plot(angles_2, player_stats_2, color="#FDBB30",
                label=label_player, marker='o', markersize=4
    )
    axs[1].fill(angles_2, player_stats_2, color="#FDBB30", alpha=0.5)
    axs[1].set_thetagrids(angles_2 * 180 / np.pi, subjects_2)
    axs[1].set_title("Estatísticas Percentuais", pad=35, fontsize=14)

    #Ativa as grades no gráfico e posiciona a legenda
    for ax in axs:
        ax.grid(True)
        ax.legend(loc="upper right")

    plt.tight_layout()

    return fig

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
from pandas import DataFrame


def plot_radar_charts(subjects_1, stats_1, subjects_2, stats_2, player_stats, label_media, label_player) -> Figure:
    # Configuração do layout
    fig, axs = plt.subplots(1, 2, subplot_kw=dict(polar=True), figsize=(12, 8))  # Dois subplots lado a lado

    angles_1 = np.linspace(0, 2 * np.pi, len(subjects_1), endpoint=False)
    angles_1 = np.concatenate((angles_1, [angles_1[0]]))
    stats_1 = np.concatenate((stats_1, [stats_1[0]]))  # Adiciona o primeiro valor ao final
    player_stats_1 = np.concatenate((player_stats[:len(subjects_1)], [player_stats[0]]))  # Mesmo para as estatísticas do jogador

    subjects_1 = subjects_1 + [subjects_1[0]]

    axs[0].plot(angles_1, stats_1, color = "blue", label = label_media, marker = "o", markersize = 4)
    axs[0].fill(angles_1, stats_1, color = "blue", alpha=0.25)
    axs[0].plot(angles_1, player_stats_1, color = "yellow", label = label_player, marker='o', markersize = 4)
    axs[0].fill(angles_1, player_stats_1, color = "yellow", alpha = 0.25)
    axs[0].set_thetagrids(angles_1 * 180 / np.pi, subjects_1)
    axs[0].set_title("Estatísticas Acumulativas", pad = 35, fontsize = 14)

    angles_2 = np.linspace(0, 2 * np.pi, len(subjects_2), endpoint=False)
    angles_2 = np.concatenate((angles_2, [angles_2[0]]))
    stats_2 = np.concatenate((stats_2, [stats_2[0]]))
    player_stats_2 = np.concatenate((player_stats[len(subjects_1)-1:], [player_stats[len(subjects_1)-1]]))

    subjects_2 = subjects_2 + [subjects_2[0]]

    axs[1].plot(angles_2, stats_2, color="blue", label=label_media, marker="o", markersize=4)
    axs[1].fill(angles_2, stats_2, color="blue", alpha=0.25)
    axs[1].plot(angles_2, player_stats_2, color="yellow", label=label_player, marker='o', markersize=4)
    axs[1].fill(angles_2, player_stats_2, color="yellow", alpha=0.25)
    axs[1].set_thetagrids(angles_2 * 180 / np.pi, subjects_2)
    axs[1].set_title("Estatísticas Percentuais", pad = 35, fontsize = 14)

    for ax in axs:
        ax.grid(True)
        ax.legend(loc = "upper right")

    plt.tight_layout()
    return plt.show()


def ranking_barchart(dataframe: DataFrame, columns: list[str], reverse = False) -> Figure:
    """Cria uma figura com gráficos de barras para estatísticas da NBA, destacando sempre o Indiana Pacers

    Parâmetros:
        dataframe: dataframe com os dados
        columns (list of strings): lista com as colunas (estatísticas) do dataframe a serem visualizadas
        Reverse (booleano): Controla a ordenação do gráfico. Se True, ordena do menor para o maior valor. Se False, do maior para o menor.

    Returns:
        Figure: Objeto Figure contendo gráficos de barras verticais
    """

    fig, axes = plt.subplots(nrows = 2, ncols = int(len(columns) / 2), figsize = (30, 15)) #Cria uma figura com subplots em duas linhas e número de colunas baseado na quantidade de estatísticas
    axes = axes.flatten() #Transforma matriz de axes em lista para iteração

    #Itera sobre cada métrica informada em "columns", criando um gráfico
    for i, column in enumerate(columns):
        ax = axes[i] #Seleciona o subplot atual
        media = dataframe[column].mean() #Calcula a média da métrica atual para usá-la como linha de referência

        #Ordena o dataframe pela métrica atual
        dataframe = dataframe.sort_values(by = column, ascending = reverse).reset_index(drop = True)

        #Cria uma lista com o nome dos 8 primeiros times da coluna ordenada e outra lista com as respectivas métricas desses times
        bar_points, bar_team = dataframe[column].head(8).astype(float).tolist(), dataframe["team"].head(8).tolist()

        #Verifica se o Indiana Pacers está entre os 8 primeiros, e se não estiver, adiciona-o
        if "Indiana Pacers" not in bar_team:
            index = dataframe.query("team == 'Indiana Pacers'").index[0]
            bar_team[-1], bar_points[-1] = "Indiana Pacers", dataframe.loc[dataframe["team"] == "Indiana Pacers", column].values[0]
        else:
            index = bar_team.index("Indiana Pacers") + 1
        
        #Cria os rótulos das barras
        eixo_labels = [
            f"{idx + 1}° {team.split()[-1]}" if team != "Indiana Pacers" else f"{index}° {team.split()[-1]}"
            for idx, team in enumerate(bar_team)
        ]

        #Define o estilo do gráfico
        sns.set_style("darkgrid")

        #Gera o gráfico com coloração amarela para Indiana e azul para os demais
        sns.barplot(
            y = bar_points,
            x = eixo_labels,
            data = dataframe.head(8),
            ax  = ax,
            hue = "team",
            palette = ["yellow" if team == "Indiana Pacers" else "b" for team in bar_team],
            legend = False,
        )

        #Ajusta as posições dos rótulos no eixo x para evitar sobreposição
        for i, label in enumerate(ax.get_xticklabels()):
            if i % 2: label.set_y(-0.03)

        #Adiciona os valores dos times no topo da barra 
        for bar in ax.patches:
            ax.annotate(
                f"{bar.get_height():.1f}",
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                fontsize = 10,
                color = "black",
                va = "bottom",
                ha = "center",
                xytext = (0, 3),
                textcoords = "offset points"
            ) 

        #Adiciona uma linha horizontal vermelha com a média da estatística
        ax.axhline(y = media, color = 'red', linestyle = '--', linewidth = 1.2, label = f"Média ({media:.2f}")

        #Define os títulos e rótulos dos eixos
        ax.set_title(f"Melhores times em {column}")
        ax.set_xlabel("Times")
        ax.set_ylabel(f"{column} por jogo")

        #Remove as bordas superiores e direitas do gráfico
        ax.spines[["top", "right"]].set_visible(False)

    return fig


def efficiency_scatter(dataframe: DataFrame, columns: list[str], name: str) -> Figure:
    """Cria uma figura com um gráfico de dispersão (scatter plot) com base em duas estatísticas fornecidas, destacando o nome de cada jogador

    Parâmetros:
        dataframe (DataFrame): dataframe com os dados
        columns (list of strings): lista com duas strings. A primeira representa a eficiência (%) e a segunda, a quantidade (tentativas)
        name (string): Título do gráfico

    Returns:
        Figure: Objeto Figure contendo um gráfico de dispersão
    """

    #Extrai os dados das colunas indicadas no dataframe
    efficiency = [i for i in dataframe[columns[0]]] #Eficiência
    attempts = [i for i in dataframe[columns[1]]] #Quantidade

    #Cria a figura
    fig, ax = plt.subplots(figsize = (15, 6))

    #Define o estilo do Gráfico
    sns.set_style("darkgrid")

    #Gera o gráfico de dispersão
    scatter = sns.scatterplot(
        data = dataframe,
        x = efficiency,
        y = attempts,
        s = 100,
        ax = ax
    )

    #Adiciona o nome dos jogadores
    for index, txt in enumerate(dataframe["Player"]):
        plt.annotate(
            txt,
            (dataframe.iloc[index][columns[0]], dataframe.iloc[index][columns[1]]),
            fontsize = 8,
            textcoords = "offset points",
            xytext = (6, -3), 
            ha = "left"
        )

    #Define os títulos, rótulos dos eixos e configurações visuais
    plt.grid(True, linestyle = "--", alpha = 0.7)
    plt.title(name, fontsize = 14)
    plt.xlabel("Eficiência (%)", fontsize = 12)
    plt.ylabel("Quantidade", fontsize = 12)
    plt.tight_layout()

    return fig
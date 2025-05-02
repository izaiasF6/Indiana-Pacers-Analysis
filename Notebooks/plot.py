import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_radar_charts(subjects_1, stats_1, subjects_2, stats_2, media, player_stats, label_media, label_player, color_media, color_player):
    # Configuração do layout
    fig, axs = plt.subplots(1, 2, subplot_kw=dict(polar=True), figsize=(12, 8))  # Dois subplots lado a lado

    angles_1 = np.linspace(0, 2 * np.pi, len(subjects_1), endpoint=False)
    angles_1 = np.concatenate((angles_1, [angles_1[0]]))
    stats_1 = np.concatenate((stats_1, [stats_1[0]]))  # Adiciona o primeiro valor ao final
    player_stats_1 = np.concatenate((player_stats[:len(subjects_1)], [player_stats[0]]))  # Mesmo para as estatísticas do jogador

    subjects_1 = subjects_1 + [subjects_1[0]]

    axs[0].plot(angles_1, stats_1, color=color_media, label=label_media, marker="o", markersize=4)
    axs[0].fill(angles_1, stats_1, color=color_media, alpha=0.25)
    axs[0].plot(angles_1, player_stats_1, color=color_player, label=label_player, marker='o', markersize=4)
    axs[0].fill(angles_1, player_stats_1, color=color_player, alpha=0.25)
    axs[0].set_thetagrids(angles_1 * 180 / np.pi, subjects_1)
    axs[0].set_title("Estatísticas Acumulativas", pad = 35, fontsize = 14)

    angles_2 = np.linspace(0, 2 * np.pi, len(subjects_2), endpoint=False)
    angles_2 = np.concatenate((angles_2, [angles_2[0]]))
    stats_2 = np.concatenate((stats_2, [stats_2[0]]))
    player_stats_2 = np.concatenate((player_stats[len(subjects_1)-1:], [player_stats[len(subjects_1)-1]]))

    subjects_2 = subjects_2 + [subjects_2[0]]

    axs[1].plot(angles_2, stats_2, color=color_media, label=label_media, marker="o", markersize=4)
    axs[1].fill(angles_2, stats_2, color=color_media, alpha=0.25)
    axs[1].plot(angles_2, player_stats_2, color=color_player, label=label_player, marker='o', markersize=4)
    axs[1].fill(angles_2, player_stats_2, color=color_player, alpha=0.25)
    axs[1].set_thetagrids(angles_2 * 180 / np.pi, subjects_2)
    axs[1].set_title("Estatísticas Percentuais", pad = 35, fontsize = 14)

    for ax in axs:
        ax.grid(True)
        ax.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


def ranking_barchart(dataframe, columns: list[str], Reverse = False):
    fig, axes = plt.subplots(nrows=2, ncols=int(len(columns) / 2), figsize=(30, 15))
    axes = axes.flatten()

    for i, column in enumerate(columns):
        ax = axes[i]
        media = dataframe[column].mean()

        dataframe = dataframe.sort_values(by = column, ascending = Reverse).reset_index(drop = True)
        bar_points, bar_team = dataframe[column].head(8).astype(float).tolist(), dataframe["team"].head(8).tolist()

        if "Indiana Pacers" not in bar_team:
            index = dataframe.query("team == 'Indiana Pacers'").index[0]
            bar_team[-1], bar_points[-1] = "Indiana Pacers", dataframe.loc[dataframe["team"] == "Indiana Pacers", column].values[0]
        else:
            index = bar_team.index("Indiana Pacers") + 1
        
        eixo_labels = [
            f"{idx + 1}° {team.split()[-1]}" if team != "Indiana Pacers" else f"{index}° {team.split()[-1]}"
            for idx, team in enumerate(bar_team)
        ]

        sns.set_style("darkgrid")
        sns.barplot(
            y = bar_points,
            x = eixo_labels,
            data = dataframe.head(8),
            ax  = ax,
            hue = "team",
            palette = ["yellow" if team == "Indiana Pacers" else "b" for team in bar_team],
            legend = False,
        )

        for i, label in enumerate(ax.get_xticklabels()):
            if i % 2: label.set_y(-0.03)


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

        ax.axhline(y = media, color = 'red', linestyle = '--', linewidth = 1.2, label = f"Média ({media:.2f}")
        ax.set_title(f"Melhores times em {column}")
        ax.set_xlabel("Times")
        ax.set_ylabel(f"{column} por jogo")
        ax.spines[["top", "right"]].set_visible(False)

    plt.show()


def efficiency_scatter(dataframe, columns, name: str):
    efficiency = [i for i in dataframe[columns[0]]]
    attempts = [i for i in dataframe[columns[1]]]

    plt.figure(figsize = (15, 6))
    sns.set_style("darkgrid")

    scatter = sns.scatterplot(
        data = dataframe,
        x = efficiency,
        y = attempts,
        s = 100
    )

    for index, txt in enumerate(dataframe["Player"]):
        plt.annotate(
            txt,
            (dataframe.iloc[index][columns[0]], dataframe.iloc[index][columns[1]]),
            fontsize = 8,
            textcoords = "offset points",
            xytext = (6, -3), 
            ha = "left"
        )

    plt.grid(True, linestyle = "--", alpha = 0.7)
    plt.title(name, fontsize = 14)
    plt.xlabel("Eficiência (%)", fontsize = 12)
    plt.ylabel("Quantidade", fontsize = 12)
    plt.tight_layout()

    plt.show()
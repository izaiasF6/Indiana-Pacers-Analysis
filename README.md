# Análise da temporada regular 2023-2024 do Indiana Pacers

### Descrição
Este projeto realiza uma análise descritiva da temporada regular 2023-2024 do Indiana Pacers, baseada na seguinte business question: "Quais fatores estatísticos mais contribuíram para o sucesso do Indiana Pacers na temporada 23-24 e quais podem ser melhorados?".

### Objetivos
 - Explorar o desempenho dos jogadores dos Pacers
 - Comparar os dados estatísticos dos Pacers com outras franquias - tanto em nível coletivo quanto individual
 - Identificar os pontos fortes e as principais fraquezas de Indiana

### Fontes dos dados
 - all_season_datenbank: dataset publicado no kaggle por Stefan Arndt. Clique [aqui](https://www.kaggle.com/datasets/smac91/nba-teamstats-from-all-sesons-1947-2024) para acessá-lo
 - Nba-player-data(in): dataset publicado no kaggle por orkunaktas4. Clique [aqui](https://www.kaggle.com/datasets/orkunaktas/nba-players-stats-2324) para acessá-lo

### Ferramentas
 - Python 3.11
 - Pandas
 - Numpy
 - Matplotlib
 - Seaborn
 - Jupyter Notebook

### Resultados
- **Ataque explosivo e coletivo:** O Indiana possui discutivelmente o melhor ataque da NBA. Além de ser o 1° em pontos e assistências, os dados indicam que o sistema ofensivo de Indiana também é equilibrado e coletivo na finalização de jogadas.
- **Alta eficiência nos arremessos:** O time apresenta ótimo rendimento nos arremessos de quadra, com destaque para a precisão da bola de 2 pontos.
- **Ótimas Aquisicões na offseason:** As aquisiçãos de Obi Toppin e do importantíssimo Pascal Siakam, foram movimentos que elevaram o nível da equipe e que compensaram a saída dos bancários Bruce Brown e Buddy Hield, que foram utilizados como moeda de troca. Siakam foi o líder do time em pontos e rebotes, e um dos jogadores mais consistentes em toda a NBA. Já Obi Toppin foi um reserva que entrou em todos os jogos do time e entregou bons números para um bancário.
- **Tyrese Haliburton:** O franchise player da equipe teve uma temporada de consolidação entre os melhores da sua posição. Com média de duplo-duplo, Haliburton aliou criatividade com eficiência, sendo talvez o principal responsável por reerguer a cultura vencedora no Indiana Pacers.
- **Myles Turner e Aaron Nesmith:** ambos se destacam como opções defensivas sólidas, além de contribuírem ofensivamente, principalmente espaçando a quadra.
- **Banco participativo:** a rotação dos Pacers é sólida e produtiva, com um banco que contribui ofensivamente e mantém o ritmo da equipe mesmo quando os titulares descansam.
- **Dependência excessiva de Haliburton na criação de jogads:** Apesar de seu talento e visão de jogo, o quinteto titular depende excessivamente de Haliburton para armar as jogadas. Essa centralização pode tornar a equipe vulnerável quando ele está mal ou ausente.
- **Defesa frágil:** Embora possua bons números em tocos e roubos, a equipe de Indianápolis é dona de uma das piores defesas da NBA. Além de ser uma equipe que toma muitos pontos por jogo, também permite uma alta taxa de conversão de arremessos, tanto no garrafão, quanto no perímetro. Este é um ponto extremamente preocupante para um time que futuramente deve figurar frequentemente nos playoffs, onde defesas sólidas costumam se sobressair.
- **Deficiência em rebotes:** Os rebotes são um dos maiores pontos críticos da equipe. O desempenho é pífio, principalmente em rebotes defensivos, onde possíveis adversários diretos em séries de playoffs, como o Boston Celtics e o New York Knicks, podem facilmente explorar.
- **Classe de rookies fraca:** Dos três rookies da equipe, apenas Ben Sheppard teve minutos de jogo significativos, sendo o único a se consolidar na rotação do elenco, consequentemente também sendo o que demonstrou mais potencial de evolução. Jarace Walker teve poucos jogos e poucos minutos de média. Por último, Isaiah Wong participou de apenas um jogo da equipe.

### Sugestões
- **Reforçar o garrafão com reboteiros**
  1. Buscar pivôs ou ala-pivôs com bom histórico de rebotes (tanto via draft, quanto trocas)
  2. Trabalhar para que principalmente Myles Turner desenvolva este aspecto em seu jogo
  3. Estimular esforço do time inteiro nos rebotes - apenas Siakam está acima da média nessa métrica.

- **Reestruturar a parte defensiva**
  1. Implementar um esquema de ajuda defensiva mais estruturado, principalmente no garrafão
  2. Investir em bons defensores de perímetro, já que os adversários convertem um número considerável de arremessos de 3 pontos
  3. Reduzir a minutagem de jogadores com baixa entrega defensiva, em momentos chaves dos jogos

- **Diversificar o playmaking**
  1. Incentivar maior participação on-ball de Andrew Nembhard
  2. Utilizar rotações onde Tyrese Haliburton e T.J. McConnell atuam juntos

- **Otimização ofensiva**
  1. Continuar priorizando cestas de alta eficiência, como bandejas, pick and roll, etc.
  2. Aumentar o volume de arremessos de jogadores com alta eficiência, mas baixo volume, como Nembhard e Nesmith
  3. Obter um bom shooter de 3 pontos para suprir as saídas de Bruce Brown e Buddy Hield

- **Desenvolvimento de rookies**
  1. Dar mais minutos de jogo para Ben Sheppard em seu segundo ano
  2. Utilizar Jarace Walker em jogos menos importantes, para avaliar seu real potencial
  3. Continuar utilizando Isaiah Wong no time da G-League

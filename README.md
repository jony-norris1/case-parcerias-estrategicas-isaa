# Case Parcerias Estratégicas ISAAC

Este repositório contém a análise e resolução de um case prático envolvendo o desenvolvimento de uma estratégia de parcerias para a empresa de soluções educacionais ISAAC.

## Descrição do Case

A ISAAC é uma empresa edtech que fornece soluções de ensino para escolas. Ela precisava aumentar o número de escolas parceiras, porém estava aquém da meta estabelecida.

O objetivo deste case é analisar os motivos para essa situação e recomendar um plano de ação utilizando conceitos de gestão estratégica.

## Conteúdo

O repositório inclui:

- Notebook Python com a análise exploratória dos dados
- Planilhas e gráficos gerados durante a análise
- Documento escrito com o case e recomendações

## Análise e Resultados

A partir da investigação dos dados disponíveis, foi possível identificar os principais fatores que impactavam o desempenho dos canais de aquisição.

Com base nisso, um plano de ação foi recomendado, incluindo:

- Otimização das estratégias de marketing
- Realocação de recursos para canais mais eficientes
- Pesquisas de mercado para entender necessidades
- Revisão de metas de crescimento

O caso exemplifica uma situação comum em gestão estratégica e utiliza conceitos como análise de mercado, inteligência competitiva e definição de estratégias para resolver o desafio.

## Ferramentas Utilizadas

- Python
- Pandas, Matplotlib e Seaborn para análise de dados
- Google Colab para desenvolvimento colaborativo 
- PowerPoint para apresentação

## Código Python Detalhado

Aqui está uma explicação mais detalhada do código Python desenvolvido no Google Colab para análise dos dados deste caso:

O código começa importando bibliotecas essenciais para manipulação e visualização de dados, como Pandas, Numpy, Matplotlib e Seaborn. 

Em seguida, é definida uma função chamada `ler_todas_as_planilhas_do_excel()` que lê todas as planilhas de um arquivo Excel passado como parâmetro e retorna um dicionário com cada planilha em um DataFrame distinto.

O arquivo "base_case_estrategia_comercial.xlsx" é lido usando essa função, permitindo acessar facilmente cada planilha posteriormente.

O dataframe específico da planilha "Página1" é selecionado para análise, por conter os dados principais. Nele, são identificados os canais de origem únicos.

Então, agrupamentos e cálculos estatísticos são feitos nesse dataframe para obter insights como:

- Faturamento total por canal
- Receita média por canal 
- Receita mediana por canal
- Top 10% de escolas por receita em cada canal

Em seguida, diversos gráficos são plotados usando Matplotlib e Seaborn para visualizar esses insights de forma clara e impactante, incluindo:

- Gráfico de barras das receitas por canal
- Boxplot da distribuição das receitas médias
- Histograma da distribuição geral de receitas
- Gráfico de dispersão receita média x mediana
- Gráfico de pizza com % de faturamento por canal

O código completo pode ser visto [neste link do Colab](https://colab.research.google.com/drive/1c-hC2mOWqApkwMxzm_GP48mW7_98klM9?usp=sharing).

Essa análise permitiu extrair e comunicar visualmente os principais insights dos dados, fundamentais para o desenvolvimento das recomendações estratégicas apresentadas neste caso.

## Autor

Este caso foi desenvolvido por João Paula como parte de um processo seletivo. Sinta-se à vontade para utilizar este conteúdo e enviar feedback.
```

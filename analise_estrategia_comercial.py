import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm.auto import tqdm

def ler_todas_as_planilhas_do_excel(caminho_arquivo):
    # Supondo que você tenha uma função chamada 'ler_todas_as_planilhas_do_excel' que lê todas as planilhas de um arquivo Excel
    # Detalhes de implementação para esta função não foram fornecidos, então certifique-se de defini-la antes de usar este código.

    # Implementação de espaço reservado para fins de demonstração
    # Substitua isso pela implementação real de sua função
    dataframes = pd.read_excel(caminho_arquivo, sheet_name=None)
    return dataframes

# Ler todas as planilhas do arquivo Excel
dataframes = ler_todas_as_planilhas_do_excel('base_case_estrategia_comercial.xlsx')

# Imprimir o nome de cada dataframe
print("Dataframes neste arquivo:", ", ".join(dataframes.keys()))

# Acessar um dataframe específico chamado 'Página1'
pagina1_df = dataframes['Página1']

# Verificar os canais de origem
canais_origem = pagina1_df['Canal Origem'].unique()
print(f'Canais de Origem: {canais_origem}')

# Obter o faturamento por canal de origem
faturamento_por_canal = pagina1_df.groupby('Canal Origem')['Faturamento'].sum()
print(faturamento_por_canal)

# Calcular a receita média por escola por canal de origem
avg_rev_by_channel = pagina1_df.groupby('Canal Origem')['Faturamento'].mean()
print(avg_rev_by_channel)

# Calcular a receita mediana por escola por canal de origem
median_rev_by_channel = pagina1_df.groupby('Canal Origem')['Faturamento'].median()
print(median_rev_by_channel)

# Identificar as 10% principais escolas por receita para cada canal
top_10_by_channel = {}
for channel in tqdm(canais_origem, desc='Calculando top 10% por canal'):
    channel_df = pagina1_df[pagina1_df['Canal Origem'] == channel]
    threshold = np.percentile(channel_df['Faturamento'], 90)
    top_10 = channel_df[channel_df['Faturamento'] >= threshold]
    top_10_by_channel[channel] = top_10

print('Número de escolas no top 10% por receita:')
for channel, df in top_10_by_channel.items():
    print(f'{channel}: {len(df)} escolas')

# Visualizações
# Gráfico de barras para o faturamento por canal
plt.figure(figsize=(12, 6))
sns.barplot(x=faturamento_por_canal.index, y=faturamento_por_canal.values)
plt.title('Faturamento por Canal de Origem')
plt.xlabel('Canal de Origem')
plt.ylabel('Faturamento')
plt.xticks(rotation=45)
plt.show()

# Boxplot para a receita média por canal
plt.figure(figsize=(12, 6))
sns.boxplot(x='Canal Origem', y='Faturamento', data=pagina1_df)
plt.title('Distribuição da Receita Média por Canal de Origem')
plt.xlabel('Canal de Origem')
plt.ylabel('Receita Média')
plt.xticks(rotation=45)
plt.show()

# Histograma para a distribuição de receita
plt.figure(figsize=(10, 6))
sns.histplot(pagina1_df['Faturamento'], bins=30, kde=True)
plt.title('Distribuição de Receita por Escola')
plt.xlabel('Faturamento')
plt.ylabel('Contagem')
plt.show()

# Gráfico de dispersão para relação entre receita média e mediana por canal
plt.figure(figsize=(10, 6))
sns.scatterplot(x=avg_rev_by_channel, y=median_rev_by_channel, hue=avg_rev_by_channel.index)
plt.title('Relação entre Receita Média e Mediana por Canal de Origem')
plt.xlabel('Receita Média por Canal')
plt.ylabel('Receita Mediana por Canal')
plt.legend(title='Canal de Origem', bbox_to_anchor=(1, 1))
plt.show()

# Gráfico de pizza para a participação de cada canal no faturamento total
plt.figure(figsize=(8, 8))
plt.pie(faturamento_por_canal, labels=faturamento_por_canal.index, autopct='%1.1f%%', startangle=90)
plt.title('Participação de Cada Canal no Faturamento Total')
plt.show()

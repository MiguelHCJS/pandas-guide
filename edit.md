Manipulação de dados

loc() e iloc(): acessam dados em um DataFrame por meio de rótulos ou índices numéricos.
filter(): filtra dados em um DataFrame com base em uma condição.
drop(): remove linhas ou colunas de um DataFrame.
merge(): combina dois ou mais DataFrames.
Transformação de dados

map(): aplica uma função a cada valor de uma coluna.
apply(): aplica uma função a cada linha ou coluna de um DataFrame.
replace(): substitui valores em uma coluna.
to_numeric(): converte valores de uma coluna para números.
Classificação de dados

groupby(): agrupa dados em categorias.
describe(): fornece estatísticas descritivas sobre dados.
value_counts(): conta a frequência de valores em uma coluna.
Outras funções úteis

shape(): retorna o tamanho de um DataFrame.
columns(): retorna as colunas de um DataFrame.
index(): retorna o índice de um DataFrame.
head(): retorna as primeiras linhas de um DataFrame.
tail(): retorna as últimas linhas de um DataFrame.
A seguir, são apresentados alguns exemplos de como essas funções podem ser utilizadas para realizar tarefas semelhantes às que são realizadas no Excel:

Procv

A função loc() do Pandas pode ser utilizada para realizar uma pesquisa semelhante à função Procv do Excel. Por exemplo, para encontrar o valor de uma célula na coluna B de um DataFrame com base no valor de uma célula na coluna A, podemos utilizar o seguinte código:

Python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})

value = df.loc[df['A'] == 2, 'B']

print(value)
Use code with caution. Learn more
Este código retornará o valor 20, que é o valor da célula na linha 2 da coluna B.

Junta de Excel

A função merge() do Pandas pode ser utilizada para juntar dois DataFrames de forma semelhante à função Junta de Excel. Por exemplo, para juntar dois DataFrames com base na coluna ID, podemos utilizar o seguinte código:

Python
df1 = pd.DataFrame({'ID': [1, 2, 3], 'A': [10, 20, 30]})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'B': [40, 50, 60]})

df = pd.merge(df1, df2, on='ID')

print(df)
Use code with caution. Learn more
Este código retornará o seguinte DataFrame:

   ID  A  B
0  1  10  40
1  2  20  50
2  3  30  60
Checando dado de uma coluna específica

A função isin() do Pandas pode ser utilizada para verificar se um valor está presente em uma coluna de um DataFrame. Por exemplo, para verificar se o valor 10 está presente na coluna A de um DataFrame, podemos utilizar o seguinte código:

Python
df = pd.DataFrame({'A': [1, 2, 3, 10]})

value = 10

result = df['A'].isin([value])

print(result)
Use code with caution. Learn more
Este código retornará o seguinte valor booleano:

True

Manipulação de dados

append(): adiciona linhas ou colunas a um DataFrame.
concat(): combina vários DataFrames.
query(): filtra dados em um DataFrame com base em uma expressão SQL.
stack(): converte um DataFrame de formato wide para formato long.
unstack(): converte um DataFrame de formato long para formato wide.
Transformação de dados

fillna(): preenche valores ausentes em uma coluna.
dropna(): remove linhas ou colunas com valores ausentes.
replace(): substitui valores em uma coluna por outros valores.
astype(): converte o tipo de dados de uma coluna.
to_datetime(): converte uma coluna de string para um objeto datetime.
Classificação de dados

groupby(): agrupa dados em categorias.
describe(): fornece estatísticas descritivas sobre dados.
value_counts(): conta a frequência de valores em uma coluna.
boxplot(): cria um gráfico de caixa e bigodes.
hist(): cria um histograma.
Análise de dados

corr(): calcula a correlação entre duas colunas.
ttest_ind(): realiza um teste t para comparar duas médias.
anova(): realiza uma análise de variância.
linear_regression(): realiza uma regressão linear.
decision_tree(): cria uma árvore de decisão.
Essas são apenas algumas das muitas funções do Pandas que podem ser úteis para análise de dados. Para saber mais sobre cada função, você pode consultar a documentação do Pandas.

Aqui estão alguns exemplos de como essas funções podem ser utilizadas:

Manipulação de dados

Para adicionar uma linha a um DataFrame, podemos utilizar o seguinte código:
Python
df = pd.DataFrame({'A': [1, 2, 3]})

df.append({'A': 4}, ignore_index=True)

print(df)
Use code with caution. Learn more
Este código retornará o seguinte DataFrame:

   A
0  1
1  2
2  3
3  4
Para combinar dois DataFrames, podemos utilizar o seguinte código:
Python
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})
df2 = pd.DataFrame({'C': [4, 5, 6], 'D': [40, 50, 60]})

df = pd.concat([df1, df2], axis=1)

print(df)
Use code with caution. Learn more
Este código retornará o seguinte DataFrame:

   A  B  C  D
0  1  10  4
1  2  20  5
2  3  30  6
Transformação de dados

Para preencher valores ausentes em uma coluna, podemos utilizar o seguinte código:
Python
df = pd.DataFrame({'A': [1, 2, 3, None]})

df['A'].fillna(0, inplace=True)

print(df)
Use code with caution. Learn more
Este código retornará o seguinte DataFrame:

   A
0  1
1  2
2  3
3  0
Para remover linhas ou colunas com valores ausentes, podemos utilizar o seguinte código:
Python
df = pd.DataFrame({'A': [1, 2, 3, None], 'B': [10, 20, 30, None]})

df.dropna(inplace=True)

print(df)
Use code with caution. Learn more
Este código retornará o seguinte DataFrame:

   A
0  1
1  2
2  3
Espero que isso ajude!


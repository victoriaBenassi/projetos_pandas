import pandas as pd

nome_cidade= pd.Series(['Itapevi','Rio de Janeiro','Belo Horizonte',\
                       'Santo Andre','Itaquecetuba','Carapicuiba','Barueri',\
                        'Itu','São Paulo'])

populacao = pd.Series([260000, 6700000, 2700000, 720000, 375000,\
                       400000, 276000, 175000, 12000000])

data_frame = pd.DataFrame({'Cidade': nome_cidade, 'População': populacao})

print(data_frame)

populacao_cidades = dict(zip(nome_cidade, populacao))

print(populacao_cidades) #dicionario

print(type(populacao_cidades))

print(populacao_cidades['Itu'])

print('Belo Horizonte' in populacao_cidades)

#data_frame.to_csv('C:\\treino\\projetos_pandas\\data_frame.cvs')
data_frame.to_csv('data_frame.cvs')
cidade_populacao = pd.read_csv('data_frame.cvs', index_col=0)

print(cidade_populacao)
print(cidade_populacao.info())
print(cidade_populacao.columns)
print(cidade_populacao.index)
print(cidade_populacao.head(3))
print(cidade_populacao.describe())
print(cidade_populacao.tail())


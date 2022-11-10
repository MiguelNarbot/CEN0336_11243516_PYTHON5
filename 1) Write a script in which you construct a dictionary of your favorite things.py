#1) Write a script in which you construct a dictionary of your favorite things.

import pandas as pd #utiliza-se a biblioteca pandas para uma melhor visualização do dicionário e dados

fav_dict={'livro':'pequeno_principe', 'música':'cold_water', 'arvore':'cedro'}

fav_dict=pd.DataFrame({'livro':['pequeno_principe'], 'música':['cold_water'], 'arvore':['cedro']}) #tranformar o dicionário em uma tabela
fav_dict  #para deixar mais legivel e compreensível, utilizei a bibliotéca pandas.
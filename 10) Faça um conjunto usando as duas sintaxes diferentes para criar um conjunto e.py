#10)Make a set using the two different syntaxes for creating a set myset = set() and myset2 = {}. What is the difference? Does it matter how you make it?

#Resposta
#"Dicionário" e "set" são tipos de dados, em python, no qual pode-se armazenar uma lista de objetos. 
#No caso da primeira sintaxe, "mySet=set()" há criação de um set vazio, todavia cria um espaço com interação, no qual os elementos interiores
#podem ser modificáveis, além de serem valores únicos (itens exclusivos e separados).
#Já no segundo caso, "mySet2={}", há criação de dicionário (lista), ou seja, os itens são apresentados em conjuntos e não de forma separada.

mySet = set('ATGTGGG')
mySet2 = {'ATGCCT'}

print (" Para mySet:", mySet,"\n","Para mySet2:",mySet2)




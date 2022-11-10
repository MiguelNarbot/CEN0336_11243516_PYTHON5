#11)Write a script to find the intersection, difference, union, and symetrical difference between these two sets.

#Set A = 3 14 15 9 26 5 35 9

#Set B = 60 22 14 0 9

a = set([3, 14, 15, 9, 26, 5, 35, 9])
b=set([60, 22, 14, 0, 9])

#já unindo os resultados em um só print

print(" Intersecção = ", a&b,"\n Diferença = ", a-b,"\n União = ", a|b,"\n Diferença_simétrica = ", a^b) #aqui há junção de todas as operações. 
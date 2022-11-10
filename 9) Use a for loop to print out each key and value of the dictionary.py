#9)Use a for loop to print out each key and value of the dictionary.

fav_dict={'livro':'pequeno_principe', 'música':'cold_water', 'arvore':'cedro'}

for key,value in fav_dict.items():    #essa é a parte que o exercício pede. Se ela for colocada somente com o fav_dict, a saída será "meu/minha livro favorito livro é pequeno_principe
    print("Meu/minha {} favorita/o é {}".format(key,value))
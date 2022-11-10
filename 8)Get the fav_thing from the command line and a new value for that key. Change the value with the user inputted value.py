#8)Get the fav_thing from the command line and a new value for that key. Change the value with the user inputted value.

import sys

fav_dict={'livro':'pequeno_principe', 'música':'cold_water', 'arvore':'cedro'}

categoria_nova=sys.argv[1]
novo_fav=sys.argv[2]
fav_dict[categoria_nova]=novo_fav

print("Coloque o seu novo favorito: {}".format(categoria_nova))
novo_fav=input()

fav_dict[categoria_nova]=novo_fav

for key in fav_dict:
  print(key,"\t", fav_dict[key])
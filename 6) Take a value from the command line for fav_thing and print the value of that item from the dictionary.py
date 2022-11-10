#6) Take a value from the command line for fav_thing and print the value of that item from the dictionary. 
#Maybe you want to print out all the keys to the user so that they know what to pick from. Check out input()

import sys

fav_dict={'livro':'pequeno_principe', 'música':'cold_water', 'arvore':'cedro'}

print("coloque um item para fav_thing: {}".format(fav_dict.keys()))
categoria=input()

print(fav_dict[categoria])

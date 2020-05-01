import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png')
plt.imshow(img)
plt.show()





# data["sprites"]["front_default"]
# https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png


#this are the types of keys available for sprites, sprites are images of the pokemon
#data["sprites"].keys()
#dict_keys(['back_default', 'back_female', 'back_shiny', 'back_shiny_female', 'front_default', 'front_female', 'front_shiny', 'front_shiny_female'])

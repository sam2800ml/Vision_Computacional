Bow sift
El problema es cada imagen va a tener caracteristicas diferentes, por lo que es dificil poder pasarselo a un modelo

Bag of words
Se escogen unas caracteristicas comparandolas con las demas buscando  la mas cercana a los datos de entrada.
A cada imagen, se le haya su caracteristica y con su descriptor, los vectores se ubican en un espacio, esto se realiza con todo el conjunto de los datos.
Se usa un aprendizaje no supervisado como lo seria  K-means, para que el algoritmo pueda encontrarlas solo con las caracteristicas que encontro n cada imagen.
Los keypoints que vienen en los descriptores, y despues diviendolos por la cantidad de carcateristicas que queramos usar con klusters
k-means mueve los centros, y cada centro dice sobre los centros de cada caracteristicas.
Una vez con los centros, se quedan con esos vectores que hacen informacion a este, 
La codificacion es cambiar los keypoints en una forma de manera numerica para poder identificarlo de una manera, despues se agrupa por esta codificacion la cual se hizo 
Una vez completada la codificacion, se hace un histograma para poder hacer la visualizacion de la distribucaion de la cantidad de caracteristicas que hayo por imagenes

se extrae caracteristicas de la imagen las cuales no vayan a variar de imagen a imagen
despues se genera el vocabulario digital, lo que hace es obtener los keypoints mas importantes, bins histograma.
Vector de palabras visuales lo que se hace es deteerminar la cantidad de veces que aparecen estos keypoints en las imagenes para poder hacer el conteo
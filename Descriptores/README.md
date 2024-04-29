Descriptors
Es un metodo con el cual se pueden extraer caracteristicas descriptivas de un punto de interes, o de una imagen completa, son como una huella digital la cual ayuda a distinguir entre una caracteristica y otra, convirtiendolas en una cadena de numeros.
<br>
scale invariance
invariante a la escala y a la rotacion, 

SIFT -> Es un extractor de caracteristicas, 
1. Se va a ubicar los posibles key points en el espacio de escala
2. Se colocan de una manera precisa los keypoints
3. Se asigna una orientacion para tratar de hacerlo invariante a la rotaciono
4. Describe los puntos claves a una dimension de alto vector 
<br>


# Explicacion de cada componente
1. Scale space extreme detection
<br>

la imagen se le hacen distintas escalas para hacerla que no varie, le aplica gaussianos con distintos sigmas, 
La diferenciacion permite calcular los cambios que hay en las imagenes, El numero mas grande es donde el cambio se identifica a mayor escala, 
Lo que se hace es que cada matriz se le reduce la dimension y ademas tambien se le aplica un filtrado, despues se va pasando por cada matriz buscando el numero mas grande en cada escala, y despues va a marcarlo para indicar que tenemos un key point
Cuando en un histograma tenemos en una misma parte dentro de un rango pequeño se le llama histograma de bajo contraste, sin embaego si tenemos uno donde esta por todo el plano es de alto contraste

2. Keypoint Localization. 
<br>
Para algunos puntos los cuales estan ya sea en partes donde no hay mucho cambios de contraste o que estan en los bordes se eliminan ya que no contienen mucha importancia como caracteristica, 
Para bajo contraste de las caracteristicas simplemente miramos la intensidad de estos, si la intensidad es menor a 0.03 significa que esta en bajo contraste lo que haria es que se deshecharia

3. Orientation Assigment
<br>
Con el histograma de 36 bins, se considera el pico mas grande, para poder darle  una orientación.

4. Keypoint Description
<br>
Para tener un vector mas controlado el cual ayuda a buscar si las carcateristicas coinciden, se describen, y surgen de las orientaciones, se divide en una matriz de 16x16 y despues se buscan las orientaciones, y por cada cuadro se sacan 8 orientaciones
se emparejan los descriptores,  

### SIFT 
Las ventajas de sift -> se van a encontrar keypoints por imagen por eso es local
    1. Caracteristicas locales, para cada imagen se realiza el proceso
    2. Genera gran cantidad de caracteristicas e incluso en imagenes pequeñas
    3. es muy eficiente
    4. Puede ser usando en diferentes tipos de caracteristicas



### SURF
Funciona con un kernel de integracion, 


### ORB

### BRISK

### AKAZE

### FREAK 


### Matching caracteristicas

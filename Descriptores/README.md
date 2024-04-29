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



# SURF (/Speeded-Up Robust Features/)
es un detector de caracteristicas y descriptor, se usa en reconocimiento de objetos, registro de imagenes, classificacion, o reconstruccion 3d, se inspira en el descriptor **SIFT**.
Usa deteccion por matriz de hesse, esta matriz se llena con la segunda derivada de la imagen.
<br>
![Matriz_Hesse](image.png)
Donde los valores de Lxx,Lxy,Lyy son esta segunda derivada de la imagen, en una direccion.
La imagen original se compone del valor aproximado del determinante de matriz de cada pixel.
<br>
![Det](image-1.png)
El valor de 0.8 es empirico, ya que se requiere el suavizado Gaussiano, este utiliza lo que seria filtros de caja, ya que al obtener las derivadas de ambos lados se puede representar con numeros, lo que hace que sea mas eficiente el calculo.


Una de las mayores diferencias con sift, es que antes se escalaban las imagenes a diferentes tamaños, en este caso con surf se escala de diferentes tamaños el filtro
<br>
![alt text](image-2.png)

Despues el posicionamiento de estos puntos caracteristicos, este se hace haciendo una comparacion entre todos los filtros que ya se tienen buscando el maximo o el minimo.
<br>
![alt text](image-3.png)
Tambien se eliminan aquellos numeros los cuales sean inferiores al umbral, lo que reduce la cantidad de caracteristicas.

Para determinar la direccion de estos puntos, no se toma el histograma de gradiente, el punto caracteristico como centro se calcula el radio de 6s, esta s es el valor de la escala del punto caracteristico, y se suma la respuesta de los puntos en ese sector en ambas direcciones, la respuesta cercana a el punto tiene mas valor que las que estan alejadas.
<br>
![Direccion](image-4.png)

Se toma un marco cuadrado alrededor del punto, este se divide en 16 regiones, estas regiones cuentan las caracteristicas de las ondas haar de 25 pixeles en las direcciones horizontales y verticales.
<br>
![descriptor](image-5.png)

por lo que cada area tiene 4 valores, por lo que se habla de que tiene un vector de 64D, que es la mitad del SIFT.

# ORB

# BRISK

# AKAZE

# FREAK 




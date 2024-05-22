# Autoencoders
Los autoencoders son modelos basados en redes neuronales las  cuales son usadas de forma de entrenamiento no supervisado, para poder descubrir corecciones en los datos.
Los autoencoders tienen las siguientes partes:
1. Encoder:  es la parte de la red la cual toma la entrada y produce un encoder de una baja dimensionalidad
2. Cuello de botella: Es la capa oculta de menor dimension donde se produce la codificacion.
3. Decodificador: Este toma la codificacion y recre la entrada.
>

>
La capa de cuello de botella es la capa con la menor dimensionalidad posible, nuestro target del modelo es que nuestra entrada sea la reconstruccion equivalente de la salida, por lo que se usa una funcion de perdida llamada **Reconstruction Loss**, y esta se da como el error entre lo que seria la entrada y la salida que obtuvimos del modelo.
En el momento en el cual se esta haciendo el calculo de esa cantidad de nodos los cuales se va a utilizar en el cuello de botella, ya que un numero muy grande puede crear una dimension muy grande en el encoder, por lo que puede generar que se aprenda los datos de entrada, por lo que presentaria un overfitting, y si se usa un numero de nodos bajo es complicado que se pueda obtener la relacion entre las imagenes.
>
## PCA Autoencoders
PCA lo que ayuda es poder encontrar la menor dimensionalidad que pueda describir los datos originales, este lo hace captando las maximas variaciones posibles en los datos y su correlacion.
Pero los PCA son muy buenos para cuando los datos son lineales, pero cuando no lo son los mejores son los autoencoders para la reduccion de esa dimensionalidad.

## Aplicacion de autoencoders.
1. Deteccion de anomalidades: Los autoencoders lo que hacen es captar la informacion la cual hay dentro de los datos, por lo que cuando se usa en un dataset ayuda a poder encontrar esa relacion en las imagenes, por lo que podra recrear muy bien las imagenes, por lo que si hacemos la creacion de un dataset con unas imagenes estipuladas, en el momento de pasarle una imagen con anomalia el error aumentara con esto detectando que presenta  un problema la imagen.
2. Removedor de ruido: Si hacemos la creacion de un encoder el cual tenga los datos con un ruido y creado la salida que sean los datos ya limpios, ya que se hace la reduccion de esa dimensionalidad a una manera peqeuña, se pierde ese ruido, para guardar las caracteristicas de salida.
3. Son usadas como modelos generativo, usando un modelo que es el autoencoder de variacion.

## Tipos de autoencoders
1. Autoencoder estándar: También conocido como autoencoder denso, es el tipo más básico de autoencoder. Consiste en una capa de entrada, una capa codificadora, una capa decodificadora y una capa de salida.

2. Autoencoder convolucional (CAE): Utiliza capas convolucionales en lugar de capas totalmente conectadas para manejar datos de imágenes. Es especialmente útil para preservar la estructura espacial de las imágenes.

3. Autoencoder variacional (VAE): Introduce una distribución probabilística en el espacio latente, lo que permite generar nuevos datos que siguen la distribución de los datos de entrenamiento. Los VAE son útiles para la generación de imágenes y para el aprendizaje de representaciones distribuidas.

4. Autoencoder con restricción de sparse (SAE): Impone restricciones en la actividad de la capa oculta, lo que significa que solo un pequeño número de neuronas se activan a la vez. Esto puede ayudar a aprender representaciones más robustas y significativas de los datos.

5. Autoencoder apilado: Consiste en apilar múltiples capas de autoencoders para formar una arquitectura más profunda. Cada capa aprende una representación progresivamente más abstracta de los datos.

6. Autoencoder denoising (DAE): Se entrena para reconstruir datos que han sido corrompidos por ruido. Esto ayuda al autoencoder a aprender representaciones más robustas y a filtrar el ruido de los datos de entrada.

7. Autoencoder recurrente (RAE): Adecuado para datos secuenciales, como series temporales o texto. Utiliza capas recurrentes en lugar de capas totalmente conectadas para codificar y decodificar la secuencia de datos.
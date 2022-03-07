# Data Project 2 IoT - Grupo 5 - Letspray

# Proyecto
El objetivo de este segundo Data Project es crear un producto IoT escalable, opensource y basado plenamente en cloud.

<p align="center">
   <img src="https://github.com/Ciarzi/DP2_G5/blob/main/Imagenes/Logo%20DP2.png?raw=true" alt="[YOUR_ALT]"/>
</p>

# ¿Qué es Letspray?
Con la intención de ayudar al medioambiente, nace Letspray. Somos una start up que gracias a la tecnología IoT y a través de Cloud quiere frenar el malgasto de agua actual cuando se riega.

Queremos ayudarte a ahorrar agua, tanto si tienes dos plantas en tu casa o todo un jardín. Para ello, proporcionamos un sensor que se coloca en la tierra y es capaz de enviar información, como la húmedad o la temperatura entre otros, y determinar qué cantidad de agua se necesita.

Pero nuestra misión no se detiene en las viviendas, el sensor también sirve para las tierras de cultivo. Pues optimizar el agua que se gasta cosechando es de vital importancia debido a la extensión del terreno.

# Conócenos
- [Thais Casares González](https://github.com/thais1987 "Thais")
- [Jaime Torres Natividad](https://github.com/Alvaromasa "Jaime")
- [Álvaro Masa De Vega](https://github.com/jatona27 "Álvaro")
- [Hermán Redondo Lázaro](https://github.com/Ciarzi "Hermán")
- [Luis Andreu Navarro](https://github.com/Luisand8 "Luis")

# Arquitectura
<p align="center">
   <img src="https://github.com/Ciarzi/DP2_G5/blob/main/Imagenes/Arquitectura.png" alt="[YOUR_ALT]"/>
</p>

# Tutorial paso a paso

1- Dado que se trata de un proyecto basado en la nube, lo primero es elegir un servicio de Cloud. En nuestro caso, [Google Cloud Platform](https://cloud.google.com/ "Regístrate aquí")

2- Una vez registrados lo primero es [ir a la consola](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/1.png) y [acceder a SQL](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/2.jpeg)

3- De las opciones que aparecen hay que seleccionar [MySQL](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/3.jpeg) [(en caso de no tener activada la API de Compute Engine te pedirá que la actives)](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/4.jpeg)

4- Lo siguiente es llenar los datos de configuración que se solicitan y seleccionar [Create instance](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/5.jpeg)

5- Una vez  la instancia está creada el siguiente paso es seleccionar la opción [Databases](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/6.jpeg)
   
   5.1- Es posible que haya que esperar a que se [actualice](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/7.jpeg)

6- Una vez se pueda seleccionar [Create Database](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/8.jpeg) le damos, seleccionamos un nombre para la base de datos y seleccionamos [Create](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/9.jpeg)




1- Cloud SQL --> DB creada
2- Cloud Function 
  trigger Pub/Sub con Cloud Scheduler cada 30 min

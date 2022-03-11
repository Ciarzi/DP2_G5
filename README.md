# Data Project 2 IoT - Grupo 5 - Letspray

# Proyecto
El objetivo de este segundo Data Project es crear un producto IoT escalable, opensource y basado plenamente en cloud.

<p align="center">
   <img src="https://github.com/Ciarzi/DP2_G5/blob/main/Informaci%C3%B3n%20adicional/Logo%20DP2.png" alt="[YOUR_ALT]"/>
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
   <img src="https://github.com/Ciarzi/DP2_G5/blob/main/Arquitectura.png" alt="[YOUR_ALT]"/>
</p>

# Cómo llevar a cabo el Data Project paso a paso

# Prerrequisitos

1- Dado que se trata de un proyecto basado en la nube, lo primero es elegir un servicio de Cloud. En nuestro caso hemos escogido, [Google Cloud Platform](https://cloud.google.com/ "Regístrate aquí"). Una vez registrados, lo primero es [ir a la consola](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/1.png)

2- Hay que descargar el programa [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) para más adelante

# SQL

3- Ya una vez dentro de GCP, lo primero será [acceder a SQL](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/2.jpeg)

4- De las opciones que aparecen hay que seleccionar [MySQL](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/3.jpeg) (en caso de no tener activada la API de Compute Engine [te pedirá que la actives](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/4.jpeg))

5- Lo siguiente es llenar los datos de configuración que se solicitan y seleccionar ["Create instance"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/5.jpeg)

6- Una vez se crea la instancia el siguiente paso es seleccionar la opción ["Databases"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/6.jpeg)
   
   6.1- Es posible que haya que esperar a que se [actualice](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/7.jpeg)

7- Una vez se pueda seleccionar ["Create Database"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/8.jpeg) le damos, seleccionamos un nombre para la base de datos y seleccionamos ["Create"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/9.jpeg)

Con esto ya tenemos nuestra instancia de BD lista y funcionando.

# Cloud Scheduler

8- El siguiente paso es escribir en la barra de búsqueda [Cloud Scheduler](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/10.jpeg) y una vez seleccionado darle a ["Create job"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/11.jpeg)

9- Aquí toca llenar la [información que se solicita](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/12.jpeg). Dado que nuestro sensor está pensado para enviar información cada 30 minutos, nosotros hemos escrito [(*/30 * * * *)](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/13.jpeg)
            
    */30 * * * *

10- En el apartado de "Configure the execution" hay que rellenar los datos de la siguiente manera, en donde pone:

   - Target type, seleccionaremos ["Pub/Sub"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/14.jpeg)
      
   - Select a Cloud Pub/Sub topic, selecionaremos ["Create a Topic"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/15.jpeg). Ahí habrá que llenar el campo "Topic id",     nosotros hemos puesto "datagen_trigger" y una vez puesto el nombre, seleccionar ["Create Topic"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/16.jpeg)
   
   - Message body, escribiremos lo siguiente: [{"message":"hello"}](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/17.jpeg)
        
    {"message":"hello"}
   
11- Hecho todo lo anterior, [le damos a "Create"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/18.jpeg)

Con esto ya queda creado el Job en el Cloud Schedule que se ejecutará [cada 30 minutos](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/19.jpeg)

# Cloud Function (sensorFunct)

12- Antes de empezar debemos ir a nuestra función de SQL y permitir el acceso a la IP que vayamos a usar. Para ello hay que acceder a la base de datos SQL creada anteriormente y entrar a ["Connections"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/20.png). Una vez ahí, seleccionamos ["Edit network"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/20.png) y escribimos la IP. En nuestro caso, para facilitar las cosas, hemos permitido el acceso a cualquier IP. Para ello, donde pone "network" hay que escribir 0.0.0.0/0

    0.0.0.0/0

13- Además, hay que añadir la contraseña de la base de datos. Siguiendo en SQL nos vamos a ["Users" y en los tres puntos a la derecha de root añadimos la contraseña de "datapdb2"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/29.jpg)

14- Antes de nada vamos a abrir el programa de MySQL Workbench que hemos descagado antes

15- Una vez dentro, hay que clickar en el símbolo ["+"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/27.png) que aparece para añadir una base de datos SQL.

16- Ya con el menú abierto hemos de introducir la IP del proyecto. Esta es independiente de cada proyecto, para saber cuál es la de TÚ proyecto hay que acceder a SQL y mirar la [dirección IP](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/26.png). Además, hemos de introducir el "Username" de root y en clickar en ["Store in Vault"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/28.jpeg) para introducir la contraseña relacionada con la base de datos, en nuestro caso es "datapdb2", también hay que añadir un nombre, en nuestro caso "all".

17- Una vez creada la conexión con SQL toca copiar el código que se encuentra en la carpeta DB del repositorio, específicamente el que se encuentra en el archivo [dbCreate.txt](https://github.com/Ciarzi/DP2_G5/blob/main/DB/dbCreate.txt). Destacar que en la primera línea de código, despues de ["use"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/30.png) has de escribir el nombre de TÚ base de datos.

18- Pasando ya por fin a GCP, para crear nuestra primera Cloud Function lo primero es escribir en la barra de búsqueda Cloud Function y seleccionar ["Create Function"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/21.png)

19- Una vez en las opciones de creación, hay que ponerle un nombre a la función, en nuestro caso ["sensorFunct"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/22.png) (dado que ya está creado previamente, aparece un error diciendo que ya existe una función con ese nombre, se puede poner el nombre que se quiera)

20- A la hora de seleccionar la región nosotros hemos elegigo "europe-west1"

21- En donde pone "Trigger", seleccionamos "Pub/Sub" y creamos un topic llamado (en nuestro caso) ["datagen_trigger"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/23.png) y le damos a "Save"

22- Lo siguiente es ir a la parte de "Runtime, build, connections and security settings"

23- Al final, donde pone "Runtime environment variables" hay que presionar ["ADD VARIABLE"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/24.jpg) y escribir en donde pone "Name" SENSOR_PROJECT_ID, y en donde pone "Value" el id del proyecto, en nuestro caso "letspray2"

24- Presionamos "Next".

25- Lo siguiente es escoger el lenguaje en donde pone ["Runtime"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/25.png), en nuestro caso Python 3.9. 

26- Una vez seleccionado, a la izquierda aparecerán dos archivos, en el que pone "main.py" hay que copiar el código que se encuentra en la carpeta CloudFunctionsCode del repositorio, específicamente el que se encuentra en el archivo [sensorFunct.py](https://github.com/Ciarzi/DP2_G5/blob/main/CloudFunctionsCode/sensorFunct.py). 

27.1- CUIDADO, los datos son independientes de cada proyecto. En "host" tienes que escribir la dirección IP de TÚ, la misma que has debido usar en MySQL Workbench y en "database" el nombre de TÚ base de datos.

28- En el archivo de requirements.txt hay que copiar el código que se encuentra en la carpeta CloudFunctionsCode del repositorio, específicamente el que se encuentra en el archivo [requirements.txt](https://github.com/Ciarzi/DP2_G5/blob/main/CloudFunctionsCode/requirements.txt)

    mysql-connector-python                
    google-cloud-pubsub
    
29- Click en Deploy.

¡Ya tenemos lista la primera Cloud Function de nuestro proyecto!

# Cloud Function (data_processing_function)

30- Lo primero es escribir en la barra de búsqueda Cloud Function y seleccionar ["Create Function"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/21.png)

31- Una vez en las opciones de creación, hay que ponerle un nombre a la función, en nuestro caso ["data_processing_function"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/31.png) (dado que ya está creado previamente, aparece un error diciendo que ya existe una función con ese nombre, se puede poner el nombre que se quiera)

32- A la hora de seleccionar la región nosotros hemos elegigo "europe-west1"

33- En donde pone "Trigger", seleccionamos "Pub/Sub" y creamos un topic llamado (en nuestro caso) ["sprinkler_trigger"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/31.png) y le damos a "Save"

34- Al final, donde pone "Runtime environment variables" hay que presionar ["ADD VARIABLE"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/24.jpg) y escribir en donde pone "Name" SENSOR_PROJECT_ID, y en donde pone "Value" el id del proyecto, en nuestro caso "letspray2"

35- Presionamos "Next".

36- Lo siguiente es escoger el lenguaje en donde pone ["Runtime"](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/33.png), en nuestro caso Python 3.9. 

37- Una vez seleccionado, a la izquierda aparecerán dos archivos, en el que pone "main.py" hay que copiar el código que se encuentra en la carpeta CloudFunctionsCode del repositorio, específicamente el que se encuentra en el archivo [data_processing_function.py](https://github.com/Ciarzi/DP2_G5/blob/main/CloudFunctionsCode/data_processing_function.py). 

37.1- CUIDADO, los datos son independientes de cada proyecto. En "host" tienes que escribir la dirección IP de TÚ, la misma que has debido usar en MySQL Workbench y en "database" el nombre de TÚ base de datos.

38- En el archivo de requirements.txt hay que copiar el código que se encuentra en la carpeta CloudFunctionsCode del repositorio, específicamente el que se encuentra en el archivo [requirements.txt](https://github.com/Ciarzi/DP2_G5/blob/main/CloudFunctionsCode/requirements.txt)

    mysql-connector-python                
    google-cloud-pubsub
    
39- Click en Deploy.

¡Ya tenemos lista la segunda Cloud Function de nuestro proyecto!

# ¿Cómo ver los datos?

40- Por último, para ver los datos recopilados tenemos que ir a MySQL Workbench. En la conexión creada anteriormente, tras haber ejecutado el código que hemos pegado antes, escribimos la [siguiente línea de código](https://github.com/Ciarzi/DP2_G5/blob/main/Tutorial/34.png) y la ejecutamos (donde pone letspraydb, has que escribir el nombre de TÚ base de datos), esto nos mostrará en pantalla los datos: 

    select * from letspraydb.sensorsInput

Con esto, queda por finalizado el segundo Data Project :)

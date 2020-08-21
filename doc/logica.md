# Logica de ejecucion

En este archivo se describe como se maneja la logica del programa, los diferentes
modulos que lo manejan y demas

## Diseño del sistema

El sistema esta diseñado con 4 carpetas importantes y el archivo main.py, el archivo
main es el que inicia la ejecucion del programa y las carpetas views, controllers,
helpers y models, las cuales contienen diferentes partes del programa.

La carpeta controllers contiene los controladores de cada aspecto del programa y
controla las operacion de I/O entre el usuario y el sistema, ademas contiene toda
la logica para manejar la base de datos, asi como la lectura y escritura de archivos,
ademas maneja los datos que son recibidos por el usuario e invoca a las instancias
de las vistas y el modelos de datos.

La carpeta views contiene la logica para mostrar datos por la consola, por lo que
no maneja ningun tipo de logica mas alla de la necesaria para mostrar los datos
correspondiente.

La carpeta models contiene los modelos de datos que se usara en el programa.

La carpeta helpers contiene logica que no se considera lo suficientemente relevante
para ser un controlador, pero ayuda en la funcion de este y su logica es invocada
de manera recurrente por modulos que no tienen nada que ver entre si.

## Modulos

El sistema esta compuesto por diferentes modulos que manejan distintos aspectos
del sistema, en este caso tenemos dos partes importantes:

- Capa inferior: manejo de los datos, esta capa se encarga de manejar las consultas
  a la base de datos, y de manejar la lectura de archivos, todo esto a peticion
  de algun controlador.
- Capa media: esta capa es el controlador ya que el controlador es el que invoca
  las funcionalidades de la capa inferior en funcion de lo que ocurra en la capa
  superior.
- Capa superior: formada por el controlador y la vista, esta es con la que el usuario
  interactua.

El sistema tiene los siguientes modulos:

[Base de datos](#base-de-datos)

[Controladores](#controladores)

[Vistas](#vistas)

[Lectura y escritura de archivos](#lectura-y-escritura-de-archivos)

### Base de datos

La base de datos esta compuesta por tres partes fundamentales:

- Los datos: contiene los datos en si, unicamente se encarga de mantener los datos
  cargados en memoria.
- Las validaciones (Escritura): procesa los datos que recibe e interpreta si son
  validos, verifica si no se viola ninguna regla, como por ejemplo que la clave
  principal debe ser unica, de ocurrir una violacion debe informarlo para que esta
  situacion pueda ser solventada.
- Las consultas (Lectura): este modulo procesa una instruccion de consulta y devuelve
  los datos segun los criterios de consulta, debe informar si la consulta tuviera
  un criterio invalido.

La base de datos unicamente debe realizar validaciones para preservar su integridad
por lo que no debe realizar logica para solucionar los conflictos, ya que esta tarea
debe ser delegada a una instancia superior.

### Controladores

Los controladores son la esencia del programa ya que estos se encargan de llamar
a las vistas de consola o por graphviz, recibir los datos del usuario, realizar
las validaciones necesarias en alto nivel (por ejemplo decidir que hacer si la
base de datos encuentra un error en la escritura de un dato), realizar las consultas
a la base de datos y realizar las consultas a los archivos csv para posteriormente
procesarlos y realizar las operaciones necesarias.

Se encuentran principalmente formados por los siguientes elementos:

- Invocacion de las vistas: esta parte llama a las vistas y les pasa los parametros
  necesarios para dibujar la informacion en consola y/o por graphviz.
- Manejo de ficheros: se encargan de manejar los ficheros es decir llama al parser
  de los archivos csv, para obtener su informacion y de crear una estructura de
  datos en memoria para poder realizar operaciones con ella.
- Manejo de datos del usuario: debe recibir los datos que ingrese el usuario, asi
  como de manejarlos.
- Manejo de la base de datos: este componente debe manejar las operaciones de lectura
  y escritura de la base de datos, debe recibir las validaciones de bajo nivel que
  crea la base de datos y debe procesarlas para completar las operaciones requeridas
  por el usuario.

### Vistas

Las vistas son instancias de codigo que unicamente se encargan de mostrar al usuario
la informacion necesaria para el funcionamiento del programa.


### Lectura y escritura de archivos

Se considera que este debe ser un modulo separado debido a que debe realizar varias
operaciones, como parsear el fichero, validarlo y devolverlo a la instancia desde
la que se llamo.
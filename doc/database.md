# Base de datos

Aqui se describe el funcionamiento de la base de datos que almacena los datos en
la memoria RAM, permite que se escriban datos y realizar consultas a la base de
datos

## Funcionamiento general

La base de datos es en esencia una lista de python vacia, que sera manejada siempre
por los mismos metodos para evitar posibles conflictos.

``` python
db = list()
```

Si bien el programa permite realizar operaciones en bloque y ademas debe realizar
validaciones a las referencias de otros cursos, en esencia unicamente se tendran
4 operaciones basicas, las cuales llamaremos de bajo nivel:

- Create
- Read
- Update
- Delete

Ninguna de estas valida ningun tipo de dato mas alla de que los tipos de datos sean
validos, no verifica la integridad de los datos ni que las referencias entre cursos
esten rotas.

Create, delete y update son funciones individuales mientras que la funcion read
puede funcionar en modo indivdual o en modo grupal, este ultimo devuelve un tipo
de dato estructurado que contenga todas las entradas en una tupla, para evitar que
esta sea modificada.

Create pide como parametro un objeto tipo curso y lo agrega a la lista, devuelve
el objeto recien creado.

Read pide como parametro un numero entero que devuelve todas las entradas que tengan
como codigo ese numero, si no se pasan parametros devuelve toda la lista.

Update pide como parametro un id, y el objeto curso, modifica todos los id con los
nuevos datos.

Delete pide como parametro un id, y elimina todas las entradas que tengan ese id
despues devuelve la lista de datos eliminados.

### Resolucion de conflictos

Como se puede observar en ningun momento se valida que la clave principal es decir
el codigo sea unico, y el resto de funciones alteran a todas las entradas por igual,
esto es asi por diseño ya que simplifica su codificacion, y ademas facilita la
verificacion de duplicados ya que basta con obtener el tamaño de la tupla.

En el alto nivel existen las 4 operaciones pero ademas deben verificar la integridad
de los datos y realizar las validaciones correspondientes, principalmente deben
verificar 2 cosas, que el codigo sea unico, y que las referencias a otros cursos
sean validas, es decir que no se esten referenciando cursos que no existen.

Create realiza primero una operacion read de bajo nivel para verificar que no
existan entradas con ese codigo, si no existen invoca un create de bajo nivel
para crear el elemento, si existe entonces invoca un update de bajo nivel para
sobrescribir el dato.

Read realiza una consulta, pero esta consulta puede ser estructurada de diversas
maneras, a diferencia del read de bajo nivel que solo admite como parametro el id
este read permite otros criterios de consulta mas complejos, debe notificar mediante
excepciones cuando una consulta sea vacio o invalida.

Update realiza primero recibe los datos desde el usuario, si se modiica el id,
realiza un readde bajo nivel para observar si la actualizacion no crea problemas
de referencias a otros cursos, si no crea ningun conflicto entonces procede a
actualizar el dato, si los crea, guarda todos los datos que debe modificar y
actualiza las referencias, si no se modifica el id simplemente se actualiza el dato.

Delete realiza primer un read de bajo nivel para encontrar las referencias a ese
curso, si no existen referencias ejecuta el borrado, si existen entonces impide
la ejecucion de la operacion y debe notificar la operacion mediante excepciones.

Todas estas operaciones son realizadas de manera individual.

## Estructura

Para funcionar esta base de datos utiliza dos archivos helpers llamados
core_db.py y database.py, los cuales gestionan bajo y alto nivel respectivamente
database.py es la que se expone a los controladores, ya que contiene las 4 operaciones
en el alto nivel y desde esta llama a las funciones del bajo nivel para realizar
sus operaciones, para manejar la base de datos unicamente se le pasa como parametro
la informacion que necesita para funcionar y la lista que funciona como base de datos.

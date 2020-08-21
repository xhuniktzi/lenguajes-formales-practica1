# Validaciones

Aqui se describen todas las validaciones necesarias que deben realizarse durante
la ejecucion del programa.

## Menu principal

Se debe validar si la opcion ingresada por el usuario es valida, y si no informar del
error y continuar con la ejecucion hasta que se ingrese una opcion valida
**Esto aplica para todos los menu de seleccion en general**

## Cargar archivo de entrada

Se debe validar que los valores de:

- codigo
- nombre
- opcionalidad
- semestre
- creditos
- estado

deben estar obligatoriamente y ademas que el valor de prerequisitos debe estar vinculado
a un codigo que ya este registrado previamente y/o que se este agregando en la operacion
actual, es decir si no se encuentra debe encolarse para procesarse despues de que
todas las operaciones esten terminadas.

se debe verificar que el valor de codigo no exista previamente y si lo hace entonces
los datos deben ser actualizados con la nueva información.

Se debe verificar si los valores de opcionalidad y de estado son validos respecto
a los valores definidos en la tabla que se encuentra en la seccion de
[Informacion General](info_general.md)

## Gestionar cursos

En la funcion agregar cursos se debe verificar que el curso no exista previamente,
si existiera entonces debe sobrescribir su contenido con el nuevo valor e informar
del suceso al usuario.

En la funcion editar curso, si se modifica el codigo del curso debe verificar que
no exista previamente ese codigo, si no existe permite la modificacion y actualiza
todas las referencias a ese curso que existan dentro de la base de datos.

En la funcion eliminar curso, debe verificar que no existan refertencias a ese curso
en otros elementos del tipo curso, si existen debe informar al usuario.

## Conteo de creditos

Cuando se solicite el conteo de creditos obligatorios hasta el semestre n, se debe
considerar que el valor de n sea valido, esto aplica de la misma forma cuando se
pidas el conteo por semestre individual.

## Mapa de cursos

Debe informar cuando se intente obtener un mapa de los cursos cuando no existen
cursos cargados.

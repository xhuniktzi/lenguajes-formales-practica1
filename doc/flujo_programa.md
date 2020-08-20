# Flujo de ejecucion del programa

Aqui se describe el flujo del programa

1. Pagina de Inicio
2. Menu principal
   - Cargar Archivo de entrada
      1. Solicitar url del archivo csv
      2. parsear el archivo csv
      3. validar
      4. cargar en memoria
      5. regresar al menu -> 2
   - Gestionar cursos
     - Listar Cursos
     - Mostrar Curso
     - Agregar Curso
       1. solicitar datos
       2. validar
       3. agregar
       4. regresar -> gestionar cursos
     - Editar Curso
       1. solicitar datos
       2. validar
       3. modificar
       4. regresar -> gestionar cursos
     - Eliminar Curso
     - Salir -> 2
   - Conteo de creditos
     - Contar aprobados
     - Cursando
     - pendientes
     - obligatorios desde semestre 1 a n
       1. solicitar n
       2. validar
       3. mostrar
       4. regresar -> conteo de creditos
     - creditos del semestre n
       1. solicitar n
       2. validar
       3. mostrar
       4. regresar -> conteo de creditos
     - Salir -> 2
   - Mapa de cursos
     1. validar
     2. generar imagen
     3. mostar automaticamente
     4. regresar -> 2
   - Salir -> exit()

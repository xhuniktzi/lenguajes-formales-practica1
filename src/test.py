# from helpers.core_db import core_create, core_read, core_update, core_delete
# from helpers.database
from models.Curso import Curso
from models.Estado import Estado
from models.Opcionalidad import Opcionalidad

from helpers.database import create, read, update, delete


def list_data():
    for obj in db:
        print(obj.codigo)
        print(obj.nombre)
        print(obj.codigo_requisitos)
        print(obj.opcionalidad)
        print(obj.semestre)
        print(obj.creditos)
        print(obj.estado)
        print('\n')
        pass
    pass


db = list()

curso_1 = Curso()
curso_1.codigo = 1
curso_1.nombre = "IPC"
curso_1.codigo_requisitos = [1, 4, 8, 14]
curso_1.opcionalidad = Opcionalidad.obligatorio
curso_1.semestre = 4
curso_1.creditos = 6
curso_1.estado = Estado.cursando

curso_2 = Curso()
curso_2.codigo = 3
curso_2.nombre = "Lenguajes"
curso_2.codigo_requisitos = [1, 45, 4, 4]
curso_2.opcionalidad = Opcionalidad.opcional
curso_2.semestre = 5
curso_2.creditos = 10
curso_2.estado = Estado.aprobado

curso_3 = Curso()
curso_3.codigo = 4
curso_3.nombre = "Mate"
curso_3.codigo_requisitos = [1, 45, 4]
curso_3.opcionalidad = Opcionalidad.opcional
curso_3.semestre = 3
curso_3.creditos = 12
curso_3.estado = Estado.pendiente

# core_update(db, 4, curso_2)

# for obj in db:
#     print(obj.codigo)
#     print(obj.nombre)
#     print(obj.codigo_requisitos)
#     print(obj.opcionalidad)
#     print(obj.semestre)
#     print(obj.creditos)
#     print(obj.estado)
# pass


curso_new = Curso()
curso_new.codigo = 56
curso_new.nombre = "dfdsfds"
curso_new.codigo_requisitos = [4]
curso_new.opcionalidad = Opcionalidad.opcional
curso_new.semestre = 3
curso_new.creditos = 15
curso_new.estado = Estado.pendiente

create(db, curso_1)
create(db, curso_2)
create(db, curso_3)

print('****1****\n')  # print(read(db))
for obj in read(db):
    print(obj.nombre)
    pass

# map(lambda obj: print(obj.nombre), read(db))
# update(db, curso_2, 4)

print('****2****\n')
# print(read(db))
for obj in read(db, opcionalidad=Opcionalidad.opcional, codigo=1):
    print(obj.nombre)
    pass
# map(lambda obj: print(obj.nombre), read(db))

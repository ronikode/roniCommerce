# Ecommerce - RoniCommerce

### Install

### DJANGO MODELS - ORM

# Object Relation Mapping - Gestiona mediante el lenguaje de programacion o framework la construccion DDL, DML
# SQL -> Lenguaje de consulta para las base de datos.
# CREATE TABLE item_model (id, name , description not null)
# ItemModel.objects.create(name="Item A", description="Este es un item") -> un registro en bd
# Select * from item_model where name="item a"; => ItemModel.objects.filter(name="item a")

# Desventaja
[sentencia ORM ] => [sentencia SQL]

### MODELS - MIGRACIONES
1.- python manage.py makemigrations <app_name>  (Revisa el modelo y actualiza)
2.- python manage.py migrate <app_name>         (Ejecuta sentencia SQL de cambio)

- python manage.py showmigrations <app_name>    (Muestra las migracione aplicadas o no del proyecto)

- python manage.py sqlmigrate catalogue 0001_initial
BEGIN;
--
-- Create model ItemModel
--
CREATE TABLE "item" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"name" varchar(150) NOT NULL,
"sku" varchar(20) NOT NULL,
"description" text NOT NULL,
"pvp" decimal NOT NULL);
COMMIT;

### DJANGO SHELL
python manage.py shell

- Ej:
from catalogue.models.item import ItemModel
ItemModel.objects.all()                 # Consulta todos los items
ItemModel.objects.create(name="Item A", description="Item A", pvp=10)  # Crea un registro en bd.
ItemModel.objects.count()               # Cantidad de registros
ItemModel.objects.filter(pvp__gt=5)     # Devuelve listado de items con pvp mayor que 5.

### Django managment user
python manage.py createsuperuser # Crea un superusuario que puede acceder al admin site.

### Django import and export
python manage.py dumpdata catalogue # Para exportar.
python manage.py loaddata catalogue # Para importar
# MVP de tasas de cambio

## Correr el proyecto

- sudo docker-compose build
- sudo chown -R $USER:$USER mvp manage.py
- docker-compose run web python manage.py migrate
- docker-compose run web python manage.py createsuperuser
  - Es el usuario y contraseña que usarás para acceder.
- docker-compose up
- Ir a localhost, hacer login y hacer cambios en las tasas.

## Documentación del código

El MVP usa dos contenedores de Docker: Un proyecto de Django (fullstack) y una base de datos Postgres.

### Proyecto Django

Cuenta con dos vistas:

- Login: Usuarios con autorización pasan a Home.
- Home: Se puede ver un Google Sheets embebido con tasas de cambio. Al editar una tasa de cambio se enviará un correo electrónico. Está acción está generada con Apps Scripts.

### App Scripts y Google Sheets

- Script: La función onTasaEdit es activada al producirse un cambio en las celdas de la columna de Tasa.
- Activadores: Se añadió un activador de edición que llama a la función onTasaEdit cada vez que se produce un cambio en la hoja.

**Consideraciones de App Scripts**
La función predeterminada onEdit no tiene permisos para llamar a fetch, por lo que para hacer una llamada POST a Zapier se debe crear una función con otro nombre y usar un activador de edición.

### Zapier

Se llama a una ruta en Zapier que envía un correo a sebastian.hurtado@utec.edu.pe con información sobre el cambio.

## Consideraciones del MVP

### Stack

Se eligió Django por los siguientes motivos:

- Django te ofrece una conexión sencilla a la base de datos mediante su ORM integrado.
- Tiene rutas predefinidas para creación, recuperación y administración de cuentas. Estas no han sido revisadas en el proyecto, pero se puede extender sobre esto de ser necesario.

### Seguridad

Algunos aspectos no considerados de seguridad por ser un MVP:

- Credenciales de producción sueltas en el docker-compose file. Por ejemplo, de la base de datos. Esto se puede corregir con un release de producción más sofisticado que oculte las variables usando un .env.
- Si bien el documento de google sheets está protegido por un login, el documento en sí es público en edición. Esto con el fin de poder editar el documento desde la página web.

### Escalabilidad

- El sistema de usuarios ofrecido por Django es altamente escalable y las funcionalidades son extendibles: logout, login, recuperación de contraseñas, registro, entre otras.

### Usabilidad

- El proyecto es usable por desarrolladores que puedan correr los contenedores en sus máquinas.
- Con un release de producción se podría compartir con un grupo interno y reducido de personas en el equipo de Xepelin.

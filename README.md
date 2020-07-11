# SIGproyectoAPI
API del proyecto final de SIG


***Esta rama (master) está siendo automáticamente desplegada en Heroku.***
Para probar todos sus endpoints o utilizarla ocupar https://sigdb.herokuapp.com.


## Informacion General

Este API sirve en conjunto con una aplicación móvil desarrollada en Xamarin Forms.
El repositorio de la app es el siguiente: https://github.com/jossehblanco/SIGproyecto

El API está desarrollado en Flask (Python 3.8) y hace uso de las siguientes librerías:
- sqlalchemy
- flask-jwt-extended
- flask


## Endpoints

####  /login

Se encarga de loggear a un usuario. Devuelve un token creado usando JWT.
Espera un POST con Basic Authorization que contanga "username" y "password"

####  /register
Se encarga de registrar un nuevo usuario.
Espera un POST que tenga: 
- "Content-Type" : "application/json" en el header
- { username : username, password : password} en el cuerpo


####  /circles
Devuelve una lista de todas las zonas de riesgo en la base (zonas con radio > 0, ya que si el radio es 0 se trata de una persona individual).
Espera el token en el header de la siguiente forma: "Authorization" : "Bearer <TOKEN>"

####  /circlesdev
Devuelve una lista de las zonas de riesgo SIN requerir el token de autorización.
***Este endpoint NO debe ser usado en producción.***



# Basado en 

[Django filter And Pagination](https://www.youtube.com/watch?v=dkJ3uqkdCcY&ab_channel=TauhidCodes)

# iniciaclización de django
```
django-admin startproject mysite .
django-admin startapp myapp
```

# el comando populate

```
python manage.py makemigrations
python manage.py migrate
python manage,py populate
```


Un detalle interesante es el uso de el directorio managment dentro de la app, esto permite 
ejecutar código como si fuera un comando de manage.py, de hecho al escribir:

`python manage.py`

se muestra (solo pongo los ultimos renglones):

```
[rest_framework]
    generateschema

[myapp]
    populate         <----- 

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```

de manera que podemos escribir:

`python manage.py populate`

para se ejecutar el script de la funcion populate! (que aqui pobla la base de datos con datos aletorios, gracias fake)

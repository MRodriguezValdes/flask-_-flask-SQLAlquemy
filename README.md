# Paso #1:
# Creacion del entorno virtual
---
Primero que todo debemos comprobar si tenemos instalada la herramienta venv de python.

Una vez instalada ejecutamos los siguientes pasos:

1. Abrimos en una terminal en el la ruta donde deseamos crear nuestros poryecto
2. Creamos una carpeta con el comando: ```mkdir nombre_de_la_carpeta```
3. Entramos dentro de ella : ```cd nombre_de_la_carpeta```
4. Como me encuentro en un sistema Linux ejecuto el comando: ```python3 -m venv env``` pero si nos encontramos en Windows ejecutamos el comando ```py -3 -m venv env```
5.Una vez creado el entorno procedemos a su activacion para poder instalar las herramientas necesarias para realizacion del mismo. Para ello ejecutamos el comando ```source env/bin/activate ``` o en Windows ```env\Scripts\activate```.

En la siguiente captura ya he instalado los recursos necesarios para llevar a cabo este tutorial:

![](img/1.png)
---

# Paso #2:
# Creamos un archivo python y procedemos a configurar nuestra base de datos.
---
![](img/2.png)

Como podemos observar :
1. Primero importamos lo que vamos a necesitar
2. Creamos una instancia que por convenio se llama app
3. Haciendo uso del metodo ```config``` configuramos nuestra base de datos.
4. Por ultimo establecemos una relacion entre nuestra app de Flask y nuestra base de datos.
---

# Paso #3:
# Creamos nuestras tablas (Models)
![](img/3.png)
![](img/4.png)
![](img/5.png)

Como podemos observar:

1. Creamos las columnas de nuestras tablas y establecemos el tipo de datos de cada una de ellas.
2. Establecemos como primary_key la columna id en las 3 tablas.
3. En caso de la tabla Order , la columna order_date recibira por defecto la hora en ese momento.
4. Las columnas que no pueden recibir un valor nulo , contienen dentro de su declaracion la palabra reservada ```nullable``` con valor ```False``` 
5. Las columnas que son unicas , contienen dentro de su declaracion la palabra reservada ```unique``` con valor ```True``` 

# Paso #4
# Establecemos la relacion entre nuestras tablas
![](img/6.png)
![](img/7.png)
![](img/8.png)


# Quedando nuestro codigo de la siguiente manera
![](img/9.png)

# Paso #5
# Creacion del archivo que contiene nuestra base de datos.Comprobamos su correcto funcionamiento
![](img/10.png)
Pasos:
1. Accedemos a la consola Flask haciendo uso del comando ```flask shell```
2. Importamos de nuestra aplicacion flask "app" db para poder generar nuestra base de datos.
3. Generamos nuestra base de datos haciendo uso del comando ```db.create_all()```

### Procedemos a comprobar su correcto funcionamiento 

![](img/11.png)

Pasos:

1. Debemos verificar que tenemos instalada la herramienta sqlite3
2. Ejecutamos el comando ```sqlite3 nombre_del_archivo_db```
3. Verificamos las tablas creadas con el comando ```.tables```
4. Verificamos el esquema de cada una de nuestras tablas con el comando ```.schema```

De esa forma comprobamos que todo esta en orden y podemos continuar.

# Paso #6
# Agregar informacion a nuestra base de datos

![](img/12.png)

Pasos:

1. Accedemos a nuestra consola Flask con  el comando ```flask shell```
2. Importamos de nuestra app flask "app": db , Product, Order, Customer
3. Para crear un registro primero creamos una variable y creamos una instancia de la clase (model) , en este caso queremos agregra un cliente llamado jhondoe
4. Añadimos a nuestra base de datos al cliente haciendo uso del comando ```db.session.add(nombre_de_la_variable)```
5. Por ultimo, guardamos los cambios con el comando ```db.session.commit()```

### Procedemos a comprobar que hemos agregado correctamente a nuestro cliente

![](img/13.png)

Pasos:
1. Ejecutamos el comando ```sqlite3 nombre_del_archivo_db```
2. Realizamos una query ```select * from customer;```
3. Observamos que nuestro usuario ha sido agregado correctamente

### Añadimos mas datos a nuestra base de datos

![](img/14.png)

### Comprobamos que han sido agregados forma correcta

![](img/15.png)


# Paso #7
# Actualizar nuestra base de datos

![](img/16.png)

Pasos:
1. Accedemos a nuestra consola Flask
2. Importamos de nuestra app flask "app" : db, Customer
3. Realizamos una query utilizando un filtro ```filter_by()``` y decimos por convenio que queremos solo el primer registro utilizando ```first()```
4. Comprobamos que es el registro que deseamos actualizar
5. En este caso deseo actualizar la direccion ```jhondoe.address = "..."```
6. Una vez actualizado el valor , guardamos los cambios ```db.session.commit()```

# Paso #8
# Borrar datos

![](img/17.png)
![](img/18.png)
![](img/19.png)
![](img/20.png)


Pasos:

1. Creamos un nuevo registro , para luego eliminarlo.
2. Comprobamos que ha sido agregado correctamente.
3. Hacemos una query para poder encontrar el registro que deseamos y lo asignamos una variable.
4. Coprobamos que es el registro que deseamos eliminar
5. Eliminamos el registro haciendo uso del comando ```db.session.delete(nombre_de_la_variable)```
6. Guardamos los cambios con ```db.session.commit()
```
7. Comprobamos que ha sido eliminado correctamente.
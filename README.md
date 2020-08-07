# **Instrucciones para correr el server**

## Secure server

```python
#Comentar esta linea
# URL = "http://localhost:8000/index.php"

#Descomentar esta linea
URL = "http://localhost:8000/indexProtected.php"

```

En consola se debe de correr el el root folder de el repo de servers

```
php -S localhost:8000/indexProtected.php
```

## Unsecure server

```python
#Comentar esta linea
# URL = "http://localhost:8000/indexProtected.php"

#Descomentar esta linea
URL = "http://localhost:8000/index.php"

```

En consola se debe de correr el el root folder de el repo de servers

```
php -S localhost:8000/index.php
```
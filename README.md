<h1 align="center">Proyecto Portafolio</h1>

<div align="center">
<img aling="center" width="900" height="400" src="index.png" />
</div>

### Para poder correr el proyecto correctamente debes seguir los pasos siguientes:
### Clonar el repositorio en la terminal
    git clone https://github.com/starkymc/Portafolio


### Dentro de nuestra carpeta creamos nuestro entorno virtual
    virtualenv -p python3 env

### Entramos al entorno virtual
    .\env\Scripts\activate

### Instalamos los requerimientos
    pip install -r requirements.txt

### En este caso se uso la base de datos mysql con las siguientes configuraciones en caso quieras configurar aqui esta la estructura
 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            
            'NAME': 'portafolio', #nombre de la bd
            
            'USER': '', #nombre del usuario
            
            'PASSWORD': '', #password del usuario
            
            'HOST': 'localhost', #host
            
            'PORT': '3306'  #puerto
        }
    }

### Hacemos las migraciones en la terminal
    python manage.py makemigrations
    python manage.py migrate

### Finalmente ya tenemos todo listo corremos el programa
    python manage.py runserver

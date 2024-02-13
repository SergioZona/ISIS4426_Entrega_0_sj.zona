# ISIS4426 - Entrega 0

**Estudiante:** Sergio Julian Zona Moreno (201914936)

## Vídeo de Explicación de la Aplicación

El vídeo de explicación de la aplicación se encuentra en el siguiente [URL](https://youtu.be/Kyp48Td8Swg).

## Backend y Despliegue

El Backend fue desarrollado en Flask, un framework web ligero de Python, mientras que el servidor de despliegue WSGI utilizado es Hypercorn.

Para ejecutar el backend desde el directorio raíz del proyecto, puedes utilizar el siguiente comando:

```bash
hypercorn flaskr.app:asgi_app --bind localhost:5000
```

### Colecciones en Postman

La documentación de las colecciones en Postman se encuentra en la siguiente [URL](https://documenter.getpostman.com/view/12924938/2sA2r3Z6Jf).

## Frontend

El frontend fue desarrollado utilizando Vite + React. Aunque se estableció la conexión con el backend, no se logró un avance significativo en su desarrollo.

Para instalar las dependencias del frontend, ejecuta el siguiente comando desde el directorio del frontend:

```bash
npm install
```

## Imagen Docker del Backend

La imagen de Docker, que contiene únicamente el backend, ha sido creada y está disponible para su acceso en la siguiente [URL](https://hub.docker.com/r/sharkstorm1010/backend).

Para ejecutar la imagen, simplemente ejecuta el siguiente comando:

```bash
docker run -it -p 5000:8000 backend
```

# Trabajo práctico 1 - Robótica Industrial
Para este trabajo vamos a resolver el problema 1, Cinemática inversa numérica, la cual dice:
> Desarrollar un algoritmo para resolver la cinemática inversa en forma numérica que contemple las configuraciones y que tenga un acierto del $100\%$

En este trabajo necesitamos 
 * Desarrollar el algoritmo con sus respectivos tests
 * Crear una memoria técnica, que equivale al informe
 * Crear una presentación

Opcionalmente crear un archivo .csv con el instante de muestreo, los valores articulares, para demostrar el funcionamiento del algoritmo

## Archivos
El programa esta hecho en un notebook de python (`.ipynb`) donde integra el uso de uv para las dependencias del proyecto

## Para la presentación
Se encuentra un proyecto de Motion Canvas, para correrlo solo se necesita: 
```bash
cd presentacion
npm start
```
Este abre un puerto en `http://localhost:9000/`, ahí se puede ver la pestaña de "Video settings" y clickeando en el dropdown de Render/Present se puede poner modo presentación

## Para la memoria tecnica
Se encuentra un proyecto de Latex, para compilarlo se puede usar el contenedor de Docker que permite no instalar nada más alla de Docker
```bash
docker run --mount type=bind,source=./informe,target=/latex juanbiancuzzo/latex:latest 1>/dev/null
```


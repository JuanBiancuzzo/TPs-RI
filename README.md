# Trabajo práctico 1 - Robótica Industrial
Para este trabajo vamos a resolver el problema 1, Cinemática inversa numérica, la cual dice:
> Desarrollar un algoritmo para resolver la cinemática inversa en forma numérica que contemple las configuraciones y que tenga un acierto del $100\%$

En este trabajo necesitamos 
 * Desarrollar el algoritmo con sus respectivos tests
 * Crear una memoria técnica, que equivale al informe
 * Crear una presentación

Opcionalmente crear un archivo .csv con el instante de muestreo, los valores articulares, para demostrar el funcionamiento del algoritmo

## Para editar el proyecto tenemos
Para editarlo como un notebook normal, se puede correr el siguiente comando
```bash
marimo edit cinematica-inversa.py --sandbox
```
también tiene la alternativa de correr dentro de VSCode, con el plugin "marimo"

Para editar y modificar la view, se tiene que correr de la siguiente forma
```bash
uvx --with marimo-studio --with deno marimo edit cinematica-inversa.py --sandbox
```


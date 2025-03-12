# Explicacion sobre el código Python

>En el enunciado de este código se nos pide introducir un nombre el cual tiene asignado una edad, según el nombre que nosotros introduzcamos, la edad será una u otra.



<center>

## Indice

- [codigo completo](#codigo-completo)

- [Lista/Array](#array)

- [diccionario](#diccionario)

- [Bucle condicional](#bucle)

- [Funcion busucar palabra](#funcion)

</center>


<br>

<div id="codigo-completo"></div>
Este sería el código completo, vamos a desglosarlo:

<br>

```python
def buscarPalabra(objetivo, palabras,):
    for palabra in palabras : 
        if palabra == objetivo:
            return True
    return False




nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]

edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}


while True:
    nombre = input("Buscar un nombre: ")
    estaElnombre = buscarPalabra(nombre, nombres)

    if estaElnombre == True:
        print("El nombre existe")
    else:
        print("El nombre no existe")
```

-----------

<div id = "array"></div>

### Lista/Array con nombres a usar.

```python
nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
```

Esta lista o array, nos indica cuales son los nombres posibles,
 en el diccionario __(que veremos mas adelante)__
se nos indicará la edad correspondiente a cada uno de los nombres.






---------


<br>
<div id ="diccionario"></div>

### Aquí tenemos el _diccionario_:
```python
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}
```
Como podemos observar en el código, esto se denomina diccionario, y en este caso se nos proporciona la edad de cada persona, según el nombre que introduzcamos saldrá por consola una u otra.


<div id="bucle"></div>
### Bucle condicional:


```python
while True:
    nombre = input("Buscar un nombre: ")
    estaElnombre = buscarPalabra(nombre, nombres)

    if estaElnombre == True:
        print("El nombre existe")
    else:
        print("El nombre no existe")
```

Este es el bucle por el cual el programa identificará si el nombre introducido es correcto y el valor no es inventado.
En caso de existir el nombre, ej : *"Mengano"*, el programa continuará su bucle realizando las operaciones siguientes indicandonos  previamente que el nombre existe.
En caso de lo contrario, el programa ejecutará el mensaje *"El nombre no existe"*.

<div id = "funcion"></div>


### Funcion para buscar la palabra

```python
def buscarPalabra(objetivo, palabras,):
    for palabra in palabras : 
        if palabra == objetivo:
            return True
    return False
```

Aquí tenemos la funcion para buscar la palabra, la cual funciona mediante dos argumento *"objetivo"* y *"palabra"*,
el bucle *for* presenta una condicion para ver si la palabra es igual que el objetivo buscado, de ser así, nos devolverá un valor booleano *"true"* o *"false"*.
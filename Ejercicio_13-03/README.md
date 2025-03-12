# Ejercicio Block Cypher

## DES
Ejemplo de ejecución
```
python des.py
```

## 3DES
Ejemplo de ejecución
```
python des3.py
```

## AES
Ejemplo de ejecución
```
python aes.py
```

## Unit Testing
Ejemplo de ejecución
```
python main.test.py
```

## Preguntas
- ¿Qué tamaño de clave se está usando para DES, 3DES y AES?
Se utilizan 8, 24 y 32 bytes respectivamente.

- ¿Qué modo de operación está implementado?
  - DES: Se está utilizando el modo ECB
  - 3DES: Se está utilizando el modo CBC
  - AES: Se está utilizando el modo ECB y CBC

- ¿Por qué no debemos usar ECB en datos sensibles?  
No debemos usar ECB en datos sensibles porque no oculta patrones de datos. Al cifrar bloques idénticos de texto plano, produce bloques idénticos de texto cifrado, lo que puede revelar información sobre los datos originales. Esto es especialmente visible en imágenes cifradas donde se pueden distinguir patrones y formas del contenido original. (GeeksforGeeks, 2024)

- ¿Cual es la diferencia entre ECB vs CBC, se puede notar directamente en una imagen?
Sí, ECB cifra cada bloque independientemente, lo que causa que se puedan ver los patrones de la imagen. CBC encadena bloques usando un IV, ocultando mejor los patrones originales.

- ¿Que es el IV?
El IV o Initialization Vector es un valor aleatorio que se utiliza junto con la clave para cifrar datos y generar mayor aleatoriedad en el cifrado individual de los bloques.

- ¿Que es el PADDING?
El padding es una tecnica que consiste en agregar una cantidad de bytes a una cadena para que el algoritmo de cifrado por bloques pueda completar un número exacto de bloques.

- ¿En qué situaciones se recomienda cada modo de operación?
  - CBC: Se suele utilizar en archivos grandes y que deben estar mayormente asegurados.
  - ECB: Se suele utilizar en archivos pequeños que no contengan patrones debido a que dichos patrones pueden ser notados luego de la encripción (como imagenes).

- ¿Cómo elegir un modo seguro en cada lenguaje de programación?
El modo a utilizar no varía segun el lenguaje de programación sino que depende de el uso que se le dará. Como se pudo observar en este ejercicio, python puede utilizar ambos. Para la encripción de textos puede usarse tanto CBC como EBC donde dependerá de la seguridad y velocidad de encripción. Para imagenes es recomendable utilizar ECB ya que con este no se reconocerán patrones dentro de la imagen.

## Referencias

```
GeeksforGeeks. (2024, May 7). ECB Mode vs CBC Mode in Cryptography. GeeksforGeeks. https://www.geeksforgeeks.org/ecb-mode-vs-cbc-mode-in-cryptography/
```
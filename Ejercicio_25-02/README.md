# Ejercicio Cifrado de flujo

## Uso

```bash
python main.py "texto" "keystream"
```
Por defecto, el texto a cifrar es "Hello world!!!" y el keystream es "1234567890".

## Ejecución de tests

```bash
python main.test.py
```

## Ejemplos de uso

### Ejemplo 1

Input:
```bash
python main.py "Hello world" "1234567890"                        
```
Output:
```bash
cyphered text: =U8e@
decyphered text: Hello world
```

### Ejemplo 2

Input:
```bash
python main.py "El patito" "aabs123"   
```
Output:
```bash
cyphered text: 
@R< 
decyphered text: El patito
```

### Ejemplo 3

Input:
```bash
python main.py "El gato dice miau" "elperro12"   
```
Output:
```bash
cyphered text: 'n
                 +6K17*YZ?
                          $
decyphered text: El gato dice miau
```





## Preguntas

1. ¿Qué sucede cuando cambias la clave utilizada para generar el keystream?
Cuando se cambia la clave, el keystream generado es diferente, por lo que el texto cifrado será diferente.

2. ¿Qué riesgos de seguridad existen si reutilizas el mismo keystream para cifrar dos mensajes diferentes?
Si se reutiliza el mismo keystream para cifrar dos mensajes diferentes y por alguna razón el keystream es descubierto, se pueden descifrar ambos mensajes sin necesidad de conocer el nonce o la key utilizada para generar ambos mensajes.

3. ¿Cómo afecta la longitud del keystream a la seguridad del cifrado?
La longitud del keystream afecta la seguridad del cifrado, ya que si el keystream es demasiado corto, el cifrado será más vulnerable a los ataques de fuerza bruta.

4. ¿Qué consideraciones debes tener al generar un keystream en un entorno real?
El keystream debe ser generado de forma aleatoria y no debe ser predecible. En un caso real, el keystream se debe generar en el servidor y no en el cliente, ya que si el cliente es comprometido, el keystream puede ser descubierto y utilizado para descifrar los mensajes sin necesidad de conocer la key o el algoritmo utilizado para generar el keystream.

5. ¿Qué mejoras ofrecen estos algoritmos frente a un PRNG sencillo? (ChaCha20 y otros)
Los algoritmos modernos de cifrado de flujo ofrecen una serie de mejoras frente a un PRNG sencillo, como:
- Garantía que el keystream sea aleatorio y no predecible.
- Un estado de 512 bits, lo que garantiza un periodo de generación de números pseudoaleatorios muy largo.
- Un mayor grado de seguridad, ya que el algoritmo de cifrado de flujo se basa en un algoritmo de cifrado simétrico.
- Un mayor rendimiento, ya que el algoritmo de cifrado de flujo se basa en operaciones XOR, que son operaciones muy rápidas.

## Referencias

```
Bernstein, D. (s.f.). The Salsa20 family of stream ciphers. https://cr.yp.to/snuffle/salsafamily-20071225.pdf
```

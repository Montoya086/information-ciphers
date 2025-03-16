# Lab3

## Part 1
[IR](https://github.com/Montoya086/information-ciphers/tree/main/Lab3/Part-1)

### Preguntas
**¿Por qué el cifrado ECB revela los patrones de la imagen?**
Porque ECB cifra cada bloque independientemente, sin usar un vector de inicialización. Esto significa que bloques idénticos de la imagen se cifrarán de manera idéntica, manteniendo los patrones visuales originales.

**¿Cómo cambia la apariencia con CBC?**
Utilizando CBC se puede observar una mayor aleatoriedad que no permite ver los patrones de la imagen.

**¿Qué tan seguro es usar ECB para cifrar datos estructurados?**
No es seguro. ECB no oculta patrones ni relaciones entre bloques, lo que puede revelar información sensible en datos estructurados.
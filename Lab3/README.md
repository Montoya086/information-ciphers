# Lab3

## Part 1
[IR](https://github.com/Montoya086/information-ciphers/tree/main/Lab3/Part-1)

### Ejecución
```bash
cd Part-1
python main.py
```

### Preguntas
**¿Por qué el cifrado ECB revela los patrones de la imagen?**
Porque ECB cifra cada bloque independientemente, sin usar un vector de inicialización. Esto significa que bloques idénticos de la imagen se cifrarán de manera idéntica, manteniendo los patrones visuales originales.

**¿Cómo cambia la apariencia con CBC?**
Utilizando CBC se puede observar una mayor aleatoriedad que no permite ver los patrones de la imagen.

**¿Qué tan seguro es usar ECB para cifrar datos estructurados?**
No es seguro. ECB no oculta patrones ni relaciones entre bloques, lo que puede revelar información sensible en datos estructurados.

## Part 2
[IR](https://github.com/Montoya086/information-ciphers/tree/main/Lab3/Part-2)

### Ejecución
```bash
cd Part-2
docker-compose up (--build)
```

```bash
cd Part-2
python client.py
```

### Preguntas
**¿Se puede identificar que los mensajes están cifrados con AES-CBC?**
![img](./resources/wireshark.png)
Como se puede observar en la imagen, el texto enviado está totalmente cifrado. A simple vista no es posible identificar el algoritmo utilizado, pero en una comunicación real se suele enviar el algoritmo utilizado en los headers de la solicitud.

**¿Cómo podríamos proteger más esta comunicación?**
Se puede mejorar de muchas maneras, pero la principal mejora que se puede hacer es incluir un algoritmo de autenticidad para evitar la modificación del mensaje por terceros.
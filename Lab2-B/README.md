# Lab2 part B

**¿Por qué las imágenes se corrompen al aplicar xor con una llave de texto?**

Esto se puede deber principalmente a que estamos importando el archivo completo de la imagen en formato png. Todos los formatos son diferentes, pero algunos como png tienen una estructura específica y cambiarla de alguna forma puede hacer que la imagen sea imposible de abrir nuevamente.


**Inconvenientes al hacer xor entre imágenes**

Al hacer un xor entre imágenes, hay que tener en cuenta que cada formato de archivo tiene sus propias estructuras y esto puede corromper la imagen. También es necesario tomar en cuenta que en un mismo formato puede existir diferente compresión y formato de colores, por lo que hay que adaptar ambas imágenes al mismo formato.


## Bibliografía
```
Sabih. (2018, May 31). Does PIL image.convert(“RGB”) convert images to sRGB or AdobeRGB? Stack Overflow. https://stackoverflow.com/questions/50622180/does-pil-image-convertrgb-convert-images-to-srgb-or-adobergb
```

```
ladyfafa. (2010, August 12). How do you decode Base64 data in Python? Stack Overflow. https://stackoverflow.com/questions/3470546/how-do-you-decode-base64-data-in-python
```
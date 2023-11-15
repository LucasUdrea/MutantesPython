# Mutans

- Lucas Udrea
- Legajo: 51656
- Email: udrealucas@gmail.com

## Fin del challenge

- Se buscó crear un programa que le permita al usuario saber a partir de un código genético representado en una matriz de [6x6] si una persona es o no un mutante.
- Un mutante será aquel que tenga al menos en 2 líneas de código genético repetido 4 veces consecutivas un "genoma" ya sea en sentido horizontal, vertical o diagonal.
- Además, se corrobora que el código genético ingresado sea el correcto y se devuelve un valor de verdad a partir de la finalización del código.

## Cómo fue resuelto

El desafío de detectar mutantes a partir de una secuencia de ADN [6x6] fue abordado con un enfoque centrado en la eficiencia y la minimización de chequeos innecesarios. Se implementaron funciones especializadas para recorrer la matriz de ADN y realizar comprobaciones en las direcciones necesarias: horizontal, vertical y diagonal.

- **Minimización de Chequeos:** Para ser lo más eficiente posible, cada función verifica primero los caracteres en los extremos de una posible secuencia mutante antes de examinar los caracteres intermedios. Esta aproximación reduce significativamente el número de comparaciones necesarias para identificar una secuencia mutante.
- **Funciones Específicas:** Se utilizaron cuatro funciones principales (`check_horizontal`, `check_vertical`, `check_diagonal`, `check_anti_diagonal`) para analizar la matriz de ADN. Cada una de estas funciones está diseñada para buscar secuencias mutantes en su respectiva orientación, contribuyendo de manera integral a la detección precisa de mutantes.
- **Manejo de Errores y Validaciones:** El programa también incluye mecanismos para validar las entradas de ADN, asegurándose de que cumplan con los criterios establecidos (longitud y caracteres permitidos) y manejar adecuadamente cualquier error o entrada inválida.

## Cómo correrlo

El programa se ejecuta completamente en la consola. Para utilizarlo, sigue estos pasos:

1. **Ejecución del Programa:** Abre tu terminal o consola de comandos y navega hasta el directorio donde se encuentra el archivo del programa. Una vez allí escribe la siguiente línea(Asegurate de tener Python instalado):

```
python Mutants.py
```

2. **Ingresar Datos de ADN:** Una vez iniciado el programa, se te pedirá que ingreses las secuencias de ADN. Cada secuencia debe ser de 6 caracteres y solo contener los caracteres 'A', 'T', 'C', 'G'.

3. **Resultados:** Después de ingresar todas las secuencias, el programa evaluará si el ADN corresponde a un mutante o no y mostrará el resultado.

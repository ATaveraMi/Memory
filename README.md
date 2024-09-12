## Cambios realizados por Marce

### Punto uno y dos

Se ha implementado una nueva velocidad para los proyectiles:

- **Velocidad**: 

### Contar y desplegar el numero de taps

- Se agregó  `state = {'mark': None, 'taps': 0}` y `state['taps'] += 1 ` para llevar un conteo.

- Se agregú una función que checa si los tiles han sdo "revealed"
### Código clave
```python
if all_revealed():  # Checa si todas las tiles se revelaron
        goto(0, -220)
        color('black')
        write("All tiles revealed!", align='center', font=('Arial', 30, 'bold'))
```



## Cambios realizados por Tavera

### Agregar Letras en lugar de Texto


- **las tarjetas pasaron de ser números a letras**
```python
tiles = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:32] * 2 #Cambiar a letras
```

### Reposicionar elementos

- Se centraron las letras moviendo a Turtle en su eje x y eje y

```python
goto(x + 15, y + 5) Reposicionar leteras

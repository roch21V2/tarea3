# tarea3



### Preparación de los datos: 
📊 prepare_data(df: pd.DataFrame) -> pd.DataFrame
Esta función toma un DataFrame de Pandas que contiene al menos las columnas FirstName y ModifiedDate, y lo transforma para prepararlo para análisis o modelado. Devuelve un nuevo DataFrame con características procesadas.

🔧 ¿Qué hace exactamente?
Filtra y ordena los datos
Solo mantiene las columnas FirstName y ModifiedDate, y ordena las filas en función de la fecha (ModifiedDate), de la más antigua a la más reciente.
Calcula la longitud de los nombres
Crea una nueva columna llamada FirstNameLen, que contiene la longitud (número de caracteres) del nombre (FirstName).
Normaliza las fechas
Convierte las fechas de ModifiedDate en un número de días desde la fecha más antigua en el DataFrame. Esto ayuda a trabajar con fechas como una variable numérica.
Devuelve el resultado
El DataFrame final solo contiene dos columnas: FirstNameLen y ModifiedDate (en días desde el mínimo), y se resetea el índice.
📥 Input esperado:

Un DataFrame con al menos:

FirstName (str): Nombre de una persona
ModifiedDate (datetime o str): Fecha asociada al registro
📤 Output:

Un DataFrame con:

FirstNameLen: Longitud del nombre
ModifiedDate: Número de días desde la primera fecha en el dataset


📊 Modelos de Regresión: Comparación entre Regresión Lineal y Random Forest

Este proyecto compara el desempeño de dos modelos de regresión —Regresión Lineal y Random Forest— para predecir la columna ModifiedDate en función de la longitud del nombre (FirstNameLen).


### Creación de Modelos
🧹 Preprocesamiento de Datos
Se utiliza la columna FirstNameLen como variable independiente (X).
La variable objetivo (y) es ModifiedDate, la cual originalmente es de tipo datetime.

✂️ División de Datos
Se dividen los datos en conjuntos de entrenamiento y prueba (80% - 20%) usando:



🤖 Modelos Utilizados
Regresión Lineal: Modelo simple que asume una relación lineal entre la variable independiente y la dependiente.
Random Forest Regressor: Modelo de ensamble que utiliza múltiples árboles de decisión para mejorar la precisión.


📈 Evaluación del Modelo
Se utilizan tres métricas para comparar ambos modelos:

Mean Squared Error (MSE): Promedio de los errores al cuadrado.
Mean Absolute Error (MAE): Promedio de los errores absolutos.
R² Score: Proporción de la varianza explicada por el modelo.

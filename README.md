# Despliegue de un servicio entrenado a partir de una base de datos SQL

## Authors

* **Nombre de mi equipo**: BookML.
* **Repositorio de github**: `https://github.com/roch21V2/tarea3`
* **Roles**
  * Luis Angel: Departamento de modelos *(Creación de modelos de regresión lineal)*
  * Jorge Rocha: Departamento de modelos *(Creación de modelos de random forest)*
  * Pamela Ruiz: Departamento de datos *(Exploración de datos)*
  * Gadiel Wisar: Departamento de datos *(Feature engineer)*
  * Azahel Ramirez: Departamento de despliegue *(Despliegue del modelo en la nube)*
  
## Instalación

### Pre-requisitos

* Python 3.10
* (uv)[https://docs.astral.sh/uv/getting-started/installation/]

### Pasos

1. **Clona el repositorio**: 
   
   ```bash
   git clone https://github.com/roch21V2/tarea3
   cd tarea3
   ```

3. **Instala el proyecto**:

    ```bash
    uv sync
    ```

4. **Obtén las variables de ambiente**:

    You must create a `.env` file with the following variables:

    ```bash
    cp .env.example .env
    ```

    You must fill the `.env` file with your credentials following the example.

## Estructura del proyecto

```shell

├── README.md       -> This file with the project description
├── pyproject.toml  -> Project configuration file
├── uv.lock         -> Project dependency lock file
├── .env.example    -> Example of environment variables (must create a .env file)
├── .python-version -> Python version used in the project
├── data            -> Directory for storing data files
│   ├── 00-raw          -> Directory for raw data files
│   ├── 01-preprocess   -> Directory for preprocessed files
├── models          -> Directory for storing trained models
├── notebooks       -> Directory for Jupyter notebooks
├── src             -> Directory for score.py
... 
```

---

---

## Instrucciones

1. Montar base de datos en SQL.
   
   Abran un servidor en Azure con la base de datos de prueba de SQL.

2. Entrenar modelo usando dicha base de datos.

    El modelo, una regresión, deberá predecir fecha de modificación (ModifiedDate) de la tabla SalesLT.customer.

3. Desplegar servicio en la nube.

## RÚBRICA DE EVALUACIÓN:

* **2 pt.** Diferencia con los códigos vistos en clase.
* **2 pt.** Dependencia de la IA. (Nada = 1 pt. Total = 0 pt.).
* **3 pt.** Respeto a la confidencialidad.
* **3 pt.** Calidad del repositorio:

* Código en general (limpieza, legibilidad y funcionalidad).
* Documentación.

## FORMATO DE ENTREGA:

* Suban los archivos necesarios para correr el API (no es necesario que suban los archivos para hacer el despliegue),
* Con texto, de manera similar a la actividad 2, reporten lo ocurrido:

### Ejemplo de texto de un entregable:

* **Nombre de mi equipo**: Adeptus Mechanicus.
* **Departamento**: Departamento de modelos.
* **Puesto desempeñado**: Fabricador General de Marte.
* **Repositorio de github**: https://github.com/admech/tarea_3_cloud_computing

*Si no hallan la forma de subir los archivos necesarios, envíenlos por correo y notifiquen tal cuestión en el texto del entregable.*

*Buena Suerte!*

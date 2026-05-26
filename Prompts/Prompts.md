<!-- Orquestador -->

Actúa como ingeniero de software.

Crea un archivo orchestrator.py en Python.

Objetivo:
Construir un agente orquestador para un sistema de análisis predictivo.

El agente NO debe contener lógica analítica.

Debe:
- recibir una ruta de dataset
- llamar secuencialmente tres skills
- retornar resultados finales

Skills:
1. preparar_datos()
2. ejecutar_eda()
3. entrenar_modelo()

Agregar comentarios y estructura limpia.

<!-- SKILLS -->

Completa el archivo preparar_datos.py.

Contexto:
Este archivo corresponde a una skill dentro de un sistema agéntico para análisis predictivo de rendimiento estudiantil.

Responsabilidad única:
Preparación de datos.

Implementa una función:

preparar_datos(ruta)

La función debe:

Cargar el CSV usando pandas
Mostrar dimensiones del dataset
Mostrar tipos de datos
Eliminar duplicados
Revisar valores nulos
Limpiar datos básicos si es necesario
Mantener separación de responsabilidades (NO hacer EDA)
NO entrenar modelos
Retornar el dataframe preparado
Agregar comentarios claros y código modular

Completa el archivo analisis_eda.py.

Contexto:
Este archivo corresponde a la Skill 2 de un sistema agéntico para análisis predictivo de rendimiento estudiantil.

Objetivo:
Realizar análisis exploratorio del dataset.

Implementa una función:

ejecutar_eda(df)

Requisitos:

Recibir un DataFrame ya preparado
Mostrar información general del dataset
Generar estadísticas descriptivas
Mostrar distribución de variables numéricas
Generar matriz de correlación
Crear gráficos usando matplotlib
Mostrar valores faltantes
NO modificar el dataframe
NO entrenar modelos
Retornar un diccionario resumen
Guardar gráficos dentro de:

outputs/eda/

Agregar comentarios y estructura limpia.


Completa el archivo modelado.py.

Contexto:
Este archivo corresponde a la Skill 3 de un sistema agéntico para análisis predictivo de rendimiento estudiantil.

Objetivo:
Entrenar y seleccionar el mejor modelo.

Implementa función:

entrenar_modelo(df)

Requisitos:

Identificar variable objetivo automáticamente (si existe columna rendimiento usarla)
Separar X e y
Codificar variables categóricas
Dividir train/test (80/20)
Entrenar:
Logistic Regression
Decision Tree
Random Forest
Evaluar:

accuracy
precision
recall
f1-score
Seleccionar mejor modelo.

Retornar:

{
"modelo_ganador": ...,
"metricas": ...
}

NO generar gráficos.
NO limpiar datos.
Agregar comentarios.

<!-- NOTEBOOK -->

Prompt para el notebook: Actúa como un arquitecto profesional de proyectos de Data Science e IA.

Genera un notebook Jupyter (.ipynb) completo para un proyecto universitario titulado:

"Sistema Agéntico para Análisis Predictivo del Rendimiento Estudiantil"

Contexto:
Ya existe un sistema desarrollado en Python con:
- Un agente orquestador (Orquestador.py)
- Tres skills:
   1. preparar_datos (limpieza y preparación)
   2. ejecutar_eda (análisis exploratorio con gráficos)
   3. entrenar_modelo (modelos de machine learning)

El notebook NO debe replicar todo el código de los .py, sino explicar el proceso y mostrar resultados.

Estructura obligatoria del notebook:

1. Introducción
- Explicar el objetivo del proyecto
- Explicar qué es un sistema agéntico
- Describir el pipeline (preparación → EDA → modelado)

2. Carga de datos
- Cargar el dataset con pandas
- Mostrar primeras filas (df.head())

3. Descripción del dataset
- Número de filas y columnas
- Explicación de variables
- Identificar la variable objetivo (exam_score)

4. Preparación de datos (Skill 1)
- Explicar qué se hizo (no copiar funciones)
- Mostrar:
   - eliminación de duplicados
   - limpieza de columnas
   - revisión de nulos
- Aclarar que esto está automatizado en la skill preparar_datos

5. Análisis Exploratorio (EDA - Skill 2)
- Mostrar gráficos desde:
   outputs/eda/
- Incluir:
   - matriz de correlación
   - distribución de variables
- Explicar insights:
   - variables más relacionadas con exam_score
   - variables con poco impacto

6. Modelado Predictivo (Skill 3)
- Explicar transformación de exam_score a rendimiento
- Explicar modelos usados:
   - Logistic Regression
   - Decision Tree
   - Random Forest
- Explicar métricas:
   accuracy, precision, recall, f1-score

7. Resultados
- Mostrar modelo ganador
- Mostrar métricas finales
- Interpretar resultados
- Mencionar problema de desbalance de clases

8. Conclusiones
- Qué se logró
- Qué variables fueron importantes
- Limitaciones del modelo
- Posibles mejoras

Requisitos adicionales:
- Usar celdas Markdown para explicación
- Usar pocas celdas de código (solo demostración)
- Incluir comentarios claros
- Mantener lenguaje académico pero claro
- No duplicar lógica del agente
- Mostrar imágenes con IPython.display

El resultado debe ser un notebook limpio, bien estructurado y listo para entrega universitaria.

________________________helpers prompt______________________

Estoy trabajando en un proyecto de análisis predictivo en Python con arquitectura modular basada en:

- Agent (Orquestador)
- Skills (preparación de datos, EDA, modelado)
- Notebooks
- outputs

Quiero crear una carpeta llamada "helpers" con utilidades reutilizables que NO formen parte de la lógica principal del pipeline.

Genera el código completo para los siguientes archivos dentro de la carpeta helpers:

1. logger.py
- Funciones para imprimir títulos, subtítulos, mensajes de éxito y error
- Deben usar prints formateados con separadores visuales

2. rutas.py
- Funciones para manejar rutas usando pathlib
- Obtener ruta de Data y outputs

3. utils.py
- Funciones pequeñas reutilizables como:
  - formatear porcentajes
  - cálculos simples

4. files.py
- Funciones para:
  - crear directorios si no existen
  - limpiar directorios (eliminar y volver a crear)

Requisitos:
- Código limpio y bien organizado
- Buenas prácticas
- Documentación breve en cada función (docstrings)
- Compatible con el resto del pipeline

No incluyas lógica de negocio (EDA, limpieza, modelos), solo utilidades.

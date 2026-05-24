Sistema Agéntico de Análisis Predictivo
Descripción
Este proyecto implementa un sistema agéntico para el análisis predictivo del rendimiento estudiantil, utilizando un pipeline automatizado compuesto por múltiples etapas:
Preparación de datos
Análisis exploratorio (EDA)
Entrenamiento de modelos de Machine Learning
El sistema está diseñado bajo una arquitectura modular basada en Skills y un Agente Orquestador, permitiendo automatizar todo el flujo de análisis.

ProyectoAnaliticaDatos/
│
├── Agent/
│   └── Orquestador.py
│
├── Skills/
│   ├── preparar_datos.py
│   ├── analisis_eda.py
│   └── modelado.py
│
├── Data/
│   └── StudentPerformanceFactors.csv
│
├── Notebooks/
│   └── Sistema_Agentico_Rendimiento_Estudiantil.ipynb
│
├── outputs/
│   └── eda/
│
└── Main.py

Arquitectura del Sistema
El sistema sigue un enfoque agéntico:
Orquestador: Controla el flujo del pipeline
Skills: Ejecutan tareas específicas
Skill 1: Preparación de datos
Skill 2: Análisis exploratorio (EDA)
Skill 3: Modelado predictivo

Resultados
El pipeline genera:
Dataset limpio y procesado
Análisis exploratorio con gráficos
Modelos de Machine Learning evaluados
Selección del mejor modelo
Ejemplo de salida:
Modelo ganador: Decision Tree
F1-Score: ~0.95

Notebook
El notebook incluye:
Análisis exploratorio manual
Visualización de datos
Explicación del proceso
Integración con el pipeline automatizado
Tecnologías Utilizadas
Python
Pandas
NumPy
Matplotlib / Seaborn
Scikit-learn
Flujo del Pipeline
Carga de datos
Limpieza y transformación
Análisis exploratorio
Ingeniería de variables
Entrenamiento de modelos
Evaluación y selección
Objetivo
Predecir el nivel de rendimiento estudiantil (Bajo, Medio, Alto) a partir de variables académicas y socioeconómicas.

Autores: 
Diana Cristina Patiño Rámirez
Juan José Betancur Cardona
Juan José Franco Grisales
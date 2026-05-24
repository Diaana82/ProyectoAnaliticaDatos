# 🔗 Integración del Notebook con el Pipeline Automatizado

## Descripción General

El notebook **Sistema_Agentico_Rendimiento_Estudiantil.ipynb** ha sido integrado con el **Agente Orquestador**, permitiendo ejecutar todo el pipeline de análisis predictivo directamente desde el notebook.

## ¿Qué es la Integración?

La integración permite:

✅ **Ejecutar el pipeline completo** desde el notebook con una sola celda
✅ **Visualizar resultados** del análisis exploratorio y modelo
✅ **Acceder a los datos** preparados para análisis adicionales
✅ **Reproducir análisis** consistentemente
✅ **Documentar todo el flujo** en un único lugar

## Estructura de la Integración

### Sección 9: INTEGRACIÓN CON EL PIPELINE AUTOMATIZADO

Esta nueva sección en el notebook contiene:

1. **Celda de Ejecución**: Importa el Orquestador y ejecuta el pipeline completo
2. **Visualización de Dataset**: Muestra el dataset preparado
3. **Visualización de EDA**: Presenta el análisis exploratorio
4. **Visualización del Modelo**: Muestra métricas y features importantes
5. **Documentación**: Explica cómo acceder a los resultados

## Cómo Usar

### Opción 1: Ejecución Secuencial (Recomendado)

1. Abre el notebook en Jupyter/VS Code
2. Ejecuta las celdas 1 a 8 para ver el análisis manual exploratorio
3. Desplázate hasta la **Sección 9** (Integración con el Pipeline)
4. Ejecuta las celdas de la Sección 9 para:
   - Ejecutar el pipeline completo
   - Ver el dataset preparado
   - Ver el análisis exploratorio (EDA)
   - Ver resultados del modelo

### Opción 2: Ejecución Solo del Pipeline

```python
# Ejecutar directamente en una celda del notebook
from Agent.Orquestador import ejecutar_pipeline

resultados = ejecutar_pipeline('../Data/StudentPerformanceFactors.csv')
```

### Opción 3: Desde Python Script

```python
import sys
from pathlib import Path
from Agent.Orquestador import ejecutar_pipeline

resultados = ejecutar_pipeline('Data/StudentPerformanceFactors.csv')
```

## Estructura de Resultados

El pipeline retorna un diccionario con:

```python
resultados = {
    'dataset': DataFrame,          # Dataset limpio y normalizado
    'eda': dict,                   # Análisis exploratorio
    'modelo': dict                 # Modelo entrenado y métricas
}
```

### Acceso a Componentes

```python
# Dataset preparado
df_preparado = resultados['dataset']

# Análisis exploratorio
dimensiones = resultados['eda']['dimensiones']
variables_numericas = resultados['eda']['variables_numericas']
estadisticas = resultados['eda']['estadisticas_numericas']

# Modelo y métricas
nombre_modelo = resultados['modelo']['nombre_modelo']
metricas = resultados['modelo']['metricas']
importancia_features = resultados['modelo']['importancia_features']
accuracy = resultados['modelo']['metricas']['accuracy']
f1_score = resultados['modelo']['metricas']['f1_score']
```

## Ejemplos de Uso

### Ejemplo 1: Obtener el DataFrame Preparado

```python
df_limpio = resultados['dataset']
print(f"Filas: {df_limpio.shape[0]}")
print(f"Columnas: {df_limpio.shape[1]}")
```

### Ejemplo 2: Análisis de Features Importantes

```python
importancias = resultados['modelo']['importancia_features']
top_5 = importancias.head(5)
print("Top 5 features más importantes:")
print(top_5)
```

### Ejemplo 3: Evaluación del Modelo

```python
metricas = resultados['modelo']['metricas']
print(f"Accuracy:  {metricas['accuracy']:.4f}")
print(f"Precision: {metricas['precision']:.4f}")
print(f"Recall:    {metricas['recall']:.4f}")
print(f"F1-Score:  {metricas['f1_score']:.4f}")
```

### Ejemplo 4: Análisis Adicional con EDA

```python
eda = resultados['eda']
print(f"Variables numéricas: {len(eda['variables_numericas'])}")
print(f"Variables categóricas: {len(eda['variables_categoricas'])}")
print(f"Valores nulos: {eda['total_valores_nulos']}")
```

## Flujo de Ejecución

```
┌─────────────────────────────────────────────────────────────┐
│   NOTEBOOK: Sistema_Agentico_Rendimiento_Estudiantil        │
└─────────────────────────────────────────────────────────────┘
                        ↓
                   SECCIÓN 9
                   (Integración)
                        ↓
    ┌───────────────────────────────────────┐
    │ from Agent.Orquestador import         │
    │        ejecutar_pipeline              │
    └───────────────────────────────────────┘
                        ↓
    ┌───────────────────────────────────────────────────────┐
    │   AGENTE ORQUESTADOR                                  │
    ├───────────────────────────────────────────────────────┤
    │  ↓ ejecutar_pipeline()                                │
    │    ├─→ SKILL 1: Preparar Datos                        │
    │    ├─→ SKILL 2: Análisis Exploratorio (EDA)           │
    │    └─→ SKILL 3: Entrenamiento de Modelos              │
    │  ↓ Retorna: dict con dataset, eda, modelo            │
    └───────────────────────────────────────────────────────┘
                        ↓
    ┌───────────────────────────────────────┐
    │   RESULTADOS EN EL NOTEBOOK           │
    │   - Dataset Preparado                 │
    │   - Análisis Exploratorio             │
    │   - Métricas del Modelo               │
    │   - Features Importantes              │
    └───────────────────────────────────────┘
```

## Ventajas de esta Integración

| Aspecto | Ventaja |
|---------|---------|
| **Automatización** | Todo el pipeline en una celda |
| **Documentación** | Código + análisis en un solo lugar |
| **Reproducibilidad** | Mismos resultados cada ejecución |
| **Flexibilidad** | Acceso a datos intermedios |
| **Mantenimiento** | Cambios en Skills se reflejan automáticamente |
| **Escalabilidad** | Fácil de modificar y extender |

## Archivos Involucrados

```
ProyectoAnaliticaDatos-1/
├── Notebooks/
│   └── Sistema_Agentico_Rendimiento_Estudiantil.ipynb  ← INTEGRADO
├── Agent/
│   └── Orquestador.py                                   ← COORDINADOR
├── Skills/
│   ├── preparar_datos.py
│   ├── analisis_eda.py
│   └── modelado.py
├── Data/
│   └── StudentPerformanceFactors.csv
└── INTEGRACION_NOTEBOOK_PIPELINE.md                     ← ESTE ARCHIVO
```

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'Agent'"

**Solución**: Asegúrate de ejecutar las celdas en orden y de que la ruta al proyecto es correcta:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path('../').resolve()))
```

### Error: "FileNotFoundError: Archivo no encontrado"

**Solución**: Verifica que la ruta del dataset es correcta:
```python
from pathlib import Path
ruta = Path('../Data/StudentPerformanceFactors.csv')
print(f"Ruta existe: {ruta.exists()}")
print(f"Ruta absoluta: {ruta.resolve()}")
```

### El pipeline se ejecuta muy lentamente

**Causa**: Probablemente es normal para dataset grandes o modelos complejos.
**Solución**: Los algoritmos pueden tardar varios minutos en completarse.

## Próximas Extensiones

Ideas para expandir la integración:

- [ ] Agregar visualizaciones interactivas de Plotly
- [ ] Exportar resultados a Excel/PDF
- [ ] Implementar predicciones en tiempo real
- [ ] Crear dashboard interactivo
- [ ] Agregar validación cruzada
- [ ] Implementar hyperparameter tuning

## Contacto y Soporte

Para preguntas o problemas con la integración:

1. Revisa la documentación en el notebook
2. Consulta el código en `Agent/Orquestador.py`
3. Verifica las Skills en `Skills/`

---

**Última actualización**: Mayo 2026
**Versión**: 1.0
**Estado**: Integrado y Funcional ✅

# ⚡ Inicio Rápido: Notebook + Pipeline

## 5 Pasos para Ejecutar el Pipeline desde el Notebook

### 1. Abre el Notebook
```
Notebooks/Sistema_Agentico_Rendimiento_Estudiantil.ipynb
```

### 2. Desplázate hasta la Sección 9
Busca la sección titulada **"9. INTEGRACIÓN CON EL PIPELINE AUTOMATIZADO"**

### 3. Ejecuta las Celdas (En orden)

**Celda 1**: Importar e Inicializar
```python
import sys
from pathlib import Path

ruta_proyecto = Path('../').resolve()
if str(ruta_proyecto) not in sys.path:
    sys.path.insert(0, str(ruta_proyecto))

from Agent.Orquestador import ejecutar_pipeline
ruta_dataset = '../Data/StudentPerformanceFactors.csv'

print("🚀 Ejecutando pipeline de análisis predictivo...\n")

try:
    resultados = ejecutar_pipeline(ruta_dataset)
    print("\n✅ Pipeline ejecutado exitosamente!")
except Exception as e:
    print(f"❌ Error al ejecutar el pipeline: {str(e)}")
    raise
```

**Celda 2**: Ver Dataset Preparado
```python
dataset = resultados['dataset']
print(f"✓ Dimensiones: {dataset.shape[0]} filas × {dataset.shape[1]} columnas")
print(f"✓ Memoria: {dataset.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
display(dataset.head())
```

**Celda 3**: Ver Análisis Exploratorio
```python
eda = resultados['eda']
print(f"✓ Dimensiones: {eda.get('dimensiones')}")
print(f"✓ Variables numéricas: {len(eda.get('variables_numericas', []))}")
print(f"✓ Variables categóricas: {len(eda.get('variables_categoricas', []))}")
print(f"✓ Valores nulos: {eda.get('total_valores_nulos', 0)}")
```

**Celda 4**: Ver Resultados del Modelo
```python
modelo = resultados['modelo']
print(f"✓ Modelo: {modelo.get('nombre_modelo')}")
metricas = modelo.get('metricas', {})
print(f"✓ Accuracy:  {metricas.get('accuracy'):.4f}")
print(f"✓ F1-Score:  {metricas.get('f1_score'):.4f}")

if 'importancia_features' in modelo:
    print(f"\n🔍 Top 5 Features:")
    for idx, (feature, imp) in enumerate(modelo['importancia_features'].head(5).items(), 1):
        print(f"   {idx}. {feature}: {imp:.4f}")
```

### 4. Espera a que se Completen todas las Celdas

El pipeline normalmente tarda entre **2-5 minutos** en completarse completamente.

### 5. ¡Listo! 🎉

Ahora tienes acceso a:
- ✅ Dataset preparado: `resultados['dataset']`
- ✅ Análisis EDA: `resultados['eda']`
- ✅ Modelo entrenado: `resultados['modelo']`

## Análisis Avanzados con los Resultados

Después de ejecutar el pipeline, puedes usar los resultados para:

### Análisis de Features
```python
importancias = resultados['modelo']['importancia_features']
print("Top 10 Features:")
print(importancias.head(10))
```

### Predicciones Personalizadas
```python
modelo_obj = resultados['modelo']['modelo']  # Si está disponible
# Realizar predicciones personalizadas aquí
```

### Visualizaciones Adicionales
```python
import matplotlib.pyplot as plt
import seaborn as sns

df = resultados['dataset']
plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.show()
```

## Información Rápida

| Componente | Ubicación |
|-----------|-----------|
| Notebook | `Notebooks/Sistema_Agentico_Rendimiento_Estudiantil.ipynb` |
| Orquestador | `Agent/Orquestador.py` |
| Data | `Data/StudentPerformanceFactors.csv` |
| Skills | `Skills/preparar_datos.py`, `analisis_eda.py`, `modelado.py` |

## Solución de Problemas Rápida

| Problema | Solución |
|---------|----------|
| Error de ruta | Verifica que el notebook esté en `Notebooks/` |
| ImportError | Ejecuta primero la celda de importación |
| Dataset no encontrado | La ruta debe ser `../Data/StudentPerformanceFactors.csv` |
| Errores de memoria | Espera a que las celdas anteriores se completen |

---

**Nota**: Para documentación completa, consulta `INTEGRACION_NOTEBOOK_PIPELINE.md`

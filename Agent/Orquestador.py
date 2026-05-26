from pathlib import Path
import sys

# Agregar el directorio padre al path para importar Skills
sys.path.insert(0, str(Path(__file__).parent.parent))

from Skills.preparar_datos import preparar_datos
from Skills.analisis_eda import ejecutar_eda
from Skills.modelado import entrenar_modelo


def _validar_ruta_dataset(ruta_dataset):
    """Valida que la ruta del dataset sea válida."""
    ruta = Path(ruta_dataset)

    if not ruta.exists():
        raise FileNotFoundError(f"❌ Archivo no encontrado: {ruta_dataset}")

    if not ruta.is_file():
        raise ValueError(f"❌ La ruta no es un archivo: {ruta_dataset}")

    if ruta.suffix.lower() != '.csv':
        raise ValueError(f"❌ Archivo debe ser CSV, se recibió: {ruta.suffix}")

    print(f"✓ Validación exitosa: {ruta_dataset}\n")


def _ejecutar_etapa(nombre_etapa, funcion, *args):
    """
    Ejecuta una etapa del pipeline con manejo de errores.

    Parámetros:
    -----------
    nombre_etapa : str
        Nombre descriptivo de la etapa
    funcion : callable
        Función a ejecutar
    args : tuple
        Argumentos para la función
    """
    print(f"\n{'=' * 60}")
    print(f"▶️  ETAPA {nombre_etapa}")
    print(f"{'=' * 60}")

    try:
        resultado = funcion(*args)
        print(f"\n✅ {nombre_etapa} completada exitosamente\n")
        return resultado

    except Exception as e:
        print(f"\n❌ Error en {nombre_etapa}: {str(e)}\n")
        raise


def ejecutar_pipeline(ruta_dataset):
    """
    Orquestador que ejecuta el pipeline de análisis predictivo.

    Coordina la ejecución secuencial de tres skills:
    1. Preparación de datos
    2. Análisis exploratorio (EDA)
    3. Entrenamiento de modelos

    Parámetros:
    -----------
    ruta_dataset : str
        Ruta del archivo CSV con datos crudos

    Retorna:
    --------
    dict
        {
            'dataset': DataFrame preparado,
            'eda': Diccionario con análisis exploratorio,
            'modelo': Diccionario con modelo y métricas
        }

    Notas:
    ------
    - El agente COORDINA el flujo, no contiene lógica analítica
    - Cada etapa es independiente y modular
    - Los errores se propagan con contexto claro
    """

    print("\n" + "=" * 60)
    print("🤖 INICIANDO PIPELINE DE ANÁLISIS PREDICTIVO")
    print("=" * 60)

    # Validar entrada
    print("\n📋 Validando entrada...")
    _validar_ruta_dataset(ruta_dataset)

    # Etapa 1: Preparación de datos
    dataset_preparado = _ejecutar_etapa(
        "1: PREPARACIÓN DE DATOS",
        preparar_datos,
        ruta_dataset
    )

    # Etapa 2: Análisis exploratorio
    analisis_eda = _ejecutar_etapa(
        "2: ANÁLISIS EXPLORATORIO (EDA)",
        ejecutar_eda,
        dataset_preparado
    )

    # Etapa 3: Entrenamiento de modelos
    modelo_entrenado = _ejecutar_etapa(
        "3: ENTRENAMIENTO DE MODELOS",
        entrenar_modelo,
        dataset_preparado
    )

    # Resumen final
    print("=" * 60)
    print("✅ PIPELINE COMPLETADO EXITOSAMENTE")
    print("=" * 60)
    print(f"\n📊 Resumen de resultados:")
    print(f"   • Dataset: {dataset_preparado.shape[0]} filas × {dataset_preparado.shape[1]} columnas")
    print(f"   • EDA: Análisis generado con {len(analisis_eda)} métricas")
    print(f"   • Modelo ganador: {modelo_entrenado['nombre_modelo']}")
    print(f"   • F1-Score: {modelo_entrenado['metricas']['f1_score']:.4f}")
    print("=" * 60 + "\n")

    # Retornar resultados
    resultados = {
        "dataset": dataset_preparado,
        "eda": analisis_eda,
        "modelo": modelo_entrenado
    }

    return resultados


if __name__ == "__main__":
    import sys
    
    try:
        ruta_dataset = "Data/StudentPerformanceFactors.csv"
        resultados = ejecutar_pipeline(ruta_dataset)
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

import sys
from pathlib import Path
from Agent.Orquestador import ejecutar_pipeline


def _mostrar_resumen_final(resultados):
    """Muestra un resumen detallado de los resultados del pipeline."""
    print("\n" + "=" * 60)
    print("📊 RESUMEN FINAL DEL PIPELINE")
    print("=" * 60)

    # Información del dataset
    dataset = resultados['dataset']
    print(f"\n🗂️  DATASET PREPARADO:")
    print(f"   Filas: {dataset.shape[0]}")
    print(f"   Columnas: {dataset.shape[1]}")
    print(f"   Memoria: {dataset.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

    # Información del EDA
    eda = resultados['eda']
    print(f"\n📈 ANÁLISIS EXPLORATORIO (EDA):")
    print(f"   Dimensiones: {eda.get('dimensiones', 'N/A')}")
    print(f"   Variables numéricas: {len(eda.get('variables_numericas', []))}")
    print(f"   Variables categóricas: {len(eda.get('variables_categoricas', []))}")
    print(f"   Total valores nulos: {eda.get('total_valores_nulos', 'N/A')}")

    # Información del modelo
    modelo = resultados['modelo']
    print(f"\n🤖 MODELO ENTRENADO:")
    print(f"   Modelo ganador: {modelo.get('nombre_modelo', 'N/A')}")
    print(f"   Variable objetivo: {modelo.get('variable_objetivo', 'N/A')}")
    print(f"   Tamaño train: {modelo.get('shape_train', 'N/A')}")
    print(f"   Tamaño test: {modelo.get('shape_test', 'N/A')}")

    # Métricas de desempeño
    metricas = modelo.get('metricas', {})
    print(f"\n📊 MÉTRICAS DE DESEMPEÑO:")
    print(f"   Accuracy:  {metricas.get('accuracy', 'N/A'):.4f}")
    print(f"   Precision: {metricas.get('precision', 'N/A'):.4f}")
    print(f"   Recall:    {metricas.get('recall', 'N/A'):.4f}")
    print(f"   F1-Score:  {metricas.get('f1_score', 'N/A'):.4f}")

    print("\n" + "=" * 60)
    print("✅ EJECUCIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 60 + "\n")


def _manejar_error(error):
    """Maneja errores y muestra mensaje informativo."""
    print("\n" + "=" * 60)
    print("❌ ERROR EN LA EJECUCIÓN")
    print("=" * 60)
    print(f"\nTipo de error: {type(error).__name__}")
    print(f"Mensaje: {str(error)}")
    print("\n" + "=" * 60)
    print("⚠️  El pipeline no se completó exitosamente")
    print("=" * 60 + "\n")

    return 1


def main():
    """
    Función principal que ejecuta el sistema agéntico completo.

    Flujo:
    1. Define ruta del dataset
    2. Ejecuta el pipeline
    3. Muestra resumen final
    4. Captura errores
    """
    print("\n" + "=" * 60)
    print("🚀 SISTEMA AGÉNTICO DE ANÁLISIS PREDICTIVO")
    print("=" * 60)

    # Definir ruta del dataset
    ruta_dataset = "data/StudentPerformanceFactors.csv"

    print(f"\n📁 Ruta del dataset: {ruta_dataset}")

    try:
        # Ejecutar pipeline
        resultados = ejecutar_pipeline(ruta_dataset)

        # Mostrar resumen final
        _mostrar_resumen_final(resultados)

        return 0

    except FileNotFoundError as e:
        print(f"\n❌ Archivo no encontrado: {e}")
        return _manejar_error(e)

    except ValueError as e:
        print(f"\n❌ Error de validación: {e}")
        return _manejar_error(e)

    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        return _manejar_error(e)


if __name__ == "__main__":
    codigo_salida = main()
    sys.exit(codigo_salida)
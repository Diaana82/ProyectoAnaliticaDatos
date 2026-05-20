from Skills.Skill1 import preparar_datos
from Skills.Skill2 import ejecutar_eda
from Skills.Skill3 import entrenar_modelo


def ejecutar_pipeline(ruta_dataset):
    """
    Orquestador que ejecuta el pipeline de análisis de datos.

    Flujo:
    1. Preparar datos (Skill1)
    2. Ejecutar EDA (Skill2)
    3. Entrenar modelo (Skill3)

    Args:
        ruta_dataset: Ruta del archivo de dataset

    Returns:
        dict: Resultados del pipeline con datos preparados, análisis EDA y modelo entrenado
    """

    # Etapa 1: Preparar datos
    datos_preparados = preparar_datos(ruta_dataset)

    # Etapa 2: Ejecutar EDA
    analisis_eda = ejecutar_eda(datos_preparados)

    # Etapa 3: Entrenar modelo
    modelo_entrenado = entrenar_modelo(datos_preparados)

    # Retornar resultados del pipeline
    resultados = {
        "datos_preparados": datos_preparados,
        "analisis_eda": analisis_eda,
        "modelo": modelo_entrenado
    }

    return resultados

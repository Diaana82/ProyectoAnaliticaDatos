"""
EJEMPLO_USO.md - Guía de uso de las utilidades de la carpeta helpers

Este archivo muestra ejemplos prácticos de cómo usar cada módulo.
"""

# =====================================================================
# EJEMPLOS DE USO DEL MÓDULO LOGGER
# =====================================================================

from helpers.logger import (
    print_title, print_subtitle, print_success, print_error,
    print_info, print_separator, print_metric
)

# Ejemplo: Imprimir títulos y subtítulos
print_title("ANÁLISIS EXPLORATORIO DE DATOS")
print_subtitle("1. Carga de Datos")

# Ejemplo: Mensajes de éxito y error
print_success("Datos cargados correctamente")
print_info("Procesando 1000 registros")
print_error("Columna 'edad' contiene valores nulos")

# Ejemplo: Métricas
print_metric("Total de registros", 1000)
print_metric("Precisión del modelo", 0.95)
print_metric("Tamaño del dataset", 250, "MB")


# =====================================================================
# EJEMPLOS DE USO DEL MÓDULO RUTAS
# =====================================================================

from helpers.rutas import (
    get_data_dir, get_output_dir, get_eda_output_dir,
    get_file_path, ensure_path_exists
)
import pandas as pd

# Ejemplo: Cargar datos desde Data/
data_dir = get_data_dir()
df = pd.read_csv(data_dir / "StudentPerformanceFactors.csv")

# Ejemplo: Guardar resultados en outputs/eda/
eda_dir = get_eda_output_dir()
ensure_path_exists(eda_dir)  # Crear si no existe
df.describe().to_csv(eda_dir / "estadisticas.csv")

# Ejemplo: Usar rutas dinámicas
csv_path = get_file_path("Data", "datos.csv")
output_path = get_file_path("outputs/eda", "grafico.html")


# =====================================================================
# EJEMPLOS DE USO DEL MÓDULO UTILS
# =====================================================================

from helpers.utils import (
    format_percentage, format_number, calculate_percentage,
    calculate_percentage_change, to_float, is_numeric, is_empty
)

# Ejemplo: Formateo de números
porcentaje = format_percentage(0.8567)  # "85.67%"
numero = format_number(1000.567)         # "1,000.57"

# Ejemplo: Cálculos
ratio = calculate_percentage(25, 100)    # 0.25
cambio = calculate_percentage_change(100, 150)  # 0.5

# Ejemplo: Conversión segura
valor = to_float("3.14")        # 3.14
valor_defecto = to_float("abc", default=0.0)  # 0.0

# Ejemplo: Validación
print(is_numeric("42"))         # True
print(is_empty([]))             # True
print(is_empty("datos"))        # False


# =====================================================================
# EJEMPLOS DE USO DEL MÓDULO FILES
# =====================================================================

from helpers.files import (
    create_directory, clean_directory, list_files,
    file_exists, directory_exists, get_file_count
)
from pathlib import Path

# Ejemplo: Crear directorio
output_dir = Path("outputs/modelos")
create_directory(output_dir)

# Ejemplo: Limpiar directorio
clean_directory(output_dir)

# Ejemplo: Listar archivos
csv_files = list_files(get_data_dir(), pattern="*.csv")
print(f"Encontrados {len(csv_files)} archivos CSV")

# Ejemplo: Validar existencia
if file_exists(get_data_dir() / "datos.csv"):
    print("El archivo de datos existe")

# Ejemplo: Contar archivos
count = get_file_count(get_data_dir(), pattern="*.csv")
print(f"Total de archivos CSV: {count}")


# =====================================================================
# EJEMPLO COMPLETO: PIPELINE TÍPICO
# =====================================================================

from helpers.logger import print_title, print_subtitle, print_success, print_info
from helpers.rutas import get_data_dir, get_eda_output_dir, ensure_path_exists
from helpers.files import create_directory, list_files, file_exists
from helpers.utils import format_percentage, format_number
import pandas as pd

def ejemplo_pipeline():
    """Ejemplo de un flujo típico usando helpers."""
    
    # 1. Inicio
    print_title("PIPELINE DE ANÁLISIS PREDICTIVO")
    
    # 2. Preparar directorios
    print_subtitle("Preparación de Directorios")
    eda_dir = get_eda_output_dir()
    ensure_path_exists(eda_dir)
    print_success(f"Directorio creado: {eda_dir}")
    
    # 3. Cargar datos
    print_subtitle("Carga de Datos")
    data_dir = get_data_dir()
    csv_files = list_files(data_dir, pattern="*.csv")
    print_info(f"Archivos encontrados: {len(csv_files)}")
    
    if csv_files:
        df = pd.read_csv(csv_files[0])
        print_success(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")
    
    # 4. Análisis
    print_subtitle("Análisis Exploratorio")
    print_info(f"Tamaño del dataset: {format_number(df.memory_usage().sum())} bytes")
    print_info(f"Completitud de datos: {format_percentage(df.notna().sum().sum() / (df.shape[0] * df.shape[1]))}")
    
    # 5. Guardar resultados
    print_subtitle("Guardando Resultados")
    stats_file = eda_dir / "estadisticas.csv"
    df.describe().to_csv(stats_file)
    print_success(f"Estadísticas guardadas en {stats_file}")
    
    print_title("PROCESO COMPLETADO")

# Descomentar para ejecutar:
# ejemplo_pipeline()

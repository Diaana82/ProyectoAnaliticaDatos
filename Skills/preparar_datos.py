import pandas as pd


def _mostrar_dimensiones(df):
    """Muestra las dimensiones del dataset."""
    filas, columnas = df.shape
    print(f"\n Dimensiones del dataset: {filas} filas × {columnas} columnas")


def _mostrar_tipos_datos(df):
    """Muestra los tipos de datos de cada columna."""
    print("\n Tipos de datos:")
    print(df.dtypes)


def _revisar_valores_nulos(df):
    """Revisa y reporta valores nulos en el dataset."""
    nulos = df.isnull().sum()
    if nulos.sum() > 0:
        print("\n  Valores nulos detectados:")
        print(nulos[nulos > 0])
        print(f"Total de celdas nulas: {nulos.sum()}")
    else:
        print("\n✓ No hay valores nulos en el dataset")


def _eliminar_duplicados(df):
    """Elimina filas duplicadas del dataset."""
    duplicados_iniciales = df.duplicated().sum()
    if duplicados_iniciales > 0:
        print(f"\n🔄 Eliminando {duplicados_iniciales} fila(s) duplicada(s)...")
        df = df.drop_duplicates(ignore_index=True)
        print(f"✓ Duplicados eliminados. Nuevo tamaño: {len(df)} filas")
    else:
        print("\n✓ No hay filas duplicadas")
    return df


def _limpiar_datos_basicos(df):
    """Realiza limpieza básica de datos."""
    # Eliminar espacios en blanco en columnas de texto
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()

    # Eliminar filas donde todas las columnas son nulas
    filas_iniciales = len(df)
    df = df.dropna(how='all')
    filas_eliminadas = filas_iniciales - len(df)
    if filas_eliminadas > 0:
        print(f"\n🧹 Se eliminaron {filas_eliminadas} fila(s) completamente vacía(s)")
    # Convertir nombres columnas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df
    

def preparar_datos(ruta):
    """
    Prepara y limpia datos desde un archivo CSV.

    Parámetros:
    -----------
    ruta : str
        Ruta del archivo CSV a cargar

    Retorna:
    --------
    pd.DataFrame
        Dataframe preparado y limpio

    Proceso:
    --------
    1. Carga el CSV
    2. Muestra dimensiones
    3. Muestra tipos de datos
    4. Elimina duplicados
    5. Revisa valores nulos
    6. Limpia datos básicos
    """

    print("=" * 60)
    print("🔄 INICIANDO PREPARACIÓN DE DATOS")
    print("=" * 60)

    # Cargar CSV
    try:
        df = pd.read_csv(ruta)
        print(f"\n✓ Archivo cargado exitosamente: {ruta}")
    except FileNotFoundError:
        print(f"\n❌ Error: No se encontró el archivo en {ruta}")
        raise
    except Exception as e:
        print(f"\n❌ Error al cargar el archivo: {e}")
        raise

    # Mostrar dimensiones iniciales
    _mostrar_dimensiones(df)

    # Mostrar tipos de datos
    _mostrar_tipos_datos(df)

    # Eliminar duplicados
    df = _eliminar_duplicados(df)

    # Limpiar datos básicos
    df = _limpiar_datos_basicos(df)

    # Revisar valores nulos
    _revisar_valores_nulos(df)

    # Resumen final
    print("\n" + "=" * 60)
    print("✅ PREPARACIÓN DE DATOS COMPLETADA")
    print("=" * 60)
    _mostrar_dimensiones(df)
    print("=" * 60 + "\n")

    return df

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# Configurar estilo de gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


def _crear_directorio_salida():
    """Crea el directorio de salida para gráficos si no existe."""
    ruta_salida = Path("outputs/eda")
    ruta_salida.mkdir(parents=True, exist_ok=True)
    return ruta_salida


def _mostrar_info_general(df):
    """Muestra información general del dataset."""
    print("\n📊 INFORMACIÓN GENERAL DEL DATASET")
    print("=" * 60)
    print(f"Tamaño: {df.shape[0]} filas × {df.shape[1]} columnas")
    print(f"\nNombres de columnas:")
    print(df.columns.tolist())
    print(f"\nTipos de datos:")
    print(df.dtypes)
    print("\nPrimeras 5 filas:")
    print(df.head())


def _generar_estadisticas_descriptivas(df):
    """Genera y muestra estadísticas descriptivas."""
    print("\n📈 ESTADÍSTICAS DESCRIPTIVAS")
    print("=" * 60)
    estadisticas = df.describe()
    print(estadisticas)
    return estadisticas


def _analizar_valores_faltantes(df):
    """Analiza y reporta valores faltantes."""
    print("\n⚠️  ANÁLISIS DE VALORES FALTANTES")
    print("=" * 60)

    nulos = df.isnull().sum()
    porcentaje_nulos = (df.isnull().sum() / len(df) * 100).round(2)

    resumen_nulos = pd.DataFrame({
        'Columna': nulos.index,
        'Valores Nulos': nulos.values,
        'Porcentaje (%)': porcentaje_nulos.values
    })

    resumen_nulos = resumen_nulos[resumen_nulos['Valores Nulos'] > 0]

    if len(resumen_nulos) > 0:
        print("\nValores faltantes detectados:")
        print(resumen_nulos.to_string(index=False))
    else:
        print("✓ No hay valores faltantes en el dataset")

    return resumen_nulos


def _mostrar_distribucion_numericas(df, ruta_salida):
    """Genera gráficos de distribución para variables numéricas."""
    print("\n📊 DISTRIBUCIÓN DE VARIABLES NUMÉRICAS")
    print("=" * 60)

    # Seleccionar solo columnas numéricas
    numericas = df.select_dtypes(include=[np.number]).columns.tolist()

    if not numericas:
        print("⚠️  No hay variables numéricas en el dataset")
        return

    print(f"Variables numéricas encontradas: {numericas}")

    # Crear subplots para distribuciones
    n_cols = len(numericas)
    n_rows = (n_cols + 2) // 3  # 3 gráficos por fila

    fig, axes = plt.subplots(n_rows, 3, figsize=(15, 4*n_rows))
    axes = axes.flatten()

    for idx, col in enumerate(numericas):
        axes[idx].hist(df[col], bins=30, edgecolor='black', alpha=0.7)
        axes[idx].set_title(f'Distribución: {col}', fontweight='bold')
        axes[idx].set_xlabel(col)
        axes[idx].set_ylabel('Frecuencia')

    # Ocultar subplots vacíos
    for idx in range(len(numericas), len(axes)):
        axes[idx].set_visible(False)

    plt.tight_layout()
    ruta_grafico = ruta_salida / "distribucion_variables.png"
    plt.savefig(ruta_grafico, dpi=300, bbox_inches='tight')
    print(f"✓ Gráfico guardado: {ruta_grafico}")
    plt.close()


def _generar_matriz_correlacion(df, ruta_salida):
    """Genera y visualiza la matriz de correlación."""
    print("\n🔗 MATRIZ DE CORRELACIÓN")
    print("=" * 60)

    # Seleccionar solo columnas numéricas
    numericas = df.select_dtypes(include=[np.number])

    if numericas.shape[1] < 2:
        print("⚠️  No hay suficientes variables numéricas para correlación")
        return pd.DataFrame()

    # Calcular correlación
    matriz_corr = numericas.corr()
    print("\nMatriz de correlación:")
    print(matriz_corr)

    # Visualizar matriz de correlación
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        matriz_corr,
        annot=True,
        fmt='.2f',
        cmap='coolwarm',
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.8},
        ax=ax
    )
    ax.set_title('Matriz de Correlación', fontweight='bold', fontsize=14)
    plt.tight_layout()

    ruta_grafico = ruta_salida / "matriz_correlacion.png"
    plt.savefig(ruta_grafico, dpi=300, bbox_inches='tight')
    print(f"✓ Gráfico guardado: {ruta_grafico}")
    plt.close()

    return matriz_corr


def _generar_boxplots(df, ruta_salida):
    """Genera boxplots para variables numéricas."""
    print("\n📦 BOXPLOTS DE VARIABLES NUMÉRICAS")
    print("=" * 60)

    numericas = df.select_dtypes(include=[np.number]).columns.tolist()

    if not numericas:
        print("⚠️  No hay variables numéricas para boxplot")
        return

    fig, axes = plt.subplots(1, len(numericas), figsize=(4*len(numericas), 5))

    if len(numericas) == 1:
        axes = [axes]

    for idx, col in enumerate(numericas):
        axes[idx].boxplot(df[col].dropna())
        axes[idx].set_title(f'Boxplot: {col}', fontweight='bold')
        axes[idx].set_ylabel(col)

    plt.tight_layout()
    ruta_grafico = ruta_salida / "boxplots_variables.png"
    plt.savefig(ruta_grafico, dpi=300, bbox_inches='tight')
    print(f"✓ Gráfico guardado: {ruta_grafico}")
    plt.close()


def _generar_resumen(df, estadisticas, matriz_corr, nulos):
    """Genera un diccionario resumen del análisis."""
    resumen = {
        'dimensiones': df.shape,
        'columnas': df.columns.tolist(),
        'tipos_datos': df.dtypes.to_dict(),
        'estadisticas_descriptivas': estadisticas.to_dict(),
        'total_valores_nulos': df.isnull().sum().sum(),
        'matriz_correlacion': matriz_corr.to_dict() if not matriz_corr.empty else {},
        'variables_numericas': df.select_dtypes(include=[np.number]).columns.tolist(),
        'variables_categoricas': df.select_dtypes(include=['object']).columns.tolist(),
        'memoria_mb': df.memory_usage(deep=True).sum() / 1024**2
    }
    return resumen


def ejecutar_eda(df):
    """
    Realiza análisis exploratorio del dataset (EDA).

    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame preparado para análisis

    Retorna:
    --------
    dict
        Diccionario con resumen del análisis EDA

    Proceso:
    --------
    1. Muestra información general
    2. Genera estadísticas descriptivas
    3. Analiza valores faltantes
    4. Visualiza distribución de variables
    5. Genera matriz de correlación
    6. Crea boxplots
    7. Retorna resumen completo
    """

    print("\n" + "=" * 60)
    print("🔍 INICIANDO ANÁLISIS EXPLORATORIO (EDA)")
    print("=" * 60)

    # Crear directorio de salida
    ruta_salida = _crear_directorio_salida()

    # Análisis paso a paso
    _mostrar_info_general(df)
    estadisticas = _generar_estadisticas_descriptivas(df)
    nulos = _analizar_valores_faltantes(df)
    _mostrar_distribucion_numericas(df, ruta_salida)
    matriz_corr = _generar_matriz_correlacion(df, ruta_salida)
    _generar_boxplots(df, ruta_salida)

    # Generar resumen
    resumen = _generar_resumen(df, estadisticas, matriz_corr, nulos)

    # Resumen final
    print("\n" + "=" * 60)
    print("✅ ANÁLISIS EDA COMPLETADO")
    print("=" * 60)
    print(f"📁 Gráficos guardados en: {ruta_salida}")
    print("=" * 60 + "\n")

    return resumen

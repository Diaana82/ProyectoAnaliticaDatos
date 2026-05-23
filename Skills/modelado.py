import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
    )


def _transformar_exam_score_a_rendimiento(df):
    """
    Transforma exam_score en variable categórica rendimiento.

    Reglas:
    - exam_score < 60 → Bajo
    - 60 <= exam_score < 75 → Medio
    - exam_score >= 75 → Alto
    """
    df_transformado = df.copy()

    # Buscar columna exam_score (sin importar mayúsculas)
    columnas_minusculas = {col.lower(): col for col in df_transformado.columns}

    if 'exam_score' not in columnas_minusculas:
        print("⚠️  Columna 'exam_score' no encontrada. Continuando sin transformación.")
        return df_transformado

    col_exam_score = columnas_minusculas['exam_score']

    # Crear categorías de rendimiento
    def categorizar_rendimiento(score):
        if score < 60:
            return 'Bajo'
        elif score < 75:
            return 'Medio'
        else:
            return 'Alto'

    # Aplicar transformación
    df_transformado['rendimiento'] = df_transformado[col_exam_score].apply(categorizar_rendimiento)

    # Eliminar columna exam_score
    df_transformado = df_transformado.drop(columns=[col_exam_score])

    print(f"\n✓ Transformación exam_score → rendimiento completada")
    print(f"  Bajo:  {(df_transformado['rendimiento'] == 'Bajo').sum()} muestras")
    print(f"  Medio: {(df_transformado['rendimiento'] == 'Medio').sum()} muestras")
    print(f"  Alto:  {(df_transformado['rendimiento'] == 'Alto').sum()} muestras")

    return df_transformado


def _identificar_variable_objetivo(df):
    """
    Identifica automáticamente la variable objetivo.
    Prioriza columna 'rendimiento' si existe, sino busca la última columna.
    """
    # Prioridad: buscar columna 'rendimiento'
    columnas_minusculas = [col.lower() for col in df.columns]

    if 'rendimiento' in columnas_minusculas:
        idx = columnas_minusculas.index('rendimiento')
        variable_objetivo = df.columns[idx]
        print(f"✓ Variable objetivo identificada: '{variable_objetivo}'")
        return variable_objetivo

    # Alternativa: última columna
    variable_objetivo = df.columns[-1]
    print(f"⚠️  'rendimiento' no encontrada. Usando última columna: '{variable_objetivo}'")
    return variable_objetivo


def _separar_features_target(df, variable_objetivo):
    """Separa características (X) y variable objetivo (y)."""
    if variable_objetivo not in df.columns:
        raise ValueError(f"Variable objetivo '{variable_objetivo}' no encontrada")

    y = df[variable_objetivo]
    X = df.drop(columns=[variable_objetivo])

    print(f"\n✓ Features (X): {X.shape[1]} columnas")
    print(f"✓ Target (y): {y.shape[0]} muestras")

    return X, y


def _codificar_variables_categoricas(X, X_test=None):
    """
    Codifica variables categóricas usando LabelEncoder.
    Retorna X codificado y opcionalmente X_test codificado.
    """
    X_encoded = X.copy()
    label_encoders = {}

    # Identificar columnas categóricas
    categoricas = X_encoded.select_dtypes(include=['object']).columns

    if len(categoricas) == 0:
        print("✓ No hay variables categóricas para codificar")
        if X_test is not None:
            return X_encoded, X_test.copy(), label_encoders
        return X_encoded, label_encoders

    print(f"\n🔤 Codificando {len(categoricas)} variable(s) categórica(s)")

    # Codificar variables categóricas
    for col in categoricas:
        le = LabelEncoder()
        X_encoded[col] = le.fit_transform(X_encoded[col].astype(str))
        label_encoders[col] = le
        print(f"  ✓ {col}: {len(le.classes_)} categorías codificadas")

    # Codificar X_test si se proporciona
    if X_test is not None:
        X_test_encoded = X_test.copy()
        for col in categoricas:
            X_test_encoded[col] = label_encoders[col].transform(
                X_test_encoded[col].astype(str)
            )
        return X_encoded, X_test_encoded, label_encoders

    return X_encoded, label_encoders


def _dividir_datos(X, y, test_size=0.2, random_state=42):
    """Divide datos en entrenamiento y prueba (80/20)."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )

    print(f"\n📊 División train/test (80/20):")
    print(f"  ✓ Entrenamiento: {X_train.shape[0]} muestras")
    print(f"  ✓ Prueba: {X_test.shape[0]} muestras")

    return X_train, X_test, y_train, y_test


def _analizar_distribucion_clases(y):
    """Analiza y muestra la distribución de clases en la variable objetivo."""
    print(f"\n📊 DISTRIBUCIÓN DE CLASES")
    print("=" * 60)

    distribucion = y.value_counts().sort_index()
    total = len(y)
    desbalance = distribucion.max() / distribucion.min()

    print("\nConteo por clase:")
    for clase, conteo in distribucion.items():
        porcentaje = (conteo / total) * 100
        barra = "█" * int(porcentaje / 2)
        print(f"  {clase:10s}: {conteo:5d} ({porcentaje:5.1f}%) {barra}")

    print(f"\n⚠️  Ratio de desbalance: {desbalance:.2f}:1")

    if desbalance > 2:
        print("   → Dataset DESBALANCEADO. Aplicando class_weight='balanced'")
    else:
        print("   → Dataset BALANCEADO")

    return distribucion


def _entrenar_modelos(X_train, X_test, y_train, y_test):
    """
    Entrena 3 modelos con class_weight='balanced' para manejar desbalance.
    Retorna resultados con métricas y matrices de confusión.
    """
    modelos = {
        'Logistic Regression': LogisticRegression(
            max_iter=1000,
            class_weight='balanced',
            random_state=42
        ),
        'Decision Tree': DecisionTreeClassifier(
            class_weight='balanced',
            random_state=42
        ),
        'Random Forest': RandomForestClassifier(
            n_estimators=100,
            class_weight='balanced',
            random_state=42
        )
    }

    resultados = {}

    print(f"\n🤖 ENTRENANDO MODELOS CON class_weight='balanced'")
    print("=" * 60)

    for nombre, modelo in modelos.items():
        # Entrenar
        modelo.fit(X_train, y_train)

        # Predicciones
        y_pred = modelo.predict(X_test)

        # Calcular métricas
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

        # Matriz de confusión
        conf_matrix = confusion_matrix(y_test, y_pred)

        # Reporte de clasificación (incluye soporte por clase)
        class_report = classification_report(
            y_test, y_pred,
            output_dict=True,
            zero_division=0
        )

        # Guardar resultados
        resultados[nombre] = {
            'modelo': modelo,
            'y_pred': y_pred,
            'metricas': {
                'accuracy': round(accuracy, 4),
                'precision': round(precision, 4),
                'recall': round(recall, 4),
                'f1_score': round(f1, 4)
            },
            'confusion_matrix': conf_matrix,
            'classification_report': class_report
        }

        # Mostrar resultados
        print(f"\n{nombre}:")
        print(f"  Accuracy:  {accuracy:.4f}")
        print(f"  Precision: {precision:.4f}")
        print(f"  Recall:    {recall:.4f}")
        print(f"  F1-Score:  {f1:.4f}")

        # Mostrar soporte por clase
        print(f"\n  Soporte por clase:")
        for clase in y_test.unique():
            soporte = (y_test == clase).sum()
            print(f"    {clase}: {soporte} muestras")

    return resultados


def _reportar_matriz_confusion(nombre_modelo, conf_matrix, clases):
    """Muestra la matriz de confusión de un modelo."""
    print(f"\n  Matriz de Confusión ({nombre_modelo}):")
    print("  " + " ".join(f"{clase:>8s}" for clase in clases))

    for i, clase in enumerate(clases):
        fila = "  " + clase[:8].ljust(8) + " ".join(
            f"{conf_matrix[i][j]:>8d}" for j in range(len(clases))
        )
        print(fila)


def _seleccionar_mejor_modelo(resultados, y_test):
    """Selecciona el modelo con mejor F1-Score y muestra matriz de confusión."""
    mejor_nombre = max(
        resultados.keys(),
        key=lambda x: resultados[x]['metricas']['f1_score']
    )

    mejor_modelo = resultados[mejor_nombre]['modelo']
    mejores_metricas = resultados[mejor_nombre]['metricas']
    conf_matrix_mejor = resultados[mejor_nombre]['confusion_matrix']
    clases = sorted(y_test.unique())

    print("\n" + "=" * 60)
    print(f"🏆 MEJOR MODELO: {mejor_nombre}")
    print(f"  F1-Score: {mejores_metricas['f1_score']:.4f}")
    print("=" * 60)

    # Mostrar matriz de confusión del mejor modelo
    _reportar_matriz_confusion(mejor_nombre, conf_matrix_mejor, clases)

    return mejor_nombre, mejor_modelo, mejores_metricas


def entrenar_modelo(df):
    """
    Entrena múltiples modelos de clasificación y selecciona el mejor.

    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame con características y variable objetivo o exam_score

    Retorna:
    --------
    dict
        {
            'modelo_ganador': modelo entrenado,
            'metricas': diccionario con accuracy, precision, recall, f1_score,
            'nombre_modelo': nombre del mejor modelo
        }

    Proceso:
    --------
    1. Transforma exam_score en rendimiento (si existe)
    2. Identifica variable objetivo automáticamente
    3. Separa X (features) e y (target)
    4. Codifica variables categóricas
    5. Divide datos 80/20 (train/test)
    6. Entrena 3 modelos:
       - Logistic Regression
       - Decision Tree
       - Random Forest
    7. Evalúa con accuracy, precision, recall, f1-score
    8. Selecciona mejor modelo por F1-Score
    """

    print("\n" + "=" * 60)
    print("🚀 INICIANDO ENTRENAMIENTO DE MODELOS")
    print("=" * 60)

    # Paso 0: Transformar exam_score a rendimiento
    df_transformado = _transformar_exam_score_a_rendimiento(df)

    # Paso 1: Identificar variable objetivo
    variable_objetivo = _identificar_variable_objetivo(df_transformado)

    # Paso 2: Separar X e y
    X, y = _separar_features_target(df_transformado, variable_objetivo)

    # Paso 2.5: Analizar distribución de clases
    _analizar_distribucion_clases(y)

    # Paso 3: Codificar variables categóricas
    X_encoded, label_encoders = _codificar_variables_categoricas(X)

    # Paso 4: Dividir datos
    X_train, X_test, y_train, y_test = _dividir_datos(X_encoded, y)

    # Paso 5 y 6: Entrenar y evaluar modelos
    resultados = _entrenar_modelos(X_train, X_test, y_train, y_test)

    # Paso 7: Seleccionar mejor modelo
    nombre_mejor, modelo_ganador, mejores_metricas = _seleccionar_mejor_modelo(resultados, y_test)

    # Retornar resultado
    resultado_final = {
        'modelo_ganador': modelo_ganador,
        'nombre_modelo': nombre_mejor,
        'metricas': mejores_metricas,
        'variable_objetivo': variable_objetivo,
        'label_encoders': label_encoders,
        'shape_train': X_train.shape,
        'shape_test': X_test.shape
    }

    print("\n✅ ENTRENAMIENTO COMPLETADO")
    print("=" * 60 + "\n")

    return resultado_final

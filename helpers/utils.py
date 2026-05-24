"""
utils.py - Módulo de utilidades generales y cálculos simples.

Contiene funciones reutilizables para formateo de datos, cálculos matemáticos
y transformaciones comunes utilizadas en el pipeline de análisis.
"""

from typing import Union, List
import math


# =====================================================================
# FUNCIONES DE FORMATEO
# =====================================================================

def format_percentage(value: Union[int, float], decimals: int = 2) -> str:
    """
    Formatea un número como porcentaje.
    
    Args:
        value: Número a formatear (0.0 a 1.0 o 0 a 100)
        decimals: Número de decimales (default: 2)
    
    Returns:
        str: Número formateado como porcentaje con símbolo %
    
    Example:
        >>> format_percentage(0.8567)
        '85.67%'
        >>> format_percentage(0.5, decimals=1)
        '50.0%'
    """
    # Si el valor está entre 0 y 1, convertir a porcentaje
    if 0 <= value <= 1:
        value = value * 100
    
    return f"{value:.{decimals}f}%"


def format_number(value: Union[int, float], decimals: int = 2) -> str:
    """
    Formatea un número con separadores de miles y decimales.
    
    Args:
        value: Número a formatear
        decimals: Número de decimales (default: 2)
    
    Returns:
        str: Número formateado
    
    Example:
        >>> format_number(1000.567)
        '1,000.57'
        >>> format_number(999, decimals=0)
        '999'
    """
    return f"{value:,.{decimals}f}".rstrip('0').rstrip('.')


def format_size_bytes(bytes_value: int) -> str:
    """
    Convierte bytes a formato legible (KB, MB, GB, etc).
    
    Args:
        bytes_value: Tamaño en bytes
    
    Returns:
        str: Tamaño formateado legiblemente
    
    Example:
        >>> format_size_bytes(1024)
        '1.00 KB'
        >>> format_size_bytes(1048576)
        '1.00 MB'
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.2f} PB"


# =====================================================================
# FUNCIONES MATEMÁTICAS Y ESTADÍSTICAS
# =====================================================================

def calculate_percentage(part: Union[int, float], total: Union[int, float]) -> float:
    """
    Calcula el porcentaje que representa una parte del total.
    
    Args:
        part: Parte o numerador
        total: Total o denominador
    
    Returns:
        float: Porcentaje como decimal (0.0 a 1.0)
    
    Example:
        >>> calculate_percentage(25, 100)
        0.25
        >>> calculate_percentage(15, 50)
        0.3
    """
    if total == 0:
        return 0.0
    return part / total


def calculate_percentage_change(old_value: Union[int, float], 
                               new_value: Union[int, float]) -> float:
    """
    Calcula el cambio porcentual entre dos valores.
    
    Args:
        old_value: Valor anterior
        new_value: Valor nuevo
    
    Returns:
        float: Cambio porcentual como decimal
    
    Example:
        >>> calculate_percentage_change(100, 150)
        0.5
        >>> calculate_percentage_change(100, 80)
        -0.2
    """
    if old_value == 0:
        return 0.0
    return (new_value - old_value) / abs(old_value)


def round_half_up(value: float, decimals: int = 0) -> float:
    """
    Redondea un número usando la regla del redondeo por mitades hacia arriba.
    
    Args:
        value: Número a redondear
        decimals: Número de decimales (default: 0)
    
    Returns:
        float: Número redondeado
    
    Example:
        >>> round_half_up(1.5)
        2.0
        >>> round_half_up(2.675, 2)
        2.68
    """
    multiplier = 10 ** decimals
    return math.floor(value * multiplier + 0.5) / multiplier


def clamp(value: Union[int, float], min_val: Union[int, float], 
          max_val: Union[int, float]) -> Union[int, float]:
    """
    Limita un valor entre un mínimo y máximo.
    
    Args:
        value: Valor a limitar
        min_val: Valor mínimo
        max_val: Valor máximo
    
    Returns:
        Union[int, float]: Valor limitado
    
    Example:
        >>> clamp(5, 0, 10)
        5
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
    """
    return max(min_val, min(value, max_val))


# =====================================================================
# FUNCIONES DE CONVERSIÓN Y TRANSFORMACIÓN
# =====================================================================

def to_float(value: any, default: float = 0.0) -> float:
    """
    Convierte un valor a float de forma segura.
    
    Args:
        value: Valor a convertir
        default: Valor por defecto si la conversión falla
    
    Returns:
        float: Valor convertido o default
    
    Example:
        >>> to_float("3.14")
        3.14
        >>> to_float("abc", default=0.0)
        0.0
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def to_int(value: any, default: int = 0) -> int:
    """
    Convierte un valor a int de forma segura.
    
    Args:
        value: Valor a convertir
        default: Valor por defecto si la conversión falla
    
    Returns:
        int: Valor convertido o default
    
    Example:
        >>> to_int("42")
        42
        >>> to_int(3.7)
        3
        >>> to_int("abc", default=-1)
        -1
    """
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return default


# =====================================================================
# FUNCIONES DE VALIDACIÓN
# =====================================================================

def is_numeric(value: any) -> bool:
    """
    Verifica si un valor es numérico.
    
    Args:
        value: Valor a verificar
    
    Returns:
        bool: True si es numérico, False en caso contrario
    
    Example:
        >>> is_numeric(42)
        True
        >>> is_numeric("3.14")
        True
        >>> is_numeric("abc")
        False
    """
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def is_empty(value: any) -> bool:
    """
    Verifica si un valor está vacío (None, "", [], etc).
    
    Args:
        value: Valor a verificar
    
    Returns:
        bool: True si está vacío, False en caso contrario
    
    Example:
        >>> is_empty(None)
        True
        >>> is_empty("")
        True
        >>> is_empty([])
        True
        >>> is_empty("datos")
        False
    """
    return value is None or (isinstance(value, (str, list, dict)) and len(value) == 0)

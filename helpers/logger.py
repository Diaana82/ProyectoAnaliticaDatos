"""
logger.py - Módulo de logging y formatting de mensajes para el pipeline.

Proporciona funciones para imprimir títulos, subtítulos, mensajes de éxito,
error e información con formato visual consistente en toda la aplicación.
"""

from typing import Optional


def print_title(text: str) -> None:
    """
    Imprime un título principal con separadores visuales.
    
    Args:
        text: Texto del título a mostrar
    
    Example:
        >>> print_title("ANÁLISIS EXPLORATORIO DE DATOS")
    """
    separator = "=" * 80
    print(f"\n{separator}")
    print(f"{text.center(80)}")
    print(f"{separator}\n")


def print_subtitle(text: str) -> None:
    """
    Imprime un subtítulo con separador inferior.
    
    Args:
        text: Texto del subtítulo a mostrar
    
    Example:
        >>> print_subtitle("Preparación de Datos")
    """
    print(f"\n{'─' * 80}")
    print(f"▶ {text}")
    print(f"{'─' * 80}\n")


def print_success(text: str) -> None:
    """
    Imprime un mensaje de éxito con indicador visual.
    
    Args:
        text: Texto del mensaje de éxito
    
    Example:
        >>> print_success("Datos cargados correctamente")
    """
    print(f"✓ {text}")


def print_error(text: str) -> None:
    """
    Imprime un mensaje de error con indicador visual.
    
    Args:
        text: Texto del mensaje de error
    
    Example:
        >>> print_error("No se encontró el archivo de datos")
    """
    print(f"✗ {text}")


def print_info(text: str, indent: int = 0) -> None:
    """
    Imprime un mensaje de información con indentación opcional.
    
    Args:
        text: Texto del mensaje
        indent: Número de espacios para indentar (default: 0)
    
    Example:
        >>> print_info("Procesando archivo...")
        >>> print_info("Subproceso completado", indent=2)
    """
    spaces = " " * indent
    print(f"{spaces}ℹ {text}")


def print_separator(char: str = "─", length: int = 80) -> None:
    """
    Imprime un separador visual.
    
    Args:
        char: Carácter a usar para el separador (default: "─")
        length: Longitud del separador (default: 80)
    
    Example:
        >>> print_separator()
        >>> print_separator("=", 50)
    """
    print(f"{char * length}")


def print_metric(label: str, value: any, unit: str = "") -> None:
    """
    Imprime una métrica con formato clave-valor.
    
    Args:
        label: Etiqueta de la métrica
        value: Valor de la métrica
        unit: Unidad de medida (opcional)
    
    Example:
        >>> print_metric("Filas procesadas", 1000, "registros")
        >>> print_metric("Precisión", 0.95)
    """
    unit_str = f" {unit}" if unit else ""
    print(f"  • {label}: {value}{unit_str}")

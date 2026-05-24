"""
rutas.py - Módulo para gestionar rutas del proyecto usando pathlib.

Proporciona funciones centralizadas para acceder a directorios clave
como Data y outputs, evitando rutas hardcodeadas en el código.
"""

from pathlib import Path
from typing import Optional


# Ruta base del proyecto (directorio donde está este archivo)
BASE_DIR = Path(__file__).resolve().parent.parent


def get_data_dir() -> Path:
    """
    Obtiene la ruta del directorio de datos (Data/).
    
    Returns:
        Path: Ruta al directorio Data
    
    Example:
        >>> data_dir = get_data_dir()
        >>> df = pd.read_csv(data_dir / "datos.csv")
    """
    return BASE_DIR / "Data"


def get_output_dir() -> Path:
    """
    Obtiene la ruta del directorio de salida (outputs/).
    
    Returns:
        Path: Ruta al directorio outputs
    
    Example:
        >>> output_dir = get_output_dir()
        >>> df.to_csv(output_dir / "resultados.csv")
    """
    return BASE_DIR / "outputs"


def get_eda_output_dir() -> Path:
    """
    Obtiene la ruta del directorio de salida EDA (outputs/eda/).
    
    Returns:
        Path: Ruta al directorio outputs/eda
    
    Example:
        >>> eda_dir = get_eda_output_dir()
        >>> fig.write_html(eda_dir / "grafico.html")
    """
    return get_output_dir() / "eda"


def get_notebooks_dir() -> Path:
    """
    Obtiene la ruta del directorio de notebooks (Notebooks/).
    
    Returns:
        Path: Ruta al directorio Notebooks
    """
    return BASE_DIR / "Notebooks"


def get_skills_dir() -> Path:
    """
    Obtiene la ruta del directorio de skills (Skills/).
    
    Returns:
        Path: Ruta al directorio Skills
    """
    return BASE_DIR / "Skills"


def get_agent_dir() -> Path:
    """
    Obtiene la ruta del directorio de agent (Agent/).
    
    Returns:
        Path: Ruta al directorio Agent
    """
    return BASE_DIR / "Agent"


def get_prompts_dir() -> Path:
    """
    Obtiene la ruta del directorio de prompts (Prompts/).
    
    Returns:
        Path: Ruta al directorio Prompts
    """
    return BASE_DIR / "Prompts"


def get_helpers_dir() -> Path:
    """
    Obtiene la ruta del directorio de helpers (helpers/).
    
    Returns:
        Path: Ruta al directorio helpers
    """
    return BASE_DIR / "helpers"


def get_file_path(directory: str, filename: str) -> Path:
    """
    Obtiene la ruta completa de un archivo en un directorio específico.
    
    Args:
        directory: Nombre del directorio (ej: 'Data', 'outputs', 'outputs/eda')
        filename: Nombre del archivo
    
    Returns:
        Path: Ruta completa al archivo
    
    Example:
        >>> file_path = get_file_path("Data", "datos.csv")
        >>> file_path = get_file_path("outputs/eda", "grafico.html")
    """
    return BASE_DIR / directory / filename


def ensure_path_exists(path: Path) -> None:
    """
    Crea el directorio si no existe.
    
    Args:
        path: Ruta del directorio a crear
    
    Example:
        >>> custom_dir = get_output_dir() / "modelos"
        >>> ensure_path_exists(custom_dir)
    """
    path.mkdir(parents=True, exist_ok=True)


def get_base_dir() -> Path:
    """
    Obtiene la ruta base del proyecto.
    
    Returns:
        Path: Ruta al directorio raíz del proyecto
    """
    return BASE_DIR

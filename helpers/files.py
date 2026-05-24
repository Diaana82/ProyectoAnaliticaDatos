"""
files.py - Módulo para operaciones de archivos y directorios.

Proporciona funciones para crear directorios, limpiar directorios,
listar archivos y otras operaciones comunes con el sistema de archivos.
"""

import shutil
from pathlib import Path
from typing import List, Optional


def create_directory(path: Path) -> Path:
    """
    Crea un directorio si no existe.
    
    Args:
        path: Ruta del directorio a crear
    
    Returns:
        Path: Ruta al directorio creado
    
    Example:
        >>> from pathlib import Path
        >>> output_dir = Path("outputs/analisis")
        >>> create_directory(output_dir)
    """
    path.mkdir(parents=True, exist_ok=True)
    return path


def clean_directory(path: Path) -> None:
    """
    Elimina todos los contenidos de un directorio y lo vuelve a crear vacío.
    
    Args:
        path: Ruta del directorio a limpiar
    
    Raises:
        FileNotFoundError: Si la ruta no existe
    
    Example:
        >>> clean_directory(Path("outputs/eda"))
    """
    if path.exists():
        shutil.rmtree(path)
    create_directory(path)


def remove_directory(path: Path) -> None:
    """
    Elimina un directorio y todo su contenido.
    
    Args:
        path: Ruta del directorio a eliminar
    
    Example:
        >>> remove_directory(Path("outputs/temp"))
    """
    if path.exists():
        shutil.rmtree(path)


def list_files(directory: Path, pattern: str = "*", recursive: bool = False) -> List[Path]:
    """
    Lista archivos en un directorio con patrón opcional.
    
    Args:
        directory: Ruta del directorio
        pattern: Patrón de búsqueda (ej: "*.csv", "*.py")
        recursive: Si es True, busca recursivamente en subdirectorios
    
    Returns:
        List[Path]: Lista de rutas a archivos encontrados
    
    Example:
        >>> files = list_files(Path("Data"), pattern="*.csv")
        >>> all_py_files = list_files(Path("."), pattern="*.py", recursive=True)
    """
    if not directory.exists():
        return []
    
    if recursive:
        return list(directory.rglob(pattern))
    else:
        return list(directory.glob(pattern))


def list_directories(directory: Path) -> List[Path]:
    """
    Lista todos los subdirectorios en un directorio.
    
    Args:
        directory: Ruta del directorio
    
    Returns:
        List[Path]: Lista de rutas a subdirectorios
    
    Example:
        >>> subdirs = list_directories(Path("outputs"))
    """
    if not directory.exists():
        return []
    return [d for d in directory.iterdir() if d.is_dir()]


def file_exists(path: Path) -> bool:
    """
    Verifica si un archivo existe.
    
    Args:
        path: Ruta del archivo
    
    Returns:
        bool: True si existe, False en caso contrario
    
    Example:
        >>> if file_exists(Path("Data/datos.csv")):
        ...     print("El archivo existe")
    """
    return path.is_file()


def directory_exists(path: Path) -> bool:
    """
    Verifica si un directorio existe.
    
    Args:
        path: Ruta del directorio
    
    Returns:
        bool: True si existe, False en caso contrario
    
    Example:
        >>> if directory_exists(Path("outputs")):
        ...     print("El directorio existe")
    """
    return path.is_dir()


def get_directory_size(path: Path) -> int:
    """
    Obtiene el tamaño total de un directorio en bytes.
    
    Args:
        path: Ruta del directorio
    
    Returns:
        int: Tamaño en bytes
    
    Example:
        >>> size = get_directory_size(Path("outputs"))
        >>> print(f"Tamaño: {size} bytes")
    """
    if not path.exists():
        return 0
    
    total_size = 0
    for filepath in path.rglob('*'):
        if filepath.is_file():
            total_size += filepath.stat().st_size
    return total_size


def copy_file(source: Path, destination: Path) -> Path:
    """
    Copia un archivo de origen a destino.
    
    Args:
        source: Ruta del archivo origen
        destination: Ruta del archivo destino
    
    Returns:
        Path: Ruta al archivo copiado
    
    Raises:
        FileNotFoundError: Si el archivo origen no existe
    
    Example:
        >>> copy_file(Path("Data/original.csv"), Path("outputs/backup.csv"))
    """
    if not source.exists():
        raise FileNotFoundError(f"El archivo {source} no existe")
    
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return destination


def move_file(source: Path, destination: Path) -> Path:
    """
    Mueve un archivo de origen a destino.
    
    Args:
        source: Ruta del archivo origen
        destination: Ruta del archivo destino
    
    Returns:
        Path: Ruta al archivo movido
    
    Raises:
        FileNotFoundError: Si el archivo origen no existe
    
    Example:
        >>> move_file(Path("temp.csv"), Path("outputs/procesado.csv"))
    """
    if not source.exists():
        raise FileNotFoundError(f"El archivo {source} no existe")
    
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source), str(destination))
    return destination


def delete_file(path: Path) -> None:
    """
    Elimina un archivo.
    
    Args:
        path: Ruta del archivo a eliminar
    
    Example:
        >>> delete_file(Path("temp/temporal.csv"))
    """
    if path.exists():
        path.unlink()


def get_file_count(directory: Path, pattern: str = "*") -> int:
    """
    Cuenta el número de archivos en un directorio.
    
    Args:
        directory: Ruta del directorio
        pattern: Patrón de búsqueda (default: "*")
    
    Returns:
        int: Número de archivos encontrados
    
    Example:
        >>> count = get_file_count(Path("Data"), pattern="*.csv")
    """
    if not directory.exists():
        return 0
    return len(list(directory.glob(pattern)))


def ensure_unique_filename(path: Path) -> Path:
    """
    Asegura que un nombre de archivo sea único agregando un número si es necesario.
    
    Args:
        path: Ruta del archivo deseado
    
    Returns:
        Path: Ruta con nombre único
    
    Example:
        >>> path = ensure_unique_filename(Path("outputs/resultado.csv"))
        >>> # Si existe, devuelve "resultado (1).csv", luego "resultado (2).csv", etc
    """
    if not path.exists():
        return path
    
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 1
    
    while True:
        new_name = f"{stem} ({counter}){suffix}"
        new_path = parent / new_name
        if not new_path.exists():
            return new_path
        counter += 1

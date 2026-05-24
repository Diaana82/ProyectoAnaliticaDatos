"""
Paquete helpers - Utilidades reutilizables para el pipeline de análisis.

Contiene módulos de logging, gestión de rutas, utilidades generales
y operaciones con archivos.
"""

from . import logger
from . import rutas
from . import utils
from . import files

__version__ = "1.0.0"
__all__ = ["logger", "rutas", "utils", "files"]

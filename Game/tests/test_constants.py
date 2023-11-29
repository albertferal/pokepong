# Contenido de test_constants.py

from .. import constants  # Importa el módulo constants desde el directorio superior

def test_constants_values():
    assert constants.WIDTH > 0  
    assert constants.HEIGHT > 0  

# Contenido de test_main.py

from .. import main  # Importa el módulo main desde el directorio superior

def test_suma():
    assert main.suma(2, 3) == 4

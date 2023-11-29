# Contenido de test_constants.py

from constants import WIDTH, HEIGHT  # Importa las constantes que quieres probar desde constants.py

def test_constants_values():
    assert WIDTH > 0  # Verifica si WIDTH es mayor que cero
    assert HEIGHT > 0  # Verifica si HEIGHT es mayor que cero

# Puedes agregar más pruebas para otras constantes o valores según sea necesario

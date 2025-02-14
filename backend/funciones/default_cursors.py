import ctypes

def restaurar_cursores():
    """Restaura los cursores del sistema a los predeterminados de Windows."""
    print("🔄 Restaurando cursores predeterminados de Windows...")

    # Restaura todos los cursores al valor predeterminado del sistema
    ctypes.windll.user32.SystemParametersInfoW(0x0057, 0, None, 0)

    print("✅ Cursores restaurados correctamente.")

# 📌 Ejecutar la función
restaurar_cursores()

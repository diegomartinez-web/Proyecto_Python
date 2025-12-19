"""
 GENERADOR DE CONTRASEÑAS SEGURAS
Autor: Diego Martínez
Versión: 1.0
"""

import random
import string

def generar_contrasena(longitud=12, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
    """
    Genera una contraseña segura con los parámetros especificados.
    
    Args:
        longitud (int): Longitud de la contraseña (mínimo 8)
        usar_mayusculas (bool): Incluir letras mayúsculas
        usar_numeros (bool): Incluir números
        usar_simbolos (bool): Incluir símbolos especiales
        
    Returns:
        str: Contraseña generada
    """
    # Validar longitud mínima
    if longitud < 8:
        longitud = 8
        print("  Longitud aumentada a 8 (mínimo recomendado)")
    
    # Definir los conjuntos de caracteres
    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase if usar_mayusculas else ""
    numeros = string.digits if usar_numeros else ""
    simbolos = "!@#$%&*+-?" if usar_simbolos else ""
    
    # Combinar todos los caracteres disponibles
    todos_caracteres = letras_minusculas + letras_mayusculas + numeros + simbolos
    
    # Asegurar que hay al menos un carácter de cada tipo seleccionado
    contrasena = []
    
    if letras_minusculas:
        contrasena.append(random.choice(letras_minusculas))
    if letras_mayusculas:
        contrasena.append(random.choice(letras_mayusculas))
    if numeros:
        contrasena.append(random.choice(numeros))
    if simbolos:
        contrasena.append(random.choice(simbolos))
    
    # Completar el resto de la contraseña
    for _ in range(longitud - len(contrasena)):
        contrasena.append(random.choice(todos_caracteres))
    
    # Mezclar los caracteres
    random.shuffle(contrasena)
    
    # Convertir lista a string
    return ''.join(contrasena)

def evaluar_fortaleza(contrasena):
    """
    Evalúa la fortaleza de una contraseña.
    
    Args:
        contrasena (str): Contraseña a evaluar
        
    Returns:
        str: Nivel de fortaleza (Débil, Media, Fuerte, Muy Fuerte)
    """
    longitud = len(contrasena)
    tiene_minusculas = any(c.islower() for c in contrasena)
    tiene_mayusculas = any(c.isupper() for c in contrasena)
    tiene_numeros = any(c.isdigit() for c in contrasena)
    tiene_simbolos = any(c in "!@#$%&*+-?" for c in contrasena)
    
    puntaje = 0
    
    # Puntos por longitud
    if longitud >= 8:
        puntaje += 1
    if longitud >= 12:
        puntaje += 1
    if longitud >= 16:
        puntaje += 1
    
    # Puntos por complejidad
    if tiene_minusculas:
        puntaje += 1
    if tiene_mayusculas:
        puntaje += 1
    if tiene_numeros:
        puntaje += 1
    if tiene_simbolos:
        puntaje += 1
    
    # Determinar nivel de fortaleza
    if puntaje <= 3:
        return "Débil"
    elif puntaje <= 5:
        return "Media"
    elif puntaje <= 7:
        return "Fuerte"
    else:
        return "Muy Fuerte"

def mostrar_ejemplos():
    """
    Muestra ejemplos de contraseñas generadas.
    """
    print("\n" + "="*50)
    print(" EJEMPLOS DE CONTRASEÑAS GENERADAS")
    print("="*50)
    
    # Ejemplo 1: Contraseña básica
    contrasena1 = generar_contrasena(longitud=10, usar_mayusculas=True, usar_numeros=True, usar_simbolos=False)
    fortaleza1 = evaluar_fortaleza(contrasena1)
    print(f"\n1. Contraseña básica (10 caracteres, sin símbolos):")
    print(f"   {contrasena1}")
    print(f"   Fortaleza: {fortaleza1}")
    
    # Ejemplo 2: Contraseña fuerte
    contrasena2 = generar_contrasena(longitud=16, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True)
    fortaleza2 = evaluar_fortaleza(contrasena2)
    print(f"\n2. Contraseña fuerte (16 caracteres, con todo):")
    print(f"   {contrasena2}")
    print(f"   Fortaleza: {fortaleza2}")
    
    # Ejemplo 3: Contraseña numérica
    contrasena3 = generar_contrasena(longitud=8, usar_mayusculas=False, usar_numeros=True, usar_simbolos=False)
    fortaleza3 = evaluar_fortaleza(contrasena3)
    print(f"\n3. Contraseña numérica (8 caracteres, solo números):")
    print(f"   {contrasena3}")
    print(f"   Fortaleza: {fortaleza3}")

def main():
    """
    Función principal que ejecuta el generador.
    """
    print("="*50)
    print(" GENERADOR DE CONTRASEÑAS SEGURAS")
    print("="*50)
    
    # Generar una contraseña con configuración por defecto
    contrasena = generar_contrasena()
    fortaleza = evaluar_fortaleza(contrasena)
    
    print(f"\n Contraseña generada automáticamente:")
    print(f"   {contrasena}")
    print(f"   Longitud: {len(contrasena)} caracteres")
    print(f"   Fortaleza: {fortaleza}")
    
    # Mostrar ejemplos
    mostrar_ejemplos()
    
    print("\n" + "="*50)
    print(" Consejo: Guarda tus contraseñas en un lugar seguro.")
    print("="*50)

if __name__ == "__main__":
    main()
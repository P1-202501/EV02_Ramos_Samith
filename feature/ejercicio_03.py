import logging
import re

def configurar_logger():
    logging.basicConfig(
        filename="intentos_contrasena.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def es_contraseña_valida(contrasena):
    if len(contrasena) < 8:
        logging.error("La contraseña debe tener al menos 8 caracteres.")
        return False, "La contraseña debe tener al menos 8 caracteres."
    if len(re.findall(r"\d", contrasena)) < 2:
        logging.error("La contraseña debe contener al menos dos números.")
        return False, "La contraseña debe contener al menos dos números."
    if not any(c.isupper() for c in contrasena):
        logging.error("La contraseña debe contener al menos una letra mayúscula.")
        return False, "La contraseña debe contener al menos una letra mayúscula."
    return True, "Contraseña válida."

def solicitar_contraseña():
    configurar_logger()
    intentos = 0
    
    while intentos < 3:
        contrasena = input("Ingrese su contraseña: ")
        es_valida, mensaje = es_contraseña_valida(contrasena)
        
        if es_valida:
            logging.info("Contraseña válida.")
            print("[INFO] Contraseña válida")
            return
        else:
            print(f"[ERROR] {mensaje}")
            intentos += 1
            
    print("Demasiados intentos fallidos. Programa terminado.")
    logging.error("Tres intentos fallidos. Programa finalizado.")
    
solicitar_contraseña()




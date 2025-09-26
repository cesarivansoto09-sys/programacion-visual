
import random
import time

# =========================
# 1. Monitoreo de sensores de temperatura
# =========================
def monitoreo_temperatura():
    print("## 1. Monitoreo de sensores de temperatura ##")
    temperaturas_simuladas = [random.randint(50, 100) for _ in range(20)]
    ventilador_encendido = False
    indice = 0

    while indice < len(temperaturas_simuladas):
        temperatura_actual = temperaturas_simuladas[indice]
        print(f"Temperatura actual: {temperatura_actual} °C")

        if temperatura_actual > 70 and not ventilador_encendido:
            print("Ventilador encendido")
            ventilador_encendido = True
        elif temperatura_actual < 65 and ventilador_encendido:
            print("Ventilador apagado")
            ventilador_encendido = False
        else:
            print("Ventilador en funcionamiento")

        estado = "encendido" if ventilador_encendido else "apagado"
        print(f"Estado del ventilador: {estado}")
        indice += 1
        time.sleep(0.3)
    print("\n--- Fin del monitoreo de temperatura ---\n")


# =========================
# 2. Validación de clave de acceso
# =========================
def validacion_clave():
    print("## 2. Validación de clave de acceso ##")
    clave_correcta = [1, 2, 3, 4]
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        clave_ingresada = [random.randint(0, 9) for _ in range(4)]
        print(f"Clave ingresada: {clave_ingresada}")

        if clave_ingresada == clave_correcta:
            print("Acceso concedido ")
            break
        else:
            intentos += 1
            print(f"Clave incorrecta. Intento {intentos} de {max_intentos}")

        if intentos == max_intentos:
            print(" Alarma activada ")
    print("\n--- Fin de validación de clave ---\n")


# =========================
# 3. Adquisición y procesamiento de señales analógicas
# =========================
def adquisicion_voltaje():
    print("## 3. Adquisición y procesamiento de señales analógicas ##")
    dispositivos = 5
    voltages = [round(random.uniform(3.0, 4.2), 2) for _ in range(dispositivos)]

    for i, vol in enumerate(voltages, 1):
        if vol < 3.3:
            print(f"Batería {i}: {vol} V --> Baja")
        elif vol >= 4.0:
            print(f"Batería {i}: {vol} V --> Óptima")
        else:
            print(f"Batería {i}: {vol} V --> Advertencia")
    print("\n--- Fin del procesamiento de voltajes ---\n")


# =========================
# 4. Registro de estados digitales
# =========================
def registro_botones():
    print("## 4. Registro de estados digitales ##")
    botones = [random.choice([True, False]) for _ in range(10)]

    def botones_presionados(botones):
        return [i for i, estado in enumerate(botones) if estado]

    print("Estados de los botones (True=presionado, False=no presionado):")
    print(botones)
    print("Botones presionados en índices:", botones_presionados(botones))
    print("\n--- Fin del registro de botones ---\n")


# =========================
# Menú principal
# =========================
if __name__ == "__main__":
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Monitoreo de sensores de temperatura")
        print("2. Validación de clave de acceso")
        print("3. Adquisición y procesamiento de voltajes")
        print("4. Registro de estados digitales")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            monitoreo_temperatura()
        elif opcion == "2":
            validacion_clave()
        elif opcion == "3":
            adquisicion_voltaje()
        elif opcion == "4":
            registro_botones()
        elif opcion == "5":
            break
        else:
            print("Opción inválida, intente de nuevo.")




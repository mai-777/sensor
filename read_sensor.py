import sqlite3
from serial import Serial

# Conectar o crear la base de datos
bd = sqlite3.connect(
    "sensor.sqlite",
    detect_types=sqlite3.PARSE_DECLTYPES
)
bd.row_factory = sqlite3.Row

# Ejecutar script SQL para crear la tabla, si no existe
with open("sensor.sql") as f:
    bd.executescript(f.read())

# Configurar la conexión con el puerto serie (cambia el puerto según sea necesario)
puerto = Serial("/dev/ttyUSB0", 9600)  # Cambia '/dev/ttyUSB0' por el puerto correcto en tu sistema
puerto.readline()  # Descartar primer renglón

try:
    while True:
        lineaRenglon = puerto.readline().decode().strip()

        try:
            # Asumimos que la línea es un valor numérico simple
            valor = float(lineaRenglon)
            print(valor)

            # Insertar el valor en la base de datos
            bd.execute(
                "INSERT INTO valores (valor_sensor) VALUES (?)",
                (valor,)
            )
            bd.commit()

        except ValueError:
            print(f"Valor inválido: {lineaRenglon}")

except KeyboardInterrupt:
    print('Fin del programa')
    bd.close()

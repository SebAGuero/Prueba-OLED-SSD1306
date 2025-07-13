import machine
import ssd1306
import time

# Inicializar I2C (pines y frecuencia según tu conexión)
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21), freq=400000)

# Crear objeto OLED (128x64, o 128x32 según tu pantalla)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

oled.fill(0)  # limpiar pantalla

oled.text("HOLA MUNDO", 0, 0)
oled.text("Usando libreria", 0, 10)
oled.text("ssd1306 oficial", 0, 20)

oled.show()  # mostrar contenido

# Bucle vacío para mantener encendida la pantalla
while True:
    time.sleep(1)

import time
import board
import adafruit_tcs34725
import explorerhat


i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_tcs34725.TCS34725(i2c)




# Main loop reading color and printing it every second.
while True:

    color = sensor.color
    color_rgb = sensor.color_rgb_bytes
    print(
        "RGB color as 8 bits per channel int: #{0:02X} or as 3-tuple: {1}".format(
            color, color_rgb
        )
    )
    # Read the color temperature and lux of the sensor too.
    temp = sensor.color_temperature
    lux = sensor.lux
    # print("Temperature: {0}K Lux: {1}\n".format(temp, lux))
    # Delay for a second and repeat.
    time.sleep(1.0)

    








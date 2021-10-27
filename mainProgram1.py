import board
import adafruit_tcs34725
import explorerhat
import time


i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_tcs34725.TCS34725(i2c)

button1 = explorerhat.touch.one
button2 = explorerhat.touch.two
button3 = explorerhat.touch.three

sleep_time = 0.1
min_sleep = 0.001

step_sequence = [
[0,1,0,0],
[1,1,0,0],
[1,0,0,0],
[1,0,1,0],
[0,0,1,0],
[0,0,1,1],
[0,0,0,1],
[0,1,0,1]
]

ourColor = ""
ourColor_rgb = ""
color2Right = ""
color2Right_rgb = ""
color2Left = ""
color2Left_rgb = ""

def drive(color):
    while color == ourColor:
        explorerhat.motor.two.forward(70)
        explorerhat.motor.one.backward(70)

    explorerhat.motor.two.stop()
    explorerhat.motor.one.stop()
    
red = False
green = False
blue = False

# Main loop reading color and printing it every second.
while True:
    
    color = sensor.color
    color_rgb = sensor.color_rgb_bytes
    

    if button1.is_pressed():
        print("RGB color as 8 bits per channel int #1: #{0:02X} or as 3-tuple: {1}".format(
                color, color_rgb
            ))
        ourColor = color
        ourColor_rgb = color_rgb
        red = True
        
    elif button2.is_pressed():
        print("RGB color as 8 bits per channel int #2: #{0:02X} or as 3-tuple: {1}".format(
                color, color_rgb
            ))
        color2Right = color
        color2Right_rgb = color_rgb
        green = True
    
    elif button3.is_pressed():
        print("RGB color as 8 bits per channel int #3: #{0:02X} or as 3-tuple: {1}".format(
                color, color_rgb
            ))
        color2Left = color
        color2Left_rgb = color_rgb
        blue = True

    # Read the color temperature and lux of the sensor too.
    temp = sensor.color_temperature
    lux = sensor.lux
    #print("Temperature: {0}K Lux: {1}\n".format(temp, lux))
    # Delay for a second and repeat.

    # if (button1Pressed):
    #     drive(color)

    print("SENSING COLOR: #{0:02X} or as 3-tuple: {1}".format(
                color, color_rgb
            ))
    if red == True:

        if color == ourColor:
            explorerhat.motor.two.forward(60)
            explorerhat.motor.one.backward(60)
            print("OUR COLOR: #{0:02X} or as 3-tuple: {1}".format(
                    color, color_rgb
                ))
        

        elif (int(color_rgb[0]) > 0):
            print("Motor two forward, green")
            explorerhat.motor.one.backward(40)
            explorerhat.motor.two.stop()

        elif (int(color_rgb[2]) > 0):
            print("Motor two stop, blue")
            explorerhat.motor.one.forward(40)
            explorerhat.motor.two.stop()

        else: 
            print(color_rgb[0])
            print(color_rgb[2])
            print("Go in else")
            explorerhat.motor.two.stop()
            explorerhat.motor.one.stop()

    

    time.sleep(1.0)



while True:
    for step in step_sequence:
        for pin in range(4):
            explorerhat.output[pin].write(step[pin])
        time.sleep(sleep_time)
        if sleep_time > min_sleep:
            sleep_time /= 1.1
        print(sleep_time)
        if sleep_time < 0.005:
            explorerhat.motor.two.stop()
            explorerhat.motor.one.stop()
            break

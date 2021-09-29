from gpiozero import Motor
from gpiozero import Robot

motor1 = Motor(4, 14)
motor2 = Motor(17, 27)

# motor1.forward()
# motor2.backward()


motor1.forward(0.5)
motor2.backward(0.5)

# motor1.forward()
# motor2.backward()
# while True:
    # sleep(5)
 #   motor1.reverse()
 #   motor2.reverse()
    
#motor1.stop()
#motor2.stop()

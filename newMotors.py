 import explorerhat, time

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

 while True:
     for step in step_sequence:
         for pin in range(4):
             explorerhat.output[pin].write(step[pin])
         time.sleep(sleep_time)
         if sleep_time > min_sleep:
             sleep_time /= 1.1

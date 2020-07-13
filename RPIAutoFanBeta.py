import RPi.GPIO as GPIO
import time
import tempfile
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, RPi.GPIO.OUT)
while True:
  tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
  cpu_temp =  tempFile.read()
  tempFile.close()
  print (cpu_temp)
  time.sleep(1)
return float(cpu_temp)/1000
system = int(cpu_temp/1000)
if system >=40 :
    GPIO.output(channel,1)
else :
    GPIO.output(channel,0)

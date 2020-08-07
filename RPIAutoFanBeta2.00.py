try:
  import RPi.GPIO as GPIO
  import time
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(10, GPIO.OUT)
  GPIO.setwarnings(False)
  while True:
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    if int(cpu_temp)>40894:
      GPIO.output(10,1)
      print("Wraning!CPU is hot!"+cpu_temp)
    else :
      GPIO.output(10,0)
      print("CPU is okay!"+cpu_temp)
    time.sleep(1)
finally:
  GPIO.cleanup()

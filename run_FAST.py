from serial import Serial
from time import sleep
from subprocess import run

n = '5'
n2 = '6'

while input('Press enter to upload ') == '':
    Serial('COM'+n,baudrate=1200).close()
    sleep(1)
    run(["C:\\Progra~2\\Arduino\\hardware\\tools\\avr/bin/avrdude", "-CC:\\Progra~2\\Arduino\\hardware\\tools\\avr/etc/avrdude.conf", "-v", "-patmega32u4", "-cavr109", "-PCOM"+n2, "-b57600", "-D", "-Uflash:w:C:\\Users\\Hedengren\\Desktop\\Python\\tclab_v2/tclab_v2.ino.hex:i"])
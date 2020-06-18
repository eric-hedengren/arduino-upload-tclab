from serial.tools import list_ports
from subprocess import run
from serial import Serial
import time

x = ' - Arduino Leonardo ('
y = ' - Arduino Leonardo bootloader ('

while True:
    for i in list_ports.comports():
        print('Repeat')
        i = str(i)
        if y in i:
            print('Uploading...')
            time.sleep(1)
            run(["C:\\Progra~2\\Arduino\\hardware\\tools\\avr/bin/avrdude", "-CC:\\Progra~2\\Arduino\\hardware\\tools\\avr/etc/avrdude.conf", "-v", "-patmega32u4", "-cavr109", "-P"+i[:i.index(y)], "-b57600", "-D", "-Uflash:w:C:\\Users\\Hedengren\\Desktop\\Python\\tclab_v2/tclab_v2.ino.hex:i"])
            time.sleep(1)
        elif x in i:
            try:
                # Check for previously uploaded files
                print('Already uploaded files')
            except:
                print('Open and close')
                time.sleep(2)
                Serial(i[:i.index(x)],baudrate=1200).close()
                time.sleep(.5)
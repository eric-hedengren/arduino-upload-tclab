from serial.tools.list_ports import comports
from serial import Serial
from time import sleep
from subprocess import run


# Auto detect all ports to upload, then upload to correct ports

while input('Press enter ') != 'quit':
    port = ("Arduino" in comports())
    Serial('COM'+port[:port.index(" - Arduino")],baudrate=1200).close()
    sleep(1)
    boot_port = ('bootloader' in comports())
    run(["C:\\Progra~2\\Arduino\\hardware\\tools\\avr/bin/avrdude", "-CC:\\Progra~2\\Arduino\\hardware\\tools\\avr/etc/avrdude.conf", "-v", "-patmega32u4", "-cavr109", "-P"+boot_port[:boot_port.index(" - Arduino Leonardo bootloader")], "-b57600", "-D", "-Uflash:w:tclab_v2.ino.hex:i"])
from serial.tools.list_ports import comports
from serial import Serial
from time import sleep
from subprocess import run

arduino = 'Arduino Leonardo ('
arduino_bootloader = 'Arduino Leonardo bootloader ('

while input('Press enter ') != 'quit':
    current_ports = comports()
    open_ports = [i.device for i in current_ports if arduino in i.description]
    for com in open_ports:
        Serial(com,baudrate=1200).close()
        sleep(1)
        upload_port = [i.device for i in comports() if arduino_bootloader in i.description]
        run(["C:\\Progra~2\\Arduino\\hardware\\tools\\avr/bin/avrdude", "-CC:\\Progra~2\\Arduino\\hardware\\tools\\avr/etc/avrdude.conf", "-v", "-patmega32u4", "-cavr109", "-P"+upload_port[0], "-b57600", "-D", "-Uflash:w:tclab_v2.ino.hex:i"])
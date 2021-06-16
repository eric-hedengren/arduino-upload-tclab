from serial.tools.list_ports import comports
from serial import Serial
import subprocess
import time


def bootloader_search():
    for port in comports():
        if port.description.startswith(open_device):
            return port.device


device = 'Arduino Leonardo ('
open_device = 'Arduino Leonardo bootloader ('

avrdude_program = 'C:\\Progra~2\\Arduino\\hardware\\tools\\avr/bin/avrdude'
config_location = '-CC:\\Progra~2\\Arduino\\hardware\\tools\\avr/etc/avrdude.conf'
flash_file = '-Uflash:w:tclab_v2.ino.hex:i'

upload_command = [avrdude_program,config_location,'-v','-patmega32u4','-cavr109',None,'-b57600','-D',flash_file]

port_parameter = '-P{port}'


while True:
    for port in comports():
        if port.description.startswith(device): # and the drive is clean
            Serial(port.device,baudrate=1200).close()

            while bootloader_search() == None:
                continue

            upload_port = bootloader_search()

            upload_command[5] = port_parameter.format(port=upload_port)
            subprocess.check_output(upload_command,shell=True)

            while bootloader_search() != None:
                continue
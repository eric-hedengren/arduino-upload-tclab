import subprocess
from serial import Serial
from serial.tools.list_ports import comports


def bootloader_wanted():
    while True:
        for port in comports():
            if port.description.startswith(open_device):
                return port.device

def bootloader_unwanted():
    while True:
        port_list = []

        for port in comports():
            if port.description.startswith(open_device):
                port_list.append(port.description)
        
        if port_list == []:
            return


avrdude_program = 'C:\\Progra~2\\Arduino\\hardware\\tools\\avr/bin/avrdude'
config_location = '-CC:\\Progra~2\\Arduino\\hardware\\tools\\avr/etc/avrdude.conf'
flash_file = '-Uflash:w:tclab_v2.ino.hex:i'

upload_command = [avrdude_program,config_location,None,'-patmega32u4','-cavr109','-b57600','-D',flash_file]

device = 'Arduino Leonardo ('
open_device = 'Arduino Leonardo bootloader ('

port_parameter = '-P{port}'


while True:
    for port in comports():
        if port.description.startswith(device):
            Serial(port.device,baudrate=1200).close()

            upload_port = bootloader_wanted()

            upload_command[2] = port_parameter.format(port=upload_port)
            subprocess.check_output(upload_command,shell=True)

            bootloader_unwanted()
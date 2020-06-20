from serial.tools.list_ports import comports
from serial import Serial
from subprocess import run
from time import sleep

arduino = 'Arduino Leonardo ('
arduino_bootloader = 'Arduino Leonardo bootloader ('

while True:
    print('Loop')
    for device in comports():

        device = str(device)
        if bootloader in device:
            print('Uploading...')
            com_boot = device[:device.index(bootloader)]
            sleep(1)
            run(["C:\\Progra~2\\Arduino\\hardware\\tools\\avr/bin/avrdude", "-CC:\\Progra~2\\Arduino\\hardware\\tools\\avr/etc/avrdude.conf", "-v", "-patmega32u4", "-cavr109", "-P"+com_boot, "-b57600", "-D", "-Uflash:w:tclab_v2.ino.hex:i"])
            sleep(1)
        elif arduino in device:
            com = device[:device.index(arduino)]
            print(com)
            '''
            try:
                a = Serial(com)
                print('Reeead')
                #a.read()
                print('Gotcha')
                a.close()
                # Check for previously uploaded files
                print('Already uploaded files')
            '''
            #except:
            print('Open and close')
            sleep(2)
            Serial(com,baudrate=1200).close()
            sleep(1)

# Get ports list, find all boot ports and upload, otherwise find all unopened ports and open them. Find a way to check if files have already been uploaded.

while True:
    ports_list = comports()
    boot_ports = [i for i in ports_list if bootloader in i]

    if bootloader in ports:
        boot_com = ports[ports.index(bootloader)]

current_ports = comports()
upload_ports = [i.device for i in current_ports if arduino_bootloader in i.description]
for comport in upload_ports: # multi thread
    run(["C:\\Progra~2\\Arduino\\hardware\\tools\\avr/bin/avrdude", "-CC:\\Progra~2\\Arduino\\hardware\\tools\\avr/etc/avrdude.conf", "-v", "-patmega32u4", "-cavr109", "-P"+comport, "-b57600", "-D", "-Uflash:w:tclab_v2.ino.hex:i"])
open_ports = [i.device for i in current_ports if arduino in i.description]
for comport in open_ports:
    Serial(comport,baudrate=1200).close()
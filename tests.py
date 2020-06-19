from serial.tools.list_ports import comports

arduino = ' - Arduino Leonardo ('

# put comports() into a list

ports_list = list(comports())
print(list(ports_list))
boot_ports = [i for i in ports_list if arduino in i]
print(boot_ports)
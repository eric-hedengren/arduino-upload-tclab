# To Use

Simply run the python program and plug in Arduinos, the code should automatically start uploading the firmware.

# For Arduino Firmware Updates

Use the arduinos desktop app to generate a new ino hex file if want to update the firmware code for your arduino before uploading. If you plug in an arduino and run the code with the app preferences set to show upload details, it will display the location of the cached ino hex file, and this is what avrdude needs to flash to your device. Copy that file to the same folder as the python file that uploads the firmware so the command line can use it, and you're all set.

# LED Indicators

First LED labeled "ON" always stays green if plugged in. 

Second LED labeled "L" blinks yellow slowly if no firmware has been loaded. If firmware has been loaded in the same session, it will be off. If firmware has been loaded but a new session is started, it will stay on. This light will pulse quickly if the device is in bootloader mode.

Third LED labeled "TX" only turns on during firmware uploading.

Fourth LED labeled "RX" blinks once quickly when the device is first plugged in, and lights up during firmware uploading.

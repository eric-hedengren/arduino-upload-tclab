# For Arduino Firmware Updates

Use the arduinos desktop app to generate a new ino hex file if want to update the firmware code for your arduino before uploading. If you plug in an arduino and run the code with the app preferences set to show upload details, it will display the location of the cached ino hex file, and this is what avrdude needs to flash to your device. Copy that file to the same folder as the python file that uploads the firmware so the command line can use it, and you're all set.

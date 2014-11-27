this will contain the library which manages the RFID magic

new RFID().waitForNext

David James Patterson
So - the RFID stuff. Two options.
The option that didn't work for me was this one: http://blog.whaleygeek.co.uk/raspberry-pi-rfid-tag-reader/

This has a pure software I2C package. I didn't work out where you could configure pins and wot not but I imagine it's possible.

Didn't work on my Pi but it's worth a try because if it does work it's easy to set up.

Second option is switching on the I2C driver, rebooting, installing the Quick2Wire python library and wgetting rfid.py of the skpang site: http://skpang.co.uk/blog/archives/946

The board I gave you is an SL030: http://skpang.co.uk/catalog/hf-rfid-module-sl030-33v-i2c-p-1065.html




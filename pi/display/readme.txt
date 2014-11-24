

to install the Display demo. 

git clone https://github.com/embeddedartists/gratis.git

then inside 'PlatformWithOS'
run:

sudo apt-get install libfuse-dev

sudo modprobe spi-bcm2708
COG_VERSION=V2 make rpi-epd_test
sudo ./driver-common/epd_test 2.7

sudo apt-get install python-pip
sudo pip install xhtml2pdf

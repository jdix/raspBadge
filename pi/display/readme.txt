

to install the Display demo. 


sudo apt-get update
sudo apt-get upgrade 

git clone https://github.com/embeddedartists/gratis.git

then inside 'PlatformWithOS'
run:

sudo apt-get install libfuse-dev

sudo modprobe spi-bcm2708
COG_VERSION=V2 make rpi-epd_test
sudo ./driver-common/epd_test 2.7

sudo apt-get install python-pip
sudo apt-get install python-dev

sudo pip install xhtml2pdf
sudo pip install pillow

COG_VERSION=V2 make rpi-epd_fuse
sudo modprobe spi-bcm2708
sudo mkdir /tmp/epd
sudo ./driver-common/epd_fuse --panel=2.7 -o allow_other -o default_permissions /tmp/epd

sudo COG_VERSION=V2 make rpi-install
sudo service epd-fuse start
ls -l /dev/epd

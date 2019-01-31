# CMC BH-30 Controller Menu
This program is for use with a CMC BH-30 HF linear amplifier in an amateur radio application.

It's meant to run on a Raspberry Pi with an LCD display, buttons, and relay board.

The selected relay shorts one of 16 pins to a common pin in order to select the pre-defined "channel" set on the amplifier.

Selecting a band by pressing a button or by using the CLI menu will tell the BH-30 to switch bands.

If the band selected is already the active band, the program will retrieve and display the latest DX spots for that band.

Relay board: https://www.amazon.ca/gp/product/B01BY1693A

Display: https://www.amazon.ca/gp/product/B071FGZX8G

![prototype](https://photos.app.goo.gl/Z58Z2YGjEpCud4iS7)

Quick start:

    sudo apt-get update

    sudo apt-get install git

    sudo apt-get install python3-pip

    sudo pip3 install RPi.GPIO

    sudo pip3 install pytz

    sudo pip3 install requests

    sudo pip3 install xmltodict

    sudo pip3 install rpi-displays

    sudo apt-get install python3-smbus

    sudo pico /etc/modules

    add the following lines:

        i2c-dev

        i2c-bcm2708
        
    sudo raspi-config

        -> Interfacing Options

            -> Enable i2c

    sudo reboot now

    git clone https://github.com/va3dxv/BH30Menu.git

    cd BH30Menu

    ./BH30Menu or ./BH30Menu -cli

More info to come

Brian - VA3DXV

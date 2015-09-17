# Raspi-Plate-Demo

This is an H-Bridge and IR LED Pi Hat for controlling the Rasperry Pi with an IR Remote Control.

The following sites were instrumental in setting up LIRC and having Python interface with it.
* https://piface.github.io/pifacecad/lirc.html
* http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/
* http://ozzmaker.com/2013/10/24/how-to-control-the-gpio-on-a-raspberry-pi-with-an-ir-remote/

This site helped with setting up the Python script to run on boot.
* http://www.raspberrypi-spy.co.uk/2013/07/running-a-python-script-at-boot-using-cron/

The PiHat standard as defined by the Raspberry Pi Foundation
* https://github.com/raspberrypi/hats

All of the Python code was made to run under Python3 however it's likely that it will run under Python2 since the python-lirc library works in both versions of Python.

The EAGLE design files were made using V7 of EAGLE. The PiHat_Standard_Outline.lbr contains packages that conform to the PiHat standard.

For any questions or concerns contact support@cadsoftusa.com or call 954-237-0932.

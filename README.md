Location Tracking with WIFI
=======

This project will track the location of a WIFI receiver. Think if a machine includes a WIFI module, we can use this project to locate it in a 2D space. For ths feature, it includes two part:

1. Obtain the WIFI signal strength of a WIFI receiver. This part is sourced from [PyWiWiProject](https://github.com/6e726d/PyWiWi). It is a straightforward project to gain WIFI signal strength by Windows native API. We choose this it just for the easy demo purpose. 
2. A trilateration algorithm to calculate location coordinate by determining the distance 

Setup
=======

This will work in Windows 7, please:

1. Install the Python 2.7 in your OS. Then, download Comtypes from: [Comtypes-1.1.1](https://pypi.python.org/packages/source/c/comtypes/comtypes-1.1.1.zip#md5=4591233e932bed92fc7a09084b240199)
2. Unzip Comtypes and run:  `python setup.py install ` to install Comtypes
3. CD to example folder, and run:  `python list_networks_signal.py `

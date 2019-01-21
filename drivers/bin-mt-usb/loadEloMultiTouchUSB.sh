#! /bin/sh

# Create Elo Devices for communication
/etc/opt/elo-mt-usb/eloCreateFifo.sh

# Load the Elo kernel module [input device driver]
/sbin/insmod /etc/opt/elo-mt-usb/elo_mt_input_mod_`uname -r`.ko 

# Load the PC speaker kernel module into memory for Beep-On-Touch 
#modprobe pcspkr
sleep 1

# Load the Elo USB Touchscreen Daemon into memory
/etc/opt/elo-mt-usb/elomtusbd

# dec82

To set up the development environment install [`abcli`](https://github.com/kamangir/awesome-bash-cli), then open a terminal and type in,

```bash
# dev
abcli git clone dec82 install
```

To build the hardware, follow [these instructions](https://github.com/kamangir/blue-bracket/blob/main/designs/dec82.md). 

| ![image](https://github.com/kamangir/blue-bracket/raw/main/images/dec82-7.jpg) | ![image](https://github.com/kamangir/blue-bracket/raw/main/images/dec82-6.jpg) |
|---|---| 

To install the software, follow [these instructions](https://github.com/kamangir/awesome-bash-cli/wiki/Raspberry-Pi) to set up a headless Raspberry Pi w/ [`abcli`](https://github.com/kamangir/awesome-bash-cli) enabled. Then. in your development environment, open a terminal and type in,

```bash
# dev
abcli ssh rpi <rpi-hostname>

# rpi
abcli cookie copy dec82q # or dec82
abcli init

sudo raspi-config
# Interface Options -> Camera -> Yes
# Interface Options -> I2C -> Yes
# Interface Options -> SSH -> Yes
# System Options -> Boot / Auto Login -> Console Autologin
# Reboot.
```


To interact w/ the device, press and hold the button for less than `3 s` to take a picture and more than `10 s` to shut down the device. Hold more than `3 s` and less than `10 s` initiates an update and reboot of the application.
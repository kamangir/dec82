# dec82

A wearable Raspberry Pi + Grove + Camera.

## Dev Env Set-up


On a Mac or Linux machine install [`abcli`](https://github.com/kamangir/awesome-bash-cli). Then open a terminal and type in,

```bash
abcli git clone dec82 install
```

## Hardware Build

![20221113_141520](https://user-images.githubusercontent.com/1007567/201549578-87e6f84c-6c79-4a4b-8fd1-343c3ed77519.jpg)

Details coming soon to [blue brackets](https://github.com/kamangir/blue-bracket). 🚧 

## Hardware Setup

Follow the [instructions to set up a headless Raspberry Pi](https://github.com/kamangir/awesome-bash-cli/wiki/Raspberry-Pi) w/ [`abcli`](https://github.com/kamangir/awesome-bash-cli).

Open a terminal and type in,

```bash
# ssh
abcli ssh rpi <machine-name>

# rpi
abcli cookie copy dec82
abcli init
sudo raspi-config
# enable camera and I2C, reboot, and ssh back in.
dec82 validate_hardware
```

🚧
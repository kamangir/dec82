# dec82

A wearable Raspberry Pi + Grove + Camera.

## Dev Env Set-up


On a Mac or Linux machine install [`abcli`](https://github.com/kamangir/awesome-bash-cli). Then open a terminal and type in,

```bash
abcli git clone dec82 install
```

## Hardware Build

| ![20221113_141520](https://user-images.githubusercontent.com/1007567/201549578-87e6f84c-6c79-4a4b-8fd1-343c3ed77519.jpg) | ![20221106_195914](https://user-images.githubusercontent.com/1007567/202607615-5cb500eb-8d54-4eaf-95f0-0488146c91ad.jpg) | ![20221117_074952](https://user-images.githubusercontent.com/1007567/202607628-b3008f70-5a7f-4df6-81fa-0ddd3a65fed4.jpg) |
|---|---|---|


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

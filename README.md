# dec82

To set up the development environment install [`abcli`](https://github.com/kamangir/awesome-bash-cli), then open a terminal and type in,

```bash
# dev
abcli git clone dec82 install
```

![image](https://github.com/kamangir/blue-bracket/raw/main/images/dec82-1.jpg)

To build the hardware, follow [these instructions](https://github.com/kamangir/blue-bracket/blob/main/designs/dec82.md). Then follow [these instructions](https://github.com/kamangir/awesome-bash-cli/wiki/Raspberry-Pi) to set up a headless Raspberry Pi w/ [`abcli`](https://github.com/kamangir/awesome-bash-cli) enabled.

In your development environment, open a terminal and type in,

```bash
# dev
abcli ssh rpi <rpi-hostname>

# rpi
abcli cookie copy dec82
abcli init

sudo raspi-config
# enable camera and I2C, reboot, and ssh back in.

grove validate button
grove validate oled_128x64
```

![image](https://user-images.githubusercontent.com/1007567/204118904-fc9a3173-1e1d-42e2-af21-eb2e1947d965.png)

🚧

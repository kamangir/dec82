# dec82

To install the development environment install [`abcli`](https://github.com/kamangir/awesome-bash-cli), then open a terminal and type in,

```bash
abcli git clone dec82 install
```

| ![20221113_141520](https://user-images.githubusercontent.com/1007567/201549578-87e6f84c-6c79-4a4b-8fd1-343c3ed77519.jpg) | ![20221106_195914](https://user-images.githubusercontent.com/1007567/202607615-5cb500eb-8d54-4eaf-95f0-0488146c91ad.jpg) | ![20221117_074952](https://user-images.githubusercontent.com/1007567/202607628-b3008f70-5a7f-4df6-81fa-0ddd3a65fed4.jpg) |
|---|---|---|

To build the hardware, follow [these instructions](https://github.com/kamangir/blue-bracket/blob/main/designs/dec82.md). Then follow [these instructions](https://github.com/kamangir/awesome-bash-cli/wiki/Raspberry-Pi) to set up a headless Raspberry Pi w/ [`abcli`](https://github.com/kamangir/awesome-bash-cli) enabled.

In your development environment, open a terminal and type in,

```bash
# ssh
abcli ssh rpi <rpi-hostname>

# rpi
abcli cookie copy dec82
abcli init

sudo raspi-config
# enable camera and I2C, reboot, and ssh back in.

grove validate button
```

🚧
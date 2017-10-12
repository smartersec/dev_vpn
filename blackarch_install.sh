#!/bin/bash
pacman -Sy && pacman -S encfs --noconfirm && pacman -S figlet --noconfirm && pacman -S surf --noconfirm && pacman -S speedtest-cli --noconfirm
chmod +x patvpn.py
./patvpn.py

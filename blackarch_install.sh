#!/bin/bash
pacman -Sy && pacman -S shadowsocks-libev --noconfirm && pacman -S encfs --noconfirm && pacman -S figlet --noconfirm && pacman -S surf --noconfirm && pacman -S speedtest-cli --noconfirm
chmod +x patvpn.py
ln -s /root/PatriotVPN/patvpn.py /usr/bin/patvpn
patvpn

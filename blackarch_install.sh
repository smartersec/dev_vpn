#!/bin/bash
pacman -Sy && pacman -S shadowsocks-libev --noconfirm && pacman -S encfs --noconfirm && pacman -S figlet --noconfirm && pacman -S surf --noconfirm && pacman -S speedtest-cli --noconfirm
chmod +x patvpn-blackarch.py
ln -s /root/PatriotVPN/patvpn-blackarch.py /usr/bin/patvpn
echo 'socks5   127.0.0.1   1080' >> /etc/proxychains.conf
patvpn

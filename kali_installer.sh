#!/bin/bash
apt-get update && apt-get install shadowsocks-libev encfs figlet surf speedtest-cli -y
chmod +x patvpn-blackarch.py
ln -s /root/PatriotVPN/patvpn-blackarch.py /usr/bin/patvpn
echo 'socks5   127.0.0.1   1080' >> /etc/proxychains.conf
patvpn

#!/usr/bin/env python2
import sys
import subprocess
import time
import os
import json
import getpass

def lsconf():
    subprocess.call(['ls', 'patvpn/'])

def connect():
    os.system('ls patvpn/')
    conf = raw_input('Choose a connection: ')
    os.system('ss-local -c ~/patvpn/%s.json'% conf) 


def cont():
    con = raw_input('Hit any key to continue or n + enter to exit...')
    if con == 'n':
        sys.exit(1)
    
def show_ip():
    print 'Your current IP address info is:\r\n'
    os.system('proxychains curl ipinfo.io')

def ip_leak():
    print 'Checking ipleak.net for DNS leaks...'
    time.sleep(2)
    os.system('proxychains surf ipleak.net')

def speed():
    os.system('proxychains speedtest')

def enc():
    print 'Setting up encrypted file system....'
    os.system('encfs ~/.patvpn ~/patvpn')
    os.system('ls -a ~/patvpn')

def umnt():
    print 'Unmounting encrypted file system....'
    os.system('fusermount -u ~/patvpn')
    os.system('ls -a ~/patvpn')

def create_conf():
    nme = raw_input('Config file name:')
    srv_ip = raw_input('Server IP address:')
    lcl_pt = raw_input('Local port:')
    passw = getpass.getpass('Enter the VPN password:')
    with open("~/patvpn/%s.json" % nme, "w") as outfile:
        json.dump({"server":"%s" % srv_ip, "server_port":31333, "local_address":"127.0.0.1", "local_port":"%s" % int(lcl_pt), "password":"%s" % passw, "timeout":300, "method":"aes-256-cfb", "fast_open":False}, outfile, indent=4)



def main():
    while True:
        os.system('clear')
        print '\r\n\r\n'
        subprocess.call(['figlet', '-cf', 'usaflag', 'Patriot VPN'])
        print """
              ------------------------------------------------------\r\n
              [1] Create configs
              [2] List configs
              [3] Connect to Patriot VPN
              [4] Show your Patriot VPN IP address
              [5] Check ipleak.net
              [6] Check VPN speed through speedtest.net
              [7] Set up encrypted file system
              [8] Unmount encrypted file system
              [0] Exit

              """
        op = raw_input('Pick an option:')
        if op == '1':
            create_conf()
            cont()
        elif op == '2':
            lsconf()
            cont()
        elif op == '3':
            connect()
            cont()
        elif op == '4':
            show_ip()
            cont()
        elif op == '5':
            ip_leak()
            cont()
        elif op == '6':
            speed()
            cont()
        elif op == '7':
            enc()
            cont()
        elif op == '8':
            umnt()
            cont()
        elif op == '0':
            sys.exit(1)
        else:
            continue


if __name__ == '__main__':
    main()

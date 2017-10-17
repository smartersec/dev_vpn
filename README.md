# PatriotVPN
An extremely fast, end-to-end encrypted SOCKS5 proxy based on [Shadowsocks][1]

[1]:<https://github.com/shadowsocks/shadowsocks/tree/master> "Shadowsocks github repo"

#### Dependencies:
##### Install shadowsocks-libev, surf, encfs, speedtest-cli, proxychains
    sudo apt-get install shadowsocks-libev surf encfs speedtest-cli proxychains
    
##### In Arch:
        sudo pacman -S shadowsocks-libev surf encfs speedtest-cli proxychains

##### Edit /etc/proxychains.conf as follows:

    # proxychains.conf  VER 4.x
    #
    #        HTTP, SOCKS4a, SOCKS5 tunneling proxifier with DNS.


    # The option below identifies how the ProxyList is treated.
    # only one option should be uncommented at time,
    # otherwise the last appearing option will be accepted
    #
    #dynamic_chain
    #
    # Dynamic - Each connection will be done via chained proxies
    # all proxies chained in the order as they appear in the list
    # at least one proxy must be online to play in chain
    # (dead proxies are skipped)
    # otherwise EINTR is returned to the app
    #
    strict_chain
    #
    # Strict - Each connection will be done via chained proxies
    # all proxies chained in the order as they appear in the list
    # all proxies must be online to play in chain 
    # otherwise EINTR is returned to the app
    #
    #round_robin_chain
    #
    # Round Robin - Each connection will be done via chained proxies
    # of chain_len length
    # all proxies chained in the order as they appear in the list
    # at least one proxy must be online to play in chain
    # (dead proxies are skipped).
    # the start of the current proxy chain is the proxy after the last
    # proxy in the previously invoked proxy chain.
    # if the end of the proxy chain is reached while looking for proxies
    # start at the beginning again.
    # otherwise EINTR is returned to the app
    # These semantics are not guaranteed in a multithreaded environment.
    #
    #random_chain
    #
    # Random - Each connection will be done via random proxy
    # (or proxy chain, see  chain_len) from the list.
    # this option is good to test your IDS :)

    # Make sense only if random_chain or round_robin_chain
    #chain_len = 2

    # Quiet mode (no output from library)
    quiet_mode

    # Proxy DNS requests - no leak for DNS data
    proxy_dns

    # set the class A subnet number to use for the internal remote DNS mapping
    # we use the reserved 224.x.x.x range by default,
    # if the proxified app does a DNS request, we will return an IP from that range.
    # on further accesses to this ip we will send the saved DNS name to the proxy.
    # in case some control-freak app checks the returned ip, and denies to
    # connect, you can use another subnet, e.g. 10.x.x.x or 127.x.x.x.
    # of course you should make sure that the proxified app does not need
    # *real* access to this subnet.
    # i.e. dont use the same subnet then in the localnet section
    #remote_dns_subnet 127
    #remote_dns_subnet 10
    remote_dns_subnet 224

    # Some timeouts in milliseconds
    tcp_read_time_out 15000
    tcp_connect_time_out 8000

    ### Examples for localnet exclusion
    ## localnet ranges will *not* use a proxy to connect.
    ## Exclude connections to 192.168.1.0/24 with port 80
    # localnet 192.168.1.0:80/255.255.255.0

    ## Exclude connections to 192.168.100.0/24
    # localnet 192.168.100.0/255.255.255.0

    ## Exclude connections to ANYwhere with port 80
    # localnet 0.0.0.0:80/0.0.0.0

    ## RFC5735 Loopback address range
    ## if you enable this, you have to make sure remote_dns_subnet is not 127
    ## you'll need to enable it if you want to use an application that
    ## connects to localhost.
    localnet 127.0.0.0/255.0.0.0

    ## RFC1918 Private Address Ranges
    # localnet 10.0.0.0/255.0.0.0
    # localnet 172.16.0.0/255.240.0.0
    # localnet 192.168.0.0/255.255.0.0

    # ProxyList format
    #       type  ip  port [user pass]
    #       (values separated by 'tab' or 'blank')
    #
    #       only numeric ipv4 addresses are valid
    #
    #
    #        Examples:
    #
    #               socks5  192.168.67.78   1080    lamer   secret
    #               http    192.168.89.3    8080    justu   hidden
    #               socks4  192.168.1.49    1080
    #               http    192.168.39.93   8080
    #
    #
    #       proxy types: http, socks4, socks5
    #        ( auth types supported: "basic"-http  "user/pass"-socks )
    #
    [ProxyList]
    # add proxy here ...
    # meanwile
    # defaults set to "tor"
    #socks4         127.0.0.1 9051
    socks5  127.0.0.1 1080

##### Save and exit.

##### Change the script to an executable:
    chmod +x patvpn.py
    
##### Create a symlink to /usr/bin
    ln -s /path/to/patvpn.py /usr/bin/patvpn
    
##### Run PatriotVPN
    patvpn
    
##### When you see the menu, hit option 7 to create the encrypted file system, answer 'y' to create both folders necessary, choose "p" for pre-configured paranoia mode, create a passphrase for the encrypted file system. Hit any key to continue.

```diff
- NOTE: Encfs does NOT encrypt your traffic. 
It only provides an encrypted container to store your 
configs and other things you might want to keep in 
the folder. Just be sure to point your browsers 
download location to that folder.
```

##### Pick option 1 to initialize the configs, then enter the server information noted in the install guide(beta-testers)

##### Pick option 3 then enter 
    pat 
##### to connect

##### Check your connection with 
    proxychains curl ipinfo.io
    
##### in another terminal, or pick option 5 to check for DNS leaks




#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(' [+] %d/tcp Open') % tgtPort
    except:
        print('[-] %d/tcp Closed') % tgtPort
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('Unknown Host %s ') %tgtHost
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('[+] Scan Results for: ') + tgtName[0]
    except:
        print('[+] Scan Results For ') + tgtIP
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    print("""
          _____                _____                    _____                    _____                    _____                                  
         /\    \              |\    \                  /\    \                  /\    \                  /\    \                 ______          
        /::\    \             |:\____\                /::\    \                /::\____\                /::\    \               |::|   |         
       /::::\    \            |::|   |               /::::\    \              /:::/    /               /::::\    \              |::|   |         
      /::::::\    \           |::|   |              /::::::\    \            /:::/    /               /::::::\    \             |::|   |         
     /:::/\:::\    \          |::|   |             /:::/\:::\    \          /:::/    /               /:::/\:::\    \            |::|   |         
    /:::/__\:::\    \         |::|   |            /:::/__\:::\    \        /:::/____/               /:::/__\:::\    \           |::|   |         
   /::::\   \:::\    \        |::|   |           /::::\   \:::\    \      /::::\    \              /::::\   \:::\    \          |::|   |         
  /::::::\   \:::\    \       |::|___|______    /::::::\   \:::\    \    /::::::\    \   _____    /::::::\   \:::\    \         |::|   |         
 /:::/\:::\   \:::\____\      /::::::::\    \  /:::/\:::\   \:::\____\  /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \  ______|::|___|___ ____ 
/:::/  \:::\   \:::|    |    /::::::::::\____\/:::/  \:::\   \:::|    |/:::/  \:::\    /::\____\/:::/  \:::\   \:::\____\|:::::::::::::::::|    |
\::/    \:::\  /:::|____|   /:::/~~~~/~~      \::/   |::::\  /:::|____|\::/    \:::\  /:::/    /\::/    \:::\  /:::/    /|:::::::::::::::::|____|
 \/_____/\:::\/:::/    /   /:::/    /          \/____|:::::\/:::/    /  \/____/ \:::\/:::/    /  \/____/ \:::\/:::/    /  ~~~~~~|::|~~~|~~~      
          \::::::/    /   /:::/    /                 |:::::::::/    /            \::::::/    /            \::::::/    /         |::|   |         
           \::::/    /   /:::/    /                  |::|\::::/    /              \::::/    /              \::::/    /          |::|   |         
            \::/____/    \::/    /                   |::| \::/____/               /:::/    /               /:::/    /           |::|   |         
             ~~           \/____/                    |::|  ~|                    /:::/    /               /:::/    /            |::|   |         
                                                     |::|   |                   /:::/    /               /:::/    /             |::|   |         
                                                     \::|   |                  /:::/    /               /:::/    /              |::|   |         
                                                      \:|   |                  \::/    /                \::/    /               |::|___|         
                                                       \|___|                   \/____/                  \/____/                 ~~              
                                                                                                                                                 
    """)
    parser = optparse.OptionParser('Usage of program: ' + '-H < target host > -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='Specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='Specify target ports seperated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()

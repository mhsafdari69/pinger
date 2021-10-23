'''
TODO ist bei lines 20 21 soll dir Argumente, die wir zu curl passen, richtig werden
und der String mit formatierung soll auch korrigiert werden.
der restliche code auf Zeile 47 soll auch geschriebe werden.

'''
import ipaddress
import platform  
import subprocess
import argparse

def ping (host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command)==0 

def pinger(start_ip, end_ip=None):
    start_ip = ipaddress.IPv4Address(start_ip)
    if end_ip :
        end_ip = ipaddress.IPv4Address(end_ip)
        for ip_int in range(int(start_ip), int(end_ip)):
            res = ping(str(ipaddress.IPv4Address(ip_int)))
            # TODO print(f"curl ipinfo.io/%i/geo?token=$TOKEN",ip_int)
            # TODO subprocess.call(f"curl ipinfo.io/%f/geo?token=$TOKEN",str(ipaddress.IPv4Address(ip_int)))
    else:
            res = ping(str(ipaddress.IPv4Address(start_ip)))
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='pinger is a python software to if a server is up or down.'
    +'You can with pinger checke a range of ip to find out which one is up or down')
    parser.add_argument('-r',help='to scan a range of ip.')
    parser.add_argument('-o',help='to scan just one ip.')
    args = parser.parse_args()
    if (args.r == None or args.o == None):
        print('\n\n------------------------------------ pinger -----------------------------------------\n')
        print('pinger is a python software to if a server is up or down.\n'
    +'You can with pinger checke a range of ip to find out which one is up or down \n')
        command = input('What do you want to scan a range of IP (r) or just one IP (o): ')
        if command == 'r':
            start_ip = input('start IP: ')
            end_ip = input ('end IP: ')
            pinger(start_ip, end_ip)
        
        if command == 'o':
            start_ip = input('IP: ')
            pinger(start_ip)
    #else:

#! /usr/bin/env python3
import sys
import argparse
import bjoern
from qxn.wsgi import application



def get_ip(parser, ip_port):
    loc, port = ip_port.rsplit(':', 1)
    def perror(err):
        print('\n\033[1;31m', 'Error: ', err, '\033[0m', sep='', end='\n\n')
        parser.print_help()
        print()
        sys.exit(1)
    try:
        port = int(port)
    except:
        perror('port number must be an number, try 8080, 9090')
    if 80 > port or port > 65535:
        perror('port number must be within [80-65535] range')
    if ':' in loc:
        #bjoern doesn't support ipv6 yet
        perror('ipv6 is not supported')
    return (loc, port)

    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--unix',
                       help='unix socket address, examples: @myunix /tmp/myunix')
    group.add_argument('-i', '--ipaddress-port',
                       help='ipv4:port of listening , examples: 127.0.0.1:1234, localhost:1234')
    args = parser.parse_args()
    
    if args.unix:
        loc = 'unix:' + args.unix
        port = None
    else:
        loc, port = get_ip(parser, args.ipaddress_port)
    sock = bjoern.bind_and_listen(loc, port, True)

    print()
    print('\033[1;32m', 'Server listening on ', sep='',  end='')

    if port:
        print('\033[1;34m', 'http://%s:%s' % (loc,port), sep='')
    else:
        print('\033[1;35m', loc, sep='')

    print('\033[0m')
    bjoern.server_run(sock, application)
        

    
    
    
    



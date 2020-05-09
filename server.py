#!/usr/bin/env python3


if __name__ != '__main__':
    raise Exception('Please try running this file as a script instead.')


from argparse import ArgumentParser
from http.server import SimpleHTTPRequestHandler

from os import getcwd
from os import chdir
from os.path import basename

from socketserver import TCPServer
from sys import argv


cwd = getcwd()

arg_parser = ArgumentParser(
    prog = basename(argv[0]),
    usage = '%(prog)s --address "localhost" --port "8080"',
    epilog = 'For more projects see: https://github.com/S0AndS0')


arg_parser.add_argument('--address', '--ip',
                        help = 'Local IP address to bind/listen for connections on',
                        required = False,
                        default = '127.0.0.1')


arg_parser.add_argument('--directory',
                        help = '',
                        required = False,
                        default = cwd)

arg_parser.add_argument('--port',
                        help = 'Local port number to bind/listen for connections on',
                        required = False,
                        default = 8080,
                        type = int)


args = vars(arg_parser.parse_args())


Warning('http.server is not recommended for production. It only implements basic security checks.')
if args['directory'] is not cwd:
    chdir(args['directory'])


with TCPServer(
    server_address = (args['address'], args['port']),
    RequestHandlerClass = SimpleHTTPRequestHandler
) as httpd:
    httpd.serve_forever()

import os, argparse
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer


def open_http(host, port, directory):
    
    web_path = os.path.abspath(directory)
    os.chdir(web_path)

    protocol = "HTTP/1.0"

    SimpleHTTPRequestHandler.protocol_version = protocol
    httpd = BaseHTTPServer.HTTPServer((host, port), SimpleHTTPRequestHandler)

    sa = httpd.socket.getsockname()
    print "Serving HTTP for ", web_path, " at ", host, ":", port, "..."
    
    try:    
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.socket.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--host', default='127.0.0.1', help='The host for the server.')
    parser.add_argument('-p', '--port', type=int, default=7001, help='The port to serve HTTP on.')
    parser.add_argument('-d', '--dir', default='./', help='The directory that holds the contents of the site.')

    args = parser.parse_args()

    open_http(args.host, args.port, args.dir)

if __name__ == "__main__":
    main()

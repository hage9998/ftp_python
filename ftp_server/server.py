import logging
import sys

from pyftpdlib.handlers import FTPHandler
# servidor normal
#from pyftpdlib.servers import FTPServer
# servidor multiprocesso
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
import os
def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # anonymous user
    authorizer.add_anonymous(os.getcwd(), perm='elradfmwM')

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.permit_foreign_addresses = True

    # Instantiate FTP server class and listen on 0.0.0.0:21
    address = ('127.0.0.1', 21)
    server = FTPServer(address, handler)

    # start ftp server
    server.serve_forever() 

if __name__ == "__main__":
    main()
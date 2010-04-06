""" defines the serverConnectionDaemon
"""
import threading
import socket
import time

import ircparse as parse


CONNECTIONS = {}

class ServerConnectionDaemon(threading.Thread):
    """Opens connections to servers and polls for events
    on the socket object
    """

    def __init__(self):
        """
        """
        threading.Thread.__init__(self)

    def run(self):
        """
        Arguments:
        - `self`:
        """
        while 1:
            time.sleep(1)
            #goes through connections and calls ircParse's
            #on them, returning an Event object, or None            
            events = map(lambda x:parse.process_data(x), CONNECTIONS.items())
            events = filter(lambda x:x!=None, events)
            for e in events:
                e.printC()

def connect_to_server(nick, connection, server_address,
                          password=None, port=6667):
    """
    Arguments:
    - nick : The nick you wish to connect with
    - connection : the socket object wishing to establish a connection
    - server_address : the address of the external server
    - password: password on the receiving server
    - port: port with which you wish to connect
    """
    #TODO Write messages to send
    #nick password and identifing information to IRC
    #TODO Error checking/exception handling
    tmp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tmp.connect((server_address, port))
    
    CONNECTIONS[tmp] = connection
    return tmp

def get_connection(self, nick):
    '''
    Return the connection object so that ORCBot can store it in it's validated
    user dictionary.
    '''
    #TODO: Write this function
    return "aConnectionObject"

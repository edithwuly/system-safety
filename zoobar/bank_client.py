from flask import g, render_template, request
from debug import *
import os
import rpclib
import sys

sys.path.append(os.getcwd())
import readconf

@catch_err
def init(username):
    host = readconf.read_conf().lookup_host('bank')
    with rpclib.client_connect(host) as c:
        return c.call('init', username = username)

def transfer(sender, recipient, zoobars, token):
    host = readconf.read_conf().lookup_host('bank')
    with rpclib.client_connect(host) as c:
        return c.call('transfer', sender = sender, recipient = recipient, zoobars = zoobars, token = token)

def balance(username):
    host = readconf.read_conf().lookup_host('bank')
    with rpclib.client_connect(host) as c:
        return c.call('balance', username = username)

def get_log(username):
    host = readconf.read_conf().lookup_host('bank')
    with rpclib.client_connect(host) as c:
        return c.call('get_log', username = username)

        

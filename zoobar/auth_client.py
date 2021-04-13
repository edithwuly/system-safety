from debug import *
from zoodb import *
import rpclib

sys.path.append(os.getcwd())
import readconf

def login(username, password):
    ## Fill in code here.
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        return c.call('login', username = username, password = password)

def register(username, password):
    ## Fill in code here.
    pdb = person_setup()
    person = pdb.query(Person).get(username)
    if person:
        return None
    newperson = Person()
    newperson.username = username
    pdb.add(newperson)
    pdb.commit()

    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        return c.call('register', username = username, password = password)

def check_token(username, token):
    ## Fill in code here.
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        return c.call('check_token', username = username, token = token)

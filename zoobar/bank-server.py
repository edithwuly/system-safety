#!/usr/bin/env python3
#
# Insert bank server code here.
#
import rpclib
import sys
import bank
from debug import *
import auth_client

class BankRpcServer(rpclib.RpcServer):
    ## Fill in RPC methods here.
    ## pass
    def rpc_init(self, username):
        return bank.init(username)

    def rpc_transfer(self, sender, recipient, zoobars, token):
        if not auth_client.check_token(sender, token) and self.caller != 'profile':
            raise PermissError()
        return bank.transfer(sender, recipient, zoobars, token)

    def rpc_balance(self, username):
        return bank.balance(username)

    def rpc_get_log(self, username):
        return bank.get_log(username)

s = BankRpcServer()
s.run_fork(sys.argv[1])

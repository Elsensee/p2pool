import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fdb6a5db'.decode('hex')
P2P_PORT = 11310
ADDRESS_VERSION = 112
RPC_PORT = 11311
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'netcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1024*320636160 >> (height + 1)//129600
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'NET'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'NetCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/NetCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.netcoin'), 'netcoin.conf')
BLOCK_EXPLORER_URL_PREFIX='http://explorer.netcoinfoundation.org/block/'
ADDRESS_EXPLORER_URL_PREFIX='http://explorer.netcoinfoundation.org/address/'
TX_EXPLORER_URL_PREFIX='http://explorer.netcoinfoundation.org/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8

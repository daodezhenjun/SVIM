

from collections import namedtuple

Svi_sample = namedtuple('Svi_sample', ['iv', 'k'])
Svi_param = namedtuple('Svi_param',['a','b','rho','m','sigma'])
Quote = namedtuple('Quote',['optionPrice','strike','T','optionType'])
Option_quote=namedtuple('Option_quote',['cnt_name','last_price','volume',  'bid_price1',  'bid_vol1','ask_price1', 'ask_vol1','time','millisec'])


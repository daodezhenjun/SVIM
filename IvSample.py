# coding=utf-8

import BSM
import math
from myglobal import *

class OptionCnt:
    option_type = None
    strike = None

    quote = None

    future_price = None
    mature_date = None
    today = None
    param_t = None
    interest = None

    iv = None
    spread_threshold = None

    def __init__(self, option_type, strike):
        self.option_type = option_type
        self.strike = strike

    def set_param(self, spread_threshold, interest, t):
        self.spread_threshold = spread_threshold
        self.interest = interest
        self.param_t = t

    def update(self, quote):
        self.quote = quote
        if self.future_price and self.strike and self.option_type and self.interest and self.param_t:
            self.iv = self.get_iv()
        else:
            print "OptionCnt have none: ", self.future_price, " ", self.strike, " ", self.option_type, \
                " ", self.interest, " ", self.param_t

    def update_fp(self, fp):
        self.future_price = fp

    def get_iv(self):

        bsm = BSM.BSM(self.option_type, self.strike, self.interest, self.param_t, self.future_price)
        return bsm.get_iv(self.option_type, self.quote.last_price)


class OptionList:
    future_cnt = None

    clist = {}
    plist = {}

    param_t = None
    interest = None
    spread_threshold = None
    future_price = None

    clist_full = False
    plist_full = False

    def __init__(self, f_cnt, t, i, spread_threshold):
        self.param_t = t
        self.future_cnt = f_cnt
        self.interest = i
        self.spread_threshold = spread_threshold

    def add(self, OptionQuote):
        cntTemp = OptionQuote.cnt_name.split('-')
        if len(cntTemp) == 3 and cntTemp[0] == self.future_cnt:
            if cntTemp[1] == 'C':
                if cntTemp[2] in self.clist:
                    self.clist[cntTemp[2]].update(OptionQuote)
                else:
                    self.clist[cntTemp[2]] = OptionCnt(1, float(cntTemp[2]))
                    self.clist[cntTemp[2]].set_param(self.spread_threshold, self.interest, self.param_t)
                    self.clist[cntTemp[2]].update_fp(self.future_price)
                    self.clist[cntTemp[2]].update(OptionQuote)

            elif cntTemp[1] == 'P':
                if cntTemp[2] in self.plist:
                    self.plist[cntTemp[2]].update(OptionQuote)
                else:
                    self.plist[cntTemp[2]] = OptionCnt(-1, float(cntTemp[2]))
                    self.plist[cntTemp[2]].set_param(self.spread_threshold, self.interest, self.param_t)
                    self.plist[cntTemp[2]].update_fp(self.future_price)
                    self.plist[cntTemp[2]].update(OptionQuote)
            else:
                print "error: OptionQuote.cnt_name is ", OptionQuote.cnt_name

        else:
            print "error len cntTemp ", cntTemp, " ", len(cntTemp), " ", cntTemp[0], " ", self.future_cnt
            print OptionQuote
            exit(0)

        if len(self.clist) >= 21:
            self.clist_full = True
        if len(self.plist) >= 21:
            self.plist_full = True

    def update_future_price(self, fp):
        for i in self.clist:
            self.clist[i].update_fp(fp)
        for i in self.plist:
            self.plist[i].update_fp(fp)
        self.future_price = fp

    def get_civ(self):
        svi_sample=[]
        if self.clist_full:
            for i in self.clist:
                svi_sample.append(Svi_sample(self.clist[i].iv, math.log(self.clist[i].strike / self.clist[i].future_price)))
            return svi_sample
        else:
            return None

    def get_piv(self):
        svi_sample = []
        if self.plist_full:
            for i in self.plist:
                svi_sample.append(Svi_sample(self.plist[i].iv, math.log(self.plist[i].strike / self.plist[i].future_price)))
            return svi_sample
        else:
            return None
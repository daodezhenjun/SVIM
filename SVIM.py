import myglobal
import math


class SVIM:
    # __param = None
    __sample = None

    def __init__(self, ssapl):
        self.__sample = ssapl

    def fitting(self, spara):
        sum_res = 0
        for i in self.__sample:
            temp_iv = self.__get_iv(spara, i.k) - i.iv
            sum_res = sum_res + temp_iv * temp_iv
        return sum_res

    def __get_iv(self, spara, kk):
        temp = kk - spara.m
        return spara.a + spara.b*(spara.rho * (temp) + math.sqrt(temp * temp + spara.sigma * spara.sigma))
    def get_iv_smile(self,spara,x):
        a=[]
        for i in xrange(len(x)):
            a.append(spara)
        return map(self.__get_iv,a,x)

import math


class BSM:
    flag = 0
    K = 0
    r = 0
    T = 0
    S = 0

    __VOL_ACCURACY1 = 0.00001
    __VOL_ACCURACY2 = -0.00001
    __b1 = 0.319381530
    __b2 = -0.356563782
    __b3 = 1.781477937
    __b4 = -1.821255978
    __b5 = 1.330274429
    __p = 0.2316419
    __c2 = 0.39894228
    __sqrt2Pi = 2.506628274
    __sqrt32 = 5.656854249
    __sqrt2_2 = 2.828427124
    __sqrt2_6 = 4.242640687

    def __init__(self, flag, K, r, T, S):
        self.flag = flag
        self.K = K
        self.r = r
        self.T = T
        self.S = S

    def __get_iv_li(self, C):

        eta = self.K * math.exp(-1 * self.r * self.T) / self.S
        rho = math.fabs(self.K * math.exp(-1 * self.r * self.T) - self.S) * self.S / (C * C)
        alpha = (2 * C / self.S + eta - 1) * self.__sqrt2Pi / (1 + eta)
        beta = math.cos(math.acos(3 * alpha / self.__sqrt32) / 3)
        if rho <= 1.4:
            try:
                return (self.__sqrt2_2 * beta / math.sqrt(self.T) - math.sqrt(
                    (8 * beta * beta - self.__sqrt2_6 * alpha / beta) / self.T))
            except ValueError:
                return float("nan")
        else:
            try:
                return (alpha + math.sqrt(alpha * alpha - (4 * (eta - 1) * (eta - 1) / (eta + 1)))) / (2 * math.sqrt(self.T))
            except ValueError:
                return float("nan")

    def __get_iv_newton(self, flag, C, vol_init):
        if math.isinf(vol_init) or math.isnan(vol_init):
            return float("nan")

        d1_temp = (math.log(self.S / self.K) + (self.r + pow(vol_init, 2) / 2) * self.T) / (vol_init * math.sqrt(self.T))
        d2_temp = d1_temp - vol_init * math.sqrt(self.T)

        f1 = self.get_theo_price(flag, d1_temp, d2_temp) - C
        if self.__VOL_ACCURACY2 < f1 < self.__VOL_ACCURACY1:
            return vol_init
        else:
            try:
                f2 = self.S * math.sqrt(self.T) * self.__norm_pdf(d1_temp)
                vol_new = vol_init - (f1 / f2)
                return self.__get_iv_newton(flag, C, vol_new)
            except ZeroDivisionError:

                return float("nan")

    def get_iv(self, flag, C):
        vol_temp = self.__get_iv_li(C)
        if math.isinf(vol_temp) or math.isnan(vol_temp):
            temp = self.__get_iv_newton(flag, C, 1)
            if math.isnan(temp):
                temp = self.__get_iv_newton(flag, C, 0.1)
                if math.isnan(temp):
                    temp = self.__get_iv_newton(flag, C, 2)
                    if math.isnan(temp):
                        return self.__get_iv_newton(flag, C, 0.5)
                    else:
                        return temp
                else:
                    return temp
            else:
                return temp

        else:
            return self.__get_iv_newton(flag, C, vol_temp)

    def __norm_pdf(self, z):
        return self.__c2 * math.exp(-0.5 * z * z)

    def __norm_cdf(self, z):
        t = 1.0 / (1.0 + math.fabs(z) * self.__p)

        n = ((((self.__b5 * t + self.__b4) * t + self.__b3) * t + self.__b2) * t + self.__b1) * t
        n = 1 - self.__norm_pdf(z) * n
        if z < 0:
            n = 1 - n
        return n

    def get_theo_price(self, flag, d1, d2):
        x = self.S * self.__norm_cdf(flag * d1)
        y = self.K * math.exp(-1 * self.r * self.T) * self.__norm_cdf(flag * d2)

        return flag * (x - y)

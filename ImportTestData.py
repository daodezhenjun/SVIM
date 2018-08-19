# coding=utf-8
import csv
import datetime as dt
import BSM
from myglobal import *
import math


def import_iv():
    # set option param
    spot = 2.483
    today = dt.date(2015, 1, 27)
    risk_free = 0.05
    qList = []

    # 读取行情


    with open('option_20150127.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            price = float(row[5])
            if (row[10] == "PO"):
                mytype = -1
            elif (row[10] == "CO"):
                mytype = 1
            else:
                print "error"
            strike = float(row[11])
            T = (dt.datetime.strptime(row[9], "%Y/%m/%d").date() - today).days / 365.0

            qList.append(Quote(price, strike, T, mytype))

    ivList = []
    for i in qList:
        # print (i.optionType, i.strike, riskFree, i.T, spot, i.optionPrice)
        bsm = BSM.BSM(i.optionType, i.strike, risk_free, i.T, spot)
        ivList.append(bsm.get_iv(i.optionType, i.optionPrice))

    svi_sample_list = []
    for i in range(0, len(ivList)):
        svi_sample_list.append(Svi_sample(ivList[i], (math.log(qList[i].strike / spot))))
    #svi_sample_list_sub = svi_sample_list[1:6]+svi_sample_list[28:34]
    svi_sample_list_sub=svi_sample_list[0:7] +svi_sample_list[28:35]
    for i6 in svi_sample_list_sub:
        print i6.iv,",",i6.k
    return svi_sample_list_sub


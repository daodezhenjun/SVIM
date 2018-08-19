#!/usr/bin/python
# coding=utf-8

import ImportTestData
from GaProcess import GaProcess
import numpy as np
import matplotlib.pyplot as plt
from myglobal import *
import SVIM



def testIvSmile(svi_sample_list):
    print svi_sample_list
    svim = SVIM.SVIM(svi_sample_list)
    gapro = GaProcess()

    gapro.setSVIM(svim)
    gapro.init()
    best_para = gapro.run_evaluate()
    print best_para

    leftX=0
    rightX=0
    for i in svi_sample_list:
        if leftX>i.k:
            leftX=i.k
        if rightX<i.k:
            rightX=i.k


    x = np.linspace(leftX, rightX, 1000)
    y = svim.get_iv_smile(Svi_param(best_para[0], best_para[1], best_para[2], best_para[3], best_para[4]), x)
    # 创建绘图对象，figsize参数可以指定绘图对象的宽度和高度，单位为英寸，一英寸=80px
    plt.figure(figsize=(8, 4))

    # 在当前绘图对象中画图（x轴,y轴,给所绘制的曲线的名字，画线颜色，画线宽度）
    plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)

    px = []
    py = []
    for i in svi_sample_list:
        px.append(i.k)
        py.append(i.iv)
    plt.scatter(px, py)
    # 显示图
    plt.show()


#svi_sample_list=ImportTestData.import_iv()
#testIvSmile(svi_sample_list)
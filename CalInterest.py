# coding=utf-8
import csv
import BSM

T=34/365
r=None
spot=2.3440
option_dict={}
bsm_list=[]

#read data
file_name="D://option.csv"

with open(file_name) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        if(row[0]=="C"):
            temp=1
        elif row[0]=="P":
            temp=-1
        else:
            print "error"
            exit(0)

        option_dict[(temp,float(row[1]))]=tuple([float(x) for x in row[5:11]])

for i in option_dict:
    bsm=BSM.BSM(i[0],i[1],r,T,spot)
    bsm.update
    bsm_list.append()


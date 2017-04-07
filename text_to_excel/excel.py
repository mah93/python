# -*- coding: utf-8 -*-
import xlwt
import os
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

excel_title=["证券公司代码","证券公司名称","结算参与人代码","基金销售人代码","结算参与人清算编号","结算参与人结算账户","法人所属监管辖区","数据日期"]
txt_path="./test.txt"
content_list=[]
max_number=65535

def txt_to_excel(path):
    start=time.clock()
    if os.path.exists(path):
        with open(path,'rb') as txt_content:
            for line in txt_content:
                txt_content_list=line.split("|")
                content_list.append(txt_content_list)
        
        x=xlwt.Workbook()

        font0 = xlwt.Font()
        font0.name='Times New Roman'
        font0.bold=True
        font0.height=240
        style0=xlwt.XFStyle()
        style0.font=font0

        sheet_row=len(content_list)
        sheet_number=sheet_row/max_number + 1

        for sheet_number_name in range(sheet_number):
            s=x.add_sheet('sheet' + str(sheet_number_name+1),cell_overwrite_ok=True)
            i=0
            for title in excel_title:
                s.col(i).width=5000
                s.write(0,i,title.decode('utf-8'),style0)
                i=i+1

            for j in range(max_number):
                k=0
                if (j+sheet_number_name * max_number)<sheet_row:
                    for content in content_list[j + sheet_number_name * max_number]:
                        s.write(j+1,k,content.decode('utf-8'))
                        k=k+1

        x.save('tbbs.xls')
        end=time.clock()
        print "read: %f s" % (end - start)
        
if __name__=='__main__':
    txt_to_excel(txt_path)

import xlwt
def write_file():
    book=xlwt.Workbook(encoding='utf-8') # 创建excel
    # 创建sheet，sheet1为表明，cell_overwrite_ok是否覆盖单元格
    sheet1=book.add_sheet(u'Sheet1',cell_overwrite_ok=True)
    # 写入数据
   # sheet1.write(0,0,"第一行表格")
   # sheet1.write(0,1,"第0行第一列")
   # sheet1.write(1,0,"第一行，第0列")
   # sheet1.write(1,1,"第一行，第一列")
    data={
        "序号":["name","chinese","math","english"],
        "1":["zhangsan",130,120,100],
        "2":["lisi",120,110,100],
        "3":["wangwu",110,112,142]
    }
    r=0
    for  i,j in data.items(): # i表示data中的key，j表示data的value
        le=len(j)   # values返回的列表长度
        if r==0:
            sheet1.write(r, 0, i, set_style('Arial', 220, True))  # 添加第 0 行 0 列数据单元格背景设为黄色
        else:
            sheet1.write(r, 0, i, )  # 添加第 1 列的数据

        for c in range(1, le + 1):  # values列表中索引
            if r == 0:
                sheet1.write(r, c, j[c - 1], set_style('Arial', 220, True))  # 添加第 0 行，2 列到第 5 列的数据单元格背景设为黄色
            else:
                sheet1.write(r, c, j[c - 1])

        r += 1  # 行数

        # sheet_merge() 合并单元格

    book.save('G:\\write.xlsx')




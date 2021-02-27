"""
功能描述：
读取：
    1、打开excel
    2、确定sheet页
    3、确定数据行和列
    4、读取一行数据
    5、读取所有数据
写入：
    1、复制原来的excel变为一个新的excel
    2、获取sheet
    3、写入
    4、保存
"""
import xlrd
import openpyxl
ec = xlrd.open_workbook("data.xls")
sheet = ec.sheet_by_index(0)   #通过索引获取sheet页，从0开始
sheet1 = ec.sheet_by_name("testdata")    #t通过sheet的名称进行查找
nrows = sheet.nrows   #获取表格的行数
ncols = sheet.ncols    #获取表格的列数
# print(nrows,ncols)
lng = sheet.cell(0,0).value        #获取单元格的值，从0开始，获取第1行第1列数据
lng2 = sheet.cell(2,4).value        #获取第3行第5列的数据
# print(lng,lng2)
row_value = sheet.row_values(0)    #获取第1行的数据，从0开始计数
# print(row_value)
col_value = sheet.col_values(0)   #获取第1列的数据，从0开始计数
print(col_value)







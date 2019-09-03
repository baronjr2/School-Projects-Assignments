import xlrd
import numpy as np
import pandas as pd
list = [0, 3, 6, 9, 12, 15, 18]
filename = 'Data.xlsx'
df0 = pd.read_excel(open(filename, 'rb'), sheet_name = 0)
df1 = pd.read_excel(open(filename, 'rb'), sheet_name = 1)
df2 = pd.read_excel(open(filename, 'rb'), sheet_name = 2)
df3 = pd.read_excel(open(filename, 'rb'), sheet_name = 3)
df4 = pd.read_excel(open(filename, 'rb'), sheet_name = 4)
df5 = pd.read_excel(open(filename, 'rb'), sheet_name = 5)
df6 = pd.read_excel(open(filename, 'rb'), sheet_name = 6)

out = pd.concat([df0, df1, df2, df3, df4, df5, df6])
out.to_excel("output2.xlsx")



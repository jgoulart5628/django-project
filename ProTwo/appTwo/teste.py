import pandas as pd
import openpyxl

data = pd.read_excel(r'/oldlin/param_func.xls')
# df = pd.DataFrame(data, columns=['Data', 'Horas'])
# print(data)
lista1 = sorted(list(data['HASH']))
for xx in lista1:
    print(xx)


# print(len(lista1))


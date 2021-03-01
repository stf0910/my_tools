import os

import pandas as pd

x=1

while x==1:
  print('0:csv->xlse\n1:xlsx->csv\n')
  ans = int(input())

  while not(0<=ans<=1):
    print('正しく入力してください。\n')
    print('0:csv->xlse\n1:xlsx->csv\n')
    ans = int(input())

  print('ファイルのパスを入力してください。\n')
  path = str(input()) 

  if ans==0:
    data = pd.read_csv(path)
    x = path.replace('.csv','')
    data.to_excel(f'{x}.xlsx',encoding='utf-8-sig')
  
  else:
    data = pd.read_excel(path)
    x = path.replace('.xlsx','')
    data.to_csv(f'{x}.csv',encoding='utf-8-sig')

  print('続けますか?\n0:いいえ\n1:はい\n')
  x = int(input())

  if not(0<=x<=1):
    print('正しく入力してください。\n')
    print('続けますか?\n0:いいえ\n1:はい\n')
    x = int(input())
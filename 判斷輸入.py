#判斷輸入.py

a = input("請輸入a ")
try:
  a=int(a)
  print("A是整數")
except:
  print("不對喔，我要整數")
  pass
try:
  a=float(a)
  print("A是小數")
except:
  pass

if( a=="APPLE"):
  print("蘋果")
else:
  print("虫合")
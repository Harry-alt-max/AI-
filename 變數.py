a=3
b=4
print(a+b) # print函數 把()裡面的東西打印出來
print(a*b)
print(a/b)
print(a-b)

# 建立不同型態的變數
name = "Alex"      # 字串 (String)
x = 25           # 整數 (Integer)
height = 175.5     # 浮點數 (Float)
abc = True   # 布林值 (Boolean)

print(type(x))
print(type(name))
print(type(height))
print(type(abc))

if(abc):
  print("英文")
else:
  print("wtf")

age=3
if(age>18):
  print("成年")
elif(8<age<18):
  print("你壞壞")
elif(age<8):
  print("瘋了嗎?")
else: #else 已經是所有條件皆不滿足的情況 所以這邊不能有假設條件
  print("合法")
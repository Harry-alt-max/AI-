import math  #導入數學計算的相關函式庫
import math as m #把數學函式庫稱為m
from math import sin,radians,cos #從math把sin,radians,cos導入
θ = m.radians(90) #角度30種成逕度
t = 1 #sec
v_θ = 30 #m/s 常數
g = 9.81 #m/s^2 常數

"""
輸入
"""
print(math.sin(θ))
x = v_θ*t*cos(θ)
y = v_θ*t*sin(θ)-(0.5*g*t*t)

"""
輸出
"""
print(x)
print(y)
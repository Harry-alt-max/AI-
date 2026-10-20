import time
from math import sin,radians,cos 

v_θ = 30
g = 9.81
θ = radians(45)

for t in range(10):
  
  y = v_θ*t*sin(θ)-(0.5*g*t*t)
  x = v_θ*t*cos(θ)
  print(f"第{t}秒 x={x:.2f}公尺 y={y:.2f}公尺")
  time.sleep(1) #sleep等待的意思

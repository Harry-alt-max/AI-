#test
from math import sin,radians
def test_function():
  print("test!")
  return "test!123"

def 加法(a,b):
  return a+b

def 求HRT(v0,theta):
  g = 9.81
  v0 = 30
  theta = radians(theta)

  H = pow(v0,2)*pow(sin(theta),2)/(2*g)
  R = pow(v0,2)*sin(2*theta)/g
  T = 2*v0*sin(theta)/g
  return H,R,T




# test.py
from math import radians, sin


def test_function():
  print("執行 test_function()...")
  return "test!123"


def 加法(a, b):
  return a + b


def 減法(a, b):
  return a - b


def 求HRT(v0, theta, g=9.81):
  """計算斜向拋射的最大高度 H、水平射程 R、飛行時間 T"""
  rad = radians(theta)

  H = (pow(v0, 2) * pow(sin(rad), 2)) / (2 * g)
  R = (pow(v0, 2) * sin(2 * rad)) / g
  T = (2 * v0 * sin(rad)) / g
  return H, R, T
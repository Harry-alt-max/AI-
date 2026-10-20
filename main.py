import test  #讀取test.py
a = test.test_function()
答案 = test.加法(3,4)
print(答案)

def 減法(a,b):
  return a-b
答案=減法(5,4)
print(答案)


print(test.求HRT(30,45))
#主程式保持簡潔是大原則
#因此發展副程式把函數切割成一個一個區塊




# main.py
import argparse
import test  # 讀取 test.py 副程式


def main():
  # 1. 建立命令列參數解析器
  parser = argparse.ArgumentParser(
      description="🚀 斜向拋射計算 CLI 工具 (直接輸入初速與角度)"
  )

  # 2. 定義必填的命令列參數：初速 (v0) 與 發射角度 (theta)
  parser.add_argument("v0", type=float, help="發射初速 (m/s)")
  parser.add_argument("theta", type=float, help="發射角度 (度)")

  # 3. 解析命令列傳進來的參數
  args = parser.parse_args()

  # 4. 呼叫副程式計算
  H, R, T = test.求HRT(args.v0, args.theta)

  # 5. 輸出結果
  print("\n=========================================")
  print("📊 斜向拋射計算結果")
  print("=========================================")
  print(f"  • 初速 (v0)    : {args.v0} m/s")
  print(f"  • 發射角度 (θ) : {args.theta}°")
  print("  -----------------------------------------")
  print(f"  • 最大高度 (H) : {H:.2f} 公尺")
  print(f"  • 水平射程 (R) : {R:.2f} 公尺")
  print(f"  • 飛行時間 (T) : {T:.2f} 秒")
  print("=========================================\n")


if __name__ == "__main__":
  main()
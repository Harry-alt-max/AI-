#tkinter python預設來做GUI的函式庫
import tkinter as tk
root = tk.Tk() # 宣告一個GUI物件叫做root
root.title("MyApp")
寬 = 600
高 = 400
left = int(1920/2-603/2)
top = 0
root.geometry(f'{寬}x{高}+{left}+{top}')

label = tk.Label(root,text="你好")
label.pack()
root.mainloop() #用mainloop把這個GUI回全跑起來








import tkinter as tk
from tkinter import ttk, messagebox

# 1. 建立主視窗物件 root
root = tk.Tk()
root.title("Tkinter 常用組件大全")

# 2. 設定視窗大小與置中位置
寬 = 600
高 = 700
left = int(1920 / 2 - 寬 / 2)
top = 100
root.geometry(f"{寬}x{高}+{left}+{top}")

# ==================== 1. Label (標籤) ====================
title_label = tk.Label(
    root, text="🚀 Tkinter 常用元件展示", font=("微軟正黑體", 16, "bold")
)
title_label.pack(pady=10)

# ==================== 2. Entry (單行輸入框) & Button (按鈕) ====================
frame_input = tk.Frame(root)  # 使用 Frame 容器將輸入框與按鈕放在同一行
frame_input.pack(pady=5)

tk.Label(frame_input, text="姓名：", font=("微軟正黑體", 10)).pack(
    side=tk.LEFT
)
entry_name = tk.Entry(frame_input, font=("微軟正黑體", 10), width=15)
entry_name.pack(side=tk.LEFT, padx=5)


def show_greeting():
  name = entry_name.get()
  if name:
    messagebox.showinfo("歡迎", f"你好，{name}！歡迎學習 Tkinter！")
  else:
    messagebox.showwarning("警告", "請先輸入姓名！")


btn_submit = tk.Button(
    frame_input, text="送出", command=show_greeting, bg="#4CAF50", fg="white"
)
btn_submit.pack(side=tk.LEFT)

# ==================== 3. Checkbutton (複選框) ====================
frame_check = tk.Frame(root)
frame_check.pack(pady=10)

var_python = tk.BooleanVar(value=True)  # 預設勾選
var_java = tk.BooleanVar(value=False)

chk_python = tk.Checkbutton(
    frame_check, text="Python", variable=var_python, font=("微軟正黑體", 10)
)
chk_python.pack(side=tk.LEFT, padx=10)

chk_java = tk.Checkbutton(
    frame_check, text="Java", variable=var_java, font=("微軟正黑體", 10)
)
chk_java.pack(side=tk.LEFT, padx=10)

# ==================== 4. Radiobutton (單選按鈕) ====================
frame_radio = tk.Frame(root)
frame_radio.pack(pady=5)

var_gender = tk.StringVar(value="男")  # 預設選擇「男」

radio_male = tk.Radiobutton(
    frame_radio,
    text="男",
    variable=var_gender,
    value="男",
    font=("微軟正黑體", 10),
)
radio_male.pack(side=tk.LEFT, padx=10)

radio_female = tk.Radiobutton(
    frame_radio,
    text="女",
    variable=var_gender,
    value="女",
    font=("微軟正黑體", 10),
)
radio_female.pack(side=tk.LEFT, padx=10)

# ==================== 5. Combobox (下拉選單 - 需使用 ttk) ====================
frame_combo = tk.Frame(root)
frame_combo.pack(pady=10)

tk.Label(frame_combo, text="選擇城市：", font=("微軟正黑體", 10)).pack(
    side=tk.LEFT
)
combo_city = ttk.Combobox(
    frame_combo, values=["台北", "台中", "高雄"], state="readonly"
)
combo_city.current(2)  # 預設選擇「高雄」
combo_city.pack(side=tk.LEFT, padx=5)

# ==================== 6. Scale (滑桿) ====================
frame_scale = tk.Frame(root)
frame_scale.pack(pady=10)

tk.Label(frame_scale, text="滿意度 (0-100)：", font=("微軟正黑體", 10)).pack(
    side=tk.LEFT
)
scale_score = tk.Scale(
    frame_scale, from_=0, to=100, orient=tk.HORIZONTAL, length=200
)
scale_score.set(80)  # 預設值
scale_score.pack(side=tk.LEFT)

# ==================== 7. Text (多行文字區域) ====================
tk.Label(root, text="備註 / 意見：", font=("微軟正黑體", 10)).pack(
    anchor="w", padx=50
)
text_area = tk.Text(root, height=4, width=40, font=("微軟正黑體", 10))
text_area.insert(tk.END, "這裡可以輸入多行文字內容...")
text_area.pack(pady=5)

# ==================== 8. Listbox (清單視窗) ====================
tk.Label(root, text="興趣列表：", font=("微軟正黑體", 10)).pack(
    anchor="w", padx=50
)
listbox_hobbies = tk.Listbox(root, height=3, width=40)
for hobby in ["寫程式", "看電影", "聽音樂", "打羽毛球"]:
  listbox_hobbies.insert(tk.END, hobby)
listbox_hobbies.pack(pady=5)

# ==================== 9. Canvas (畫布 - 用於繪圖) ====================
canvas = tk.Canvas(root, width=300, height=80, bg="#f0f0f0")
canvas.pack(pady=10)

# 在畫布上畫圓形與方形
canvas.create_oval(20, 15, 70, 65, fill="skyblue", outline="blue")
canvas.create_rectangle(100, 15, 180, 65, fill="lightgreen", outline="green")
canvas.create_text(240, 40, text="Canvas 畫布", font=("微軟正黑體", 10))

# 10. 用 mainloop 把 GUI 迴圈跑起來
root.mainloop()









# main.py
import math
import tkinter as tk
from tkinter import messagebox
import test  # 讀取副程式


def calculate():
  try:
    # 取得輸入框的數值
    v0 = float(entry_v0.get())
    theta = float(entry_theta.get())
    g = float(entry_g.get())

    # 呼叫副程式計算 H, R, T
    H, R, T = test.求HRT(v0, theta, g)

    # 顯示計算結果在畫布下方或訊息框
    result_str = (
        f"計算結果：\n最高高度(H): {H:.2f} m\n水平射程(R): {R:.2f}"
        f" m\n飛行時間(T): {T:.2f} s"
    )
    lbl_info.config(text=result_str)

    # 在 Canvas 畫布上畫出斜向拋射軌跡圖
    draw_trajectory(v0, theta, g)

  except ValueError:
    messagebox.showerror("錯誤", "請在所有欄位輸入有效的數字！")


def draw_trajectory(v0, theta_deg, g):
  """根據初速與角度在 Canvas 上繪製拋物線軌跡"""
  canvas.delete("all")  # 清空畫布

  # 畫座標軸
  canvas.create_line(50, 350, 450, 350, fill="gray", width=2)  # X軸
  canvas.create_line(50, 350, 50, 50, fill="gray", width=2)  # Y軸
  canvas.create_text(
      450, 365, text="X (距離)", font=("微軟正黑體", 9), fill="white"
  )
  canvas.create_text(
      35, 45, text="Y (高度)", font=("微軟正黑體", 9), fill="white"
  )

  theta = math.radians(theta_deg)
  total_time = 2 * v0 * math.sin(theta) / g

  # 縮放比例尺（讓畫面塞得下軌跡）
  max_r = (pow(v0, 2) * math.sin(2 * theta)) / g
  if max_r == 0:
    max_r = 1
  scale_x = 350 / max(max_r, 10)

  max_h = (pow(v0, 2) * pow(math.sin(theta), 2)) / (2 * g)
  scale_y = 250 / max(max_h, 10)

  # 計算並繪製軌跡點
  points = []
  steps = 100
  for i in range(steps + 1):
    t = (total_time / steps) * i
    x = v0 * math.cos(theta) * t
    y = v0 * math.sin(theta) * t - 0.5 * g * pow(t, 2)

    # 轉換成 Canvas 座標系（原點在左下角 50, 350）
    screen_x = 50 + x * scale_x
    screen_y = 350 - y * scale_y
    points.append((screen_x, screen_y))

  # 畫出曲線
  if len(points) > 1:
    canvas.create_line(points, fill="#00FFCC", width=3)

  # 標示文字說明
  canvas.create_text(
      250,
      20,
      text=f"拋物線軌跡模擬 (θ={theta_deg}°, v0={v0})",
      font=("微軟正黑體", 10, "bold"),
      fill="white",
  )


# --- 建立主視窗 ---
root = tk.Tk()
root.title("🚀 斜向拋射計算器與視覺化")
root.geometry("850x450")
root.config(bg="#1e4d6b")  # 呼應圖片的深藍色背景

# --- 左側：Labels (初速度、角度、重力加速度) ---
lbl_v0 = tk.Label(
    root,
    text="Label(初速度)",
    font=("微軟正黑體", 11, "bold"),
    bg="#16425b",
    fg="white",
    width=15,
    height=2,
)
lbl_v0.grid(row=0, column=0, padx=15, pady=15, sticky="w")

lbl_theta = tk.Label(
    root,
    text="Label(角度)",
    font=("微軟正黑體", 11, "bold"),
    bg="#16425b",
    fg="white",
    width=15,
    height=2,
)
lbl_theta.grid(row=1, column=0, padx=15, pady=15, sticky="w")

lbl_g = tk.Label(
    root,
    text="Label(重力加速度)",
    font=("微軟正黑體", 10, "bold"),
    bg="#16425b",
    fg="white",
    width=15,
    height=2,
)
lbl_g.grid(row=2, column=0, padx=15, pady=15, sticky="w")


# --- 中間：Entries 與 Button ---
entry_v0 = tk.Entry(root, font=("微軟正黑體", 12), width=12)
entry_v0.insert(0, "30")
entry_v0.grid(row=0, column=1, padx=10, pady=15)

entry_theta = tk.Entry(root, font=("微軟正黑體", 12), width=12)
entry_theta.insert(0, "45")
entry_theta.grid(row=1, column=1, padx=10, pady=15)

entry_g = tk.Entry(root, font=("微軟正黑體", 12), width=12)
entry_g.insert(0, "9.81")
entry_g.grid(row=2, column=1, padx=10, pady=15)

btn_calc = tk.Button(
    root,
    text="Button(計算)",
    font=("微軟正黑體", 11, "bold"),
    bg="#0b2545",
    fg="white",
    width=14,
    height=2,
    command=calculate,
)
btn_calc.grid(row=3, column=1, padx=10, pady=15)

# 顯示數值計算結果的標籤
lbl_info = tk.Label(
    root,
    text="請輸入數值並點擊計算",
    font=("微軟正黑體", 10),
    bg="#1e4d6b",
    fg="#ffeb3b",
    justify="left",
)
lbl_info.grid(row=4, column=0, columnspan=2, padx=15, pady=5)


# --- 右側：Canvas 畫布 ---
canvas = tk.Canvas(root, width=480, height=380, bg="#112233", highlightthickness=0)
canvas.grid(row=0, column=2, rowspan=5, padx=20, pady=20)

# 在畫布中央寫上提示文字（呼應圖片的「這裡是畫布」）
canvas.create_text(
    240,
    190,
    text="這裡是畫布\n(點擊計算後將顯示軌跡)",
    font=("微軟正黑體", 14, "bold"),
    fill="#88aacc",
    justify="center",
)

# 啟動視窗
root.mainloop()
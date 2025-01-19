import tkinter as tk
from tkinter import ttk

# 기본 창 생성
root = tk.Tk()
root.title("스크롤뷰 예제")
root.geometry("400x600")

# 프레임 생성
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

# 캔버스 생성
canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# 스크롤바 생성
scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 스크롤바를 캔버스에 연결
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# 스크롤 가능한 프레임 생성
scrollable_frame = tk.Frame(canvas)

# 캔버스에 프레임을 추가
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# 마우스 휠 이벤트 핸들러
def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# 마우스 휠 이벤트 바인딩
canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# # 예제 위젯 추가
# for i in range(50):
#     tk.Label(scrollable_frame, text="Label " + str(i)).pack()

studentNum = 35
nameEntries = []
scoreEntries = []
# 학생 수에 맞게 Entry 생성
for i in range(studentNum):
    num_label = tk.Label(scrollable_frame, text=str(i + 1), font=("맑은고딕", 12, "bold"))
    nameEntry = tk.Entry(scrollable_frame, font=("맑은고딕", 12), width=10)
    scoreEntry = tk.Entry(scrollable_frame, font=("맑은고딕", 12), width=10)

    # num_label.place(x=20, y=100 + 40 * i)
    # nameEntry.place(x=50, y=100 + 40 * i)
    # scoreEntry.place(x=150, y=100 + 40 * i)

    # 각 위젯을 scrollable_frame에 배치
    num_label.grid(row=i, column=0, padx=5, pady=5)
    nameEntry.grid(row=i, column=1, padx=5, pady=5)
    scoreEntry.grid(row=i, column=2, padx=5, pady=5)

    nameEntries.append(nameEntry)
    scoreEntries.append(scoreEntry)

root.mainloop()
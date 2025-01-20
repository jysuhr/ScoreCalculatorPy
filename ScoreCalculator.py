import tkinter as tk
from tkinter import ttk

studentNum = 40

# 함수 선언
def studentNumCheck():
    # 학생 수 입력값 가져오기
    global studentNum
    a = studentNumEntry.get()

    # 학생 수가 유효한지 확인
    if not a.isdigit():
        error_label.config(text="학생 수는 숫자로 입력해야 합니다!", font="bold")
        return
    
    error_label.config(text="")  # 에러 메시지 초기화
    studentNum = int(a)

    # 학생 수에 맞게 입력 필드 다시 생성
    update_input_frame()

    # 화면 전환
    inputFrame.lift()

def update_input_frame():
    # 기존의 Entry를 모두 제거
    for entry in nameEntries + scoreEntries:
        entry.destroy()

    for num in numList:
        num.destroy()

    nameEntries.clear()
    scoreEntries.clear()

    # 학생 수에 맞게 Entry 생성
    for i in range(studentNum):
        num_label = tk.Label(scrollable_frame, text=str(i + 1), font=("맑은고딕", 12, "bold"))
        nameEntry = tk.Entry(scrollable_frame, font=("맑은고딕", 12), width=10)
        scoreEntry = tk.Entry(scrollable_frame, font=("맑은고딕", 12), width=10)

        # 각 위젯을 scrollable_frame에 배치
        num_label.grid(row=i, column=0, padx=5, pady=5)
        nameEntry.grid(row=i, column=1, padx=5, pady=5)
        scoreEntry.grid(row=i, column=2, padx=5, pady=5)

        numList.append(num_label)
        nameEntries.append(nameEntry)
        scoreEntries.append(scoreEntry)

extraction_list = []

def extraction():
    extraction_list.clear()
    for i in range(studentNum):
        name = nameEntries[i].get()
        score = scoreEntries[i].get()
        
        try:
            # 실수일 경우
            floated_score = float(score)
            
        except ValueError:
            # 실수가 아닐 경우
            error_label2.config(text="점수는 실수로\n입력해야 합니다!", font="bold")
            return
        
        extraction_list.append([name, floated_score])

    calculate()
    result_refresh()
    resultTabel_refresh()
    resultFrame.lift()

avg = 0
percent = 0
result_list = [] # [순위, 이름, 점수, 등급, 비율]

def calculate():
    # 인스턴스 선언
    global avg
    global percent
    global result_list
    sum = 0
    n = len(extraction_list) # 학생 수

    # 점수 내림정렬
    result_list = sorted(extraction_list, key=lambda x: x[1], reverse=True)
    
    # 순위 추가
    for k in range(n):
        result_list[k].insert(0, k + 1)  # 순위를 리스트 맨 앞에 추가 1차

    ## 동점자 처리
    for k in range(n):
        if k > 0 and result_list[k][2] == result_list[k - 1][2]:
            result_list[k][0] = result_list[k - 1][0]  # 이전 순위와 동일하게 설정

    # result_list 작성
    for i in range(n):
        # 합계 추가
        sum += result_list[i][2]

        # 비율 추가
        percent = result_list[i][0] / n
        result_list[i].insert(4, percent)

        # 등급 추가
        grade = grade_calculate(percent)
        result_list[i].insert(3, grade)
    
    # 평균 계산
    avg = round(sum / n, 2)

def grade_calculate(percent_score):
    if 0 <= percent_score < 0.04:
        return '1'
    elif 0.04 <= percent_score < 0.11:
        return '2'
    elif 0.11 <= percent_score < 0.23:
        return '3'
    elif 0.23 <= percent_score < 0.40:
        return '4'
    elif 0.40 <= percent_score < 0.60:
        return '5'
    elif 0.60 <= percent_score < 0.77:
        return '6'
    elif 0.77 <= percent_score < 0.89:
        return '7'
    elif 0.89 <= percent_score < 0.96:
        return '8'
    elif 0.96 <= percent_score <= 1.00:
        return '9'
    else:
        return 'NaN'

def result_refresh():
    index_label1.config(text=f"학생수\t: {len(result_list)}")
    index_label2.config(text=f"평균\t: {avg}")
    index_label3.config(text=f"최고점\t: {result_list[0][2]}")
    index_label4.config(text=f"최저점\t: {result_list[-1][2]}")

# 레이블 삭제 함수
def delete_labels():
    for label in labels:
        label.destroy()
    labels.clear()

def resultTabel_refresh():
    # 기존 레이블 삭제
    delete_labels()

    a_in = len(result_list)

    for m in range(a_in):
        formatted_percent = "{:.2f}".format(round(result_list[m][4], 2))
        ka = tk.Label(scrollable_frame2, text=f"{result_list[m][0]}등\t{result_list[m][1]}\t{result_list[m][2]}점\t{result_list[m][3]}등급\t{formatted_percent}")
        ka.config(font=("맑은고딕", 12, 'bold'))
        ka.grid(row=m, column=0, padx=5, pady=2)

        student_result_list.append(ka)

def destroy_last_label():
    for last_label in student_result_list:
        last_label.destroy()

def reset():
    # 최근 레이블 삭제
    destroy_last_label()

    extraction_list.clear()
    result_list.clear()

    # 학생수 Entry 초기화
    studentNumEntry.delete(0, "end")
    studentNumEntry.focus_set()

    # 초기화면 불러오기
    studentCountFrame.lift()

# 기본 창 생성
root = tk.Tk()
root.title("성적 계산기")
root.geometry("400x600")

# 프레임 생성
infoFrame = tk.Frame(root)
resultFrame = tk.Frame(root)
inputFrame = tk.Frame(root)
studentCountFrame = tk.Frame(root)

# 프레임 배치
infoFrame.place(x=0, y=0, width=400, height=600)
resultFrame.place(x=0, y=0, width=400, height=600)
inputFrame.place(x=0, y=0, width=400, height=600)
studentCountFrame.place(x=0, y=0, width=400, height=600)  # 이 프레임이 가장 먼저 나타남

################################# studentCountFrame ###################################
# 컴포넌트 선언 - studentCountFrame
title1 = tk.Label(studentCountFrame, text="점수 계산기", font=("맑은고딕", 22, "bold"))
divider1 = tk.Canvas(studentCountFrame, width=400, height=1, bg="black")
infoButton = tk.Button(studentCountFrame, text="정보", font=("맑은고딕", 8), bg="skyblue", fg="black", command=lambda: infoFrame.lift(), height=2)

studentNumLabel = tk.Label(studentCountFrame, text="학생 수를 입력하세요", font=("맑은고딕", 14, "bold"))
studentNumEntry = tk.Entry(studentCountFrame, font=("맑은고딕", 16, "bold"), width=4)
studentNumEntry.focus_set()
studentNumButton = tk.Button(studentCountFrame, text=" 확인 ", command=studentNumCheck, font=("맑은고딕", 10, "bold"), bg="skyblue", fg="black")

error_label = tk.Label(studentCountFrame, text="", font=("맑은고딕", 10), fg="red")  # 에러 메시지 표시용


# 레이아웃 배치 - studentCountFrame
title1.place(x=10, y=10)
infoButton.place(x=340, y=15)
divider1.place(x=0, y=60)

defX = 100
defY = 140
studentNumLabel.place(x=defX, y=defY)
studentNumEntry.place(x=defX + 45, y=defY + 40)
studentNumButton.place(x=defX + 100, y=defY + 38)
error_label.place(x=defX - 35, y=defY + 80)

#################################### inputFrame #######################################
# 컴포넌트 선언 - inputFrame
title2 = tk.Label(inputFrame, text="성적 입력", font=("맑은고딕", 22, "bold"))
divider2 = tk.Canvas(inputFrame, width=400, height=1, bg="black")
name_label = tk.Label(inputFrame, text="이름", font=("맑은고딕", 10, "bold"))
score_label = tk.Label(inputFrame, text="점수", font=("맑은고딕", 10, "bold"))
calculate_button = tk.Button(inputFrame, command=extraction, text="계산\n하기", font=("맑은고딕", 12, "bold"),width=35, height=3, bg="skyblue", fg="black")
error_label2 = tk.Label(inputFrame, text="", font=("맑은고딕", 10, "bold"), fg="red")  # 점수가 숫자가 아닐 경우 에러 메시지

# 스크롤바 및 캔버스 설정 ######################## --- 1
# 캔버스 생성
canvas = tk.Canvas(inputFrame)
# canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
canvas.place(x=0, y=100, width=400, height=400)

# 스크롤바 생성
scrollbar = ttk.Scrollbar(inputFrame, orient=tk.VERTICAL, command=canvas.yview)
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
################################################# --- 1

# Entry를 저장할 리스트
numList = []
nameEntries = []
scoreEntries = []

# Entry를 처음에 45개 생성 (기본값으로 45명의 학생)
update_input_frame()

# 레이아웃 배치 - inputFrame
title2.place(x=10, y=10)
error_label2.place(x=220, y=12)
divider2.place(x=0, y=60)
name_label.place(x=70, y=74)
score_label.place(x=165, y=74)
calculate_button.place(x=10, y=510)

################################## resultFrame ######################################
# 컴포넌트 선언 - resultFrame
title3 = tk.Label(resultFrame, text="결과", font=("맑은고딕", 22, "bold"))
divider3 = tk.Canvas(resultFrame, width=400, height=1, bg="black")


index_label1 = tk.Label(resultFrame, font=("맑은고딕", 12, "bold"), anchor="w")
index_label2 = tk.Label(resultFrame, font=("맑은고딕", 12, "bold"), anchor="w")
index_label3 = tk.Label(resultFrame, font=("맑은고딕", 12, "bold"), anchor="w")
index_label4 = tk.Label(resultFrame, font=("맑은고딕", 12, "bold"), anchor="w")

tag_label =tk.Label(resultFrame, text="순위\t이름\t점수\t등급\t비율", font=("맑은고딕", 12, "bold"), fg="navy")
divider3_a = tk.Canvas(resultFrame, width=400, height=1, bg="black")

result_back_button = tk.Button(resultFrame, anchor="center", text="돌아가기", command=lambda: inputFrame.lift())
result_back_button.config(font=("맑은고딕", 12, "bold"), bg="orange", fg="black", width=7, height=2)
result_reset_button = tk.Button(resultFrame, anchor="center", text="초기화", command=reset)
result_reset_button.config(font=("맑은고딕", 12, "bold"), bg="red", fg="white", width=7, height=2)

copy_button = tk.Button(resultFrame, anchor="center", text="결과 복사", font=("맑은고딕", 12, "bold"), bg="#9acd32", width=7, height=2)

def copy_contents_refresh():
    root.clipboard_clear()

    contents = f"""
학생수\t: {len(result_list)}
평균\t\t: {avg}
최고점\t: {result_list[0][2]}
최저점\t: {result_list[-1][2]}

순위\t이름\t\t점수\t등급\t비율
"""

    for item in result_list:
        rank, name, score, grade, percent = item
        contents += f"{rank}\t{name}\t{score}\t {grade}\t{percent:.2f}\n"

    root.clipboard_append(contents)

copy_button.config(command=copy_contents_refresh)

# 스크롤바 및 캔버스 설정 ######################## --- 2
# 캔버스 생성
canvas_result = tk.Canvas(resultFrame)
canvas_result.place(x=0, y=178, width=400, height=350)

# 스크롤바 생성
scrollbar2 = ttk.Scrollbar(resultFrame, orient=tk.VERTICAL, command=canvas_result.yview)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)

# 스크롤바를 캔버스에 연결
canvas_result.configure(yscrollcommand=scrollbar2.set)
canvas_result.bind('<Configure>', lambda e: canvas_result.configure(scrollregion=canvas_result.bbox("all")))

# 스크롤 가능한 프레임 생성
scrollable_frame2 = tk.Frame(canvas_result)

# 캔버스에 프레임을 추가
canvas_result.create_window((0, 0), window=scrollable_frame2, anchor="nw")

# 마우스 휠 이벤트 핸들러
# def on_mouse_wheel(event):
#     canvas_result.yview_scroll(int(-1*(event.delta/120)), "units")

# # 마우스 휠 이벤트 바인딩
# canvas_result.bind_all("<MouseWheel>", on_mouse_wheel)
################################################# --- 2

student_result_list = []

# 레이아웃 배치 - resultFrame
title3.place(x=10, y=10)
divider3.place(x=0, y=60)

index_y = 67
index_label1.place(x=10, y=index_y)
index_label2.place(x=10, y=index_y + 20)
index_label3.place(x=10, y=index_y + 40)
index_label4.place(x=10, y=index_y + 60)

divider3_a.place(x=0, y=152)
tag_label.place(x=10, y=155)

result_back_button.place(x=10, y=540)
result_reset_button.place(x=300, y=540)
copy_button.place(x=160, y=540)

# 레이블을 저장할 리스트
labels = []

# 레이블 생성
for i in range(45):
    label = tk.Label(scrollable_frame2, text=f"프레임 생성중... {i + 1}")
    label.pack()
    labels.append(label)

################################### infoFrame #######################################
# 컴포넌트 선언 - infoFrame
info_label = tk.Label(infoFrame, font=("맑은고딕", 12), anchor="w", justify="left")
info_label.config(text='''
- 등급 계산법
    
상위 누적비율
1등급 : 0 ~ 4%
2등급 : 4 ~ 11%
3등급 : 11 ~ 23%
4등급 : 23 ~ 40%
5등급 : 40 ~ 60%
6등급 : 60 ~ 77%
7등급 : 77 ~ 89%
8등급 : 89 ~ 96%
9등급 : 96 ~ 100%


- 순위 계산법
    
점수가 동일한 학생은 같은 등수로 처리


- 비율 계산법
    
(학생 순위) / (전체 학생 수)
*소숫점 3자리에서 반올림
''')
copyright_label = tk.Label(infoFrame, font=("맑은고딕", 8), anchor="w", justify="left")
copyright_label.config(text='''  
Copyright Notice
본 프로그램의 모든 저작권은 제작자에게 있습니다.
이 프로그램에 대한 무단 복제, 수정, 배포 및 기타 저작권 침해 행위는
법적 제재를 받을 수 있습니다.

© 2025 All Rights Reserved.
''')
info_back_button = tk.Button(infoFrame, text="돌아가기", command=lambda: studentCountFrame.lift(), font=("맑은고딕", 12, "bold"), bg="orange", fg="black", height=2)

# 레이아웃 배치 - infoFrame
info_label.place(x=0, y=10)
copyright_label.place(x=0, y=440)
info_back_button.place(x=10, y=540)


###################################################################
# 메인 루프 실행
root.mainloop()

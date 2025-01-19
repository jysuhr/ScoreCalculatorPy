import tkinter as tk

# 함수 선언
studentNum = 0

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
    print(studentNum)

    # 학생 수에 맞게 입력 필드 다시 생성
    update_input_frame()

    # 화면 전환
    inputFrame.lift()

def update_input_frame():
    # 기존의 Entry를 모두 제거
    for entry in nameEntries + scoreEntries:
        entry.destroy()

    nameEntries.clear()
    scoreEntries.clear()

    # 학생 수에 맞게 Entry 생성
    for i in range(studentNum):
        num_label = tk.Label(inputFrame, text=str(i + 1), font=("맑은고딕", 12, "bold"))
        nameEntry = tk.Entry(inputFrame, font=("맑은고딕", 12), width=10)
        scoreEntry = tk.Entry(inputFrame, font=("맑은고딕", 12), width=10)

        num_label.place(x=20, y=100 + 40 * i)
        nameEntry.place(x=50, y=100 + 40 * i)
        scoreEntry.place(x=150, y=100 + 40 * i)

        nameEntries.append(nameEntry)
        scoreEntries.append(scoreEntry)

# 기본 창 생성
root = tk.Tk()
root.title("성적 계산기")
root.geometry("400x600")

# 프레임 생성
resultFrame = tk.Frame(root)
inputFrame = tk.Frame(root)
studentCountFrame = tk.Frame(root)

resultFrame.place(x=0, y=0, width=400, height=600)
inputFrame.place(x=0, y=0, width=400, height=600)
studentCountFrame.place(x=0, y=0, width=400, height=600)  # 이 프레임이 가장 먼저 나타남

###################### studentCountFrame ###########################
# 컴포넌트 선언 - studentCountFrame
title1 = tk.Label(studentCountFrame, text="점수 계산기", font=("맑은고딕", 22, "bold"))
divider1 = tk.Canvas(studentCountFrame, width=400, height=1, bg="black")
infoButton = tk.Button(studentCountFrame, text="정보", font=("맑은고딕", 8), bg="skyblue", fg="black")

studentNumLabel = tk.Label(studentCountFrame, text="학생 수를 입력하세요", font=("맑은고딕", 14, "bold"))
studentNumEntry = tk.Entry(studentCountFrame, font=("맑은고딕", 16, "bold"), width=4)
studentNumButton = tk.Button(studentCountFrame, text=" 확인 ", command=studentNumCheck, font=("맑은고딕", 10, "bold"), bg="skyblue", fg="black")

error_label = tk.Label(studentCountFrame, text="", font=("맑은고딕", 10), fg="red")  # 에러 메시지 표시용


# 레이아웃 배치 - studentCountFrame
title1.place(x=10, y=10)
infoButton.place(x=340, y=25)
divider1.place(x=0, y=60)

defX = 100
defY = 140
studentNumLabel.place(x=defX, y=defY)
studentNumEntry.place(x=defX + 45, y=defY + 40)
studentNumButton.place(x=defX + 100, y=defY + 38)
error_label.place(x=defX - 35, y=defY + 80)

########################## inputFrame #############################
# 컴포넌트 선언 - inputFrame
title2 = tk.Label(inputFrame, text="성적 입력", font=("맑은고딕", 22, "bold"))
divider2 = tk.Canvas(inputFrame, width=400, height=1, bg="black")
name_label = tk.Label(inputFrame, text="이름", font=("맑은고딕", 10, "bold"))
score_label = tk.Label(inputFrame, text="점수", font=("맑은고딕", 10, "bold"))

# Entry를 저장할 리스트
nameEntries = []
scoreEntries = []

# Entry를 처음에 3개 생성 (기본값으로 3명의 학생)
update_input_frame()

# 레이아웃 배치 - inputFrame
title2.place(x=10, y=10)
divider2.place(x=0, y=60)
name_label.place(x=78, y=74)
score_label.place(x=177, y=74)



###################################################################
# 메인 루프 실행
root.mainloop()

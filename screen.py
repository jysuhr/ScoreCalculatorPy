from tkinter import *

page = 1  # frame1이 1임, frame2는 2 frame3은 3
def next_frame():
    global page, frame1, frame2, frame3
    page += 1
    if page >= 3:
        page = 3
        frame3.lift()
    elif page == 2:
        frame2.lift()
    elif page == 1:
        frame1.lift()


def prev_frame():
    global page, frame1, frame2, frame3
    page -= 1
    if page <= 1:
        page = 1
        frame1.lift()
    elif page == 2:
        frame2.lift()
    elif page == 3:
        frame3.lift()


root = Tk()
root.title("화면 전환~~")
root.geometry("400x300+300+300")

frame3 = Frame(root, relief='solid', border=2)
frame2 = Frame(root, relief='solid', border=2)
frame1 = Frame(root, relief='solid', border=2)

but_frame = Frame(root, relief='solid', border=2)

frame3.place(x=0, y=0, width=400, height=250)
frame2.place(x=0, y=0, width=400, height=250)
frame1.place(x=0, y=0, width=400, height=250)  # 이 프레임이 가장 먼저 나타남
but_frame.place(x=0, y=250, width=400, height=50)  # 밑 바닥에 이전과 다음이 있을 버튼 영역

Label(frame3, text="Frame3", font=('consolas', 20)).pack(fill='y')
Label(frame2, text="Frame2", font=('consolas', 20)).pack(fill='y')
Label(frame1, text="Frame1", font=('consolas', 20)).pack(fill='y')

Button(but_frame, text='다음', command=next_frame).pack(side='right')
Button(but_frame, text='이전', command=prev_frame).pack(side='right')

root.mainloop()

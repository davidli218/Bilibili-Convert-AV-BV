import converter
import tkinter as tk
from tkinter import messagebox as tkm
import tkinter.font as tkf

if __name__ == '__main__':
    def convert():
        var_result.set('')
        input_id = var_input.get()
        if input_id[:2].upper() == 'AV' and len(input_id) >= 3 and input_id[2:].isdigit():
            var_result.set(converter.enc(input_id))
        elif input_id[:2].upper() == 'BV' and len(input_id) == 12 and input_id[2:].isalnum():
            var_result.set(converter.dec(input_id))
        else:
            tkm.showinfo(title='Invalid Input', message='Please input Correct ID')


    # 创建主窗口
    window = tk.Tk()
    window.title('B站 AV/BV号转换器')
    window.geometry('450x300')
    window.iconbitmap('BVid2Aid.ico')
    window.resizable(width=False, height=False)

    # 常量&变量
    font_main = tkf.Font(family="Lucida Grande", size=20)
    var_input = tk.StringVar()
    var_result = tk.StringVar()

    # 顶部LOGO图片
    canvas = tk.Canvas(window, height=200, width=450)
    image_file = tk.PhotoImage(file='welcome.gif')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack(side=tk.TOP)

    # 输入
    tk.Label(window, text='AV/BVid: ', font=font_main).place(x=30, y=150)
    entry_input = tk.Entry(window, textvariable=var_input,
                           width=16, highlightcolor='red', highlightthickness=1, font=font_main)
    entry_input.place(x=160, y=150)
    entry_input.bind("<Return>", lambda x: convert())

    # 输出
    tk.Label(window, text='Result: ', font=font_main).place(x=30, y=190)
    output_result = tk.Entry(window, textvariable=var_result, state='readonly',
                             width=16, highlightcolor='red', highlightthickness=1, font=font_main)
    output_result.place(x=160, y=190)

    # 转换按钮
    btn_login = tk.Button(window, text='Convert', command=convert, font=font_main)
    btn_login.place(relx=0.5, y=260, relwidth=0.3, anchor=tk.CENTER)

    window.mainloop()

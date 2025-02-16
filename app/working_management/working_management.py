import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
from time import strftime


def create_new_frame(container_frame):
    def time():
        string = strftime('%H:%M:%S')  # 現在時刻を取得
        label_hour_time.config(text=string)  # ラベルのテキストを更新
        label_hour_time.after(1000, time)  #

    root = container_frame.winfo_toplevel()
    root.title("tarot")

    container_working_management = tk.Frame(container_frame, background="pink")
    container_working_management.pack(fill="both", expand=True)

    # 全体の列の数、行の数を設定
    for i in range(1):
        container_working_management.grid_columnconfigure(i, weight=1)
    for i in range(6):
        container_working_management.grid_rowconfigure(i, weight=1)

    # --------------------時間エリア---------------------
    frame_time = tk.Frame(container_working_management, background="black")
    frame_time.grid(row=0, column=0, sticky="nsew")

    for i in range(2):
        frame_time.grid_columnconfigure(i, weight=1)

    for i in range(1):
        frame_time.grid_rowconfigure(i, weight=1)

    label_year_month_day = tk.Label(
        frame_time, background="black", fg="red", text="2025/02/16(日)", font=('calibri', 20, 'bold'), anchor="nw")
    label_year_month_day.grid(row=0, column=0, rowspan=1, sticky="nsew")

    label_hour_time = tk.Label(
        frame_time, background="black", fg="red", font=('calibri', 40, 'bold'), anchor="e")
    label_hour_time.grid(row=0, column=1, columnspan=2, sticky="nsew")

    time()

    # --------------------ラベルエリア---------------------
    frame_infomation_area = tk.Frame(
        container_working_management, background="white")
    frame_infomation_area.grid(row=1, column=0, rowspan=4, sticky="nsew")

    # 列の数、行の数を設定
    for i in range(4):
        frame_infomation_area.grid_columnconfigure(i, weight=1)
    for i in range(8):
        frame_infomation_area.grid_rowconfigure(i, weight=1)
    frame_infomation_area.grid_propagate(False)

    label_userid = tk.Label(
        frame_infomation_area, background="white", text="ユーザID")
    label_userid.grid(row=0, column=0, sticky="nsew", padx=10)

    entry_userid = tk.Entry(
        frame_infomation_area, background="white", font=('calibri', 20, 'bold'), width=15)
    entry_userid.grid(row=0, column=1, sticky="nsew", padx=10)

    label_password = tk.Label(
        frame_infomation_area, background="white", text="パスワード")
    label_password.grid(row=0, column=2, sticky="nsew", padx=10)

    entry_password = tk.Entry(
        frame_infomation_area, background="white", font=('calibri', 20, 'bold'), width=15)
    entry_password.grid(row=0, column=3, sticky="nsew", padx=10)

    # --------------------ボタンエリア---------------------
    frame_button = tk.Frame(container_working_management, background="gray")
    frame_button.grid(row=5, column=0, rowspan=1, sticky="nsew")

    # 列の数、行の数を設定
    for i in range(6):
        frame_button.grid_columnconfigure(i, weight=1)
    for i in range(2):
        frame_button.grid_rowconfigure(i, weight=1)

    button_entry = tk.Button(
        frame_button, background="PaleGoldenrod", text="入場", fg="blue", font=('calibri', 15, 'bold'))
    button_entry.grid(row=0, column=0, columnspan=3, sticky="nsew")

    button_exit = tk.Button(
        frame_button, background="lightgreen", text="退場", fg="blue", font=('calibri', 15, 'bold'))
    button_exit.grid(row=0, column=3, columnspan=3, sticky="nsew")

    button_exit_nextday = tk.Button(
        frame_button, background="lightgreen", text="日跨ぎ退場", fg="blue", font=('calibri', 15, 'bold'))
    button_exit_nextday.grid(row=1, column=0, columnspan=2, sticky="nsew")


root = tk.Tk()  # アプリの作成
root.geometry("640x590")
root.resizable(False, False)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
main_container = tk.Frame(root)
main_container.grid(row=0, column=0, sticky="nsew")

create_new_frame(main_container)

root.mainloop()  # アプリの待機

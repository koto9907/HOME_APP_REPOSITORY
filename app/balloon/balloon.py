import sys
import tkinter as tk
from tkinter import ttk
import time
import os
from datetime import datetime, timedelta
import time
from plyer import notification
from PIL import Image
import threading
import atexit
import common.util as util


def create_time_entry(frame_container):
    # 時間の選択肢リストを作成
    hours = [f"{hour:02d}" for hour in range(24)]
    minutes = [f"{minute:02d}" for minute in range(60)]

    # プルダウンメニューの作成
    frame_time_entry = tk.Frame(frame_container)

    global hour_combobox
    global minute_combobox

    hour_combobox = ttk.Combobox(frame_time_entry, values=hours, width=5)
    minute_combobox = ttk.Combobox(frame_time_entry, values=minutes, width=5)

    # デフォルトの選択肢を現在時刻に設定
    now = datetime.now()
    hour_combobox.set(int(now.hour))
    minute_combobox.set(int(now.minute))

    # ラベルとコンボボックスを配置
    hour_combobox.grid(row=0, column=0, padx=10)
    minute_combobox.grid(row=0, column=1, padx=10)

    return frame_time_entry


def show_notification(title, message, delay):
    time.sleep(delay)
    notification.notify(
        title=title,
        message=message,
        app_name=util.NAME_BALLOON,
        timeout=5  # 通知が表示される時間（秒）
    )


def get_delay_time(delay_hour, delay_minutes):
    # 現在時刻を取得
    now = datetime.now()

    # 指定された時刻を取得
    specified_time = datetime(
        now.year, now.month, now.day, delay_hour, delay_minutes)

    # 差秒を計算
    time_difference = specified_time - now

    return time_difference.seconds


def add_notification(data):
    # エントリーからタイトル、メッセージを取得
    title = title_entry.get()
    message = message_entry.get()

    # コンボボックスから通知する時間、分を取得して差を秒数に変換
    hour = int(hour_combobox.get())
    minutes = int(minute_combobox.get())
    delay_seconds = get_delay_time(hour, minutes)
    if (title and minutes and delay_seconds > 60):
        data.append([f"{hour}:{minutes}", title, message])
        update_table(data)

        # 差秒後にスレッドで通知を表示
        thread = threading.Thread(target=show_notification,
                                  args=(title, message, delay_seconds))
        threads.append(thread)
        thread.start()


def update_table(data):
    for i in tree.get_children():
        tree.delete(i)
    for item in data:
        tree.insert("", "end", values=item)


def create_new_frame(container_frame):
    def balloon_exe():
        add_notification(data)

    root = container_frame.winfo_toplevel()
    root.title(util.NAME_BALLOON)

    container_baloon = tk.Frame(container_frame)
    container_baloon.pack(fill="both", expand=True)

    # 列の数、行の数を設定
    for i in range(1):
        container_baloon.grid_columnconfigure(i, weight=1)
    for i in range(8):
        container_baloon.grid_rowconfigure(i, weight=1)

    # --------------------エントリーエリア---------------------
    frame_entry = tk.Frame(container_baloon)
    frame_entry.grid(row=0, column=0, sticky="nsew")

    # 列の数、行の数を設定
    for i in range(6):
        frame_entry.grid_columnconfigure(i, weight=1)
    for i in range(3):
        frame_entry.grid_rowconfigure(i, weight=1)

    # ラベル
    time_entry_label = tk.Label(frame_entry, text="時間")
    time_entry_label.grid(row=0, column=1, padx=10, sticky="nsew")
    # 入力ボックス
    time_entry = create_time_entry(frame_entry)
    time_entry.grid(row=1, column=1, padx=10)

    # ラベル
    global title_entry
    title_entry_label = tk.Label(
        frame_entry, text="タイトル")
    title_entry_label.grid(row=0, column=2, padx=10, sticky="nsew")
    # 入力ボックス
    title_entry = tk.Entry(frame_entry, width=10)
    title_entry.grid(row=1, column=2, padx=10)
    title_entry.insert(0, "title")

    # ラベル
    global message_entry
    message_entry_label = tk.Label(
        frame_entry, text="メッセージ")
    message_entry_label.grid(row=0, column=3, padx=10, sticky="nsew")
    # 入力ボックス
    message_entry = tk.Entry(frame_entry, width=20)
    message_entry.grid(row=1, column=3, columnspan=2, padx=10)
    message_entry.insert(0, "message")

    # --------------------ラベルエリア---------------------

    frame_tree = tk.Frame(container_baloon)
    frame_tree.grid(row=1, column=0, rowspan=6, sticky="nsew")

    COLUMNS_HEADER = ["時間", "タイトル", "メッセージ"]
    data = []

    global tree
    tree = ttk.Treeview(frame_tree, columns=[str(
        i) for i in range(len(COLUMNS_HEADER))], show='headings')
    for col in tree["columns"]:
        tree.heading(col, text=COLUMNS_HEADER[int(col)])
        tree.column(col, width=100 // len(COLUMNS_HEADER))
    tree.pack(fill="both", expand=True)

    # --------------------ボタンエリア---------------------
    global threads
    threads = []
    frame_button = tk.Frame(container_baloon)
    frame_button.grid(row=7, column=0, sticky="nsew")

    BUTTON_PADX = 15
    BUTTON_PADY = 5

    # 列の数、行の数を設定
    for i in range(5):
        frame_button.grid_columnconfigure(i, weight=1)
    for i in range(3):
        frame_button.grid_rowconfigure(i, weight=1)

    add_button = tk.Button(frame_button, text="登録", command=balloon_exe)
    add_button.grid(row=1, column=2, padx=BUTTON_PADX,
                    pady=BUTTON_PADY, sticky="nsew")


# root = tk.Tk()
# container = tk.Frame(root)
# container.pack(fill="both", expand=True)
# create_new_frame(container)

# root.geometry("640x590")
# root.mainloop()

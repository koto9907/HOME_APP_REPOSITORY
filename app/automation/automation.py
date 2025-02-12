import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyautogui
import time
import csv
import os
import common.util as util


def create_new_frame(container_frame):
    width = container_frame.winfo_width()
    height = container_frame.winfo_height()
    print(f"Frame width: {width}")
    print(f"Frame height: {height}")

    data = []  # テーブル表示データ
    COLUMNS_HEADER = ["動作", "X座標", "Y座標", "間隔"]  # テーブルヘッダー
    PATH_FOLDER = rf"{os.path.dirname(__file__)}\memory"
    PATH_FILE = rf"{PATH_FOLDER}\data.csv"

    def update_table():
        # テーブル再描画処理
        for i in tree.get_children():
            tree.delete(i)
        for item in data:
            tree.insert("", "end", values=item)

    def add_data():
        # テーブルにデータを追加する処理
        action = "クリック"  # 仮置き
        stop_time = 1  # 仮置き

        # 現在の座標を追加してテーブル表示データにデータを追加して、再描画
        time.sleep(1)
        x, y = pyautogui.position()
        data.append([action, x, y, stop_time])
        update_table()

    def clear_data():
        # テーブルクリア処理
        data.clear()
        update_table()

    def exe_data():
        # テーブル表示データの中にある処理を実行
        for item in data:
            pyautogui.moveTo(int(item[1]), int(item[2]), int(item[3]))
            pyautogui.click()

    def write_data():
        if messagebox.askyesno("確認", "現在のデータを書き出しますか？"):
            if not os.path.exists(PATH_FOLDER):
                os.makedirs(PATH_FOLDER)
            with open(PATH_FILE, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(data)

    def load_data():
        file_path = filedialog.askopenfilename(
            title="CSVファイルを選択してください", filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    clear_data()
                    reader = csv.reader(file)
                    for row in reader:
                        data.append(row)
                    update_table()
            except Exception as e:
                print(f"ファイルを開く際にエラーが発生しました: {e}")
        else:
            print("ファイルが選択されませんでした。")

    root = container_frame.winfo_toplevel()
    root.title(util.NAME_AUTOMARION)

    # ---------- テーブルエリア ----------
    WIDTH_TREE = 640
    container_automation = tk.Frame(container_frame)
    container_automation.pack(fill="both", expand=True)

    frame_tree = tk.Frame(container_automation)
    frame_tree.pack(fill="both", expand=True)

    tree = ttk.Treeview(frame_tree, columns=[str(
        i) for i in range(len(COLUMNS_HEADER))], show='headings')
    for col in tree["columns"]:
        tree.heading(col, text=COLUMNS_HEADER[int(col)])
        tree.column(col, width=WIDTH_TREE // len(COLUMNS_HEADER))
    tree.pack(fill="both", expand=True)

    # ---------- ボタンエリア ----------

    frame_button = tk.Frame(container_automation)
    frame_button.pack(side="bottom", fill="x")
    BUTTON_PADX = 15
    BUTTON_PADY = 5

    frame_button.grid_columnconfigure(0, weight=1)
    frame_button.grid_columnconfigure(1, weight=1)
    frame_button.grid_columnconfigure(2, weight=1)
    frame_button.grid_columnconfigure(3, weight=1)
    frame_button.grid_columnconfigure(4, weight=1)

    add_button = tk.Button(frame_button, text="記録", command=add_data)
    add_button.grid(row=0, column=0, padx=BUTTON_PADX,
                    pady=BUTTON_PADY, sticky="ew")

    clear_button = tk.Button(frame_button, text="クリア", command=clear_data)
    clear_button.grid(row=0, column=1, padx=BUTTON_PADX,
                      pady=BUTTON_PADY, sticky="ew")

    exe_button = tk.Button(frame_button, text="実行", command=exe_data)
    exe_button.grid(row=0, column=2, padx=BUTTON_PADX,
                    pady=BUTTON_PADY, sticky="ew")

    write_button = tk.Button(frame_button, text="書出", command=write_data)
    write_button.grid(row=0, column=3, padx=BUTTON_PADX,
                      pady=BUTTON_PADY, sticky="ew")

    load_button = tk.Button(frame_button, text="読込", command=load_data)
    load_button.grid(row=0, column=4, padx=BUTTON_PADX,
                     pady=BUTTON_PADY, sticky="ew")

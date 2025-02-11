import tkinter as tk
import os
import subprocess as sub
from PIL import Image, ImageTk
import importlib
import sys
import importlib
import common.util as util


class App:
    def __init__(self, module_name, func_name, file_name):
        # モジュールはapp配下にあるので、appをつける
        self.module_name = f"app.{module_name}"
        self.func_name = func_name

        # モジュール名からアイコンのパスを特定
        img_path = os.path.join(os.path.dirname(__file__),
                                util.PATH_IMG_HOME, file_name)
        self.img_path = img_path

    # アプリ記号時に既存のフレームを壊して新しいフレームを作成し画面に表示
    def module_execution(self, frame):
        # 画面の破壊
        for widget in frame.winfo_children():
            widget.destroy()

        # 同一階層のフォルダのパスをsys.pathに追加し、モジュール内のフレーム作成関数を取得
        sys.path.append(self.module_name)
        module = importlib.import_module(self.module_name)
        func = getattr(module, self.func_name)

        # フレーム作成関数
        func(frame)


def create_frame(container, app_list):
    APP_FRAME_ROWS = 4
    APP_FRAME_COLUMUNS = 4

    # containerのサイズに合わせて背景画像をリサイズ
    container.update_idletasks()
    container_width = container.winfo_width()
    container_height = container.winfo_height()

    # 画像の読み込み
    img_path = os.path.join(os.path.dirname(__file__),
                            util.PATH_IMG_HOME, util.IMG_BACKGROUND_HOME)
    img = Image.open(img_path)
    img = img.resize((container_width, container_height))
    photo = ImageTk.PhotoImage(img)

    # キャンバスに画像を設定
    canvas = tk.Canvas(container, width=container_width,
                       height=container_height, highlightthickness=0, bd=0)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.image = photo
    canvas.grid(row=0, column=0, rowspan=APP_FRAME_ROWS,
                columnspan=APP_FRAME_COLUMUNS, sticky="nsew")

    # 行と列の重み付け
    for i in range(APP_FRAME_ROWS):
        container.grid_rowconfigure(i, minsize=0)  # 最小サイズを小さく設定
    for i in range(APP_FRAME_COLUMUNS):
        container.grid_columnconfigure(i)

    # ボタンの配置
    for i, app in enumerate(app_list):
        row = i // APP_FRAME_ROWS
        column = i % APP_FRAME_COLUMUNS
        button = util.create_button(container, app.img_path, lambda app=app: app.module_execution(
            container))
        button.grid(row=row, column=column)


def main():
    # TODO 何か実装予定
    def hoge_hoge():
        print("hogehoge")

    # 戻るボタンの処理
    def back_home():
        # 既存の画面を壊して新たにホーム画面を作成する
        for widget in main_container.winfo_children():
            widget.destroy()
        create_frame(main_container, app_list)

    # 終了ボタンの処理
    def exit_sys():
        sys.exit()

    # --------------- メイン部分 ---------------
    root = tk.Tk()
    root.title(util.TITLE_HOME)

    root.geometry(f"{util.WIDTH_FRAME}x{util.HEIGH_FRAMET}")
    root.resizable(False, False)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    app_list = []

    # --------------- メインエリア ---------------
    # 各アプリ生成
    automation = App(util.APP_AUTOMATION,
                     util.CREATE_NEW_FRAME, util.ICON_AUTOMATION)
    app_list.append(automation)

    balloon = App(util.APP_BALLOON,
                  util.CREATE_NEW_FRAME, util.ICON_BALLOON)
    app_list.append(balloon)

    # ホーム画面生成
    main_container = tk.Frame(root)
    main_container.grid(row=0, column=0, sticky="nsew")

    main_container.after(100, back_home)  # 遅延実行しないと大きさ取得前に実行してバグる

    # --------------- 共通ボタンエリア ---------------
    button_container = tk.Frame(root)
    button_container.grid(row=1, column=0, sticky="ew")
    button_container.grid_columnconfigure(0, weight=1)
    button_container.grid_columnconfigure(1, weight=1)
    button_container.grid_columnconfigure(2, weight=1)

    # hogeボタン
    button1 = tk.Button(button_container, text="◀", height=3, command=hoge_hoge,
                        bg="lightgray", borderwidth=0, highlightthickness=0)
    button1.grid(row=0, column=0, sticky="nsew")

    # ホームに戻るボタン
    button2 = tk.Button(button_container, text="●", height=3, command=back_home,
                        bg="lightgray", borderwidth=0, highlightthickness=0)
    button2.grid(row=0, column=1, sticky="nsew")

    # プログラム終了ボタン
    button3 = tk.Button(button_container, text="■", height=3, command=exit_sys,
                        bg="lightgray", borderwidth=0, highlightthickness=0)
    button3.grid(row=0, column=2, sticky="nsew")

    # --------------------------------------------------

    root.mainloop()


if __name__ == "__main__":
    main()

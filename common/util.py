import tkinter as tk
import os
import tkinter as tk
import subprocess as sub
from PIL import Image, ImageTk, ImageDraw, ImageOps
import os
import importlib

# ★------------ 定数エリア ------------★


WIDTH_FRAME = 640
HEIGH_FRAMET = 640

# ------------- ホーム画面 -------------
TITLE_HOME = "HOME"  # GUIのタイトル
PATH_IMG_HOME = "home_img"  # ホーム画像関連のフォルダ名
IMG_BACKGROUND_HOME = "home_bg.png"  # ホームのBG画像名


# ------------- 各アプリ -------------
NAME_AUTOMARION = "automation"  # アプリ名
APP_AUTOMATION = f"{NAME_AUTOMARION}.{NAME_AUTOMARION}"  # モジュール名
ICON_AUTOMATION = f"{NAME_AUTOMARION}_icon.png"  # アプリアイコン画像名

NAME_BALLOON = "balloon"  # アプリ名
APP_BALLOON = f"{NAME_BALLOON}.{NAME_BALLOON}"  # モジュール名
ICON_BALLOON = f"{NAME_BALLOON}_icon.png"  # アプリアイコン画像名

CREATE_NEW_FRAME = "create_new_frame"

# ------------- 関数エリア -------------


def create_button(root, image_path, command):
    """
    角に丸みを帯びている画像ボタンを作成する

    Parameters
    ----------
    root: tkinterオブジェクト
    image_path: 画像のパス    
    command: ボタン押下時に実行する関数

    Returns
    -------
    fruit_price: ボタン
    """

    width = 100
    height = 100
    radius = 0
    # 画像を開く
    image = Image.open(image_path).convert("RGBA")

    # 画像サイズを調整
    image = image.resize((width, height))

    # マスク画像を作成（透明背景）
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)

    # 角を丸めた矩形を描画
    draw.rounded_rectangle([(0, 0), (width, height)], radius, fill=255)

    # マスクを適用して角を丸める
    rounded_image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    rounded_image.putalpha(mask)

    # PillowイメージをTkinterイメージに変換
    tk_image = ImageTk.PhotoImage(rounded_image)

    # ボタンの作成
    button = tk.Button(root, image=tk_image, command=command,
                       compound="center", borderwidth=0)
    button.image = tk_image  # ガベージコレクション対策のために参照を保持

    return button

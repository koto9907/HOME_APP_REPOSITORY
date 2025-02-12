import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random


class Card():  # クラス作成
    def __init__(self, name, normal, reverse,):  # インスタンス変数を持たせる
        self.name = name  # 名前
        self.normal = normal  # 正位置の意味
        self.reverse = reverse  # 逆位置の意味


# 各カード設定
TAROT_CARDS = [
    ["Fool", "無限の可能性、新しい始まり", "無計画、愚行"],
    ["Magician", "創造力、行動力", "欺瞞、不誠実"],
    ["HighPriestess", "直感、内面的な知恵", "隠された動機、欺瞞"],
    ["Empress", "豊かさ、育成", "自己犠牲、甘やかし"],
    ["Emperor", "秩序、権力", "独裁、固執"],
    ["Hierophant", "伝統、教育", "強制、革新の拒否"],
    ["Lovers", "愛、調和", "不和、選択の迷い"],
    ["Chariot", "成功、決意", "自己中心、挫折"],
    ["Strength", "勇気、忍耐", "弱気、過信"],
    ["Hermit", "内省、孤独", "孤立、無視"],
    ["Fortune", "運命の変化、幸運", "不運、予測不可能"],
    ["Justice", "公平、真実", "不正、偏見"],
    ["HangedMan", "自己犠牲、新しい視点", "犠牲の無駄、停滞"],
    ["Death", "変化、終焉", "抵抗、不安"],
    ["Temperance", "節度、調和", "不均衡、過剰"],
    ["Devil", "束縛、誘惑", "解放、克服"],
    ["Tower", "崩壊、突然の変化", "解放、再建"],
    ["Star", "希望、癒し", "失望、不安"],
    ["Moon", "直感、潜在意識", "混乱、幻覚"],
    ["Sun", "喜び、成功", "失敗、悲観"],
    ["Judgement", "再生、覚醒", "否定、後悔"],
    ["World", "完成、達成", "停滞、未完成"]
]


def flip_card(image_label, steps, delay):
    # 画像シーケンスを作成
    image_sequence = []
    CARD_HEIGHT = 280
    CARD_WIDTH = 140

    # TODO パスの取得方法は後で変える
    front_image = random.choice(TAROT_CARDS)
    front_img_path = rf"C:\py\APP_HOME\app\tarot\img\{front_image[0]}.jpg"
    front_image = Image.open(front_img_path)

    back_img_path = r"C:\py\APP_HOME\app\tarot\img\card.jpg"
    back_image = Image.open(back_img_path)

    for step in range(steps):
        scale = 1 - abs(step - steps // 2) / (steps // 2)
        scale = max(scale, 0.1)  # スケールが0.1以下にならないように調整

        img = back_image.resize(
            (int(CARD_WIDTH * scale), CARD_HEIGHT))
        img_tk = ImageTk.PhotoImage(img)
        image_sequence.append(img_tk)

    # 裏から表に切り替える
    for step in range(steps // 2, steps):
        scale = abs(step - steps // 2) / (steps // 2)
        scale = max(scale, 0.1)  # スケールが0.1以下にならないように調整
        img = front_image.resize(
            (int(CARD_WIDTH * scale), CARD_HEIGHT))
        img_tk = ImageTk.PhotoImage(img)
        image_sequence.append(img_tk)

    # アニメーションを実行
    def animate(index=0):
        if index < len(image_sequence):
            image_label.config(image=image_sequence[index])
            image_label.after(delay, animate, index + 1)

    animate()


def create_new_frame(container_frame):

    root = container_frame.winfo_toplevel()
    root.title("tarot")

    container_tarot = tk.Frame(container_frame)
    container_tarot.pack(fill="both", expand=True)

    # 列の数、行の数を設定
    for i in range(1):
        container_tarot.grid_columnconfigure(i, weight=1)
    for i in range(5):
        container_tarot.grid_rowconfigure(i, weight=1)

    # --------------------タロットエリア---------------------
    frame_card = tk.Frame(container_tarot, background="white")
    frame_card.grid(row=0, column=0, rowspan=4, sticky="nsew")

    for i in range(5):
        frame_card.grid_columnconfigure(i, weight=1)

    for i in range(5):
        frame_card.grid_rowconfigure(i, weight=1)

    label_tarot_card = tk.Label(frame_card, text="aaa", background="gold")
    label_tarot_card.grid(row=2, column=2, columnspan=1, sticky="n")

    # --------------------エントリーエリア---------------------
    frame_entry = tk.Frame(container_tarot)
    frame_entry.grid(row=4, column=0, sticky="nsew")

    # 列の数、行の数を設定
    for i in range(6):
        frame_entry.grid_columnconfigure(i, weight=1)

    BUTTON_PADX = 15
    BUTTON_PADY = 5

    # 列の数、行の数を設定
    for i in range(5):
        frame_entry.grid_columnconfigure(i, weight=1)
    for i in range(3):
        frame_entry.grid_rowconfigure(i, weight=1)

    fortune_telling_list = ["仕事", "恋愛", "金運"]

    combo = ttk.Combobox(frame_entry, values=fortune_telling_list, font=14)
    combo.set("何について占う")  # 初期値を設定
    combo.grid(row=1, column=1, padx=BUTTON_PADX,
               pady=BUTTON_PADY, sticky="nsew")

    add_button = tk.Button(frame_entry, text="占う", command=lambda: flip_card(
        label_tarot_card, steps=20, delay=50))
    add_button.grid(row=1, column=3, padx=BUTTON_PADX,
                    pady=BUTTON_PADY, sticky="nsew")


root = tk.Tk()  # アプリの作成
root.geometry(f"640x590")
root.resizable(False, False)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
main_container = tk.Frame(root)
main_container.grid(row=0, column=0, sticky="nsew")

create_new_frame(main_container)
img_path = r"C:\py\APP_HOME\app\tarot\img\Chariot\Death"


root.mainloop()  # アプリの待機

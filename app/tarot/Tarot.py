# -*- coding:utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
import random


class Card():  # クラス作成
    def __init__(self, name, normal, reverse,):  # インスタンス変数を持たせる
        self.name = name  # 名前
        self.normal = normal  # 正位置の意味
        self.reverse = reverse  # 逆位置の意味


# 各カード設定
Fool = Card("愚者",
            "自由、型にはまらない、無邪気、純粋、天真爛漫、可能性、発想力、天才",
            "軽率、わがまま、落ちこぼれ、ネガティブ、イライラ、焦り、意気消沈、注意欠陥多動性")
Magician = Card("魔術師",
                "起源、可能性、機会、才能、チャンス、感覚、創造",
                "混迷、無気力、スランプ、裏切り、空回り、バイオリズム低下、消極性")
HighPriestess = Card("女教皇",
                     "直感、感性、知性、安心、満足、期待、聡明、雰囲気",
                     "悲観、無気力、無神経、現実逃避、疑心暗鬼、孤立")
Empress = Card("女帝",
               "繁栄、豊穣、母権、愛情、情熱、豊満、包容力、女性的魅力、家庭の形成、謙虚、結婚",
               "挫折、軽率、虚栄心、嫉妬、感情的、浪費、情緒不安定、怠惰、虚言、過度なセックス")
Emperor = Card("皇帝",
               "支配、安定、成就・達成、男性的、権威、行動力、意思、責任感の強さ、軸",
               "未熟、横暴、傲岸不遜、傲慢、身勝手、独断的、意志薄弱、無責任")
Hierophant = Card("教皇",
                  "慈悲、連帯・協調性、信頼、尊敬、優しさ、思いやり、自信、法令・規律の遵守、人徳",
                  "守旧性、束縛、躊躇、不信感、独りよがり、逃避、虚栄、怠惰、お節介、固着")
Lovers = Card("恋人",
              "誘惑と戦う、自分への信頼、価値観の確立、情熱、共感、選択、絆、深い結びつき",
              "誘惑、不道徳、失恋、空回り、無視、集中力欠如、空虚、結婚生活の破綻、無干渉")
Chariot = Card("戦車",
               "勝利、征服、援軍、行動力、成功、積極力、突進力、開拓精神、独立・解放、体力無限大",
               "暴走、不注意、自分勝手、失敗、独断力、傍若無人、焦り、挫折、イライラ、視野の縮小")
Strength = Card("力",
                "力量の大きさ、強固な意志、不撓不屈、理性、自制、実行力、知恵、勇気、冷静、持久戦",
                "甘え、引っ込み思案、無気力、人任せ、優柔不断、権勢を振るう、卑下")
Hermit = Card("隠者",
              "経験則、高尚な助言、秘匿、精神、慎重、優等感、思慮深い、思いやり、単独行動",
              "閉鎖性、陰湿、消極的、無計画、誤解、悲観的、邪推、劣等感、疎通")
Wheel_of_Fortune = Card("運命の輪",
                        "転換点、幸運の到来、チャンス、変化、結果、出会い、解決、定められた運命、結束",
                        "情勢の急激な悪化、別れ、すれ違い、降格、アクシデントの到来、解放")
Justice = Card("正義",
               "公正・公平、善行、均衡、誠意、善意、両立、慈善",
               "不正、不公平、偏向、不均衡、一方通行、被告の立場に置かれる")
Hanged_Man = Card("吊された男",
                  "修行、忍耐、奉仕、努力、試練、着実、抑制、妥協",
                  "徒労、痩せ我慢、投げやり、自暴自棄、欲望に負ける")
Death = Card("死神",
             "停止、終末、破滅、離散、終局、清算、決着、死の予兆、終焉、消滅、全滅、満身創痍",
             "再スタート、新展開、上昇、挫折から立ち直る、再生、起死回生、覚醒、転生、輪廻転生")
Temperance = Card("節制",
                  "調和、自制、節度、献身、謙虚、低姿勢、平常心無限大、フェア、公平、平等、正当",
                  "浪費、消耗、生活の乱れ、不規則な生活、アンフェア、不公平、不平等、不正")
Devil = Card("悪魔",
             "裏切り、拘束、堕落、束縛、誘惑、悪循環、嗜虐的、破天荒、憎悪、嫉妬心、憤怒、破滅",
             "回復、覚醒、新たな出会い、リセット、生真面目、反省、猛省、出直し、転生")
Tower = Card("塔",
             "破壊、破滅、崩壊、災害、悲劇、悲惨、惨事、惨劇、凄惨、戦意喪失、記憶喪失、精神崩壊",
             "緊迫、突然のアクシデント、必要悪、誤解、不幸、無念、屈辱、天変地異")
Star = Card("星",
            "希望、ひらめき、願いが叶う、絶望からの再生",
            "失望、絶望、無気力、高望み、見損ない")
Moon = Card("月",
            "不安定、幻惑、現実逃避、潜在する危険、欺瞞、幻滅、猶予ない選択、洗脳",
            "失敗にならない過ち、過去からの脱却、徐々に好転、未来への希望、")
Sun = Card("太陽",
           "成功、誕生、祝福、勝利、約束された将来",
           "不調、落胆、衰退、堕胎・流産、意味のない時間")
Judgement = Card("審判",
                 "復活、結果、改善、覚醒、発展、敗者復活、転生",
                 "悔恨、行き詰まり、悪い報せ、再起不能")
World = Card("世界",
             "成就、完成、完全、総合、完遂、完璧、攻略、優勝、、完全制覇、正確無比、永遠不滅",
             "衰退、堕落、低迷、未完成、臨界点、調和の崩壊")

Cards = [Fool, Magician, HighPriestess, Empress, Hierophant,
         Lovers, Chariot, Strength, Hermit, Wheel_of_Fortune,
         Justice, Hanged_Man, Death, Temperance, Devil, Tower,
         Star, Moon, Sun, Judgement, World]

positions = ["正位置", "逆位置"]

root = tk.Tk()  # アプリの作成
# root.configure(bg="white")

root.geometry(  # アプリ画面のサイズ
    "1200x600"
)
root.title(  # アプリのタイトル
    "title"
)


def name(event):
    card = random.choice(Cards)  # どのカードか選ぶ
    position = random.choice(positions)  # 位置を選ぶ

    if position == "正位置":
        name = card.name
        word = card.normal
    elif position == "逆位置":
        name = card.name
        word = card.reverse

    label2.config(
        text=str(name)
    )
    label3.config(
        text=str(word)
    )


label1 = tk.Label(text=u'タロット占い', font=("MSゴシック", "48", "bold"))
label1.pack()

label2 = tk.Label(text=u'カード名が表示されます', font=("MSゴシック", "32", "bold"))
label2.pack()

label3 = tk.Label(text=u'意味が表示されます', font=("MSゴシック", "16", "bold"))
label3.pack()

Button1 = tk.Button(text=u'占う', width=50, height=2)
Button1.bind("<Button-1>", name)

Button1.pack()


canvas = tk.Canvas()
canvas.pack()


root.mainloop()  # アプリの待機

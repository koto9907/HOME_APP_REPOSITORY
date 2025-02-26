import tkinter as tk
from time import strftime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from functools import partial
import os


def create_new_frame(container_frame):
    # DB周りのセットアップ
    FIREBASE_COFNIG_FILENAME = r"your_firestore_config_file.json"

    FIREBASE_COFNIG_PATH = os.path.join(os.path.dirname(
        __file__), "config", FIREBASE_COFNIG_FILENAME)

    cred = credentials.Certificate(
        FIREBASE_COFNIG_PATH)
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    def check_user_infomation():
        # DBのフィールド名
        DBFIELD_USER_LIST = "user_list"
        DBFIELD_USER_PASSWORD = "user_password"

        # 入力値の取得
        user_id = entry_userid.get()
        user_password = entry_password.get()

        # ユーザーテーブル取得し、クエリを設定
        collection_user_list = db.collection(DBFIELD_USER_LIST)
        query = collection_user_list.where(
            'user_id', '==', user_id).stream()

        is_authenticated = False  # 認証OKフラグ

        # ユーザーID、パスワードが一致するか検索
        for doc in query:
            if doc.to_dict().get(DBFIELD_USER_PASSWORD) == user_password:
                is_authenticated = True
            break

        return is_authenticated

    def add_work_time(start_or_end):

        # DBのフィールド名
        DBFIELD_USER_ID = "user_id"
        DBFIELD_START_OR_END = "start_or_end"
        DBFIELD_WORK_TIME = "work_time"

        user_id = entry_userid.get()

        # 追加
        db.collection('work_time_list').add({
            DBFIELD_USER_ID: user_id,
            DBFIELD_START_OR_END: start_or_end,
            DBFIELD_WORK_TIME: strftime('%Y/%m/%d/%H:%M:%S')
        })

    def working_entry(start_or_end):
        # ユーザーID、パスワードが正しいかチェック
        authenticated_users = check_user_infomation()

        if authenticated_users:
            label_warning.config(text="勤務時間を記録しました")
            add_work_time(start_or_end)
        else:
            label_warning.config(text="ユーザーIDまたはパスワードが違います")

    def get_now_time():
        string = strftime('%H:%M:%S')  # 現在時刻を取得
        label_hour_time.config(text=string)  # ラベルのテキストを更新
        label_hour_time.after(1000, get_now_time)  #

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
        frame_time, background="black", fg="red", text=strftime('%Y/%m/%d(%a)'), font=('calibri', 20, 'bold'), anchor="nw")
    label_year_month_day.grid(row=0, column=0, rowspan=1, sticky="nsew")

    label_hour_time = tk.Label(
        frame_time, background="black", fg="red", font=('calibri', 40, 'bold'), anchor="e")
    label_hour_time.grid(row=0, column=1, columnspan=2, sticky="nsew")

    get_now_time()

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

    label_warning = tk.Label(
        frame_infomation_area, background="white", text="", fg="red")
    label_warning.grid(
        row=1, column=0, sticky="nsew", padx=10, columnspan=2)

    # --------------------ボタンエリア---------------------
    frame_button = tk.Frame(container_working_management, background="gray")
    frame_button.grid(row=5, column=0, rowspan=1, sticky="nsew")

    # 列の数、行の数を設定
    for i in range(6):
        frame_button.grid_columnconfigure(i, weight=1)
    for i in range(2):
        frame_button.grid_rowconfigure(i, weight=1)

    button_entry = tk.Button(
        frame_button, background="PaleGoldenrod", text="入場", fg="blue", font=('calibri', 15, 'bold'), command=partial(working_entry, "start"))
    button_entry.grid(row=0, column=0, columnspan=3, sticky="nsew")

    button_exit = tk.Button(
        frame_button, background="lightgreen", text="退場", fg="blue", font=('calibri', 15, 'bold'), command=partial(working_entry, "end"))
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

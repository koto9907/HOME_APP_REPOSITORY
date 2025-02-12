import tkinter as tk


def create_new_frame(container_frame):

    root = container_frame.winfo_toplevel()
    root.title("template")

    container_template = tk.Frame(container_frame)
    container_template.pack(fill="both", expand=True)


root = tk.Tk()  # アプリの作成
root.geometry(f"640x590")
root.resizable(False, False)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
main_container = tk.Frame(root)
main_container.grid(row=0, column=0, sticky="nsew")

create_new_frame(main_container)

root.mainloop()  # アプリの待機

import tkinter as tk
from tkinter import messagebox
import os


class LoginWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Đăng nhập")

        self.root.geometry("400x300")

        title = tk.Label(
            self.root,
            text="QUẢN LÝ CHI TIÊU",
            font=("Arial", 18, "bold")
        )

        title.pack(pady=20)

        tk.Label(
            self.root,
            text="Tên đăng nhập"
        ).pack()

        self.username = tk.Entry(self.root)

        self.username.pack(pady=5)

        tk.Label(
            self.root,
            text="Mật khẩu"
        ).pack()

        self.password = tk.Entry(
            self.root,
            show="*"
        )

        self.password.pack(pady=5)

        tk.Button(
            self.root,
            text="Đăng nhập",
            width=15,
            command=self.login
        ).pack(pady=20)

        self.root.mainloop()

    def login(self):

        user = self.username.get()

        pw = self.password.get()

        if user == "admin" and pw == "123":

            self.root.destroy()

            os.system("python main.py")

        else:

            messagebox.showerror(
                "Lỗi",
                "Sai tài khoản hoặc mật khẩu"
            )


LoginWindow()
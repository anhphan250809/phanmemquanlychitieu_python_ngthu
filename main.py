import tkinter as tk
from tkinter import Frame, ttk, messagebox
import json
import os
from typing import Self
import matplotlib.pyplot as plt

DATA_FILE = "dulieu.json"


class QuanLyChiTieu:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("QUẢN LÝ CHI TIÊU")

        self.root.geometry("1000x600")
        
        self.root.configure(bg="#f0f2f5")

        self.ds = []

        self.tai_du_lieu()

        title = tk.Label(
                self.root,
                text="PHẦN MỀM QUẢN LÝ CHI TIÊU",
                font=("Arial", 18, "bold")
            )

        title.pack(pady=10)

        frame = tk.Frame(self.root)

        frame.pack(pady=10)

        tk.Label(frame, text="Loại").grid(row=0, column=0)

        self.loai = ttk.Combobox(
                frame,
                values=["Thu", "Chi"]
            )

        self.loai.grid(row=0, column=1)

            
        self.so_tien = tk.Entry(frame)

        self.so_tien.grid(row=1, column=1)

        tk.Label(frame, text="Danh mục").grid(row=2, column=0)

        self.danh_muc = tk.Entry(frame)

        self.danh_muc.grid(row=2, column=1)

        tk.Label(frame, text="Ghi chú").grid(row=3, column=0)

        self.ghi_chu = tk.Entry(frame)

        self.ghi_chu.grid(row=3, column=1)

        tk.Button(
                    frame,
                    text="Thêm",
                    command=self.them
                ).grid(row=4, column=0, pady=5)

        tk.Button(
                    frame,
                    text="Xóa",
                    command=self.xoa
                ).grid(row=4, column=1, pady=5)

        tk.Button(
                    frame,
                    text="Biểu đồ",
                    command=self.ve_bieu_do
                ).grid(row=5, column=0, pady=5)

        tk.Button(
                    frame,
                    text="Thống kê",
                    command=self.thong_ke
                ).grid(row=5, column=1, pady=5)

        self.tree = ttk.Treeview(
                    self.root,
                    columns=("Loai", "Tien", "DanhMuc", "GhiChu"),
                    show="headings"
                )

        self.tree.heading("Loai", text="Loại")
        self.tree.heading("Tien", text="Số tiền")
        self.tree.heading("DanhMuc", text="Danh mục")
        self.tree.heading("GhiChu", text="Ghi chú")
        self.tree.pack(fill="both", expand=True)

        self.hien_thi()

        self.root.mainloop()

    def them(self):

            try:

                gd = {
                    "loai": self.loai.get(),
                    "tien": float(self.so_tien.get()),
                    "danh_muc": self.danh_muc.get(),
                    "ghi_chu": self.ghi_chu.get()
                }

                self.ds.append(gd)

                self.luu_du_lieu()

                self.hien_thi()

                messagebox.showinfo(
                    "Thông báo",
                    "Thêm thành công!"
                )

            except:

                messagebox.showerror(
                    "Lỗi",
                    "Dữ liệu không hợp lệ!"
                )

    def hien_thi(self):

            for item in self.tree.get_children():
                self.tree.delete(item)
            for gd in self.ds:

                self.tree.insert(
                    "",
                    tk.END,
                    values=(
                        gd["loai"],
                        gd["tien"],
                        gd["danh_muc"],
                        gd["ghi_chu"]
                    )
                )

    def xoa(self):

        selected = self.tree.selection()

        if not selected:
            return

        index = self.tree.index(selected[0])

        self.ds.pop(index)

        self.luu_du_lieu()

        self.hien_thi()

    def luu_du_lieu(self):

        with open(
            DATA_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.ds,
                file,
                ensure_ascii=False,
                indent=4
            )

    def tai_du_lieu(self):

        if os.path.exists(DATA_FILE):

            with open(
                DATA_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                try:
                    self.ds = json.load(file)

                except:
                    self.ds = []

    def ve_bieu_do(self):

        thu = 0
        chi = 0

        for gd in self.ds:

            if gd["loai"] == "Thu":
                thu += gd["tien"]

            else:
                chi += gd["tien"]

        plt.pie(
            [thu, chi],
            labels=["Thu", "Chi"],
            autopct="%1.1f%%"
        )

        plt.title("Biểu đồ thu chi")

        plt.show()

    def thong_ke(self):

        thu = 0
        chi = 0

        for gd in self.ds:

            if gd["loai"] == "Thu":
                thu += gd["tien"]

            else:
                chi += gd["tien"]

        so_du = thu - chi

        messagebox.showinfo(
            "Thống kê",
            f"Tổng thu: {thu:,.0f} VNĐ\n"
            f"Tổng chi: {chi:,.0f} VNĐ\n"
            f"Số dư: {so_du:,.0f} VNĐ"
        )


QuanLyChiTieu()
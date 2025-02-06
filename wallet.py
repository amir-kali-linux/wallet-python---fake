#github -----> https://github.com/amir-kali-linux/
import tkinter as tk
from tkinter import messagebox
import time
time.sleep(1)
print("https://github.com/amir-kali-linux/")
class WalletApp:
    def __init__(self, root):
        self.root = root
        self.root.title('wallets')
        self.balance = 0

        self.label = tk.Label(root, text="موجودی: 0 تومان")
        self.label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.add_button = tk.Button(root, text="موجودی افزودن", command=self.add_balance)
        self.add_button.pack()

        self.withdraw_button = tk.Button(root, text="موجودی برداشت", command=self.withdraw_balance)
        self.withdraw_button.pack()

    def add_balance(self):
        amount = int(self.amount_entry.get())
        self.balance += amount
        self.label.config(text=f"موجودی: {self.balance} تومان")
        messagebox.showinfo("موفقیت", f"{amount} موجودی به نومان اضافه شد.")

    def withdraw_balance(self):
        amount = int(self.amount_entry.get())
        if amount > self.balance:
            messagebox.showerror("خطا", "موجودی کافی نیست")
        else:
            self.balance -= amount
            self.label.config(text=f"موجودی: {self.balance} تومان")
            messagebox.showinfo("موفقیت", f"{amount} تومان از موجویبرداشت شد")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    root.resizable( 0 , 0 )
    app = WalletApp(root)
    root.mainloop()
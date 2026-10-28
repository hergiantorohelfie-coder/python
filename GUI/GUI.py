import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - SIAKAD")
        self.root.geometry("380x250")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.db_config = {
            'host': 'localhost',      
            'user': 'root',           
            'password': '',           
            'database': 'siakad'      
        }

        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        lbl_title = tk.Label(
            main_frame, 
            text="SIAKAD LOGIN",      
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",            
            fg="black"                
        )
        lbl_title.pack(pady=(0, 20))

        form_frame = tk.Frame(main_frame, bg="#f0f0f0")
        form_frame.pack()

        lbl_user = tk.Label(form_frame, text="Username:", font=("Arial", 10), bg="#f0f0f0", anchor="e", width=10)
        lbl_user.grid(row=0, column=0, padx=5, pady=6, sticky="e")
        self.entry_nip = tk.Entry(form_frame, font=("Arial", 10), width=22, relief=tk.SOLID, bd=1)
        self.entry_nip.grid(row=0, column=1, padx=5, pady=6)
        self.entry_nip.focus()

        lbl_pass = tk.Label(form_frame, text="Password:", font=("Arial", 10), bg="#f0f0f0", anchor="e", width=10)
        lbl_pass.grid(row=1, column=0, padx=5, pady=6, sticky="e")
        self.entry_email = tk.Entry(form_frame, font=("Arial", 10), width=22, show="*", relief=tk.SOLID, bd=1)
        self.entry_email.grid(row=1, column=1, padx=5, pady=6)

        btn_login = tk.Button(
            main_frame, 
            text="Login",             
            font=("Arial", 10, "bold"),
            bg="#4CAF50",             
            fg="white",               
            activebackground="#45a049",
            activeforeground="white", 
            width=15,                 
            bd=1,                     
            cursor="hand2",           
            command=self.proses_login 
        )
        btn_login.pack(pady=(20, 0))

        self.root.bind('<Return>', lambda event: self.proses_login())

    def proses_login(self):
        nip = self.entry_nip.get().strip()
        email = self.entry_email.get().strip()

        if not nip or not email:
            messagebox.showwarning("Peringatan", "Username (NIP) dan Password (Email) wajib diisi!")
            return

        conn = None
        cursor = None

        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor(dictionary=True)

            query = "SELECT nip, nama_dosen, email FROM dosen WHERE nip = %s AND email = %s"
            cursor.execute(query, (nip, email))
            user = cursor.fetchone()

            if user:
                messagebox.showinfo("Berhasil", f"Login berhasil!\nSelamat datang, {user['nama_dosen']}.")
                self.buka_dashboard(user)
            else:
                messagebox.showerror("Gagal", "Login gagal! Username atau Password salah.")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Koneksi database bermasalah:\n{err}")
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def buka_dashboard(self, user):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
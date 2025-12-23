import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

class ChatClient:
    def __init__(self):
        # self.HOST = socket.gethostname()
        self.HOST = "10.50.184.2"
        self.PORT = 55555

        self.root = tk.Tk()
        self.root.title("Python Chat App")
        self.root.geometry("400x500")
        
        self.root.withdraw()
        self.nickname = simpledialog.askstring("Nickname", "Pilih nickname kamu:", parent=self.root)
        self.root.deiconify()

        if not self.nickname:
            self.root.destroy()
            return

        self.gui_setup()
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((self.HOST, self.PORT))
        except:
            messagebox.showerror("Error", "Tidak bisa terhubung ke server")
            self.root.destroy()
            return

        receive_thread = threading.Thread(target=self.receive_message)
        receive_thread.daemon = True
        receive_thread.start()

        self.root.mainloop()

    def gui_setup(self):
        self.chat_area = scrolledtext.ScrolledText(self.root)
        self.chat_area.pack(padx=20, pady=5, expand=True, fill='both')
        self.chat_area.config(state='disabled')

        self.msg_entry = tk.Entry(self.root)
        self.msg_entry.pack(padx=20, pady=5, fill='x')
        self.msg_entry.bind("<Return>", self.write_message)

        self.send_btn = tk.Button(self.root, text="Kirim", command=self.write_message)
        self.send_btn.pack(padx=20, pady=5)

    def write_message(self, event=None):
        message = f"{self.nickname}: {self.msg_entry.get()}"
        if self.msg_entry.get().strip() != "":
            self.client.send(message.encode('utf-8'))
            self.msg_entry.delete(0, 'end')

    def receive_message(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    self.chat_area.config(state='normal')
                    self.chat_area.insert('end', message + '\n')
                    self.chat_area.yview('end')
                    self.chat_area.config(state='disabled')
            except:
                print("Terjadi kesalahan / Koneksi putus")
                self.client.close()
                break

if __name__ == "__main__":
    ChatClient()
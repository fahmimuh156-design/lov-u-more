import tkinter as tk
from tkinter import messagebox

def create_apology_app():
    # Membuat jendela utama
    root = tk.Tk()
    root.title("A Special Message For You ❤️")
    root.geometry("500x650")
    root.configure(bg="#ffe6e8")  # Warna latar belakang pastel pink
    root.resizable(False, False)

    # --- GAMBAR KARTUN / CANVAS ---
    canvas = tk.Canvas(root, width=200, height=180, bg="#ffe6e8", highlightthickness=0)
    canvas.pack(pady=(20, 10))

    # Menggambar Karakter Beruang Lucu / Hati
    # Telinga
    canvas.create_oval(35, 35, 75, 75, fill="#8B5A2B", outline="")
    canvas.create_oval(125, 35, 165, 75, fill="#8B5A2B", outline="")
    canvas.create_oval(45, 45, 65, 65, fill="#FFC0CB", outline="")
    canvas.create_oval(135, 45, 155, 65, fill="#FFC0CB", outline="")
    
    # Kepala
    canvas.create_oval(40, 40, 160, 150, fill="#A0522D", outline="")
    
    # Moncong & Hidung
    canvas.create_oval(80, 90, 120, 130, fill="#FFF8DC", outline="")
    canvas.create_oval(93, 98, 107, 110, fill="#4A2E10", outline="")
    
    # Mata (Sedih/Minta Maaf)
    canvas.create_arc(65, 75, 85, 95, start=30, extent=120, style=tk.ARC, width=3)
    canvas.create_arc(115, 75, 135, 95, start=30, extent=120, style=tk.ARC, width=3)
    
    # Air Mata Lucu
    canvas.create_oval(60, 95, 68, 108, fill="#87CEEB", outline="")
    canvas.create_oval(132, 95, 140, 108, fill="#87CEEB", outline="")

    # Hati Besar di Dada
    canvas.create_polygon(100, 175, 70, 140, 70, 125, 85, 115, 100, 130, 115, 115, 130, 125, 130, 140, 
                          fill="#FF4D6D", outline="", smooth=True)

    # --- JUDUL ---
    title_label = tk.Label(
        root, 
        text="I am So Sorry, My Love 🥺", 
        font=("Helvetica", 16, "bold"), 
        bg="#ffe6e8", 
        fg="#d63384"
    )
    title_label.pack(pady=5)

    # --- SURAT / APOLOGY LETTER (BAHASA INGGRIS) ---
    letter_text = (
        "My Dearest,\n\n"
        "I'm writing this because my words fail me when I see you upset. "
        "I am truly, deeply sorry for hurting your feelings. It was never "
        "my intention to make you feel bad or disappointed.\n\n"
        "You mean the absolute world to me, and seeing a smile on your face "
        "is my favorite thing. I promise to be better, listen more, "
        "and treat your heart with the care it deserves.\n\n"
        "Please forgive me? 💕"
    )

    text_box = tk.Text(
        root, 
        wrap=tk.WORD, 
        font=("Georgia", 11), 
        bg="#ffffff", 
        fg="#333333", 
        height=10, 
        width=42, 
        bd=0, 
        padx=15, 
        pady=15
    )
    text_box.insert(tk.END, letter_text)
    text_box.configure(state="disabled")  # Membuat teks tidak bisa diubah oleh pengguna
    text_box.pack(pady=10)

    # --- FUNGSI TOMBOL INTERAKTIF ---
    def on_forgive():
        messagebox.showinfo(
            "Yay! ❤️", 
            "Thank you for forgiving me! I love you so much! 💖\nLet's get some ice cream/boba together!"
        )
        root.destroy()

    def on_not_yet():
        messagebox.showwarning(
            "Oh no... 💔", 
            "I understand... I will keep trying to make it up to you until you smile again! 🥺❤️"
        )

    # --- TOMBOL ---
    button_frame = tk.Frame(root, bg="#ffe6e8")
    button_frame.pack(pady=10)

    btn_forgive = tk.Button(
        button_frame, 
        text="I Forgive You ❤️", 
        font=("Helvetica", 11, "bold"), 
        bg="#ff758f", 
        fg="white", 
        activebackground="#ff4d6d", 
        activeforeground="white", 
        bd=0, 
        padx=15, 
        pady=8, 
        cursor="hand2", 
        command=on_forgive
    )
    btn_forgive.grid(row=0, column=0, padx=10)

    btn_not_yet = tk.Button(
        button_frame, 
        text="Still Thinking... 🥺", 
        font=("Helvetica", 10), 
        bg="#cccccc", 
        fg="#333333", 
        bd=0, 
        padx=10, 
        pady=8, 
        cursor="hand2", 
        command=on_not_yet
    )
    btn_not_yet.grid(row=0, column=1, padx=10)

    # Jalankan aplikasi
    root.mainloop()

if __name__ == "__main__":
    create_apology_app()
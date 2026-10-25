import tkinter as tk
import time

LYRICS = [
    (0,  "I want one ticket out of your heavy gaze"),
    (4,  "I want one ticket off of your carousel"),
    (9,  "But you should know that I die slow"),
    (13, "Running through the halls of your haunted home"),
    (18, "And the toughest part is that we both know"),
    (22, "What happened to you"),
    (24, "Why you're out on your own"),
    (26, "Merry Christmas, please don't call"),
    (31, "Merry Christmas, I'm not yours at all"),
    (36, "Merry Christmas, please don't call me"),
    (41, "Please don't call me"),
    (45, "Please don't call me"),
    (49, "Please don't call me")
]

BOX_W, BOX_H = 600, 250
FONT = ("Helvetica", 16, "bold")
BG_COLOR = "#8A0000"
FG_COLOR = "#FFFFFF"

root = tk.Tk()
root.title("Merry Christmas, Please Don't Call - Lyrics")
root.geometry(f"{BOX_W}x{BOX_H}")
root.configure(bg=BG_COLOR)

label = tk.Label(
    root, 
    text="", 
    font=FONT, 
    bg=BG_COLOR, 
    fg=FG_COLOR, 
    wraplength=BOX_W - 40, 
    justify="center"
)
label.pack(expand=True)

start_time = time.time()
current_index = -1

def update_lyrics():
    global current_index
    elapsed = time.time() - start_time
    
    target_index = -1
    for i, (ts, text) in enumerate(LYRICS):
        if elapsed >= ts:
            target_index = i
            
    if target_index != current_index and target_index != -1:
        current_index = target_index
        label.config(text=LYRICS[current_index][1])
        
    root.after(100, update_lyrics)

update_lyrics()
root.mainloop()
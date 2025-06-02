import tkinter as tk
import pygame


pygame.mixer.init()


def play_note(note):
    pygame.mixer.music.load(f"sounds/{note}.mp3")
    pygame.mixer.music.play()


root = tk.Tk()
root.title("Realistic Piano in Python")
root.geometry("700x300")
root.resizable(False, False)


canvas = tk.Canvas(root, width=700, height=300)
canvas.pack()


white_keys = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3']
white_key_buttons = []
white_key_width = 100

for i, note in enumerate(white_keys):
    btn = tk.Button(root, bg="white", bd=1, relief="raised",
                    command=lambda n=note: play_note(n))
    btn.place(x=i * white_key_width, y=50, width=white_key_width, height=200)
    white_key_buttons.append(btn)


black_keys = [('Db3', 70), ('Eb3', 170), ('Gb3', 370), ('Ab3', 470), ('Bb3', 570)]
black_key_buttons = []

for note, x_pos in black_keys:
    btn = tk.Button(root, bg="black", fg="white", bd=1, relief="raised",
                    command=lambda n=note: play_note(n))
    btn.place(x=x_pos, y=50, width=60, height=130)
    black_key_buttons.append(btn)


tk.Label(root, text="Python Piano", font=("Arial", 16, "bold")).place(x=280, y=10)

root.mainloop()

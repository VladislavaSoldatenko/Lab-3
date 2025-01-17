import tkinter as tk
from tkinter import messagebox

def generate_key():
    first_part = entry.get().upper()
    if len(first_part) != 5 or not all(c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' for c in first_part):
        messagebox.showerror("Ошибка", "Введите корректную первую часть ключа (5 символов A-Z, 0-9)")
        return

    second_part = ''.join([shift_char(c, 3) for c in first_part])

    third_part = ''.join([shift_char(c, -5) for c in first_part])

    full_key = f"{first_part}-{second_part}-{third_part}"
    key_label.config(text=full_key)

def shift_char(c, shift):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    index = chars.find(c)
    if index == -1:
        return c
    new_index = (index + shift) % len(chars)
    return chars[new_index]

window = tk.Tk()
window.title("Keygen Generator")
window.geometry("800x500")

try:
    bg_img = tk.PhotoImage(file='minecraft-creeper.png')  
    label_bg = tk.Label(window, image=bg_img)
    label_bg.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    messagebox.showerror("Ошибка", f"Не удалось загрузить фоновое изображение: {e}")
    label_bg = tk.Label(window, text="Фоновое изображение не найдено", bg="white", font=('Segoe UI', 14))
    label_bg.place(relwidth=1, relheight=1)

entry_label = tk.Label(window, text="Введите первую часть ключа (5 символов):", font=('Segoe UI', 14), bg="white")
entry_label.place(relx=0.1, rely=0.2)
entry = tk.Entry(window, width=20, font=('Segoe UI', 14))
entry.place(relx=0.1, rely=0.3)

generate_button = tk.Button(window, text="Сгенерировать ключ", command=generate_key, font=('Segoe UI', 14, 'bold'), bg="lightblue")
generate_button.place(relx=0.1, rely=0.5)

key_label = tk.Label(window, text="", font=('Consolas', 18, 'bold'), bg="white", fg="blue")
key_label.place(relx=0.1, rely=0.7)

window.mainloop()
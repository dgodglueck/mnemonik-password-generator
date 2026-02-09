import tkinter as tk
from tkinter import messagebox

def generate_password():
    sentence = entry_input.get()
    if not sentence.strip():
        messagebox.showwarning("Fehler", "Bitte gib einen Satz ein!")
        return

    words = sentence.split()
    password = "".join([word[0] for word in words])
    
    entry_output.config(state='normal')
    entry_output.delete(0, tk.END)
    entry_output.insert(0, password)
    entry_output.config(state='readonly')
    
    char_count = len(password)
    label_char_count.config(text=f"Zeichenanzahl: {char_count}")

def copy_to_clipboard():
    password = entry_output.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Erfolg", "Passwort in die Zwischenablage kopiert!")
    else:
        messagebox.showwarning("Fehler", "Generiere erst ein Passwort!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Passwort-Generator")
    root.geometry("440x320")
    root.eval('tk::PlaceWindow . center')

    label_instruction = tk.Label(root, text="Gib deinen Merksatz ein:", font=("Arial", 10))
    label_instruction.pack(pady=10)

    entry_input = tk.Entry(root, width=50)
    entry_input.pack(pady=5, padx=20)
    entry_input.insert(0, "In meinem Kühlschrank stehen 3 Flaschen Cola und 1 Glas Senf!")

    btn_generate = tk.Button(root, text="Passwort generieren", command=generate_password, 
                            bg="#005D9F", fg="white", font=("Arial", 10, "bold"))
    btn_generate.pack(pady=15)

    label_result = tk.Label(root, text="Dein Passwort:")
    label_result.pack()

    entry_output = tk.Entry(root, width=30, font=("Courier", 12, "bold"), 
                             state='readonly', justify='center')
    entry_output.pack(pady=5)

    label_char_count = tk.Label(root, text="Zeichenanzahl: 0", font=("Arial", 9), fg="#666")
    label_char_count.pack(pady=2)

    btn_copy = tk.Button(root, text="In Zwischenablage kopieren", command=copy_to_clipboard, 
                         bg="#e0e0e0", font=("Arial", 9))
    btn_copy.pack(pady=10)

    root.mainloop()
import tkinter as tk
import pyperclip

# Convert text
SMALL_CAPS_MAP = {
    'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ғ',
    'g': 'ɢ', 'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ',
    'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ',
    's': 's', 't': 'ᴛ', 'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x',
    'y': 'ʏ', 'z': 'ᴢ'
}

def convert_to_small_caps(event=None):

    input_text = input_text_box.get("1.0", "end-1c")
    output_text = ""
    i = 0
    while i < len(input_text):
        if input_text[i:i+2] in ("&a", "&b", "&c", "&d", "&e", "&f", "&k", "&l", "&m", "&n", "&o", "&r"):
            output_text += input_text[i:i+2]
            i += 2
        else:
            char = input_text[i]
            if char.isupper():
                output_text += char
            else:
                output_text += SMALL_CAPS_MAP.get(char.lower(), char)
            i += 1
    output_text_box.config(state="normal")
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert("1.0", output_text)
    output_text_box.config(state="disabled")
    pyperclip.copy(output_text)

# Copy text
def copy_output_to_clipboard():
    output_text = output_text_box.get("1.0", "end-1c")
    pyperclip.copy(output_text)

# Main window
window = tk.Tk()
window.title("Small Caps Converter") 
window.configure(bg="#242424")
window.bind('<Control-c>', convert_to_small_caps)

# App width and height
app_w = 600
app_h = 340

# Center on open
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()

x = (screen_w / 2) - (app_w / 2)
y = (screen_h / 2) - (app_h / 2)

window.geometry(f"{app_w}x{app_h}+{int(x)}+{int(y)}")

# No resize
window.minsize((app_w), (app_h))
window.maxsize((app_w), (app_h))

# Input label and text box
input_label = tk.Label(window, text="Input:", font=("Consolas"), fg="white", bg="#242424")
input_label.grid(row=0, column=0, padx=10, pady=10)
input_text_box = tk.Text(window, width=53, height=5, font=("Consolas", 12), bg="#424242", fg="white", bd=0)
input_text_box.grid(row=0, column=1, padx=10, pady=10)


# Output label and text box
output_label = tk.Label(window, text="Output:", font=("Consolas"), fg="white", bg="#242424")
output_label.grid(row=1, column=0, padx=10, pady=10)
output_text_box = tk.Text(window, width=53, height=5, font=("Consolas", 12), bg="#424242", fg="white", bd=0)
output_text_box.grid(row=1, column=1, padx=10, pady=10)
output_text_box.config(state="disabled")

# Convert and copy buttons / Enter
convert_button = tk.Button(window, text="Convert", cursor="hand2", command=convert_to_small_caps, font=("Consolas", 12), padx=10, pady=10, bg="#007acc", activebackground="#00367D", activeforeground="white", bd=0, fg="white")
convert_button.place(x=100, y=240)
copy_button = tk.Button(window, text="Copy to Clipboard", cursor="hand2", command=copy_output_to_clipboard, font=("Consolas", 12), padx=10, pady=10, bg="#007acc", activebackground="#00367D", activeforeground="white", bd=0, fg="white")
copy_button.place(x=200, y=240)
enter_key = tk.Label(window, text="Press CTRL + C to Convert and Copy without using the buttons", font=("Consolas"), fg="white", bg="#242424")
enter_key.place(x=5, y=300)

# GUI loop
window.mainloop()

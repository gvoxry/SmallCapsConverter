import tkinter as tk
import pyperclip

# Convert text
def convert_to_small_caps(event=None):
    input_text = input_text_box.get("1.0", "end-1c")
    output_text = input_text.lower().replace("a", "ᴀ").replace("b", "ʙ").replace("c", "ᴄ").replace("d", "ᴅ").replace("e", "ᴇ").replace("f", "ꜰ").replace("g", "ɢ").replace("h", "ʜ").replace("i", "ɪ").replace("j", "ᴊ").replace("k", "ᴋ").replace("l", "ʟ").replace("m", "ᴍ").replace("n", "ɴ").replace("o", "ᴏ").replace("p", "ᴘ").replace("q", "ǫ").replace("r", "ʀ").replace("s", "s").replace("t", "ᴛ").replace("u", "ᴜ").replace("v", "ᴠ").replace("w", "ᴡ").replace("x", "x").replace("y", "ʏ").replace("z", "ᴢ")
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
input_text_box.bind('<Shift-Return>', convert_to_small_caps)


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
enter_key = tk.Label(window, text="Press Shift + Enter to Convert and Copy without using the buttons", font=("Consolas"), fg="white", bg="#242424")
enter_key.place(x=5, y=300)

# GUI loop
window.mainloop()
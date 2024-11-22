import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import PlayWithGemini

# Function to be called on button click
def generate_and_play_on_click():
    text_widget.delete(1.0, tk.END)
    user_input = entry.get()  # Get input from Entry widget
    language =  languages.get(language_combo.get(), "en")
    print(user_input)
    response = PlayWithGemini.translate(PlayWithGemini.generate_critic(user_input), language)
    text_widget.insert(tk.END, response + '\n')
    text_widget.yview(tk.END)
    root.update_idletasks()

    PlayWithGemini.speak_without_save(response, language)

# Create the main window
root = tk.Tk()
root.title("Movie Critic: Content Generator")

# Set window size
root.geometry("600x500")

# Create a label and an entry field for user input
label = tk.Label(root, text="Enter movie name:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

label = tk.Label(root, text="Output language:")
label.pack(pady=10)

# Language selection (combo box)
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese": "zh",
    "Japanese": "ja",
    "Telugu" : "te"
    # Add more languages here as needed
}
language_combo = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
language_combo.current(0)  # Set default language
language_combo.pack()

# Create a button that will trigger the content generation and speech
button = tk.Button(root, text="Generate & Play", command=generate_and_play_on_click)
button.pack(pady=20)


# Create a Frame to hold the Text widget and the Scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)
scrollbar = tk.Scrollbar(frame)

# Create a Text widget with scrollbars
text_widget = tk.Text(frame, wrap="word", height=10, width=10, yscrollcommand=scrollbar.set)
text_widget.pack(side="left", fill="both", expand=True)

# Attach the scrollbar to the Text widget
scrollbar.config(command=text_widget.yview)
scrollbar.pack(side="right", fill="y")


# Start the Tkinter event loop
root.mainloop()
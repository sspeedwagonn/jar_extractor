import tkinter as tk
from tkinter import filedialog
import zipfile
import os

selected_jar_file = ""
selected_extraction_folder = ""

def choose_jar_file():
    global selected_jar_file
    selected_jar_file = filedialog.askopenfilename(filetypes=[("Jar files", "*.jar")])
    if selected_jar_file:
        jar_file_label.config(text=f"Selected JAR File: {os.path.basename(selected_jar_file)}")
        check_extraction_ready()

def choose_extraction_folder():
    global selected_extraction_folder
    selected_extraction_folder = filedialog.askdirectory()
    if selected_extraction_folder:
        extraction_folder_label.config(text=f"Extraction Folder: {selected_extraction_folder}")
        check_extraction_ready()

def check_extraction_ready():
    if selected_jar_file and selected_extraction_folder:
        extract_button.config(state=tk.NORMAL)
    else:
        extract_button.config(state=tk.DISABLED)

def extract_jar():
    global selected_jar_file, selected_extraction_folder
    jar_base_name = os.path.splitext(os.path.basename(selected_jar_file))[0]
    
    extract_dir = os.path.join(selected_extraction_folder, f"{jar_base_name}_Extracted")
    os.makedirs(extract_dir, exist_ok=True)

    try:
        with zipfile.ZipFile(selected_jar_file, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        result_label.config(text=f"Extraction completed.\nFiles saved to {extract_dir}")
    except Exception as e:
        result_label.config(text=f"Extraction failed: {str(e)}")

    selected_jar_file = ""
    selected_extraction_folder = ""
    jar_file_label.config(text="")
    extraction_folder_label.config(text="")
    check_extraction_ready()

root = tk.Tk()
root.title("JAR Extractor")

choose_jar_button = tk.Button(root, text="Choose a JAR File...", command=choose_jar_file)
choose_folder_button = tk.Button(root, text="Choose Extraction Folder...", command=choose_extraction_folder)
extract_button = tk.Button(root, text="Extract", command=extract_jar, state=tk.DISABLED)
jar_file_label = tk.Label(root, text="")
extraction_folder_label = tk.Label(root, text="")
result_label = tk.Label(root, text="", wraplength=300)

choose_jar_button.grid(row=0, column=0, padx=10, pady=10)
choose_folder_button.grid(row=1, column=0, padx=10, pady=10)
extract_button.grid(row=2, column=0, padx=10, pady=10)
jar_file_label.grid(row=0, column=1, padx=10, pady=10)
extraction_folder_label.grid(row=1, column=1, padx=10, pady=10)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

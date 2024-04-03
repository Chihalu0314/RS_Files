import os
import shutil
import tkinter as tk
from tkinter import filedialog, simpledialog, ttk

def rename_files(directory, new_name):
    for i, filename in enumerate(os.listdir(directory), start=1):
        if os.path.isdir(os.path.join(directory, filename)):
            continue
        extension = os.path.splitext(filename)[1]
        new_filename = f"{new_name}_{i}{extension}"
        source = os.path.join(directory, filename)
        destination = os.path.join(directory, new_filename)
        
        os.rename(source, destination)

def create_folders(directory, num_folders, folder_names):
    for i in range(num_folders):
        folder_name = folder_names[i] if i < len(folder_names) else f"NoName{i+1}"
        os.makedirs(os.path.join(directory, folder_name), exist_ok=True)

def delete_files_with_extension(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            os.remove(os.path.join(directory, filename))

def delete_all_folders(directory):
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            shutil.rmtree(os.path.join(directory, filename))

def browse_directory():
    directory = filedialog.askdirectory()
    return directory

def main():
    window = tk.Tk()
    window.title("File Renamer, Folder Creator and File Deleter")

    # ウィンドウを常に最前面に表示
    window.attributes('-topmost', True)

    # ウィンドウのサイズを設定
    window.geometry('500x300')

    frame1 = tk.Frame(window)
    frame1.pack(pady=10)

    browse_button = tk.Button(frame1, text="Browse", command=lambda: directory_entry.insert(tk.END, browse_directory()))
    browse_button.pack(side=tk.LEFT, padx=5)

    directory_entry = tk.Entry(frame1)
    directory_entry.pack(side=tk.LEFT, padx=5)

    frame2 = tk.Frame(window)
    frame2.pack(pady=10)

    new_name_label = tk.Label(frame2, text="New Name")
    new_name_label.pack(side=tk.LEFT, padx=5)

    new_name_entry = tk.Entry(frame2)
    new_name_entry.pack(side=tk.LEFT, padx=5)

    rename_file_button = tk.Button(frame2, text="Rename Files", command=lambda: rename_files(directory_entry.get(), new_name_entry.get()))
    rename_file_button.pack(side=tk.LEFT, padx=5)

    frame3 = tk.Frame(window)
    frame3.pack(pady=10)

    num_folders_label = tk.Label(frame3, text="Number of Folders")
    num_folders_label.pack(side=tk.LEFT, padx=5)

    num_folders_var = tk.StringVar()
    num_folders_combobox = ttk.Combobox(frame3, textvariable=num_folders_var)
    num_folders_combobox['values'] = [str(i) for i in range(1, 21)]
    num_folders_combobox.pack(side=tk.LEFT, padx=5)

    create_folders_button = tk.Button(frame3, text="Create Folders", command=lambda: create_folders(directory_entry.get(), int(num_folders_var.get()), simpledialog.askstring("Input", "Enter folder names separated by commas").split(',')))
    create_folders_button.pack(side=tk.LEFT, padx=5)

    frame4 = tk.Frame(window)
    frame4.pack(pady=10)

    extension_label = tk.Label(frame4, text="Extension")
    extension_label.pack(side=tk.LEFT, padx=5)

    extension_var = tk.StringVar()
    extension_combobox = ttk.Combobox(frame4, textvariable=extension_var)
    extension_combobox['values'] = ('.txt', '.docx', '.xlsx', '.pptx', '.pdf', '.jpg', '.png', '.gif', '.mp4', '.mp3', '.wav')
    extension_combobox.pack(side=tk.LEFT, padx=5)

    delete_files_button = tk.Button(frame4, text="Delete Files", command=lambda: delete_files_with_extension(directory_entry.get(), extension_var.get()))
    delete_files_button.pack(side=tk.LEFT, padx=5)

    frame5 = tk.Frame(window)
    frame5.pack(pady=10)

    delete_folders_button = tk.Button(frame5, text="Delete All Folders", command=lambda: delete_all_folders(directory_entry.get()))
    delete_folders_button.pack(side=tk.LEFT, padx=5)

    window.mainloop()

if __name__ == "__main__":
    main()

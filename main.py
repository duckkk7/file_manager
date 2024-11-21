import os
import shutil
import stat
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog


def create_directory():
    path = filedialog.askdirectory()
    if path:
        try:
            os.makedirs(path)
            messagebox.showinfo("Success", f"Directory '{path}' created successfully.")
        except OSError as error:
            messagebox.showerror("Error", f"Error creating directory '{path}': {error}")

def open_directory():
    path = filedialog.askdirectory()
    if path:
        try:
            os.startfile(path)  # For Windows
            # os.system(f"open {path}")  # For MacOS
        except OSError as error:
            messagebox.showerror("Error", f"Error opening directory '{path}': {error}")

def move_directory():
    src = filedialog.askdirectory()
    if src:
        dst = filedialog.askdirectory()
        if dst:
            try:
                shutil.move(src, dst)
                messagebox.showinfo("Success", f"Directory '{src}' moved to '{dst}' successfully.")
            except OSError as error:
                messagebox.showerror("Error", f"Error moving directory '{src}': {error}")

def rename_directory():
    src = filedialog.askdirectory()
    if src:
        dst = filedialog.asksaveasfilename(defaultextension="", initialfile=os.path.basename(src))
        if dst:
            try:
                os.rename(src, dst)
                messagebox.showinfo("Success", f"Directory '{src}' renamed to '{dst}' successfully.")
            except OSError as error:
                messagebox.showerror("Error", f"Error renaming directory '{src}': {error}")

def copy_directory():
    src = filedialog.askdirectory()
    if src:
        dst = filedialog.askdirectory()
        if dst:
            try:
                shutil.copytree(src, dst)
                messagebox.showinfo("Success", f"Directory '{src}' copied to '{dst}' successfully.")
            except OSError as error:
                messagebox.showerror("Error", f"Error copying directory '{src}': {error}")

def delete_directory():
    path = filedialog.askdirectory()
    if path:
        try:
            shutil.rmtree(path)
            messagebox.showinfo("Success", f"Directory '{path}' deleted successfully.")
        except OSError as error:
            messagebox.showerror("Error", f"Error deleting directory '{path}': {error}")

def change_directory_attributes():
    path = filedialog.askdirectory()
    if path:
        attributes = simpledialog.askstring("Input", "Enter the attributes to change:")
        if attributes:
            try:
                for root, dirs, files in os.walk(path):
                    for dir in dirs:
                        dir_path = os.path.join(root, dir)
                        os.chmod(dir_path, stat.S_IWRITE)  # Example: make writable
                messagebox.showinfo("Success", f"Attributes of directory '{path}' changed successfully.")
            except OSError as error:
                messagebox.showerror("Error", f"Error changing attributes of directory '{path}': {error}")

def search_directory():
    path = filedialog.askdirectory()
    if path:
        keyword = simpledialog.askstring("Input", "Enter the keyword to search:")
        if keyword:
            try:
                for root, dirs, files in os.walk(path):
                    for dir in dirs:
                        if keyword in dir:
                            messagebox.showinfo("Found", f"Found directory: {os.path.join(root, dir)}")
            except OSError as error:
                messagebox.showerror("Error", f"Error searching directory '{path}': {error}")

def set_directory_permissions():
    path = filedialog.askdirectory()
    if path:
        permissions = simpledialog.askstring("Input", "Enter the permissions to set (octal):")
        if permissions:
            try:
                os.chmod(path, int(permissions, 8))
                messagebox.showinfo("Success", f"Permissions of directory '{path}' set successfully.")
            except OSError as error:
                messagebox.showerror("Error", f"Error setting permissions of directory '{path}': {error}")

def create_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if path:
        try:
            with open(path, 'w') as file:
                file.write('')
            messagebox.showinfo("Success", f"File '{path}' created successfully.")
        except OSError as error:
            messagebox.showerror("Error", f"Error creating file '{path}': {error}")

def open_file():
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if path:
        try:
            os.startfile(path)  # For Windows
            # os.system(f"open {path}")  # For MacOS
        except OSError as error:
            messagebox.showerror("Error", f"Error opening file '{path}': {error}")

def edit_file():
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if path:
        try:
            with open(path, 'a') as file:
                content = simpledialog.askstring("Input", "Enter content to add to the file:")
                if content:
                    file.write(content)
            messagebox.showinfo("Success", f"File '{path}' edited successfully.")
        except OSError as error:
            messagebox.showerror("Error", f"Error editing file '{path}': {error}")

def move_file():
    src = filedialog.askopenfilename()
    if src:
        dst = filedialog.askdirectory()
        if dst:
            try:
                shutil.move(src, dst)
                messagebox.showinfo("Success", f"File '{src}' moved to '{dst}' successfully.")
            except OSError as error:
                messagebox.showerror("Error", f"Error moving file '{src}': {error}")

def rename_file():
    src = filedialog.askopenfilename()
    if src:
        dst = filedialog.asksaveasfilename(defaultextension="", initialfile=os.path.basename(src))
        if dst:
            try:
                os.rename(src, dst)
                messagebox.showinfo("Success", f"File '{src}' renamed to '{dst}' successfully.")
            except OSError as error:
                messagebox.showerror("Error", f"Error renaming file '{src}': {error}")

def copy_file():
    src = filedialog.askopenfilename()
    if src:
        dst = filedialog.askdirectory()
        if dst:
            try:
                shutil.copy2(src, dst)
                messagebox.showinfo("Success", f"File '{src}' copied to '{dst}' successfully.")
            except OSError as error:
                messagebox.showerror("Error", f"Error copying file '{src}': {error}")

def delete_file():
    path = filedialog.askopenfilename()
    if path:
        try:
            os.remove(path)
            messagebox.showinfo("Success", f"File '{path}' deleted successfully.")
        except OSError as error:
            messagebox.showerror("Error", f"Error deleting file '{path}': {error}")

def change_file_attributes():
    path = filedialog.askopenfilename()
    if path:
        attributes = simpledialog.askstring("Input", "Enter the attributes to change (octal):")
        if attributes:
            try:
                os.chmod(path, int(attributes, 8))
                messagebox.showinfo("Success", f"Attributes of file '{path}' changed successfully.")
            except OSError as error:
                messagebox.showerror("Error", f"Error changing attributes of file '{path}': {error}")

def search_file():
    path = filedialog.askdirectory()
    if path:
        keyword = simpledialog.askstring("Input", "Enter the keyword to search:")
        if keyword:
            try:
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if keyword in file:
                            messagebox.showinfo("Found", f"Found file: {os.path.join(root, file)}")
            except OSError as error:
                messagebox.showerror("Error", f"Error searching file '{path}': {error}")

def set_file_permissions():
    path = filedialog.askopenfilename()
    if path:
        permissions = simpledialog.askstring("Input", "Enter the permissions to set (octal):")
        if permissions:
            try:
                os.chmod(path, int(permissions, 8))
                messagebox.showinfo("Success", f"Permissions of file '{path}' set successfully.")
            except OSError as error:
                messagebox.showerror("Error", f"Error setting permissions of file '{path}': {error}")

def main():
    root = tk.Tk()
    root.title("File Manager")

    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Create File", command=create_file)
    file_menu.add_command(label="Open File", command=open_file)
    file_menu.add_command(label="Edit File", command=edit_file)
    file_menu.add_command(label="Move File", command=move_file)
    file_menu.add_command(label="Rename File", command=rename_file)
    file_menu.add_command(label="Copy File", command=copy_file)
    file_menu.add_command(label="Delete File", command=delete_file)
    file_menu.add_command(label="Change File Attributes", command=change_file_attributes)
    file_menu.add_command(label="Search File", command=search_file)
    file_menu.add_command(label="Set File Permissions", command=set_file_permissions)

    directory_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Directory", menu=directory_menu)
    directory_menu.add_command(label="Create Directory", command=create_directory)
    directory_menu.add_command(label="Open Directory", command=open_directory)
    directory_menu.add_command(label="Move Directory", command=move_directory)
    directory_menu.add_command(label="Rename Directory", command=rename_directory)
    directory_menu.add_command(label="Copy Directory", command=copy_directory)
    directory_menu.add_command(label="Delete Directory", command=delete_directory)
    directory_menu.add_command(label="Change Directory Attributes", command=change_directory_attributes)
    directory_menu.add_command(label="Search Directory", command=search_directory)
    directory_menu.add_command(label="Set Directory Permissions", command=set_directory_permissions)

    root.mainloop()

if __name__ == "__main__":
    main()

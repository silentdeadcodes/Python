import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import simpledialog
from tkinter import messagebox
import subprocess
import keyword

class CodeEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Code Editor")
        self.master.geometry("800x600")

        self.dark_mode = tk.BooleanVar()
        self.dark_mode.set(False)  # Default is light mode

        self.text_widget = scrolledtext.ScrolledText(
            self.master,
            wrap="word",
            bg="white",
            fg="black",
            font=("Courier New", 12)
        )
        self.text_widget.pack(expand=True, fill="both")

        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        self.view_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_checkbutton(label="Dark Mode", variable=self.dark_mode, command=self.toggle_dark_mode)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.destroy)

        self.run_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Run", menu=self.run_menu)
        self.run_menu.add_command(label="Run Python Code", command=self.run_python_code)

        self.add_undo_redo()
        self.add_syntax_highlighting()
        self.add_line_numbers()
        self.add_find_replace()
        self.add_word_wrap()
        self.add_zoom()
        self.add_auto_indent()
        self.add_code_folding()
        self.add_multiple_tabs()  # Added this line
        self.add_code_completion()

        self.output_text = scrolledtext.ScrolledText(
            self.master,
            wrap="word",
            height=8,
            bg="white",
            fg="black",
            font=("Courier New", 12)
        )
        self.output_text.pack(expand=True, fill="both")

    def new_file(self):
        self.text_widget.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python files", "*.py"), ("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py"), ("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get(1.0, tk.END))

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py"), ("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get(1.0, tk.END))

    def run_python_code(self):
        code = self.text_widget.get(1.0, tk.END)
        self.output_text.delete(1.0, tk.END)  # Clear previous output

        try:
            process = subprocess.Popen(
                ["python", "-c", code],
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
                text=True
            )
            output, error = process.communicate(timeout=10)  # Adjust the timeout as needed
            if output:
                self.output_text.insert(tk.END, output)
            if error:
                self.output_text.insert(tk.END, error, 'error')
            self.output_text.see(tk.END)

        except Exception as e:
            print(e)

        while True:
            try:
                output, error = process.communicate(timeout=0.1)
                if output:
                    self.output_text.insert(tk.END, output)
                if error:
                    self.output_text.insert(tk.END, error, 'error')
                self.output_text.see(tk.END)
            except subprocess.TimeoutExpired:
                pass
            except Exception as e:
                print(e)

    def toggle_dark_mode(self):
        if self.dark_mode.get():
            self.text_widget.configure(bg="#282c34", fg="#abb2bf")
            self.output_text.configure(bg="#282c34", fg="#abb2bf")
        else:
            self.text_widget.configure(bg="white", fg="black")
            self.output_text.configure(bg="white", fg="black")

    def add_undo_redo(self):
        # Add undo and redo buttons/menu options
        undo_button = tk.Button(self.master, text="Undo", command=self.text_widget.edit_undo)
        redo_button = tk.Button(self.master, text="Redo", command=self.text_widget.edit_redo)
        undo_button.pack(side=tk.LEFT)
        redo_button.pack(side=tk.LEFT)

        undo_menu = tk.Menu(self.menu_bar, tearoff=False)
        redo_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Edit", menu=undo_menu)
        undo_menu.add_command(label="Undo", command=self.text_widget.edit_undo)
        undo_menu.add_command(label="Redo", command=self.text_widget.edit_redo)
        redo_menu.add_command(label="Undo", command=self.text_widget.edit_undo)
        redo_menu.add_command(label="Redo", command=self.text_widget.edit_redo)

    def add_syntax_highlighting(self):
        # Basic syntax highlighting
        self.text_widget.tag_configure("keyword", foreground="blue")
        self.text_widget.tag_configure("builtin", foreground="purple")

        def on_text_change(event):
            for tag in self.text_widget.tag_names():
                self.text_widget.tag_remove(tag, "1.0", tk.END)

            words = self.text_widget.get("1.0", tk.END).split()
            for word in words:
                if keyword.iskeyword(word):
                    self.text_widget.tag_add("keyword", f"1.0 + {len(word)}c", f"1.0 + {len(word)}c lineend")
                if word in dir(__builtins__):
                    self.text_widget.tag_add("builtin", f"1.0 + {len(word)}c", f"1.0 + {len(word)}c lineend")

        self.text_widget.bind("<KeyRelease>", on_text_change)

    def add_line_numbers(self):
        # Line numbers
        self.line_numbers = tk.Text(self.master, width=4, bg="#282c34", fg="#abb2bf", bd=0, wrap="none")
        self.line_numbers.pack(side=tk.LEFT, fill="y")
        self.line_numbers.insert(tk.END, "1\n")

        def update_line_numbers(event):
            lines = self.text_widget.get(1.0, tk.END).count("\n")
            self.line_numbers.config(state=tk.NORMAL)
            self.line_numbers.delete(1.0, tk.END)
            self.line_numbers.insert(tk.END, "\n".join(map(str, range(1, lines + 1))))
            self.line_numbers.config(state=tk.DISABLED)

        self.text_widget.bind("<Enter>", update_line_numbers)
        self.text_widget.bind("<Leave>", update_line_numbers)
        self.text_widget.bind("<Configure>", update_line_numbers)
        self.text_widget.bind("<KeyRelease>", update_line_numbers)

    def add_find_replace(self):
        # Find and replace
        find_button = tk.Button(self.master, text="Find", command=self.find)
        replace_button = tk.Button(self.master, text="Replace", command=self.replace)
        find_button.pack(side=tk.RIGHT)
        replace_button.pack(side=tk.RIGHT)

    def find(self):
        find_str = simpledialog.askstring("Find", "Enter text to find:")
        if find_str:
            start_pos = self.text_widget.search(find_str, "1.0", tk.END)
            if start_pos:
                messagebox.showinfo("Result", f"Text found at {start_pos}")
                self.text_widget.tag_add(tk.SEL, start_pos, f"{start_pos}+{len(find_str)}c")
                self.text_widget.focus_set()
            else:
                messagebox.showinfo("Result", "Text not found")

    def replace(self):
        find_str = simpledialog.askstring("Find", "Enter text to find:")
        replace_str = simpledialog.askstring("Replace", "Enter replacement text:")
        if find_str and replace_str:
            self.text_widget.replace("1.0", tk.END, self.text_widget.get("1.0", tk.END).replace(find_str, replace_str))

    def add_word_wrap(self):
        # Word wrap
        word_wrap_menu = tk.Menu(self.view_menu, tearoff=False)
        self.view_menu.add_cascade(label="Word Wrap", menu=word_wrap_menu)
        word_wrap_menu.add_checkbutton(label="Toggle Word Wrap", command=self.toggle_word_wrap)

    def toggle_word_wrap(self):
        wrap_status = self.text_widget.cget("wrap")
        if wrap_status == "none":
            self.text_widget.configure(wrap="word")
        else:
            self.text_widget.configure(wrap="none")

    def add_zoom(self):
        # Zoom in/out
        zoom_in_button = tk.Button(self.master, text="Zoom In", command=lambda: self.change_font_size(2))
        zoom_out_button = tk.Button(self.master, text="Zoom Out", command=lambda: self.change_font_size(-2))
        zoom_in_button.pack(side=tk.LEFT)
        zoom_out_button.pack(side=tk.LEFT)

    def change_font_size(self, size_change):
        current_size = self.text_widget.cget("font")[1]
        new_size = max(8, current_size + size_change)
        self.text_widget.configure(font=("Courier New", new_size))

    def add_auto_indent(self):
        # Auto-indentation
        self.text_widget.bind("<Return>", self.auto_indent)

    def auto_indent(self, event):
        current_line = self.text_widget.get(tk.INSERT).split("\n")[-1]
        leading_spaces = len(current_line) - len(current_line.lstrip())
        self.text_widget.insert(tk.INSERT, "\n" + " " * leading_spaces)

    def add_code_folding(self):
        # Code folding
        self.text_widget.tag_configure("fold", lmargin1=10)
        self.text_widget.tag_add("fold", "1.0", tk.END)
        self.text_widget

    def add_multiple_tabs(self):
        # Add implementation for multiple tabs
        pass

    def add_code_completion(self):
        # Add code completion
        pass


def main():
    root = tk.Tk()
    app = CodeEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()

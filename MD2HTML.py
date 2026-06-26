#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Converts Markdown text to HTML with support for RTL/LTR direction and Persian fonts.
Handles newline characters and offers a GUI to preview, save, and open the result in a browser.
"""

import os
import re
import webbrowser
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog

try:
    import markdown
except ImportError:
    raise RuntimeError("Please install the 'markdown' library: `pip install markdown`")

# --------------------------------------------------------------------------- #
#   CSS template (fonts, direction, etc.)
# --------------------------------------------------------------------------- #

CSS_TEMPLATE = """
<style>
html, body {{
    margin: 0;
    padding: 10px;
    font-size: 14pt;
}}
body {{
    direction: {direction};
    font-family: 'B Nazanin', 'Times New Roman', serif;
}}
table {{
    border-collapse: collapse;
    width: 100%;
}}
th, td {{
    border: 1px solid #999;
    padding: 4px 8px;
    text-align: left;
}}
</style>
"""

# --------------------------------------------------------------------------- #
#   Conversion function
# --------------------------------------------------------------------------- #

def convert_markdown(md_text, direction="rtl"):
    """
    Convert Markdown string to a full HTML document.
    direction: 'rtl' or 'ltr' – controls the text direction.
    Returns the complete HTML as a string.
    """
    html_body = markdown.markdown(md_text,
                                  extensions=['tables', 'fenced_code', 'extra'])

    full_html = f"""<!DOCTYPE html>
<html lang="fa">
<head>
<meta charset="utf-8">
<title>Converted Markdown to HTML</title>
{CSS_TEMPLATE.format(direction=direction)}
</head>
<body>
{html_body}
</body>
</html>"""
    return full_html

# --------------------------------------------------------------------------- #
#   Tkinter GUI
# --------------------------------------------------------------------------- #

class MarkdownToHTMLGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Markdown to HTML Converter")
        self.geometry("1024x720")
        self.configure(bg="#f0f0f0")

        # ------------------------------------------------------- #
        #   Main widgets
        # ------------------------------------------------------- #

        # Top frame: settings and buttons
        top_frame = ttk.Frame(self)
        top_frame.pack(fill=tk.X, padx=10, pady=5)

        self.dir_var = tk.StringVar(value="rtl")  # default RTL
        ttk.Label(top_frame, text="Text direction:").pack(side=tk.LEFT, padx=(0, 5))

        ttk.Radiobutton(top_frame, text="RTL", variable=self.dir_var,
                        value="rtl").pack(side=tk.LEFT)
        ttk.Radiobutton(top_frame, text="LTR", variable=self.dir_var,
                        value="ltr").pack(side=tk.LEFT)

        ttk.Button(top_frame, text="Convert", command=self.on_convert).pack(
            side=tk.RIGHT, padx=5
        )
        ttk.Button(top_frame, text="Save to HTML file",
                   command=self.save_to_file).pack(
            side=tk.RIGHT, padx=5
        )
        ttk.Button(top_frame, text="Open in browser",
                   command=self.open_in_browser).pack(
            side=tk.RIGHT, padx=5
        )

        # Input area
        input_label = ttk.Label(self, text="Markdown Input")
        input_label.pack(anchor=tk.W, padx=10)

        self.input_text = scrolledtext.ScrolledText(self,
                                                    wrap=tk.WORD,
                                                    width=80,
                                                    height=15)
        self.input_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        # Output area
        output_label = ttk.Label(self, text="HTML Output")
        output_label.pack(anchor=tk.W, padx=10)

        self.output_text = scrolledtext.ScrolledText(self,
                                                     wrap=tk.NONE,
                                                     width=80,
                                                     height=15)
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

    # ------------------------------------------------------- #
    #   Event handlers
    # ------------------------------------------------------- #

    def on_convert(self):
        """Read input, replace literal '\n' with actual newlines, and generate HTML."""
        md = self.input_text.get("1.0", tk.END)
        if not md.strip():
            messagebox.showwarning("Warning", "Input text is empty.")
            return

        # Replace literal '\n' with actual newline characters
        md = md.replace(r'\n', '\n').strip()

        direction = self.dir_var.get()

        try:
            html = convert_markdown(md, direction=direction)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, html)
        except Exception as e:
            messagebox.showerror("Conversion error", str(e))

    # ------------------------------------------------------- #
    #   Save to HTML file
    # ------------------------------------------------------- #

    def save_to_file(self):
        """Save the current output to a .html file."""
        current_html = self.output_text.get("1.0", tk.END).strip()
        if not current_html:
            messagebox.showwarning("Warning", "Output text is empty.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".html",
            filetypes=[("HTML Files", "*.html"), ("All files", "*.*")],
        )
        if not file_path:
            return

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(current_html)
            messagebox.showinfo("Success", f"File saved at {file_path}.")
            self.last_saved_path = file_path
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ------------------------------------------------------- #
    #   Open in browser
    # ------------------------------------------------------- #

    def open_in_browser(self):
        """
        Open the output in the default browser.
        If a file was saved previously, use that; otherwise create a temporary file.
        """
        current_html = self.output_text.get("1.0", tk.END).strip()
        if not current_html:
            messagebox.showwarning("Warning", "No output to display.")
            return

        file_path = getattr(self, "last_saved_path", None)
        try:
            if file_path and os.path.isfile(file_path):
                url = f'file://{os.path.abspath(file_path)}'
            else:
                import tempfile
                with tempfile.NamedTemporaryFile('w', delete=False,
                                                 suffix='.html',
                                                 encoding='utf-8') as tmp_file:
                    tmp_file.write(current_html)
                    file_path = tmp_file.name
                url = f'file://{os.path.abspath(file_path)}'

            webbrowser.open_new_tab(url)
        except Exception as e:
            messagebox.showerror("Error opening browser", str(e))


# --------------------------------------------------------------------------- #
#   Run the application
# --------------------------------------------------------------------------- #

if __name__ == "__main__":
    app = MarkdownToHTMLGUI()
    app.mainloop()
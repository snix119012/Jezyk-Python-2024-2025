import fitz
import tkinter as tk
from tkinter import filedialog, messagebox

okno = tk.Tk()
okno.title("PDF Reader")
okno.geometry("800x600")

scroll_y = tk.Scrollbar(okno)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

scroll_x = tk.Scrollbar(okno, orient='horizontal')
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

text = tk.Text(okno, wrap=tk.WORD, padx=10, pady=10,
               yscrollcommand=scroll_y.set,
               xscrollcommand=scroll_x.set)
text.pack(expand=True, fill='both', padx=10, pady=10)

scroll_y.config(command=text.yview)
scroll_x.config(command=text.xview)


def clear_text():
    text.delete(1.0, tk.END)


def open_pdf():
    try:
        clear_text()

        file = filedialog.askopenfilename(
            title="Select a PDF",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )

        if file:
            try:
                pdf_file = fitz.open(file)

                for page_num in range(len(pdf_file)):
                    page = pdf_file[page_num]
                    content = page.get_text()

                    text.insert(tk.END, f"\n=== Strona {page_num + 1} ===\n\n")
                    text.insert(tk.END, content)

                pdf_file.close()

                text.see("1.0")

                messagebox.showinfo("success: {file}")

            except Exception as e:
                messagebox.showerror("error: {str(e)}")

    except Exception as e:
        messagebox.showerror("error", f"error: {str(e)}")
        print(f"error: {str(e)}")


def quit_app():
    if messagebox.askokcancel("Quit", "do u want to close this app?"):
        okno.quit()


menubar = tk.Menu(okno)
okno.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_app)

text.insert(tk.END, "Wybierz 'File -> Open' aby otworzyć plik PDF.")

okno.mainloop()
from tkinter import filedialog

def export_report(text):

    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )

    if filename:

        with open(filename,"w",encoding="utf-8") as file:
            file.write(text)

        return True

    return False
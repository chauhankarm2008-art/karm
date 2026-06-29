from datetime import datetime
from report import export_report
from system_info import get_system_info
from dns_lookup import dns_lookup
from url_analyzer import analyze_url
from hash_generator import generate_hash
from password_checker import check_password
from port_scanner import scan_ports
import threading
import tkinter as tk
from tkinter import ttk

# ---------------- Window ---------------- #

root = tk.Tk()
root.title("🛡 CyberShield Pro")
root.geometry("1100x700")
root.configure(bg="#EE0823")

title = tk.Label(
    root,
    text="🛡 CyberShield Pro",
    bg="#fbfbfb",
    fg="cyan",
    font=("consolas", 26, "bold")
)
title.pack(pady=15)

BG = "#101215"
FG = "white"
ACCENT = "#3F07BF"
subtitle = tk.Label(
    root,
    text="Advanced Cyber Security Toolkit",
    bg=BG,
    fg="lightgray",
    font=("consolas",12)
)

subtitle.pack()

root.configure(bg=BG)

bg=ACCENT,
fg="white",
font=("Arial",11,"bold")

font=("Consolas",11)

# ---------------- Notebook ---------------- #
style = ttk.Style()

style.theme_use("clam")

style.configure(
    "TNotebook.Tab",
    font=("Arial",11,"bold"),
    padding=[15,8]
)
tabs = ttk.Notebook(root)
tabs.pack(fill="both", expand=True)

dashboard_tab = tk.Frame(tabs)

port_tab = tk.Frame(tabs)
password_tab = tk.Frame(tabs)
hash_tab = tk.Frame(tabs)
url_tab = tk.Frame(tabs)
dns_tab = tk.Frame(tabs)
system_tab = tk.Frame(tabs)
tabs.add(dashboard_tab, text="🏠 Dashboard")
tabs.add(port_tab, text="Port Scanner")
tabs.add(password_tab, text="Password Checker")
tabs.add(hash_tab, text="Hash Generator")
tk.Label(
    hash_tab,
    text="Enter Text",
    font=("Arial",12)
).pack(pady=10)

hash_entry = tk.Entry(
    hash_tab,
    width=50
)
hash_entry.pack()

algorithm = tk.StringVar()
algorithm.set("SHA256")

algo_menu = ttk.Combobox(
    hash_tab,
    textvariable=algorithm,
    values=[
        "MD5",
        "SHA1",
        "SHA256",
        "SHA512"
    ],
    state="readonly"
)

algo_menu.pack(pady=10)

generate_btn = tk.Button(
    hash_tab,
    text="🔑 Generate Hash",
    bg="#0097A7",
    fg="white",
    font=("Arial", 11, "bold"),
    activebackground="#0097A7",
    activeforeground="white",
    cursor="hand2",
    width=20
)

generate_btn.pack()

hash_output = tk.Text(
    hash_tab,
    width=80,
    height=8
)

hash_output.pack(pady=20)

tabs.add(url_tab, text="URL Analyzer")
tk.Label(
    url_tab,
    text="Enter URL",
    font=("Arial",12)
).pack(pady=10)

url_entry = tk.Entry(
    url_tab,
    width=60
)
url_entry.pack()

url_btn = tk.Button(
    url_tab,
    text="🌐 Analyze URL",
    bg="#00BCD4",
    fg="white",
    font=("Arial", 11, "bold"),
    activebackground="#0097A7",
    activeforeground="white",
    cursor="hand2",
    width=20
)

url_btn.pack(pady=10)

url_output = tk.Text(
    url_tab,
    width=80,
    height=12
)

url_output.pack(pady=20)

tabs.add(dns_tab, text="DNS Lookup")
tk.Label(
    dns_tab,
    text="Enter Domain",
    font=("Arial",12)
).pack(pady=10)

dns_entry = tk.Entry(
    dns_tab,
    width=40
)
dns_entry.pack()

dns_btn = tk.Button(
    dns_tab,
    text="🌍 Lookup DNS",
    bg="#00BCD4",
    fg="white",
    font=("Arial", 11, "bold"),
    activebackground="#0097A7",
    activeforeground="white",
    cursor="hand2",
    width=20
)
dns_btn.pack(pady=10)

dns_output = tk.Text(
    dns_tab,
    width=70,
    height=10
)
dns_output.pack()

tabs.add(system_tab, text="System Info")
system_btn = tk.Button(
    system_tab,
    text="💻 System Information",
    bg="#00BCD4",
    fg="white",
    font=("Arial", 11, "bold"),
    activebackground="#0097A7",
    activeforeground="white",
    cursor="hand2",
    width=25
)

system_btn.pack(pady=20)

system_output = tk.Text(
    system_tab,
    width=80,
    height=18
)

system_output.pack()

export_btn = tk.Button(
    root,
    text="📄 Export Report",
    bg="#00BCD4",
    fg="white",
    font=("Arial",11,"bold")
)

export_btn.pack(pady=5)

clock = tk.Label(
    root,
    font=("Consolas",10),
    fg="gray",
    bg=BG
)

clock.pack()

# ---------------- Port Scanner ---------------- #

tk.Label(
    port_tab,
    text="Target IP / Domain",
    font=("Arial",12)
).pack(pady=10)

port_target = tk.Entry(
    port_tab,
    width=40
)
port_target.pack()

scan_btn = tk.Button(
    port_tab,
    text="🚀 Start Scan",
    bg="#00BCD4",
    fg="white",
    font=("Arial",11,"bold"),
    activebackground="#0097A7",
    cursor="hand2"
)
scan_btn.pack(pady=10)

port_output = tk.Text(
    port_tab,
    width=80,
    height=20
)
port_output.pack()

# ---------------- Password Checker ---------------- #

tk.Label(
    password_tab,
    text="Enter Password",
    font=("Arial",12)
).pack(pady=10)

password_entry = tk.Entry(
    password_tab,
    show="*",
    width=40
)
password_entry.pack()

check_btn = tk.Button(
    password_tab,
    text="🔐 Check Password",
    bg="#00BCD4",
    fg="white",
    font=("Arial", 11, "bold"),
    activebackground="#0690C7",
    activeforeground="white",
    cursor="hand2",
    width=20
)
check_btn.pack(pady=10)

password_output = tk.Text(
    password_tab,
    width=60,
    height=12
)
password_output.pack()

tk.Label(
    dashboard_tab,
    text="Welcome to CyberShield Pro",
    font=("Arial",20,"bold"),
    fg="cyan"
).pack(pady=20)

tk.Label(
    dashboard_tab,
    text="""
🛡 Welcome to CyberShield Pro

Advanced Cyber Security Toolkit

✔ Port Scanner
✔ Password Strength Checker
✔ Hash Generator
✔ URL Safety Analyzer
✔ DNS Lookup
✔ System Information
✔ Export Report

Developer:
Karm Chauhan

Educational & Defensive Use Only
""",
    font=("Consolas",13),
    justify="left"
).pack(pady=20)
def show_system():

    system_output.delete("1.0", tk.END)

    system_output.insert(
        tk.END,
        get_system_info()
    )

system_btn.config(command=show_system)

def lookup_dns():

    dns_output.delete("1.0", tk.END)

    result = dns_lookup(dns_entry.get())

    dns_output.insert(tk.END, result)

dns_btn.config(command=lookup_dns)

def check_url():

    url_output.delete("1.0", tk.END)

    url = url_entry.get()

    if url == "":
        url_output.insert(tk.END, "Please enter a URL.")
        return

    result = analyze_url(url)

    url_output.insert(tk.END, result)

url_btn.config(command=check_url)

def create_hash():

    hash_output.delete("1.0", tk.END)

    text = hash_entry.get()

    if text == "":
        hash_output.insert(tk.END, "Please enter text.")
        return

    result = generate_hash(
        text,
        algorithm.get()
    )

    hash_output.insert(
        tk.END,
        result
    )

generate_btn.config(command=create_hash)

def analyze_password():

    password_output.delete("1.0", tk.END)

    password = password_entry.get()

    score, strength, suggestions = check_password(password)

    password_output.insert(tk.END, f"Strength : {strength}\n")
    password_output.insert(tk.END, f"Score    : {score}/100\n\n")

    if suggestions:
        password_output.insert(tk.END, "Suggestions:\n\n")

        for item in suggestions:
            password_output.insert(
                tk.END,
                f"• {item}\n"
            )
    else:
        password_output.insert(
            tk.END,
            "Excellent Password! 🎉"
        )

check_btn.config(command=analyze_password)

from tkinter import messagebox

def export_current_report():

    current_tab = tabs.tab(tabs.select(), "text")

    if current_tab == "Port Scanner":
        text = port_output.get("1.0", tk.END)

    elif current_tab == "Password Checker":
        text = password_output.get("1.0", tk.END)

    elif current_tab == "Hash Generator":
        text = hash_output.get("1.0", tk.END)

    elif current_tab == "URL Analyzer":
        text = url_output.get("1.0", tk.END)

    elif current_tab == "DNS Lookup":
        text = dns_output.get("1.0", tk.END)

    elif current_tab == "System Info":
        text = system_output.get("1.0", tk.END)

    else:
        messagebox.showwarning("Export", "Nothing to export from this tab.")
        return

    if text.strip() == "":
        messagebox.showwarning("Export", "No data available.")
        return

    if export_report(text):
        messagebox.showinfo("Success", "Report exported successfully!")
        
def update_clock():

    now = datetime.now().strftime("%d-%m-%Y   %H:%M:%S")

    clock.config(text=now)

    root.after(1000, update_clock)

update_clock()
        
def start_scan():
    target = port_target.get().strip()

    port_output.delete("1.0", tk.END)

    if not target:
        port_output.insert(tk.END, "Please enter a target.")
        return

    port_output.insert(tk.END, f"Scanning {target}...\n\n")
    root.update()

    results = scan_ports(target)

    if results and results[0][0] == "ERROR":
        port_output.insert(tk.END, results[0][1])
        return

    if len(results) == 0:
        port_output.insert(tk.END, "No common ports are open.")
        return

    port_output.insert(tk.END, "Open Ports\n")
    port_output.insert(tk.END, "-" * 30 + "\n")

    for port, service in results:
        port_output.insert(
            tk.END,
            f"Port {port:<5} | {service}\n"
        )
    
scan_btn.config(command=start_scan)

footer = tk.Label(
    root,
    text="Developed by Karm Chauhan | Cyber Security Toolkit v1.0",
    bg="#1e1e1e",
    fg="lightgray",
    font=("consolas", 11)
)

footer.pack(side="bottom", pady=5)

status = tk.Label(
    root,
    text="🟢 Status : Ready",
    bg="#1E1E1E",
    fg="white",
    anchor="w",
    font=("Consolas",10)
)
status.pack(side="bottom", fill="x")

export_btn.config(command=export_current_report)

root.mainloop()
import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import simpledialog
import subprocess
import time
import os

#gui = tk.Tk()
#pyinstaller and “noconsole” argument


def pubKey():
    global file_path
    file_path = "N/A"
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    return file_path

def connect(): 
    ip = ip_or_domain_entry.get()
    username = username_entry.get()
    port = port_entry.get()

    if isOn.get() == 1:
        connection = f"ssh -i {file_path} {username}@{ip} -p {port}"
        cmd = f"start /B start cmd.exe @cmd /k {connection}"
        os.system(cmd)
        time.sleep(2)
        gui.destroy()

    else:
        connection = f"ssh {username}@{ip} -p {port}"
        subprocess.Popen(connection, shell=True)
        cmd = f"start /B start cmd.exe @cmd /k {connection}"
        os.system(cmd)
        time.sleep(2)
        gui.destroy()
        
        
def successMessage(filename):
    popup = tk.Tk()
    popup.geometry("300x100")
    popup.title("File Creation Status")

    label = tk.Label(popup, text="Created " + filename + " successfully!", padx=20, pady=20)
    label.pack()

    ok_button = tk.Button(popup, text="OK", command=popup.destroy)
    ok_button.pack()

    popup.mainloop()


def create():
    ip = ip_or_domain_entry.get()
    username = username_entry.get()
    port = port_entry.get()
    
    if isOn.get() == 1:
        command = f"ssh -i {file_path} {username}@{ip} -p {port}"
    else:
        command = f"ssh {username}@{ip} -p {port}"
    
    fileName = simpledialog.askstring("File Name", "Enter the file name:")
    filePath = os.path.join(os.path.expanduser("~/Desktop"), fileName + ".bat")

    with open(filePath, "w") as f:
        f.write(command)
    
    successMessage(filePath)


#GUI
#GUI
#GUI
#GUI

pad = 30
mainColor = "SpringGreen4"
fgColor = "black"

gui = tk.Tk()
gui.title("BasicSSH - basicssh.com")
gui.configure(bg = mainColor)


ip_or_domain_label = tk.Label(gui, text="IP/Domain:", bg=mainColor, fg=fgColor)
ip_or_domain_label.grid(row=0, column=0, padx=pad, pady=5, sticky="w")
ip_or_domain_entry = tk.Entry(gui)
ip_or_domain_entry.grid(row=0, column=1, padx=pad, pady=5)


port_label = tk.Label(gui, text="Port:", bg=mainColor, fg=fgColor)
port_label.grid(row=1, column=0, padx=pad, pady=5, sticky="w")
port_entry = tk.Entry(gui)
port_entry.grid(row=1, column=1, padx=pad, pady=5)


username_label = tk.Label(gui, text="Username:", bg=mainColor, fg=fgColor)
username_label.grid(row=2, column=0, padx=pad, pady=5, sticky="w")
username_entry = tk.Entry(gui)
username_entry.grid(row=2, column=1, padx=pad, pady=5)

isOn = tk.IntVar()
file_selector_checkbox = tk.Checkbutton(gui, text="Pub Key?", variable=isOn, command = pubKey)
file_selector_checkbox.grid(row=4, columnspan=1, padx=10, pady=5)

connect_button = tk.Button(gui, text="Connect", command=connect)
connect_button.grid(row=4, columnspan=2, padx=10, pady=10)

create_button = tk.Button(gui, text="Create Shortcut", command=create)
create_button.grid(row=5, columnspan=4, padx=5, pady=5)

gui.mainloop()
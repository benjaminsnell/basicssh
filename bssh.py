import tkinter.filedialog as filedialog
import subprocess
import customtkinter as ctk
import customtkinter
import time
import os

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
    popup = ctk.CTk()
    popup.geometry("300x100")
    popup.title("File Creation Status")

    label = ctk.Label(popup, text="Created " + filename + " successfully!", padx=20, pady=20)
    label.pack()

    ok_button = ctk.Button(popup, text="OK", command=popup.destroy)
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
    
    fileName = customtkinter.CTkInputDialog(text="File Name:", title="Create Shortcut")
    filePath = os.path.join(os.path.expanduser("~/Desktop"), fileName + ".bat")

    with open(filePath, "w") as f:
        f.write(command)
    
    successMessage(filePath)


#GUI
#GUI
#GUI
#GUI

pad = 30
#mainColor = "SpringGreen4"
fgColor = "green"

gui = ctk.CTk()
gui.title("BasicSSH - basicssh.com")
#gui.configure(bg = mainColor)


ip_or_domain_label = ctk.CTkLabel(gui, text="IP/Domain:")
ip_or_domain_label.grid(row=0, column=0, padx=pad, pady=pad, sticky="w")
ip_or_domain_entry = ctk.CTkEntry(gui)
ip_or_domain_entry.grid(row=0, column=1, padx=pad, pady=pad)


port_label = ctk.CTkLabel(gui, text="Port:")
port_label.grid(row=1, column=0, padx=pad, pady=pad, sticky="w")
port_entry = ctk.CTkEntry(gui)
port_entry.grid(row=1, column=1, padx=pad, pady=pad)


username_label = ctk.CTkLabel(gui, text="Username:")
username_label.grid(row=2, column=0, padx=pad, pady=pad, sticky="w")
username_entry = ctk.CTkEntry(gui)
username_entry.grid(row=2, column=1, padx=pad, pady=pad)

isOn = ctk.IntVar()
file_selector_checkbox = ctk.CTkCheckBox(gui, text="Pub Key?", variable=isOn, command = pubKey)
file_selector_checkbox.grid(row=3, columnspan=1, padx=pad, pady=5)

connect_button = ctk.CTkButton(gui, text="Connect", command=connect, fg_color = fgColor)
connect_button.grid(row=4, columnspan=3, padx=pad, pady=15)

create_button = ctk.CTkButton(gui, text="Create Shortcut", command=create, fg_color = fgColor)
create_button.grid(row=5, columnspan=3, padx=pad, pady=15)

gui.mainloop()
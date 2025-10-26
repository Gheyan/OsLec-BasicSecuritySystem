# Import libraries
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
# Account Placeholder for Login
Accounts = {
    "user": {"password": "userpass", "role": "user"},
    "admin": {"password": "adminpass", "role": "admin"}
}
# Root Window
root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Gayagoy Basic Security System")
root.configure(bg="lightblue")
# Images
images = {}
def load_image(path, size):
    img = Image.open(path)
    img = img.resize(size)
    photo = ImageTk.PhotoImage(img)
    images[path] = photo
    return photo
def placeholder( entry, placeholder, showCharacter=None):
    entry.insert(0, placeholder)
    entry.config(fg="grey", show="")
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.config(fg="black")
            if showCharacter is not None:
                entry.config(show=showCharacter)

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="grey", show="")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
# Login Records for Admin
login_records = []
# Login UI
login = tk.Frame(root, bg="lightblue")
login.pack(expand=True, fill="both")
accountImage = tk.PhotoImage(file="Frontend/Images/ProfilePicture.png")
accountImageLabel = tk.Label(login, image=accountImage)
usernameEntry = tk.Entry(login)
placeholder(usernameEntry, "Enter username")
passwordEntry = tk.Entry(login)
placeholder(passwordEntry, "Enter password", showCharacter="*")
incorrectPassword = tk.Label(login, text="Incorrect Username or Password", fg="red")
loginButton = tk.Button(login, text="Login", command=lambda: loginAuthentication("user"))
accountImageLabel.pack(expand=True)
usernameEntry.pack()
passwordEntry.pack()
loginButton.pack(pady=10)
# User Home Screen UI
homeScreen = tk.Frame(root)
taskbarHome = tk.Frame(homeScreen, bg="grey", height=40)
taskbarHome.pack(side="bottom", fill="x")
appFrameHome = tk.Frame(homeScreen)
appFrameHome.pack(side="left", padx=20, pady=20)
# Desktop icons
recycleBin = load_image("Frontend/Images/RecycleBin.png", (50, 50))
computer = load_image("Frontend/Images/Computer.png", (50, 50))
folder = load_image("Frontend/Images/Folder.png", (50, 50))
recycleBinLabel = tk.Label(appFrameHome, image=recycleBin)
recycleBinText = tk.Label(appFrameHome, text="Recycle Bin")
computerLabel = tk.Label(appFrameHome, image=computer)
computerText = tk.Label(appFrameHome, text="Computer")
folderLabel = tk.Label(appFrameHome, image=folder)
folderText = tk.Label(appFrameHome, text="Folder")
recycleBinLabel.pack()
recycleBinText.pack()
computerLabel.pack()
computerText.pack()
folderLabel.pack()
folderText.pack()
# Taskbar icons
accountTaskbar = load_image("Frontend/Images/ProfilePicture.png", (30, 30))
accountTaskbarLabelHome = tk.Label(taskbarHome, image=accountTaskbar)
accountTaskbarLabelHome.pack(side="left", padx=10)
usernameHome = tk.Label(taskbarHome, text="User Account")
usernameHome.pack(side="left", padx=10)
# Spacer for left-only margin
leftSpacerHome = tk.Frame(taskbarHome, width=450, bg="grey")
leftSpacerHome.pack(side="left")
# Taskbar apps
recycleBinSmall = load_image("Frontend/Images/RecycleBin.png", (30, 30))
computerSmall = load_image("Frontend/Images/Computer.png", (30, 30))
folderSmall = load_image("Frontend/Images/Folder.png", (30, 30))
tk.Label(taskbarHome, image=recycleBinSmall).pack(side="left", padx=10)
tk.Label(taskbarHome, image=computerSmall).pack(side="left", padx=10)
tk.Label(taskbarHome, image=folderSmall).pack(side="left", padx=10)
logoutHomeButton = tk.Button(taskbarHome, text="Logout")
logoutHomeButton.pack(side="right", padx=10)
# Admin Home Screen UI
adminScreen = tk.Frame(root)
taskbarAdmin = tk.Frame(adminScreen, bg="grey", height=40)
taskbarAdmin.pack(side="bottom", fill="x")
appFrameAdmin = tk.Frame(adminScreen)
appFrameAdmin.pack(side="left", padx=20, pady=20)
# Desktop icons
tk.Label(appFrameAdmin, image=recycleBin).pack()
tk.Label(appFrameAdmin, text="Recycle Bin").pack()
tk.Label(appFrameAdmin, image=computer).pack()
tk.Label(appFrameAdmin, text="Computer").pack()
tk.Label(appFrameAdmin, image=folder).pack()
tk.Label(appFrameAdmin, text="Folder").pack()
admin = load_image("Frontend/Images/Admin.png", (50, 50))
adminLabel = tk.Label(appFrameAdmin, image=admin, cursor="hand2")
adminText = tk.Label(appFrameAdmin, text="Admin")
adminLabel.pack()
adminLabel.bind("<Button-1>", lambda e: openAdminMonitor())
adminText.pack()
# Taskbar icons
accountTaskbarLabelAdmin = tk.Label(taskbarAdmin, image=accountTaskbar)
accountTaskbarLabelAdmin.pack(side="left", padx=10)
usernameAdmin = tk.Label(taskbarAdmin, text="Admin Account")
usernameAdmin.pack(side="left", padx=10)
leftSpacerAdmin = tk.Frame(taskbarAdmin, width=450, bg="grey")
leftSpacerAdmin.pack(side="left")
# Taskbar apps
tk.Label(taskbarAdmin, image=recycleBinSmall).pack(side="left", padx=10)
tk.Label(taskbarAdmin, image=computerSmall).pack(side="left", padx=10)
tk.Label(taskbarAdmin, image=folderSmall).pack(side="left", padx=10)
adminSmall = load_image("Frontend/Images/Admin.png", (30, 30))
adminSmall = tk.Label(taskbarAdmin, image=adminSmall, cursor="hand2")
adminSmall.pack(side="left", padx=10)
adminSmall.bind("<Button-1>", lambda e: openAdminMonitor())
logoutAdminButton = tk.Button(taskbarAdmin, text="Logout")
logoutAdminButton.pack(side="right", padx=10)
# Switching between screens
def goToHome():
    username = usernameEntry.get() if usernameEntry.get() else "User"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    login_records.append((username, timestamp))
    login.pack_forget()
    adminScreen.pack_forget()
    homeScreen.pack(expand=True, fill="both")
def goToAdmin():
    login.pack_forget()
    homeScreen.pack_forget()
    adminScreen.pack(expand=True, fill="both")
def goToLogin():
    homeScreen.pack_forget()
    adminScreen.pack_forget()
    login.pack(expand=True, fill="both")
def openAdminMonitor():
    adminMonitor = tk.Toplevel(root)
    adminMonitor.title("JR GAYAGOY SPYING MONITOR")
    adminMonitor.geometry("400x300")
    title = tk.Label(adminMonitor, text="Login Records", font=("Arial", 16))
    title.pack(pady=10)
    recordsFrame = tk.Frame(adminMonitor)
    recordsFrame.pack(fill="both", expand=True)
    scrollbar = tk.Scrollbar(recordsFrame)
    scrollbar.pack(side="right", fill="y")
    listbox = tk.Listbox(recordsFrame, yscrollcommand=scrollbar.set)
    for record in login_records:
        listbox.insert(tk.END, f"Username: {record[0]} | Time: {record[1]}")
    listbox.pack(fill="both", expand=True)
    scrollbar.config(command=listbox.yview)
# Template for Login Authentication
def loginAuthentication(roleAttempt):
    username = usernameEntry.get()
    password = passwordEntry.get()
    if username in Accounts and Accounts[username]["password"] == password:
        role = Accounts[username]["role"]
        if role == "admin":
            goToAdmin()
        else:
            goToHome()
    else:
        incorrectPassword.pack()
# Button Commands
loginButton.config(command=lambda: loginAuthentication("user"))
logoutHomeButton.config(command=goToLogin)
logoutAdminButton.config(command=goToLogin)
# Start app
root.mainloop()
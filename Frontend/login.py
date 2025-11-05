# Import libraries
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import os
from supabase import create_client, Client

url: str = "https://ruiycrzcjmvfijxfwrqg.supabase.co"

key: str ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1aXljcnpjam12ZmlqeGZ3cnFnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1OTk5NzM5NywiZXhwIjoyMDc1NTczMzk3fQ.2KMDkdNso50r28zZ9lhkwiP0huEdpqR3wz3J1cPI0nY"

supabase: Client = create_client(url, key)

# Icons
images = {}
def load_image(path, size):
    """Load and resize an image, removing dark or black backgrounds."""
    global images
    key = f"{path}|{size}"
    if key in images:
        return images[key]

    img = Image.open(path).convert("RGBA").resize(size, Image.LANCZOS)
    new_data = []
    for r, g, b, a in img.getdata():
        if r < 100 and g < 100 and b < 100:
            new_data.append((r, g, b, 0))
        else:
            new_data.append((r, g, b, a))
    img.putdata(new_data)
    photo = ImageTk.PhotoImage(img)
    images[key] = photo
    return photo



# Account Placeholder for Login
Accounts = {
    "user": {"password": "userpass", "role": "user"},
    "admin": {"password": "adminpass", "role": "admin"}
}

# Root Window
root = tk.Tk()
root.title("Gayagoy Basic Security System")
root.geometry("1024x768")
root.configure(bg="lightblue")
root.resizable(True, True)


def placeholder(entry, placeholder, showCharacter=None):
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

# ========== LOGIN UI ==========
login = tk.Frame(root, bg="lightblue")
login.pack(expand=True, fill="both")

# --- Center Container (Windows 10 Style Box) ---
login_container = tk.Frame(login, bg="white", bd=0, highlightthickness=0)
login_container.place(relx=0.5, rely=0.5, anchor="center")

# Drop Shadow effect (simulated)
shadow = tk.Frame(login, bg="#a0a0a0")
shadow.place(relx=0.5, rely=0.5, anchor="center", x=6, y=6)

login_container.tkraise()

# --- Account Image  ---
accountImage = load_image("Frontend/Images/ProfilePicture.png", (80, 80))
accountImageLabel = tk.Label(login_container, image=accountImage, bg="white")
accountImageLabel.image = accountImage  
accountImageLabel.pack(pady=(20, 10))

# --- Welcome Text ---
welcomeLabel = tk.Label(
    login_container,
    text="Welcome",
    font=("Segoe UI Semibold", 24),
    bg="white",
    fg="black"
)
welcomeLabel.pack(pady=(0, 5))

# --- Subtitle ---
subtitleLabel = tk.Label(
    login_container,
    text="Input your credentials",
    font=("Segoe UI", 11),
    bg="white",
    fg="grey"
)
subtitleLabel.pack(pady=(0, 20))



# --- Username Entry ---
usernameEntry = tk.Entry(
    login_container,
    width=30,
    font=("Segoe UI", 12),
    relief="flat",
    bd=5,
    highlightthickness=1,
    highlightcolor="#c0c0c0",
    highlightbackground="#d0d0d0",
    bg="white",
    fg="black",
    insertbackground="black"
)
placeholder(usernameEntry, "Enter username")
usernameEntry.pack(pady=5, ipady=5)

# --- Password Entry ---
passwordEntry = tk.Entry(
    login_container,
    width=30,
    font=("Segoe UI", 12),
    relief="flat",
    bd=5,
    highlightthickness=1,
    highlightcolor="#c0c0c0",
    highlightbackground="#d0d0d0",
    bg="white",
    fg="black",
    insertbackground="black",
    show=""  # start visible for placeholder
)
placeholder(passwordEntry, "Enter password", showCharacter="•")
passwordEntry.pack(pady=5, ipady=5)

# --- Incorrect Password Label ---
incorrectPassword = tk.Label(
    login_container,
    text="Incorrect Username or Password",
    fg="red",
    bg="white",
    font=("Segoe UI", 10)
)
incorrectPassword.pack(pady=(5, 5))
incorrectPassword.pack_forget()  # hidden until needed

# --- Login Button ---
loginButton = tk.Button(
    login_container,
    text="Login",
    font=("Segoe UI Semibold", 12),
    bg="white",            # White background
    fg="#005A9E",          # Dark blue text
    activebackground="#E6F0FF",  # Light blue when clicked
    activeforeground="#003E73",  # Even darker text when clicked
    relief="solid",
    bd=1,
    width=20,
    pady=8,
    cursor="hand2",
    command=lambda: loginAuthentication("user")
)
loginButton.pack(pady=(15, 25))

# Add rounded edges illusion with padding
login_container.configure(padx=40, pady=30)

# ========== USER HOME SCREEN ==========
homeScreen = tk.Frame(root, bg="lightblue")
taskbarHome = tk.Frame(homeScreen, bg="grey", height=40)
taskbarHome.pack(side="bottom", fill="x")
appFrameHome = tk.Frame(homeScreen, bg="lightblue")
appFrameHome.pack(side="left", padx=20, pady=(40, 0), anchor="n")

# Desktop icons
recycleBin = load_image("Frontend/Images/RecycleBin.png", (50, 50))
computer = load_image("Frontend/Images/Computer.png", (50, 50))
folder = load_image("Frontend/Images/Folder.png", (50, 50))
recycleBinLabel = tk.Label(appFrameHome, image=recycleBin, bg="lightblue", bd=0, highlightthickness=0)
recycleBinText = tk.Label(appFrameHome, text="Recycle Bin", bg="lightblue", fg="black", bd=0, highlightthickness=0)
computerLabel = tk.Label(appFrameHome, image=computer, bg="lightblue", bd=0, highlightthickness=0)
computerText = tk.Label(appFrameHome, text="Computer", bg="lightblue", fg="black", bd=0, highlightthickness=0)
folderLabel = tk.Label(appFrameHome, image=folder, bg="lightblue", bd=0, highlightthickness=0)
folderText = tk.Label(appFrameHome, text="Folder", bg="lightblue", fg="black", bd=0, highlightthickness=0)

recycleBinLabel.pack()
recycleBinText.pack()
computerLabel.pack()
computerText.pack()
folderLabel.pack()
folderText.pack()

# Taskbar icons
accountTaskbar = load_image("Frontend/Images/ProfilePicture.png", (30, 30))
accountTaskbarLabelHome = tk.Label(taskbarHome, image=accountTaskbar, bg="grey", bd=0, highlightthickness=0)
accountTaskbarLabelHome.pack(side="left", padx=10)
usernameHome = tk.Label(taskbarHome, text="User Account", bg="grey", fg="white")
usernameHome.pack(side="left", padx=10)

# Spacer for left-only margin
leftSpacerHome = tk.Frame(taskbarHome, width=450, bg="grey")
leftSpacerHome.pack(side="left")

# Taskbar apps
taskbarIconsHome = tk.Frame(taskbarHome, bg="grey")
taskbarIconsHome.pack(expand=True)
taskbarIconsHome.place(relx=0.5, rely=0.5, anchor="center")

for img_path in [
    "Frontend/Images/RecycleBin.png",
    "Frontend/Images/Computer.png",
    "Frontend/Images/Folder.png"
]:
    icon = load_image(img_path, (30, 30))
    lbl = tk.Label(taskbarIconsHome, image=icon, bg="grey", bd=0, highlightthickness=0)
    lbl.image = icon
    lbl.pack(side="left", padx=10)

logoutHomeButton = tk.Label(
    taskbarHome,
    text="Logout",
    bg="grey",
    fg="white",
    cursor="hand2",
    font=("Segoe UI", 10, "bold"),
    padx=12,
    pady=4
)
logoutHomeButton.pack(side="right", padx=10, pady=5)

# Hover and click behavior
def on_hover_home(e):
    e.widget.config(bg="#5a5a5a")
def on_leave_home(e):
    e.widget.config(bg="grey")
logoutHomeButton.bind("<Enter>", on_hover_home)
logoutHomeButton.bind("<Leave>", on_leave_home)
logoutHomeButton.bind("<Button-1>", lambda e: goToLogin())

# ========== ADMIN HOME SCREEN ==========
adminScreen = tk.Frame(root, bg="lightblue")
taskbarAdmin = tk.Frame(adminScreen, bg="grey", height=40)
taskbarAdmin.pack(side="bottom", fill="x")
appFrameAdmin = tk.Frame(adminScreen, bg="lightblue")
appFrameAdmin.pack(side="left", padx=20, pady=(40, 0), anchor="n")

# Desktop icons
tk.Label(appFrameAdmin, image=recycleBin, bg="lightblue", bd=0, highlightthickness=0).pack()
tk.Label(appFrameAdmin, text="Recycle Bin", bg="lightblue", fg="black", bd=0, highlightthickness=0).pack()
tk.Label(appFrameAdmin, image=computer, bg="lightblue", bd=0, highlightthickness=0).pack()
tk.Label(appFrameAdmin, text="Computer", bg="lightblue", fg="black", bd=0, highlightthickness=0).pack()
tk.Label(appFrameAdmin, image=folder, bg="lightblue", bd=0, highlightthickness=0).pack()
tk.Label(appFrameAdmin, text="Folder", bg="lightblue", fg="black", bd=0, highlightthickness=0).pack()
admin = load_image("Frontend/Images/Admin.png", (50, 50))
adminLabel = tk.Label(appFrameAdmin, image=admin, cursor="hand2", bg="lightblue", bd=0, highlightthickness=0)
adminText = tk.Label(appFrameAdmin, text="Admin", bg="lightblue", fg="black", bd=0, highlightthickness=0)
adminLabel.pack()
adminLabel.bind("<Button-1>", lambda e: openAdminMonitor())
adminText.pack()

# Taskbar icons
accountTaskbarLabelAdmin = tk.Label(taskbarAdmin, image=accountTaskbar, bg="grey", bd=0, highlightthickness=0)
accountTaskbarLabelAdmin.pack(side="left", padx=10)
usernameAdmin = tk.Label(taskbarAdmin, text="Admin Account", bg="grey", fg="white")
usernameAdmin.pack(side="left", padx=10)
taskbarIconsAdmin = tk.Frame(taskbarAdmin, bg="grey")
taskbarIconsAdmin.place(relx=0.5, rely=0.5, anchor="center")


for img_path in [
    "Frontend/Images/RecycleBin.png",
    "Frontend/Images/Computer.png",
    "Frontend/Images/Folder.png"
]:
    icon = load_image(img_path, (30, 30))
    lbl = tk.Label(taskbarIconsAdmin, image=icon, bg="grey")
    lbl.image = icon
    lbl.pack(side="left", padx=10)

adminSmall = load_image("Frontend/Images/Admin.png", (30, 30))
adminLabelSmall = tk.Label(taskbarIconsAdmin, image=adminSmall, cursor="hand2", bg="grey")
adminLabelSmall.image = adminSmall
adminLabelSmall.pack(side="left", padx=10)
adminLabelSmall.bind("<Button-1>", lambda e: openAdminMonitor())

logoutAdminButton = tk.Label(
    taskbarAdmin,
    text="Logout",
    bg="grey",
    fg="white",
    cursor="hand2",
    font=("Segoe UI", 10, "bold"),
    padx=12,
    pady=4
)
logoutAdminButton.pack(side="right", padx=10, pady=5)

# Hover and click behavior
def on_hover_admin(e):
    e.widget.config(bg="#5a5a5a")
def on_leave_admin(e):
    e.widget.config(bg="grey")
logoutAdminButton.bind("<Enter>", on_hover_admin)
logoutAdminButton.bind("<Leave>", on_leave_admin)
logoutAdminButton.bind("<Button-1>", lambda e: goToLogin())

# ========== SCREEN SWITCHING ==========
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
    adminMonitor.geometry("400x260")
    adminMonitor.configure(bg="white")

    # Title
    title = tk.Label(
        adminMonitor,
        text="Login Records",
        font=("Segoe UI Semibold", 15),
        bg="white",
        fg="black"
    )
    title.pack(pady=(10, 5))

    # Table Frame
    table_frame = tk.Frame(adminMonitor, bg="white")
    table_frame.pack(fill="both", expand=True, padx=8, pady=5)

    # Define table columns (User, Date, Time)
    columns = ("User", "Date", "Time")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)

    tree.heading("User", text="User")
    tree.heading("Date", text="Date")
    tree.heading("Time", text="Time")

    tree.column("User", width=120, anchor="center")
    tree.column("Date", width=120, anchor="center")
    tree.column("Time", width=140, anchor="center")

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    for record in login_records:
        username, login_datetime = record
        dt_obj = datetime.strptime(login_datetime, "%Y-%m-%d %H:%M:%S")
        tree.insert("", "end", values=(username, dt_obj.strftime("%Y-%m-%d"), dt_obj.strftime("%H:%M:%S")))

    tree.pack(fill="both", expand=True, padx=5)

    # Style for cleaner look
    style = ttk.Style()
    style.configure("Treeview", rowheight=22, font=("Segoe UI", 10))
    style.configure("Treeview.Heading", font=("Segoe UI Semibold", 10))

# ========== LOGIN AUTHENTICATION ==========
def loginAuthentication(roleAttempt):
    username = usernameEntry.get()
    password = passwordEntry.get()

    

    response1 = (
        supabase.table("profiles").select("is_admin, email").eq("username",username).execute()
    )

    response2 = supabase.auth.sign_in_with_password(
        {
            'email': str(response1.data[0]["email"]),
            'password': str(password),
        }
    )

    print(response1.data[0]["is_admin"])
    if response2.user.aud == "authenticated":
        # role = Accounts[username]["role"]
        incorrectPassword.pack_forget()
        if response1.data[0]["is_admin"]:
            goToAdmin()
        else:
            goToHome()
    else:
        incorrectPassword.pack()

# Button Commands
loginButton.config(command=lambda: loginAuthentication("user"))

# Start app
root.mainloop()
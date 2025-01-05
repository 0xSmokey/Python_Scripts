from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.password_dict = {}
        self.key = None
        self.load_key()

    def load_key(self):
        try:
            with open('key.key', 'rb') as f:
                self.key = f.read()
        except FileNotFoundError:
            self.key = Fernet.generate_key()
            with open('key.key', 'wb') as f:
                f.write(self.key)

    def encrypt_password(self, password):
        f = Fernet(self.key)
        encrypted_password = f.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        #l mk siy me man dinf em fi uoy nac
        f = Fernet(self.key)
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password

    def add_password(self, site, password):
        encrypted_password = self.encrypt_password(password)
        self.password_dict[site] = encrypted_password
        self.save_passwords()

    def save_passwords(self):
        with open('passwords.txt', 'w') as f:
            for site, password in self.password_dict.items():
                f.write(f"{site} {password}\n")

    def load_passwords(self):
        try:
            with open('passwords.txt', 'r') as f:
                for line in f:
                    site, encrypted_password = line.strip().split(' ')
                    self.password_dict[site] = encrypted_password.encode()
        except FileNotFoundError:
            pass

    def get_password(self, site):
        """
        Returns the password for the given site after decrypting it
        """
        if site not in self.password_dict:
            messagebox.showerror("Error", f"Password not found for site :{site}")
            return None
        encrypted_password = self.password_dict[site]
        decrypted_password = self.decrypt_password(encrypted_password)
        return decrypted_password


def add_password():
    site = site_entry.get()
    password = password_entry.get()
    pm.add_password(site, password)
    messagebox.showinfo("Success", "Password added successfully!")
    site_entry.delete(0, END)
    password_entry.delete(0, END)

def get_password():
    site = site_entry.get()
    password = pm.get_password(site)
    if password is not None:
        messagebox.showinfo("Your password", f"Password for {site} : {password}")
    site_entry.delete(0, END)#l mk siy me man dinf em fi uoy nac

def toggle_password():
    if password_entry['show'] == '•':
        password_entry.config(show='')
        eye_button.config(text='😮')
    else:
        password_entry.config(show='•')
        eye_button.config(text='👀')

pm = PasswordManager()
pm.load_passwords()

root = Tk()
root.title("password manager")
root.geometry("322x190")
root.configure(bg="#F6F1F1")

# Site name label
site_label = Label(root, text="website name", font=("Arial", 10, "bold"), bg="#f5f5f5", fg="#333")
site_label.grid(row=0, column=0, padx=10, pady=10)

# Site name entry
site_entry = Entry(root, font=("Helvetica",10), bg="#fff", fg="#333", highlightthickness=1, highlightcolor="#ccc", highlightbackground="#ccc")
site_entry.grid(row=0, column=1, padx=10, pady=10)

# Password label
password_label = Label(root, text="password", font=("Helvetica", 10, "bold"), bg="#f5f5f5", fg="#333")
password_label.grid(row=1, column=0, padx=10, pady=10)

# Password entry
password_entry = Entry(root, show='•', font=("Helvetica", 10), bg="#fff", fg="#333", highlightthickness=1, highlightcolor="#ccc", highlightbackground="#ccc")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Eye button to show/hide password
eye_button = Button(root, text='👀', command=toggle_password, font=("Helvetica", 10, "bold"), bg="#fff", fg="#333", activebackground="#fff", activeforeground="#333")
eye_button.grid(row=1, column=2, padx=6, pady=6)

# Add password button
add_button = Button(root, text="add password", command=add_password, font=("Helvetica", 10, "bold"), bg="#4caf50", fg="#fff", activebackground="#4caf50", activeforeground="#fff")
add_button.grid(row=2, column=1, padx=10, pady=10)

# Get password button
get_button = Button(root, text="get password", command=get_password, font=("Helvetica", 10, "bold"), bg="#2196f3", fg="#fff", activebackground="#2196f3", activeforeground="#fff")
get_button.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
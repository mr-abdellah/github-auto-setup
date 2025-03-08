# 🚀 GitHub Auto Setup

A simple Python script to automate Git configuration and SSH key setup.

## 📌 Features
- Configures Git with your **name** and **email**.
- Sets the default branch to `main`.
- Disables pull rebase for smoother merging.
- Generates an **SSH key** if not found.
- Displays the **SSH public key** for easy GitHub setup.

---

## 📥 Installation

### Prerequisites  
Ensure you have:
- **Python 3.6+** installed  
- **Git** installed (`git --version` to check)  
- **OpenSSH** installed (Windows users: included in Windows 10+)

### Clone the Repo
```sh
git clone https://github.com/mr-abdellah/github-auto-setup.git
cd github-auto-setup
```

---

## 🔧 Usage

Run the script and follow the prompts:
```sh
python setup_github.py
```
You'll be asked to enter:
1. Your **GitHub name**
2. Your **GitHub email**

The script will configure Git and generate an SSH key if needed.

---

## 🛠 Adding Your SSH Key to GitHub

After running the script, copy your SSH key and add it to GitHub:

```sh
cat ~/.ssh/id_ed25519.pub  # Linux/macOS
type %USERPROFILE%\.ssh\id_ed25519.pub  # Windows
```

Then go to **GitHub → Settings → SSH & GPG Keys** and paste the key.

---

## 🏗 Contributing

1. **Fork** the repo  
2. Create a **new branch**:  
   ```sh
   git checkout -b feature-name
   ```
3. **Commit changes**:  
   ```sh
   git commit -m "Add new feature"
   ```
4. **Push to GitHub**:  
   ```sh
   git push origin feature-name
   ```
5. Open a **Pull Request**  

---

## 📜 License

This project is licensed under the **MIT License** – free to use, modify, and distribute.

---

🚀 **Made with ❤️ for Devs!**

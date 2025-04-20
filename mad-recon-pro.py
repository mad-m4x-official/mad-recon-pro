#!/usr/bin/env python3
import os
import platform
import subprocess
import sys
import shutil

# ---------- CONFIG ----------
TOOLS_DIR = os.path.expanduser("~/tools")
BIN_DIR = os.path.expanduser("~/.local/bin")

# ---------- SYSTEM PATH ADD ----------
def add_to_path():
    shell_rc = os.path.expanduser("~/.bashrc") if os.environ.get("SHELL", "").endswith("bash") else os.path.expanduser("~/.zshrc")
    export_line = f'\nexport PATH="$PATH:{BIN_DIR}"\n'
    if export_line.strip() not in open(shell_rc).read():
        with open(shell_rc, "a") as rc:
            rc.write(export_line)
    os.environ["PATH"] += f":{BIN_DIR}"
    print(f"[+] PATH updated and added to {shell_rc}")

# ---------- TOOL INSTALLER ----------
def install_tool(name, command):
    print(f"[+] Installing {name}...")
    path = os.path.join(TOOLS_DIR, name)
    if os.path.exists(path):
        print(f"[-] {name} already exists. Updating...")
        try:
            subprocess.run(f"cd {path} && git pull", shell=True, check=True, executable="/bin/bash")
        except subprocess.CalledProcessError:
            print(f"[!] Update failed for {name}. Skipping...")
        return
    os.chdir(TOOLS_DIR)
    for attempt in range(2):
        try:
            subprocess.run(command, shell=True, check=True, executable="/bin/bash")
            break
        except subprocess.CalledProcessError as e:
            print(f"[!] Attempt {attempt+1} failed to install {name}: {e}")
            if attempt == 1:
                print(f"[!] Skipping {name} after 2 failed attempts.")

# ---------- SYMLINK CREATION ----------
def create_symlinks():
    os.makedirs(BIN_DIR, exist_ok=True)
    for root, _, files in os.walk(TOOLS_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            if os.access(full_path, os.X_OK) and not file.endswith(('.md', '.txt', '.pyc')):
                symlink_path = os.path.join(BIN_DIR, file)
                if not os.path.exists(symlink_path):
                    try:
                        os.symlink(full_path, symlink_path)
                    except Exception:
                        pass

# ---------- DEPENDENCY CHECKERS ----------
REQUIRED_PKG = {
    "go": "sudo apt install -y golang",
    "pip": "sudo apt install -y python3-pip",
    "cargo": "sudo apt install -y cargo",
    "gem": "sudo apt install -y ruby-full",
    "snap": "sudo apt install -y snapd",
    "git": "sudo apt install -y git"
}

TERMUX_PKG = {
    "go": "pkg install -y golang",
    "pip": "pkg install -y python3-pip",
    "cargo": "pkg install -y rust",
    "gem": "pkg install -y ruby",
    "git": "pkg install -y git"
}

WINDOWS_HINT = "Please install dependencies manually via Chocolatey or Winget."

def check_dependencies():
    print("[+] Checking dependencies...")
    termux = shutil.which("pkg")
    is_windows = platform.system() == "Windows"
    for binary in REQUIRED_PKG:
        if shutil.which(binary) is None:
            print(f"[!] Missing dependency: {binary}.")
            if termux:
                subprocess.run(TERMUX_PKG[binary], shell=True)
            elif is_windows:
                print(f"[!] {binary} missing on Windows. {WINDOWS_HINT}")
            else:
                subprocess.run(REQUIRED_PKG[binary], shell=True)

# ---------- TOOL TEST ----------
def verify_installation(tool):
    if shutil.which(tool):
        print(f"[✔] {tool} installed successfully!")
    else:
        print(f"[✘] {tool} not found in PATH!")

# ---------- MAIN ----------
def main():
    banner()
    os.makedirs(TOOLS_DIR, exist_ok=True)
    check_dependencies()
    from tools import TOOLS  # tools.py has your categorized tool list
    for category, tools in TOOLS.items():
        print(f"\n===== {category} =====")
        for name, command in tools:
            install_tool(name, command)
            verify_installation(name)
    create_symlinks()
    add_to_path()
    print("\n✅ All tools installed successfully. You can now use them from anywhere in your terminal.")

# ---------- BANNER ----------
def banner():
    print("""\033[91m
 __  __           _ ____                        ____  
|  \/  | __ _ ___| |  _ \ ___  ___ ___  _ __   |  _ \ ___  ___ ___ 
| |\/| |/ _` / __| | |_) / _ \/ __/ _ \| '_ \  | |_) / _ \/ __/ __|
| |  | | (_| \__ \ |  __/  __/ (_| (_) | | | | |  _ <  __/\__ \__ \
|_|  |_|\__,_|___/_|_|   \___|\___\___/|_| |_| |_| \_\___||___/___/
\033[0m""")

if __name__ == "__main__":
    main()

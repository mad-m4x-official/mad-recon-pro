#!/usr/bin/env python3
import os
import platform
import subprocess
import sys
import shutil

# ---------- CONFIG ----------
TOOLS_DIR = os.path.expanduser("~/tools")
BIN_DIR = os.path.expanduser("~/.local/bin")

# ---------- COLORS ----------
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# ---------- TOOL INSTALLER ----------
def install_tool(name, command):
    print(f"{YELLOW}[+] Installing {name}...{RESET}")
    path = os.path.join(TOOLS_DIR, name)
    if os.path.exists(path):
        print(f"{YELLOW}[-] {name} already exists. Updating...{RESET}")
        try:
            subprocess.run(f"cd {path} && git pull", shell=True, check=True, executable="/bin/bash")
        except subprocess.CalledProcessError:
            print(f"{RED}[!] Update failed for {name}. Skipping...{RESET}")
        return
    os.chdir(TOOLS_DIR)
    for attempt in range(2):
        try:
            subprocess.run(command, shell=True, check=True, executable="/bin/bash")
            break
        except subprocess.CalledProcessError as e:
            print(f"{RED}[!] Attempt {attempt+1} failed to install {name}: {e}{RESET}")
            if attempt == 1:
                print(f"{RED}[!] Skipping {name} after 2 failed attempts.{RESET}")

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
    "git": "sudo apt install -y git"
}

WINDOWS_HINT = "Please install dependencies manually via Chocolatey or Winget."

def check_dependencies():
    print(f"{YELLOW}[+] Checking dependencies...{RESET}")
    is_windows = platform.system() == "Windows"
    for binary in REQUIRED_PKG:
        if shutil.which(binary) is None:
            print(f"{RED}[!] Missing dependency: {binary}.{RESET}")
            if is_windows:
                print(f"{RED}[!] {binary} missing on Windows. {WINDOWS_HINT}{RESET}")
            else:
                subprocess.run(REQUIRED_PKG[binary], shell=True)

# ---------- TOOL TEST ----------
def verify_installation(tool):
    if shutil.which(tool):
        print(f"{GREEN}[✔] {tool} installed successfully!{RESET}")
    else:
        print(f"{RED}[✘] {tool} not found in PATH!{RESET}")

# ---------- PATH FIX ----------
def add_to_path():
    shell_rc = os.path.expanduser("~/.bashrc") if os.environ.get("SHELL", "").endswith("bash") else os.path.expanduser("~/.zshrc")
    export_line = f'\nexport PATH="$PATH:{BIN_DIR}"\n'
    if export_line.strip() not in open(shell_rc).read():
        with open(shell_rc, "a") as rc:
            rc.write(export_line)
    os.environ["PATH"] += f":{BIN_DIR}"
    print(f"{YELLOW}[+] PATH updated and added to {shell_rc}{RESET}")

# ---------- MAIN ----------
def main():
    banner()
    os.makedirs(TOOLS_DIR, exist_ok=True)
    check_dependencies()
    from tools import TOOLS  # tools.py has your categorized tool list
    for category, tools in TOOLS.items():
        print(f"\n===== {category} =====")
        for name, command in tools:
            # Add --break-system-packages flag if pip is used
            if 'pip install' in command:
                command += ' --break-system-packages'
            install_tool(name, command)
            verify_installation(name)
    create_symlinks()
    add_to_path()
    print(f"\n{GREEN}✅ All tools installed. Open a new terminal to use them.{RESET}")

# ---------- SIMPLE BANNER ----------
def banner():
    print(f"{GREEN}[ mad-recon-pro ] Installing tools...{RESET}")

if __name__ == "__main__":
    main()

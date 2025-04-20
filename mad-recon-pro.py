import os
import sys
import subprocess
import json
import argparse
import shutil
import platform
from datetime import datetime
from termcolor import cprint, colored

# ==== CONFIG START ====
BANNER = r"""
 __  __         _ ____                       ____  ____   ___  
|  \/  |___ _ _| |  _ \__ _ _______ _ _ ___ |  _ \|  _ \ / _ \ 
| |\/| / -_) '_| | |_) \ V / _ \ \ / '_/ -_)| | | | |_) | (_) |
|_|  |_\___|_| |_|____/\_/\___/_\_\_| \___||_| |_| .__/ \___/ 
                                               |_|            
                    MAD RECON PRO
"""

TOOLS_JSON = "install_report.json"
BASE_DIR = os.path.expanduser("~/.mad-recon-pro")
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
CATEGORIES = {
    "recon": ["subfinder", "amass", "assetfinder"],
    "xss": ["kxss", "dalfox"],
    "sqli": ["sqlmap"],
    # Add more categories and tools as needed
}

COLOR_MAP = {"installing": "blue", "success": "green", "error": "red"}
# ==== CONFIG END ====

def print_banner():
    cprint(BANNER, "cyan")

def color_print(text, status):
    cprint(text, COLOR_MAP.get(status, "white"))

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        return None

def ensure_path():
    if TOOLS_DIR not in os.environ.get("PATH", ""):
        bashrc = os.path.expanduser("~/.bashrc")
        with open(bashrc, "a") as f:
            f.write(f"\nexport PATH=\"$PATH:{TOOLS_DIR}\"\n")
        os.environ["PATH"] += os.pathsep + TOOLS_DIR
        color_print("[+] PATH updated. Run 'source ~/.bashrc' to apply.", "success")

def create_symlink(tool_path, name):
    link_path = os.path.join(TOOLS_DIR, name)
    if not os.path.exists(TOOLS_DIR):
        os.makedirs(TOOLS_DIR)
    if os.path.exists(link_path):
        os.remove(link_path)
    os.symlink(tool_path, link_path)


def tool_health_check(name):
    return shutil.which(name) is not None

def install_tool(name):
    color_print(f"[*] Installing {name}...", "installing")
    success = False
    if name == "subfinder":
        run_cmd("go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")
        bin_path = os.path.expanduser("~/go/bin/subfinder")
        if os.path.exists(bin_path):
            create_symlink(bin_path, "subfinder")
            fix_subfinder_config()
            success = True
    elif name == "amass":
        run_cmd("go install github.com/owasp-amass/amass/v4/...@latest")
        bin_path = os.path.expanduser("~/go/bin/amass")
        if os.path.exists(bin_path):
            create_symlink(bin_path, "amass")
            success = True
    elif name == "sqlmap":
        repo = os.path.join(BASE_DIR, "sqlmap")
        if not os.path.exists(repo):
            run_cmd(f"git clone https://github.com/sqlmapproject/sqlmap {repo}")
        create_symlink(os.path.join(repo, "sqlmap.py"), "sqlmap")
        success = True
    else:
        color_print(f"[-] No installer defined for {name}.", "error")

    color_print(f"[+] Installed {name}" if success else f"[!] Failed {name}", "success" if success else "error")
    return {"tool": name, "status": "success" if success else "error"}


def fix_subfinder_config():
    config_path = os.path.expanduser("~/.config/subfinder/config.yaml")
    if os.path.exists(config_path):
        with open(config_path, "r+") as f:
            data = f.read()
            if "shodan:" in data and "YOUR_API_KEY" in data:
                data = data.replace("YOUR_API_KEY", "")
                f.seek(0)
                f.write(data)
                f.truncate()
        color_print("[+] Subfinder config fixed.", "success")


def save_report(results):
    with open(TOOLS_JSON, "w") as f:
        json.dump(results, f, indent=2)


def uninstall_tool(name):
    link_path = os.path.join(TOOLS_DIR, name)
    if os.path.exists(link_path):
        os.remove(link_path)
        color_print(f"[+] {name} uninstalled.", "success")
    else:
        color_print(f"[-] {name} not found.", "error")


def main():
    parser = argparse.ArgumentParser(description="MAD RECON PRO")
    parser.add_argument("--category", help="Install tools by category: recon, xss, sqli")
    parser.add_argument("--uninstall", help="Uninstall a specific tool")
    parser.add_argument("--health", action="store_true", help="Check health of all installed tools")
    parser.add_argument("--offline", action="store_true", help="Use offline mode if tools already downloaded")
    args = parser.parse_args()

    print_banner()
    ensure_path()

    results = []

    if args.uninstall:
        uninstall_tool(args.uninstall)
        return

    tools = []
    if args.category:
        tools = CATEGORIES.get(args.category.lower(), [])
        if not tools:
            color_print("[!] Invalid category.", "error")
            return
    else:
        tools = [tool for tools in CATEGORIES.values() for tool in tools]

    for tool in tools:
        results.append(install_tool(tool))

    if args.health:
        for tool in tools:
            ok = tool_health_check(tool)
            color_print(f"[*] {tool}: {'OK' if ok else 'NOT FOUND'}", "success" if ok else "error")

    save_report(results)
    color_print(f"[+] Installation completed. Report saved to {TOOLS_JSON}", "success")


if __name__ == "__main__":
    main()

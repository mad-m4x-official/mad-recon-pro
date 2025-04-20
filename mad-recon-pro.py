import os
import sys
import subprocess
import json
import argparse
import shutil
import platform
from datetime import datetime
from termcolor import cprint, colored
from difflib import get_close_matches
from flask import Flask, render_template_string, request, redirect, url_for

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
}

COLOR_MAP = {"installing": "blue", "success": "green", "error": "red"}
# ==== CONFIG END ====

app = Flask(__name__)


def print_banner():
    cprint(BANNER, "cyan")


def color_print(text, status):
    cprint(text, COLOR_MAP.get(status, "white"))


def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode().strip()
    except subprocess.CalledProcessError:
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


def get_suggestion(name):
    all_tools = [tool for tools in CATEGORIES.values() for tool in tools]
    match = get_close_matches(name, all_tools, n=1)
    return match[0] if match else None


def version_check(tool, cmd="--version"):
    path = shutil.which(tool)
    if path:
        try:
            output = subprocess.check_output([tool, cmd], stderr=subprocess.STDOUT).decode()
            return output.strip()
        except:
            return "unknown"
    return "not installed"


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


@app.route("/", methods=["GET", "POST"])
def dashboard():
    installed = [tool for tools in CATEGORIES.values() for tool in tools if tool_health_check(tool)]
    all_tools = [tool for tools in CATEGORIES.values() for tool in tools]
    if request.method == "POST":
        action = request.form.get("action")
        tool = request.form.get("tool")
        if action == "install":
            install_tool(tool)
        elif action == "uninstall":
            uninstall_tool(tool)
        return redirect(url_for("dashboard"))

    return render_template_string("""
        <h2>MAD RECON PRO Dashboard</h2>
        <form method="post">
        {% for tool in tools %}
            <div>
                <b>{{ tool }}</b>
                {% if tool in installed %}
                    <button name="action" value="uninstall">Uninstall</button>
                {% else %}
                    <button name="action" value="install">Install</button>
                {% endif %}
                <input type="hidden" name="tool" value="{{ tool }}">
            </div>
        {% endfor %}
        </form>
    """, tools=all_tools, installed=installed)


def main():
    parser = argparse.ArgumentParser(description="MAD RECON PRO")
    parser.add_argument("--category", help="Install tools by category: recon, xss, sqli")
    parser.add_argument("--uninstall", help="Uninstall a specific tool")
    parser.add_argument("--health", action="store_true", help="Check health of all installed tools")
    parser.add_argument("--offline", action="store_true", help="Use offline mode if tools already downloaded")
    parser.add_argument("--web", action="store_true", help="Run Web Dashboard")
    args = parser.parse_args()

    if args.web:
        app.run(debug=True)
        return

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
            suggestion = get_suggestion(args.category.lower())
            if suggestion:
                color_print(f"[!] Invalid category. Did you mean: {suggestion}?", "error")
            else:
                color_print("[!] Invalid category.", "error")
            return
    else:
        tools = [tool for tools in CATEGORIES.values() for tool in tools]

    for tool in tools:
        version = version_check(tool)
        color_print(f"[*] {tool} version: {version}", "installing")
        results.append(install_tool(tool))

    if args.health:
        for tool in tools:
            ok = tool_health_check(tool)
            color_print(f"[*] {tool}: {'OK' if ok else 'NOT FOUND'}", "success" if ok else "error")

    save_report(results)
    color_print(f"[+] Installation completed. Report saved to {TOOLS_JSON}", "success")


if __name__ == "__main__":
    main()

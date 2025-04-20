# 🛠️ mad-recon-pro

**mad-recon-pro** is a fully automated, all-in-one Bug Bounty & Recon toolkit that installs, updates, and configures all major tools — with support for Linux, Termux, and Windows. One command and you're ready to hack!

---

## ✨ Features

- ✅ Installs all essential Bug Bounty tools in categorized order
- ✅ Automatically updates `$PATH` (no terminal restart required)
- ✅ Organizes all tools under `~/tools`
- ✅ Verifies tool installation after setup
- ✅ Updates existing tools if already installed
- ✅ Auto-retry or skip on installation failure
- ✅ Supports Linux, Windows, and Termux
- ✅ Creates symlinks to make tools globally accessible
- ✅ Smart dependency checks and installation

---

## 📦 Tool Categories (`tools.py` contains the full list)

- 🕵️ **Subdomain Enumeration**: `amass`, `subfinder`, `findomain`, `massdns`, `dnsx`, `shuffledns`, `subjack`, `subzy`, etc.
- 🔎 **Recon & OSINT**: `theHarvester`, `recon-ng`, `shodan`, `GitHarvester`, `censys`, etc.
- 🔐 **Secrets & Git Leaks**: `gitleaks`, `trufflehog`, `git-secrets`, etc.
- 🔥 **Vulnerability Scanners**: `nuclei`, `nikto`, `wpscan`, `osv-scanner`, `vuls`, etc.
- 💣 **Exploitation Tools**: `sqlmap`, `commix`, `XSStrike`, `Dalfox`, `gf`, `tplmap`, etc.
- 📂 **Content Discovery**: `ffuf`, `dirsearch`, `feroxbuster`, `arjun`, `paramspider`, etc.
- 🛡️ **CMS Scanners**: `whatweb`, `droopescan`, `CMSeeK`, etc.
- 🧪 **Fuzzing**: `wfuzz`, `sfuzz`, `boofuzz`, `zaproxy`, etc.
- 🌐 **Web Probing**: `httpx`, `gau`, `waybackurls`, `hakrawler`, `katana`, etc.
- 🎯 **Port Scanners**: `nmap`, `naabu`, `rustscan`, `masscan`, etc.
- 🔭 **Visual Recon**: `gowitness`, `eyewitness`, `aquatone`
- 🛠️ **LFI, SSTI, RFI, RCE, SSRF, etc.**: `LFISuite`, `SSTImap`, `SSRFire`, etc.
- 📈 **Top OWASP Scanners**: `OWASP ZAP`, `Arachni`, `IronWASP`, etc.
- 📦 **Miscellaneous**: `Metasploit`, `Burp Suite`, `Interlace`, `mitmproxy`

---

## 🚀 Usage

```bash
git clone https://github.com/mad-m4x-official/mad-recon
cd mad-recon
python3 mad-recon-pro.py

File | Description
mad-recon-pro.py | Main installer script
tools.py | All categorized tools and their install commands
README.md | Documentation file you're reading right now

🧑‍💻 Author
GitHub: mad-m4x-official
Feel free to open an issue or submit a pull request for suggestions or fixes.

⚠️ Disclaimer
This toolkit is intended for educational and authorized penetration testing purposes only.
Any misuse of this toolkit is solely your responsibility.


---

You can now copy and paste this into your `README.md` file and commit it to the main branch.

Let me know if you want help writing the commit message for it or want to update it with badges, license, or demo GIFs.

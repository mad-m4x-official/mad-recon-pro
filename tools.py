# tools.py

TOOLS = {
    "🕵️‍♂️ Subdomain Enumeration": [
        "Sublist3r", "git clone https://github.com/aboul3la/Sublist3r.git",
        "amass", "go install -v github.com/owasp-amass/amass/v4/...@latest",
        "findomain", "git clone https://github.com/findomain/findomain.git && cd findomain && cargo build --release",
        "subfinder", "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
        "assetfinder", "go install github.com/tomnomnom/assetfinder@latest",
        "dnsx", "go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest",
        "shuffledns", "go install -v github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest",
        "massdns", "git clone https://github.com/blechschmidt/massdns.git && cd massdns && make",
        "subzy", "go install -v github.com/LukaSikic/subzy@latest",
        "subjack", "go install github.com/haccer/subjack@latest",
        "tko-subs", "git clone https://github.com/anshumanbh/tko-subs.git"
    ],
    "🔎 Recon / OSINT Tools": [
        "theHarvester", "git clone https://github.com/laramies/theHarvester.git",
        "recon-ng", "git clone https://github.com/lanmaster53/recon-ng.git",
        "shodan", "pip install -U shodan",
        "censys", "pip install censys",
        "spiderfoot", "git clone https://github.com/smicallef/spiderfoot.git",
        "FOCA", "echo 'Manual tool, Windows only'"),
        "DorkSearch", "git clone https://github.com/techgaun/github-dorks.git",
        "GitHarvester", "git clone https://github.com/UnkL4b/GitHarvester.git"
    ],
    "🔥 Vulnerability Scanners": [
        "nuclei", "go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest",
        "nikto", "git clone https://github.com/sullo/nikto.git",
        "wpscan", "gem install wpscan",
        "vulners", "pip install vulners",
        "osv-scanner", "go install github.com/google/osv-scanner/cmd/osv-scanner@latest",
        "vuls", "go install github.com/future-architect/vuls@latest"
    ],
    "💣 Exploitation Tools": [
        "sqlmap", "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git",
        "commix", "git clone https://github.com/commixproject/commix.git",
        "XSStrike", "git clone https://github.com/s0md3v/XSStrike.git",
        "XSSer", "git clone https://github.com/epsylon/xsser.git",
        "Dalfox", "go install github.com/hahwul/dalfox/v2@latest",
        "crlfuzz", "go install github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest",
        "gf", "go install github.com/tomnomnom/gf@latest",
        "tplmap", "git clone https://github.com/epinna/tplmap.git",
        "JWT_Tool", "git clone https://github.com/ticarpi/jwt_tool.git"
    ],
    "📂 Content Discovery": [
        "ffuf", "go install github.com/ffuf/ffuf@latest",
        "gobuster", "go install github.com/OJ/gobuster/v3@latest",
        "dirsearch", "git clone https://github.com/maurosoria/dirsearch.git",
        "feroxbuster", "cargo install feroxbuster",
        "arjun", "git clone https://github.com/s0md3v/Arjun.git",
        "paramspider", "git clone https://github.com/devanshbatham/ParamSpider.git",
        "kxss", "go install github.com/Emoe/kxss@latest"
    ],
    "🛡️ CMS Scanners": [
        "droopescan", "pip install droopescan",
        "whatweb", "git clone https://github.com/urbanadventurer/WhatWeb.git",
        "CMSeeK", "git clone https://github.com/Tuhinshubhra/CMSeeK.git"
    ],
    "🧲 Fuzzing & Testing": [
        "wfuzz", "pip install wfuzz",
        "fuff", "go install github.com/ffuf/ffuf@latest",
        "boofuzz", "pip install boofuzz",
        "sfuzz", "go install github.com/solimanosfuzz/sfuzz@latest",
        "zaproxy", "snap install zaproxy --classic"
    ],
    "🌐 Web Probing / Recon": [
        "httpx", "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest",
        "waybackurls", "go install github.com/tomnomnom/waybackurls@latest",
        "gau", "go install github.com/lc/gau/v2/cmd/gau@latest",
        "hakrawler", "go install github.com/hakluke/hakrawler@latest",
        "katana", "go install github.com/projectdiscovery/katana/cmd/katana@latest"
    ],
    "🗄️ Wordlists": [
        ("SecLists", "git clone https://github.com/danielmiessler/SecLists.git"),
        ("PayloadsAllTheThings", "git clone https://github.com/swisskyrepo/PayloadsAllTheThings.git"
    ],
    "🔐 Secrets & Git Leaks": [
        "gitleaks", "go install github.com/gitleaks/gitleaks/v8@latest",
        "trufflehog", "pip install trufflehog",
        "gittyleaks", "git clone https://github.com/kootenpv/gittyleaks.git",
        "git-secrets", "git clone https://github.com/awslabs/git-secrets.git",
        "repo-supervisor", "git clone https://github.com/auth0/repo-supervisor.git"
    ],
    "🎯 Port Scanning / Network": [
        "nmap", "sudo apt install -y nmap",
        "masscan", "git clone https://github.com/robertdavidgraham/masscan.git && cd masscan && make",
        "rustscan", "cargo install rustscan"),
        "naabu", "go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest"
    ],
    "🔭 Visual Recon": [
        "aquatone", "go install github.com/michenriksen/aquatone@latest",
        "eyewitness", "git clone https://github.com/FortyNorthSecurity/EyeWitness.git",
        "gowitness", "go install github.com/sensepost/gowitness@latest"
    ],
    "🛠️ LFI, RCE, RFI, SSTI, etc.": [
        "LFISuite", "git clone https://github.com/D35m0nd142/LFISuite.git",
        "LFI-fuzzer", "git clone https://github.com/hansmach1ne/LFI-fuzzer.git",
        "SSTImap", "git clone https://github.com/vladko312/SSTImap.git",
        "SSRFmap", "git clone https://github.com/swisskyrepo/SSRFmap.git",
        "SSRFire", "git clone https://github.com/cujanovic/SSRFire.git"
    ],
    "📈 Top OWASP Vuln Scanners": [
        "OWASP ZAP", "snap install zaproxy --classic",
        "Nikto", "git clone https://github.com/sullo/nikto.git",
        "Wapiti", "git clone https://github.com/wapiti-scanner/wapiti.git",
        "Arachni", "echo 'Arachni needs manual install from binaries'",
        "IronWASP", "echo 'IronWASP is Windows GUI tool, skip for CLI'"
    ],
    "📦 Miscellaneous": [
        "Interlace", "git clone https://github.com/codingo/Interlace.git",
        "Metasploit", "curl https://raw.githubusercontent.com/rapid7/metasploit-framework/master/msfinstall | sh",
        "Burp Suite", "echo 'Manual download required for GUI version'",
        "mitmproxy", "pip install mitmproxy"
    ]
}

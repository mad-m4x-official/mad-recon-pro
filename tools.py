TOOLS = {
    "🕵️‍♂️ Subdomain Enumeration": {
        "assetfinder": "go install github.com/tomnomnom/assetfinder@latest",
        "amass": "go install github.com/owasp-amass/amass/v4/...@latest",
        "subfinder": "GO111MODULE=on go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"
    },
    "🔎 Recon / OSINT Tools": {
        "theHarvester": "git clone https://github.com/laramies/theHarvester.git && cd theHarvester && pip install -r requirements.txt",
        "recon-ng": "git clone https://github.com/lanmaster53/recon-ng.git && cd recon-ng && pip install -r REQUIREMENTS"
    },
    "🔥 Vulnerability Scanners": {
        "nuclei": "go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest",
        "dalfox": "go install github.com/hahwul/dalfox/v2@latest"
    },
    "💣 Exploitation Tools": {
        "sqlmap": "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev",
        "XSStrike": "git clone https://github.com/s0md3v/XSStrike.git && cd XSStrike && pip install -r requirements.txt"
    },
    "🧱 Content Discovery": {
        "dirsearch": "git clone https://github.com/maurosoria/dirsearch.git",
        "ffuf": "go install github.com/ffuf/ffuf/v2@latest"
    },
    "🧩 CMS Scanners": {
        "wpscan": "gem install wpscan",
        "droopescan": "pip install droopescan"
    },
    "🧪 Fuzzing Tools": {
        "wfuzz": "pip install wfuzz",
        "fuffler": "go install github.com/dwisiswant0/fuffler@latest"
    },
    "🌐 Web Probing": {
        "httpx": "go install github.com/projectdiscovery/httpx/cmd/httpx@latest",
        "httprobe": "go install github.com/tomnomnom/httprobe@latest"
    },
    "📦 Wordlists": {
        "SecLists": "git clone https://github.com/danielmiessler/SecLists.git",
        "fuzz-wordlist": "wget https://wordlists-cdn.assetnote.io/data/manual/fuzz.txt -O fuzz.txt"
    },
    "🔐 Secrets & Git Leaks": {
        "truffleHog": "pip install truffleHog",
        "gitleaks": "go install github.com/gitleaks/gitleaks/v8@latest"
    },
    "🌊 Port Scanning": {
        "naabu": "go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest",
        "rustscan": "cargo install rustscan"
    },
    "🖼️ Visual Recon": {
        "aquatone": "GO111MODULE=on go install github.com/michenriksen/aquatone@latest"
    },
    "💥 LFI/RCE/SSRF/etc.": {
        "lfimap": "git clone https://github.com/honze-net/lfi-exploit.git",
        "SSRFmap": "git clone https://github.com/swisskyrepo/SSRFmap.git && cd SSRFmap && pip install -r requirements.txt"
    },
    "🛡️ OWASP Scanners": {
        "owasp-zap": "sudo snap install zaproxy --classic"
    },
    "⚙️ Miscellaneous": {
        "interactsh-client": "go install github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest",
        "uro": "pip install uro"
    }
}

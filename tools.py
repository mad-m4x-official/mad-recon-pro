TOOLS = {
    "🕵️‍♂️ Subdomain Enumeration": {
        "Sublist3r": "git clone https://github.com/aboul3la/Sublist3r.git",
        "amass": "go install -v github.com/owasp-amass/amass/v4/...@latest",
        "findomain": "git clone https://github.com/findomain/findomain.git && cd findomain && cargo build --release",
        "subfinder": "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
        "assetfinder": "go install github.com/tomnomnom/assetfinder@latest",
        "dnsx": "go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest",
        "shuffledns": "go install -v github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest",
        "massdns": "git clone https://github.com/blechschmidt/massdns.git && cd massdns && make",
        "subzy": "go install -v github.com/LukaSikic/subzy@latest",
        "subjack": "go install github.com/haccer/subjack@latest",
        "tko-subs": "git clone https://github.com/anshumanbh/tko-subs.git"
    },
    "🔎 Recon / OSINT Tools": {
        "theHarvester": "git clone https://github.com/laramies/theHarvester.git",
        "recon-ng": "git clone https://github.com/lanmaster53/recon-ng.git",
        "shodan": "pip install -U shodan",
        "censys": "pip install censys",
        "spiderfoot": "git clone https://github.com/smicallef/spiderfoot.git",
        "FOCA": "echo 'Manual tool, Windows only'",
        "DorkSearch": "git clone https://github.com/techgaun/github-dorks.git",
        "GitHarvester": "git clone https://github.com/UnkL4b/GitHarvester.git"
    },
    "🔥 Vulnerability Scanners": {
        "nuclei": "go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest",
        "nikto": "git clone https://github.com/sullo/nikto.git",
        "wpscan": "gem install wpscan",
        "vulners": "pip install vulners",
        "osv-scanner": "go install github.com/google/osv-scanner/cmd/osv-scanner@latest",
        "vuls": "go install github.com/future-architect/vuls@latest"
    },
    "💣 Exploitation Tools": {
        "sqlmap": "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git",
        "commix": "git clone https://github.com/commixproject/commix.git",
        "XSStrike": "git clone https://github.com/s0md3v/XSStrike.git",
        "XSSer": "git clone https://github.com/epsylon/xsser.git",
        "Dalfox": "go install github.com/hahwul/dalfox/v2@latest",
        "crlfuzz": "go install github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest",
        "gf": "go install github.com/tomnomnom/gf@latest",
        "tplmap": "git clone https://github.com/epinna/tplmap.git",
        "JWT_Tool": "git clone https://github.com/ticarpi/jwt_tool.git"
    },
    "🧱 Content Discovery": {
        "dirsearch": "git clone https://github.com/maurosoria/dirsearch.git",
        "ffuf": "go install github.com/ffuf/ffuf@latest",
        "gobuster": "go install github.com/OJ/gobuster/v3@latest"
    },
    "🧩 CMS Scanners": {
        "droopescan": "pip install droopescan",
        "wpscan": "gem install wpscan",
        "whatweb": "git clone https://github.com/urbanadventurer/WhatWeb.git"
    },
    "🧪 Fuzzing Tools": {
        "ffuf": "go install github.com/ffuf/ffuf@latest",
        "wfuzz": "pip install wfuzz",
        "fuff": "go install github.com/ffuf/ffuf@latest"
    },
    "🌐 Web Probing": {
        "httpx": "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest",
        "httprobe": "go install github.com/tomnomnom/httprobe@latest"
    },
    "📦 Wordlists": {
        "SecLists": "git clone https://github.com/danielmiessler/SecLists.git",
        "fuzzdb": "git clone https://github.com/fuzzdb-project/fuzzdb.git"
    },
    "🔐 Secrets & Git Leaks": {
        "truffleHog": "git clone https://github.com/trufflesecurity/trufflehog.git",
        "git-secrets": "git clone https://github.com/awslabs/git-secrets.git"
    },
    "🌊 Port Scanning": {
        "nmap": "apt install nmap -y",
        "rustscan": "cargo install rustscan",
        "masscan": "git clone https://github.com/robertdavidgraham/masscan"
    },
    "🖼️ Visual Recon": {
        "aquatone": "go install github.com/michenriksen/aquatone@latest",
        "Eyewitness": "git clone https://github.com/FortyNorthSecurity/EyeWitness.git"
    },
    "💥 LFI/RCE/SSRF/etc.": {
        "LFISuite": "git clone https://github.com/D35m0nd142/LFISuite.git",
        "RCE-Exploit-Collection": "git clone https://github.com/payloadbox/rce-attack-automation.git",
        "SSRF-Testing": "git clone https://github.com/swisskyrepo/PayloadsAllTheThings.git"
    },
    "🛡️ OWASP Scanners": {
        "OWASP ZAP": "echo 'Download from https://www.zaproxy.org/download/'",
        "Arachni": "echo 'Manual install recommended for Arachni'"
    },
    "⚙️ Miscellaneous": {
        "Metasploit": "apt install metasploit-framework -y",
        "Burp Suite": "echo 'Download manually from https://portswigger.net/'",
        "CyberChef": "git clone https://github.com/gchq/CyberChef.git"
    }
}

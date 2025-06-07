# 🔍 Recon Automation Tool

A Python-based automation script for performing **web reconnaissance and information gathering** on any domain using open-source tools. Built for educational, ethical hacking, and OSINT (Open-Source Intelligence) purposes.

---

## 📌 Features

This tool automates multiple recon tasks and stores the output in a structured format:

- 🧾 WHOIS Lookup — Retrieve domain registration details  
- 🌐 DNS Record Fetching — Get A, MX, and TXT records  
- 🌐 Subdomain Enumeration — Using:
  - [Amass](https://github.com/owasp-amass)
  - [Assetfinder](https://github.com/tomnomnom/assetfinder)
- 📧 Email & Metadata Collection — Using [theHarvester](https://github.com/laramies/theHarvester)
- 🧠 Technology Fingerprinting — Using [WhatWeb](https://github.com/urbanadventurer/WhatWeb)
- 💾 Organized Output — All results saved in a `recon-output-{domain}` folder

---

## 🖥️ Tools Used

| Tool           | Purpose                          |
|----------------|----------------------------------|
| `whois`        | Domain WHOIS information         |
| `dig`          | DNS records retrieval            |
| `amass`        | Passive subdomain enumeration    |
| `assetfinder`  | Fast subdomain discovery         |
| `theHarvester` | Email and metadata collection    |
| `whatweb`      | Technology fingerprinting        |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Akshay-Sutariya/Internship_tools/recon-automation.git
cd recon-automation
```

---
### 2. Install Dependencies

```bash
sudo apt update
sudo apt install whois dnsutils whatweb nmap -y
sudo apt install golang -y
pip install sublist3r

# Install Amass
sudo snap install amass

# Install assetfinder
go install github.com/tomnomnom/assetfinder@latest
export PATH=$PATH:$(go env GOPATH)/bin

# theHarvester
git clone https://github.com/laramies/theHarvester.git
cd theHarvester && pip install -r requirements.txt
cd ..
```

### 3. Usage

```bash
python3 recon_tool.py
```

### 4. Output Structure

recon-output-example.com/
```bash
├── whois.txt
├── dns_any.txt
├── dns_mx.txt
├── dns_txt.txt
├── subdomains_amass.txt
├── subdomains_assetfinder.txt
├── theHarvester.txt
├── whatweb.txt
```

🔐 Disclaimer
This tool is for educational and authorized testing purposes only.

⚠️ Do not use this script on domains you do not own or do not have permission to test. Use responsibly.



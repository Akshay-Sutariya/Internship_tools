import subprocess
import os

domain = input("Enter the target domain (e.g., example.com): ") 
output_dir = f"recon-output-{domain}"
os.makedirs(output_dir, exist_ok=True)

def run_cmd(cmd, filename):
    print(f"\n[+] Running: {cmd}")
    result = subprocess.getoutput(cmd)
    with open(f"{output_dir}/{filename}", "w") as f:
        f.write(result)
    print(f"[✓] Saved to {output_dir}/{filename}")

# WHOIS
run_cmd(f"whois {domain}", "whois.txt")

# DNS
run_cmd(f"dig {domain} any +short", "dns_any.txt")
run_cmd(f"dig {domain} mx +short", "dns_mx.txt")
run_cmd(f"dig {domain} txt +short", "dns_txt.txt")

# Subdomains with amass
run_cmd(f"amass enum -passive -d {domain}", "subdomains_amass.txt")

# Subdomains with assetfinder
run_cmd(f"assetfinder --subs-only {domain}", "subdomains_assetfinder.txt")

# Emails & metadata with theHarvester
run_cmd(f"python3 theHarvester/theHarvester.py -d {domain} -b bing,crtsh", "theHarvester.txt")

# Technology fingerprinting
run_cmd(f"whatweb {domain}", "whatweb.txt")

# Optional: Nmap (only if allowed)
# run_cmd(f"nmap -Pn -sS -T4 -F {domain}", "nmap.txt")

print("\n✅ Recon complete! All data saved in:", output_dir)

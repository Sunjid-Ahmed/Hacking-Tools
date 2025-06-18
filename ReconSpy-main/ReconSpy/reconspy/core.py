import whois
import socket
import requests
import dns.resolver

class ReconCore:
    def whois_lookup(self, domain):
        try:
            return str(whois.whois(domain))
        except Exception as e:
            return f"WHOIS lookup failed: {e}"

    def dns_lookup(self, domain):
        records = {}
        for rtype in ["A", "MX", "NS", "TXT"]:
            try:
                answers = dns.resolver.resolve(domain, rtype)
                records[rtype] = [r.to_text() for r in answers]
            except:
                records[rtype] = []
        return records

    def subdomain_lookup(self, domain):
        try:
            res = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")
            return list(set([entry['name_value'] for entry in res.json()]))
        except:
            return []
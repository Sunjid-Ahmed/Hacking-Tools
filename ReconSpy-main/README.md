# ReconSpy

Cyber security recon tool with WHOIS, DNS, Shodan, Nmap, and web interface.

````markdown
# 🕵️‍♂️ ReconSpy

![ReconSpy Logo](static/reconspy_logo.png)

ReconSpy is a modular reconnaissance and intelligence-gathering tool for cybersecurity enthusiasts, bug bounty hunters, and penetration testers. It combines powerful modules like WHOIS, DNS enumeration, Shodan integration, Nmap scanning, and a web interface for accessible recon workflows.

---

## 🚀 Features

- 🌐 **WHOIS Lookup** – Retrieve domain registration details.
- 🧠 **DNS Enumeration** – A, MX, TXT, and NS record extraction.
- 🔍 **Subdomain Discovery** – Powered by `crt.sh`.
- 🛰️ **Shodan Integration** – IoT and exposed device info.
- 🛠️ **Nmap Scanner** – Port and service detection (1–1024).
- 🌍 **Web Interface** – Run everything from a browser.
- 🧪 **GitHub Actions CI** – Built-in continuous integration support.

---

## 🛠️ Installation

### 📦 Requirements

Install Python dependencies:
```bash
pip install -r requirements.txt
````

---

## 🌐 Usage

### 🔧 CLI (Coming soon...)

### 🌍 Web Interface

```bash
python -m reconspy.webapp
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 📁 Project Structure

```
ReconSpy/
├── reconspy/             # Core functionality
├── templates/            # Web HTML UI
├── static/               # Logo & assets
├── output/               # Output logs/reports
├── .github/workflows/    # GitHub Actions CI
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🔑 API Keys

To enable **Shodan** integration, replace the placeholder in `webapp.py`:

```python
shodan = ShodanModule(api_key="YOUR_SHODAN_API_KEY")
```

Get your free key from: [https://account.shodan.io/register](https://account.shodan.io/register)

---

## ⚙️ GitHub Actions

This project uses CI to check code health:

* Python setup & install
* Basic import/runtime test for `webapp.py`

---

## 📸 Screenshots

![Web UI](static/reconspy_logo.png)

---

## 👨‍💻 Author

**Sunjid Ahmed Siyem**
Cyber Security Enthusiast
🔗 [GitHub](https://github.com/Sunjid-Ahmed)
🧠 [BugHunter Academy](https://www.facebook.com/BugHunterAcademy)

---

## 📜 License

MIT License — free to use, modify, and share.


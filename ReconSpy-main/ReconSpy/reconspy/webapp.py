from flask import Flask, request, render_template
from reconspy.core import ReconCore
from reconspy.shodan_module import ShodanModule
from reconspy.nmap_module import NmapModule

app = Flask(__name__)
recon = ReconCore()
shodan = ShodanModule(api_key="YOUR_SHODAN_API_KEY")
nmapm = NmapModule()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form['target']
        data = {
            'whois': recon.whois_lookup(target),
            'dns': recon.dns_lookup(target),
            'subdomains': recon.subdomain_lookup(target),
            'shodan': shodan.search(target),
            'nmap': nmapm.scan(target)
        }
        return render_template("result.html", target=target, data=data)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
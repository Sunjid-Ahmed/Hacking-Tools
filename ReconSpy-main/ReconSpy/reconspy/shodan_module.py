from shodan import Shodan

class ShodanModule:
    def __init__(self, api_key):
        self.api = Shodan(api_key)

    def search(self, query, pages=1):
        results = []
        for page in range(1, pages+1):
            data = self.api.search(query, page=page)
            results.extend(data['matches'])
        return results

    def dns(self, domain):
        return self.api.dns.domain_info(domain=domain)
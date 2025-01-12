from urllib.parse import urlparse, parse_qs

def parse_url(url):
    try:
        # Parse the URL
        parsed = urlparse(url)
        
        # Extract subdomains (split the domain)
        domain_parts = parsed.netloc.split('.')
        subdomain = '.'.join(domain_parts[:-2]) if len(domain_parts) > 2 else None
        main_domain = '.'.join(domain_parts[-2:])
        
        # Extract components
        components = {
            "protocol": parsed.scheme,
            "domain": parsed.netloc,
            "subdomain": subdomain,
            "main_domain": main_domain,
            "path": parsed.path,
            "query": parsed.query,
            "parameters": parse_qs(parsed.query),  # Parse query into a dictionary
            "port": parsed.port,
            "fragment": parsed.fragment
        }
        
        # Return components
        return components
    except Exception as e:
        return {"error": f"Invalid URL or parsing error: {e}"}

# Test cases
urls = [
    "https://example.com:8080/path/to/resource?key1=value1&key2=value2#section1",
    "http://subdomain.example.com/path?param=value",
    "ftp://fileserver.com/file?download=true",
    "invalid_url_without_protocol"
]

# Test the function
for url in urls:
    print(f"\nParsing URL: {url}")
    result = parse_url(url)
    for key, value in result.items():
        print(f"{key}: {value}")
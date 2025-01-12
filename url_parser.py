from urllib.parse import urlparse, parse_qs

def parse_url(url):
    # Parse the URL
    parsed = urlparse(url)
    
    # Extract components
    components = {
        "protocol": parsed.scheme,
        "domain": parsed.netloc,
        "path": parsed.path,
        "query": parsed.query,
        "parameters": parse_qs(parsed.query)  # Parse query into a dictionary
    }
    
    return components

# Test the function
url = "https://example.com/path/to/resource?key1=value1&key2=value2"
result = parse_url(url)

# Print results
print("Parsed URL Components:")
for key, value in result.items():
    print(f"{key}: {value}")
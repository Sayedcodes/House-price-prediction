import requests
import json
import socket
import re

def get_email_info(email):
    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return {"error": "Invalid email format"}
    
    # Extract domain
    domain = email.split('@')[1]
    
    # Get IP address
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        ip = "Could not resolve IP"
    
    # Basic domain info (without whois)
    basic_info = {
        'email': email,
        'domain': domain,
        'ip': ip,
        'security': {}
    }
    
    return basic_info

# Example usage
if __name__ == "__main__":
    email = input("Enter email to analyze: ")
    print(json.dumps(get_email_info(email), indent=4))
import requests
import json
import socket
import re

def get_email_info(email):
    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return {"error": "Invalid email format"}
    
    # Extract domain
    domain = email.split('@')[1]
    
    # Get IP address
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        ip = "Could not resolve IP"
    
    # Basic domain info (without whois)
    basic_info = {
        'email': email,
        'domain': domain,
        'ip': ip,
        'security': {}
    }
    
    return basic_info

# Example usage
if __name__ == "__main__":
    email = input("Enter email to analyze: ")
    print(json.dumps(get_email_info(email), indent=4))
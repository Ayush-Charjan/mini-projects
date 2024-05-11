import requests
def trace_ip(ip_address):
    try:
        # Use ipinfo.io to get information about the IP address
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()
        if 'error' in data:
            print("Error:", data['error'])
        else:
            print("IP Address:", data['ip'])
            print("Country:", data['country'])
            print("Region:", data['region'])
            print("City:", data['city'])
            print("Latitude:", data['loc'].split(',')[0])
            print("Longitude:", data['loc'].split(',')[1])
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    ip_address = input("Enter an IP address to trace: ")
    trace_ip(ip_address)

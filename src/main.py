import requests

# CONST
THREAT_INTEL_API = "http://ti.com/api"


def fetch_ip_data():
        
    response = requests.get()
    if response.status == 200:
        return response


def main():
    # get IP
    ip = "10.0.0.1"

    # fetch IP data
    data = fetch_ip_data(ip)
    
    # print data
    print(f"{data}")
    
    return None






if __name__ == '__main__':
    main()
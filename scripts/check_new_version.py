
import requests

# Define the binary sources
sources = {
    "splunk": "https://example.com/splunk/latest",
    "helm": "https://example.com/helm/latest",
}

def get_latest_version(source_url):
    response = requests.get(source_url)
    if response.status_code == 200:
        return response.text.strip()
    return None

if __name__ == "__main__":
    latest_versions = {name: get_latest_version(url) for name, url in sources.items()}
    
    # Save the latest versions in a file for other scripts
    with open("latest_versions.txt", "w") as f:
        for name, version in latest_versions.items():
            print(f"{name} latest: {version}")
            f.write(f"{name} {version}\n")

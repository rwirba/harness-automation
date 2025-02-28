import json
import requests

NEXUS_URL = "http://nexus.kihhuf.org:8081/repository/infra/"
HEADERS = {"Accept": "application/json"}

def get_nexus_version(app, os_type):
    """ Get the latest version from Nexus. """
    url = f"{NEXUS_URL}/{os_type}/{app}/current/"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.text.strip()
    return None

def get_latest_version(app, url):
    """ Fetch the latest version from official sources. """
    if "github" in url:
        response = requests.get(url)
        return response.json()["tag_name"]
    elif "kubernetes-release" in url:
        response = requests.get(url)
        return response.text.strip()
    return None

def main():
    with open("sources.json") as f:
        sources = json.load(f)

    for os_type, apps in sources.items():
        for app, url in apps.items():
            latest_version = get_latest_version(app, url)
            current_version = get_nexus_version(app, os_type)
            
            if latest_version and latest_version != current_version:
                print(f"New version found for {app}: {latest_version} (current: {current_version})")
                # Save the new version to a file for the pipeline to use
                with open(f"{app}_latest.txt", "w") as version_file:
                    version_file.write(latest_version)

if __name__ == "__main__":
    main()

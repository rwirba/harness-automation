import requests
import os

NEXUS_URL = "http://nexus.kihhuf.org:8081/repository/infra/ubuntu/"
USERNAME = "admin"
PASSWORD = "admin"

def upload_to_nexus(app, version):
    """ Uploads new version to Nexus and updates the `current` folder. """
    filepath = f"{app}-latest.bin"
    
    if os.path.exists(filepath):
        new_version_folder = f"{NEXUS_URL}/{app}/{version}/"
        current_folder = f"{NEXUS_URL}/{app}/current/"
        
        # Upload to new version folder
        with open(filepath, "rb") as f:
            response = requests.put(new_version_folder, auth=(USERNAME, PASSWORD), data=f)
            print(response.status_code, response.text)
        
        # Update current folder
        with open(filepath, "rb") as f:
            response = requests.put(current_folder, auth=(USERNAME, PASSWORD), data=f)
            print(response.status_code, response.text)

if __name__ == "__main__":
    for file in os.listdir():
        if file.endswith("_latest.txt"):
            app = file.replace("_latest.txt", "")
            with open(file) as f:
                version = f.read().strip()
                upload_to_nexus(app, version)

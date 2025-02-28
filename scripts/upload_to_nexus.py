
import os
import requests

NEXUS_URL = "https://nexus.example.com/repository"
NEXUS_USER = os.getenv("NEXUS_USER")
NEXUS_PASSWORD = os.getenv("NEXUS_PASSWORD")

def upload_to_nexus(binary_name, version):
    file_path = f"/downloads/{binary_name}-{version}.tar.gz"
    if not os.path.exists(file_path):
        print(f"File {file_path} not found, skipping upload.")
        return

    with open(file_path, "rb") as f:
        response = requests.put(
            f"{NEXUS_URL}/{binary_name}/{version}.tar.gz",
            auth=(NEXUS_USER, NEXUS_PASSWORD),
            data=f
        )

    if response.status_code == 201:
        print(f"Uploaded {binary_name} version {version} to Nexus")
    else:
        print(f"Failed to upload {binary_name} to Nexus: {response.text}")

if __name__ == "__main__":
    with open("new_versions.txt", "r") as f:
        binaries_to_update = [line.strip().split() for line in f]

    for binary, version in binaries_to_update:
        upload_to_nexus(binary, version)


import requests
import os

DOWNLOAD_DIR = "/downloads"

def download_binary(binary_name, version):
    url = f"https://example.com/{binary_name}/{version}/download"
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(DOWNLOAD_DIR, f"{binary_name}-{version}.tar.gz")
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {binary_name} version {version} to {file_path}")
        return file_path
    return None

if __name__ == "__main__":
    with open("new_versions.txt", "r") as f:
        binaries_to_update = [line.strip().split() for line in f]

    for binary, version in binaries_to_update:
        download_binary(binary, version)

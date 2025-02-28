import os

NEXUS_DIR = "/nexus/current"

def get_nexus_version(binary_name):
    version_file = os.path.join(NEXUS_DIR, binary_name, "version.txt")
    if os.path.exists(version_file):
        with open(version_file, "r") as f:
            return f.read().strip()
    return None

if __name__ == "__main__":
    with open("latest_versions.txt", "r") as f:
        latest_versions = {line.split()[0]: line.split()[1] for line in f}

    new_versions = {}

    for binary, latest_version in latest_versions.items():
        current_version = get_nexus_version(binary)
        if current_version != latest_version:
            new_versions[binary] = latest_version

    # Save the versions that need to be updated
    with open("new_versions.txt", "w") as f:
        for binary, version in new_versions.items():
            print(f"New version found for {binary}: {version}")
            f.write(f"{binary} {version}\n")

import os
import shutil

NEXUS_DIR = "/nexus"
ARCHIVE_DIR = "/nexus/archive"

def archive_old_version(binary_name):
    current_dir = os.path.join(NEXUS_DIR, "current", binary_name)
    if os.path.exists(current_dir):
        old_version = os.path.join(current_dir, "version.txt")
        if os.path.exists(old_version):
            with open(old_version, "r") as f:
                old_version_number = f.read().strip()

            archive_path = os.path.join(ARCHIVE_DIR, binary_name, old_version_number)
            shutil.move(current_dir, archive_path)
            print(f"Archived {binary_name} version {old_version_number} to {archive_path}")

if __name__ == "__main__":
    with open("new_versions.txt", "r") as f:
        binaries_to_update = [line.strip().split()[0] for line in f]

    for binary in binaries_to_update:
        archive_old_version(binary)

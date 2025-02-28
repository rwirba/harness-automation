#!/bin/bash
set -e

# Load sources.json
apps=$(jq -r 'to_entries | .[] | "\(.key) \(.value)"' sources.json)

download_binary() {
    local app=$1
    local url=$2
    echo "Downloading $app from $url"
    wget -q "$url" -O "$app-latest.bin"
}

for app in $apps; do
    url=$(jq -r ".ubuntu.${app}" sources.json)
    if [[ $url != "null" ]]; then
        download_binary $app $url
    fi
done

#!/bin/bash
url = "https://gist.github.com/152f6461ef7492cf1d8974c724d265fc.git"

until git clone "$url"; do
    echo "git clone ,retry..."
    sleep 1
done
echo "clone successfully"